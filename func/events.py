from session.SessionContent import *
from session.extraContents import *

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

extra_list = [
    "ปฐมบท",
    "อีเว้นเสริม-1",
    "อีเว้นเสริม-2",
    "อีเว้นเสริม-3",
    "อีเว้นเสริม-4",
    "อีเว้นเสริม-5",
    "อีเว้นเสริม-6",
    "อีเว้นเสริม-7",
    "อีเว้นเสริม-8",
    "อีเว้นเสริม-9",
    "อีเว้นเสริม-10"
]
extra_content = [
    extra_000(),
    extra_001()
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


def extra_event_contents(x):
    index = extra_list.index(x)
    try:
        if extra_content[index]:
            return extra_content[index]
    except IndexError:
        print(index)
        embed = discord.Embed(
            title="ไม่มีข้อมูล"
        )
        return embed


