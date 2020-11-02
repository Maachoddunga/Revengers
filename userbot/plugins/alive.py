@telebot.on(admin_cmd(pattern="alive"))
async def lol(event):
    await event.edit(f"Hi user, I'm alive and working!")
    
