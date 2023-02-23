import asyncio
import datetime

import discord

from Banks.Bank_db import Bank
from Quests.db.Mission_db import UserMission
from db.Ranking import Ranking
from db.users import Users
from func.config import img_


def expire_date():
    now = datetime.datetime.now()
    date_add = now + datetime.timedelta(days=3)
    start = now.strftime("%d/%m/%Y")
    end = date_add.strftime("%d/%m/%Y")
    date_list = [start, end]
    return date_list

class CloseReport(discord.ui.View):
    def __init__(self):
        super(CloseReport, self).__init__(timeout=None)
    @discord.ui.button(label="ปิดหน้าต่างนี้", style=discord.ButtonStyle.danger, custom_id="mission_close_btn")
    async def mission_close_btn(self, button, interaction:discord.Interaction):
        button.disabled=True
        self.clear_items()
        await interaction.response.edit_message(content="ห้องส่งสินค้ากำลังจะปิดการใช้งานใน 10 วินาที")
        await asyncio.sleep(10)
        await interaction.channel.delete()
class FineConfirm(discord.ui.View):
    def __init__(self, fine):
        super(FineConfirm, self).__init__(timeout=None)
        self.fine = fine

    @discord.ui.button(label='Aecept', style=discord.ButtonStyle.success, emoji="💵", custom_id="fine_mission_confirm")
    async def fine_mission_confirm(self, button, interaction: discord.Interaction):
        member = interaction.user
        button.disabled = False
        try:
            old = Users().wallet(member.id)
            if old < int(self.fine):
                return await interaction.response.edit_message(
                    content=f"{member.mention} : ⚠ ชำระค่าปรับไม่ได้เนื่องจากยอดเงินของคุณไม่เพียงพอ", view=None)
            else:
                total = old - int(self.fine)
                Users().wallet_update(member.id, total)
                await discord.DMChannel.send(member, f"⚠ ระบบหักค่าปรับจำนวน {self.fine} Wallet เรียบร้อย")
        except Exception as e:
            return await interaction.response.edit_message(content=e, view=None)
        else:
            if self.fine == 100:
                UserMission().expansion_time(member.id, expire_date()[0], expire_date()[1])
            else:
                UserMission().delete(member.id)
            return await interaction.response.edit_message(content="รีเซ็ตภารกิจเรียบร้อย", view=None)

    @discord.ui.button(label='Reject', style=discord.ButtonStyle.danger, emoji="⚠", custom_id="fine_mission_reject")
    async def fine_mission_reject(self, button, interaction: discord.Interaction):
        button.disabled = False
        await interaction.response.edit_message(content="คุณได้ยกเลิกการรีเซ็ตภารกิจของคุณ", view=None)


class MissionExpire(discord.ui.View):
    def __init__(self):
        super(MissionExpire, self).__init__(timeout=None)


    @discord.ui.button(label="Expansion Time", style=discord.ButtonStyle.primary, emoji="⌚",
                       custom_id="mission_expansion_time")
    async def mission_expansion_time(self, button, interaction:discord.Interaction):
        button.disabled = False
        member = interaction.user
        fine = 100
        await interaction.response.edit_message(
            content=f"การขยายเวลาในการจัดส่งสินค้า คุณต้องชำระค่าปรับจำนวน {fine} Wallet \n{member.mention} คุณต้องการที่จะขยายเวลาหรือไม่",
        embed=None,
        view=FineConfirm(fine))

    @discord.ui.button(label="Reset", style=discord.ButtonStyle.danger, emoji="💵", custom_id="fine_mission")
    async def fine_mission(self, button, interaction: discord.Interaction):
        member = interaction.user
        button.disabled = False
        fine = 50
        await interaction.response.edit_message(
            content=f"การส่งภารกิจเกินกำหนด คุณจะต้องเสียค่าปรับจำนวน {fine} Wallet ในการรีเซ็ตภารกิจใหม่\n{member.mention} คุณต้องการรีเซ็ตภารกิจหรือไม่",
            embed=None,
            view=FineConfirm(fine))


class MissionReportButton(discord.ui.View):
    def __init__(self, bot):
        super(MissionReportButton, self).__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="รายงานการจัดส่งสินค้า", emoji="📝", style=discord.ButtonStyle.secondary,
                       custom_id="mission_report")
    async def mission_report(self, button, interaction: discord.Interaction):

        button.disabled = False
        member = interaction.user
        guild = interaction.guild
        cate_name = "MISSION REPORT"
        channel_name = "🗄-ตู้หมายเลข-{}".format(member.discriminator)
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
                contact_channel = await guild.create_text_channel(name=channel_name, category=cate)
                await contact_channel.edit(sync_permissions=True, )
                await contact_channel.set_permissions(
                    member,
                    view_channel=True,
                    send_messages=True,
                    read_message_history=True,
                    read_messages=True,
                    attach_files=True
                )
                await interaction.response.edit_message(
                    content=f"ไปยังห้อง {contact_channel.mention} เพื่อแจ้งปัญหา หรือติดต่อทีมงาน", view=None,
                    embed=None)
                embed = discord.Embed(
                    title="📝 ระบบรายการจัดส่งสินค้า",
                    description="ให้ผู้เล่นใช้ปุ่มคำสั่งด้านล่างนี้ในการรายงานการจัดส่งสินค้า โดยให้ผู้เล่นไปยัง Guild Master และทำการนำสินค้าใส่ไว้ในตู้"
                                "และล๊อคตู้ให้เรียบร้อย (ภายในตู้จะมีล๊อคเตรียมไว้ให้) จับภาพสินค้าในตู้ กดปุ่มอัพโหลดและทำตามที่ระบบระบุ"
                )
                embed.add_field(name="📷 ปุ่มอัพโหลดภาพ",
                                value="ใช้สำหรับอัพโหลดรูปภาพหลักฐานการจัดส่งสินค้าภายในตู้ที่อยู่ใน Guild Master")
                embed.set_image(url=img_("guild_master"))
                return await contact_channel.send(f"{member.mention}", embed=embed, view=ImageUploadButton(self.bot))


class ImageUploadButton(discord.ui.View):
    def __init__(self, bot):
        super(ImageUploadButton, self).__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="อัพโหลดภาพ", style=discord.ButtonStyle.secondary, emoji="📷",
                       custom_id="image_upload_buton")
    async def image_upload_button(self, button, interaction: discord.Interaction):
        button.disabled = False
        member = interaction.user
        guild = interaction.guild

        def check(res):
            attachments = res.attachments
            if len(attachments) == 0:
                return False
            attachment = attachments[0]
            file_type = attachment.filename.endswith(('.jpg', '.png', 'jpeg'))
            return res.author == interaction.user and res.channel == interaction.channel and file_type
        await interaction.response.edit_message(content="System check for upload image...", embed=None, view=None)
        msg = await interaction.followup.send(f"{member.mention} 📷 อัพโหลดรูปภาพหลักฐานการจัดส่งสินค้าของคุณ")
        try:
            data = UserMission().mission(member.id)
            txt = f"```diff\n====================================\n" \
                  f"+ ชื่อภารกิจ : {data[2]}\n" \
                  f"+ ผู้ส่งสินค้า: {member.display_name}\n" \
                  f"+ จำนวนสินค้า : {data[3]}\n" \
                  f"+ รางวัลภารกิจ : {data[6]} Wallet\n" \
                  f"+ วันส่งสินค้า : {expire_date()[0]}\n" \
                  f"==================================" \
                  f"\n```" \

            img_message = await self.bot.wait_for(event="message", check=check, timeout=60)
            if img_message is not None:
                await img_message.delete()
                await msg.edit(content=img_message.attachments[0])
                try:
                    cate_name = "MISSION REPORT"
                    ch_name = "📃-รายงานภารกิจ"
                    channel = discord.utils.get(guild.channels, name=ch_name)

                    if channel:
                        send_ch = await channel.send(txt.strip())
                        await send_ch.add_reaction("🔐")
                    else:
                        cate = discord.utils.get(guild.categories, name=cate_name)
                        channel = await guild.create_text_channel(name=ch_name, category=cate)
                        await channel.set_permissions(guild.default_role, view_channel=False)
                        send_ch = await channel.send(txt.strip())
                        await send_ch.add_reaction("🔐")

                except Exception as e:
                    return await msg.edit(content=e)

        except asyncio.TimeoutError:
            return await msg.edit(
                content=f"{member.mention} : ⏲ คุณดำเนินการช้าเกินไปโปรดดำเนินการใหม่อีกครั้ง")
        else:
            try:
                if Bank().check_member(member.id) != 1:
                    Bank().new(member.id, member.discriminator)
                else:
                    pass
            except Exception as e:
                return await msg.edit(content=e)
            else:
                try:

                    old = Bank().bank(member.id)[3]
                    total = old + UserMission().mission(member.id)[6]
                    exp = Ranking().exp(member.id) + UserMission().mission(member.id)[5]
                    Bank().update(member.id, total)
                    Ranking().update_exp(member.id, exp)
                except Exception as e:
                    return await msg.edit(content=e)
                else:
                    UserMission().delete(member.id)
                    return await interaction.followup.send(
                        f"💾 ระบบได้ส่งรายงานการจัดส่งสินค้าให้กับ Guild Master เป็นที่เรียบร้อยแล้ว\n"
                                f"คุณจะได้รับเงินรางวัลจำนวน {data[6]} Wallet ภายหลังตรวจสอบความถูกต้องของสินค้าเรียบร้อย\n"
                                f"กดที่ปุ่ม เพื่อปิดห้องส่งภารกิจ", view=CloseReport())

