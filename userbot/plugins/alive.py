from userbot import name

@telebot.on(admin_cmd(pattern="alive"))
async def lol(event):
    await event.edit(f"Hi {name}, I'm alive and working!")
    
