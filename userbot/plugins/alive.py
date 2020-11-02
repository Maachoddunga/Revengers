from userbot import bot

@telebot.on(admin_cmd(pattern="alive"))
async dev lol(event)
    itsme = bot.me
    name = itsme.first_name
    await event.edit(f"Hi {name}, I'm alive and working!")
    
