from session.SessionContent import *

event_list = [
    "บทที่-1",
    "บทที่-2",
    "บทที่-3",
    "บทที่-4",
    "บทที่-5",
    "บทที่-6",
    "บทที่-7",
    "บทที่-8",
    "บทที่-9",
    "บทที่-10"
]
content = [
    event_001(),
    event_002(),
    event_003()
]
def event_contents(x):
    index = event_list.index(x)
    try:
        if content[index]:
            return content[index]
    except IndexError:
        print(index)
        embed = discord.Embed(
            title="ไม่มีข้อมูล"
        )
        return embed
