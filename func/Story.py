from session.StoryContents import *

story_lists = [
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

story = [
    story_001()

]
def story_content(x):
    index = story_lists.index(x)
    try:
        if story[index]:
            return story[index]
    except IndexError:
        print(index)
        embed = discord.Embed(
            title="ไม่มีข้อมูล"
        )
        return embed