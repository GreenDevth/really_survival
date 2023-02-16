import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option

from db.Steam import Steam, Perm
from db.users import Users
from func.config import get_cooldown_time
from func.events import event_list, event_contents
from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]


class EventCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(EventRegister(self.bot))


    server_event = SlashCommandGroup(guild_ids=[guild_id], name="server_event", description="คำสั่งสำหรับแอดมิน")

    @server_event.command(name="แสดงเนื้อหาอีเว้น", description="คำสั่งติดตั้งแคตตากอรี่และแชลแนลสำหรับแสดงเนื้อหาของอีเว้น")
    async def event_installer(
            self,
            ctx: discord.Interaction,
            event: Option(str, "เลือกอีเว้นที่ต้องการ", choices=event_list)

    ):
        guild = ctx.guild
        choices = event_list
        cate = "EVENT CONTENT"
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                view_channel=True,
                read_messages=True,
                read_message_history=True,
                send_messages=False
            )
        }
        try:
            if discord.utils.get(guild.categories, name=cate):
                pass
            else:
                await guild.create_category(name=cate, overwrites=overwrites)
        except Exception as e:
            return await ctx.response.send_message(e, ephemeral=True)
        else:
            if event == choices[int(event_list.index(event))]:
                channel_name = f"📔-{event}"
                try:
                    cates = discord.utils.get(guild.categories, name=cate)
                    channel = discord.utils.get(guild.channels, name=channel_name)
                    if channel:
                        await channel.purge()
                        await channel.send(embed=event_contents(str(event)))
                    else:
                        channle = await guild.create_text_channel(name=channel_name, category=cates)
                        await channle.send(embed=event_contents(str(event)))
                except Exception as e:
                    return await ctx.response.send_message(e, ephemeral=True)
                else:
                    return await ctx.response.send_message(f"เพิ่มข้อมูลเนื้อหาอีเว้น {event} ให้กับระบบเรียบร้อย",
                                                           ephemeral=True)

    @server_event.command(name="ลงทะเบียนกิจกรรม", description="คำสั่งแสดงปุ่มสำหรับลงทะเบียนเข้าร่วมกิจกรรม")
    async def event_register(self, ctx:discord.Interaction):
        guild = ctx.guild
        await ctx.response.defer(ephemeral=True, invisible=False)

        msg = await ctx.followup.send("ระบบกำลังประมวลผล โปรดรอสักครู่")

        ch_name = "📝-ลงทะเบียนกิจกรรม"
        cate_name = "EVENT REGISTER"

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                view_channel=True,
                read_messages=True,
                read_message_history=True,
                send_messages=False
            )
        }

        try:
            cate = discord.utils.get(guild.categories, name=cate_name)
            if cate:
                pass
            else:
                await guild.create_category(name=cate_name, overwrites=overwrites)
        except Exception as e:
            return await msg.edit(content=e)
        else:
            try:
                channel = discord.utils.get(guild.channels, name=ch_name)
                if channel:
                    await channel.purge()
                    pass
                else:
                    channel = await guild.create_text_channel(name=ch_name, category=cate)
                    await channel.set_permissions(guild.default_role, send_messages=False)
            except Exception as e:
                return await msg.edit(content=e)
            else:
                img = discord.File('./img/concept/event_frist.png')
                await channel.send(file=img, view=EventRegister(self.bot))
                return await msg.edit(content="ดำเนินการติดตั้งระบบลงทะเบียนกิจกรรมสำเร็จแล้ว")

class EventRegister(discord.ui.View):
    def __init__(self, bot):
        super(EventRegister, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(get_cooldown_time()), commands.BucketType.member)

    @discord.ui.button(label="คลิกที่ปุ่มเพื่อทำการลงทะเบียนกิจกรรม", style=discord.ButtonStyle.secondary, custom_id="event_label", disabled=True)
    async def disable_button_event_register(self, button, interaction:discord.Interaction):
        button.disabled=False
        await interaction.response.send_message("ok", ephemeral=True)
    @discord.ui.button(label="ลงทะเบียน", emoji="📝",style=discord.ButtonStyle.secondary, custom_id="event_register")
    async def event_register_button(self, button, interaction:discord.Interaction):
        button.disabled=False
        member = interaction.user
        await interaction.response.defer(ephemeral=True, invisible=False)
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        msg = await interaction.followup.send("⏳ ระบบกำลังประมวลผล กรุณารอสักครู่")
        if retry:
            return await msg.edit(content=
                f'อีก {round(retry, int(get_cooldown_time()))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง')


        try:
            if Users().check(member.id) == 0:
                return await msg.edit(content=f"{member.mention} ไม่พบข้อมูลของคุณในระบบ")
            elif Steam().check(member.id) == 1:
                return await msg.edit(content=f"{member.mention} คุณได้ลงทะเบียนไว้แล้ว")
            elif Perm().check(member.id) == 1:
                return await msg.edit(content=f"{member.mention} คุณได้ลงทะเบียนไว้แล้ว")
            else:
                steam = Users().player(member.id)[2]
                Steam().new(member.id, steam)
                Perm().new(member.id)
                return await msg.edit(content=f"{member.mention} คุณได้ลงทะเบียนเข้าร่วมกิจกรรมเป็นที่เรียบร้อยแล้ว")
        except Exception as e:
            return await msg.edit(content=e)


