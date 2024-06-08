import discord
import time

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$hello"):
        await message.channel.send("hi")

    if message.content.startswith("I'm") or message.content.startswith("Im") or message.content.startswith("i'm") or message.content.startswith("im"):
        await message.channel.send("hi im gernt")

    if message.content.startswith("$ban"):
        if not message.author.guild_permissions.ban_members:
            await message.channel.send("You cant ban people lol")
            return

        try:
            parts = message.content.split()
            if len(parts) < 2:
                await message.channel.send("bro who do i ban")
                return
            
            member = message.mentions[0]
            reason = ' '.join(parts[2:]) if len(parts) > 2 else None
            
            await message.channel.send(f'BYE BYE {member.mention} (u banned for {reason})')
            time.sleep(2)
            await member.ban(reason=reason)
        except Exception as e:
            await message.channel.send(f'An oopsie happened: {str(e)}')
       
client.run('YOUR BOT TOKEN HERE')