import discord
from discord.commands import SlashCommandGroup, Option
from discord.ext import commands

from db.Steam import Steam, Pack, Perm
from scripts.guilds import guild_data

guild_id = guild_data()["realistic"]


class SteamUpdateCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    pack = SlashCommandGroup(guild_ids=[guild_id], name="pack", description="คำสั่งจัดการแพ๊คสินค้าต่าง ๆ")

    @pack.command(name="รีเซ็ตฐานข้อมูลแพ๊กเก็ต", description="คำสั่งจัดการฐานข้อบน Really Survival database")
    async def database_pack_reset(self, ctx: discord.Interaction,
                                  database_name: Option(str, "พิมพ์ชื่อฐานข้อมูลที่ต้องการรีเซ็ต", choices=["steam", "pack","permission"])):
        await ctx.response.defer(ephemeral=True, invisible=False)
        msg = await ctx.followup.send("ระบบกำลังประมวลผลการทำงาน")

        try:
            if database_name == "steam":
                Steam().purge()
                return await msg.edit(content=f"Reset {database_name} Successfully")
            elif database_name == "pack":
                Pack().purge()
                return await msg.edit(content=f"Reset {database_name} Successfully")

            elif database_name == "permission":
                Perm().purge()
                return await msg.edit(content=f"Reset {database_name} Successfully")
            else:
                return await msg.edit(content=f"database -> ` {database_name} ` : ไม่มีอยู่ในระบบ")
        except Exception as e:
            return await msg.edit(content=e)



