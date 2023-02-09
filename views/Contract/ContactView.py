import discord.ui
from discord.ext import commands

from server.Supporter import donate, ticket_open
from views.Contract.ContactCloseView import ContactCloseButton


class ContractButton(discord.ui.View):
    def __init__(self, bot):
        super(ContractButton, self).__init__(timeout=None)
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, int(60), commands.BucketType.member)

    @discord.ui.button(label="เปิดตั่วติดต่อ", style=discord.ButtonStyle.secondary, emoji="🎫", custom_id="create_ticket")
    async def create_ticket(self, button, interaction:discord.Interaction):
        button.disabled=False
        member = interaction.user
        guild = interaction.guild
        cate_name = "CONTACT STAFF"
        channel_name = "ticket-{}".format(member.discriminator)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                view_channel=False,
                read_messages=False
            )
        }
        try:
            category = discord.utils.get(guild.categories, name=cate_name)
            if category:
                pass
            else:
                await guild.create_category(name=cate_name, overwrites=overwrites)
        except Exception as e:
            return await interaction.response.edit_message(content=e, view=None)
        else:
            try:
                cate = discord.utils.get(guild.categories, name=cate_name)
                if cate:
                    channel = discord.utils.get(guild.channels, name=channel_name)
                    if channel:
                        await channel.delete()
            except Exception as e:
                return await interaction.response.edit_message(content=e, view=None)
            else:
                overwrites = {
                    member: discord.PermissionOverwrite(
                        view_channel=True,
                        read_messages=True,
                        send_messages=True,
                        read_message_history=True
                    )
                }
            contact_channel = await guild.create_text_channel(name=channel_name, category=cate, overwrites=overwrites)
            await contact_channel.edit(sync_permissions=True, )
            await contact_channel.set_permissions(member, view_channel=True, send_messages=True,
                                                   read_message_history=True, read_messages=True)
            await interaction.response.edit_message(content=f"ไปยังห้อง {contact_channel.mention} เพื่อแจ้งปัญหา หรือติดต่อทีมงาน", view=None)
            return await contact_channel.send(f"{member.mention}",embed=ticket_open(), view=ContactCloseButton(self.bot))
    @discord.ui.button(label="สนับสนุนเซิร์ฟ", style=discord.ButtonStyle.secondary, emoji="💳", custom_id="support_server")
    async def support_server(self, button, interaction:discord.Interaction):
        button.disabled=False
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(f'อีก {round(retry, int(60))} วินาที คำสั่งถึงจะพร้อมใช้งานอีกครั้ง', ephemeral=True)
        await interaction.response.edit_message(content=donate(), view=None)