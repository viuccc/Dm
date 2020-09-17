import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='+')

BOT_OWNER_ROLE = "DM"


@bot.event
async def on_ready():
    print('Online')


@bot.command(name="senf")
async def send(ctx,*,msg):
	await ctx.message.delete()
	author=ctx.message.author
	
	for member in ctx.guild.members:
		try:
			await member.send(msg)
			embed=discord.Embed(title="Public DM",description=f"DM sent to {member.name}#{member.discriminator} \n:white_check_mark:",colour=0x142c9c)
			embed.set_image(url="https://cdn.discordapp.com/attachments/568829761531543582/573936305495605269/animated-line-image-0379.gif")
			embed.set_footer(text="Made ❤️ By ˢᵖ༒❤P⃠𝙖 𝙧 𝙖 𝙢⍟#4217 ",icon_url="https://cdn.discordapp.com/attachments/713095989593899068/720095371753291797/JPEG_20200606_170941.jpg")
			await ctx.send(embed=embed)
		except:
			embed=discord.Embed(title='''Public DM''',description=f'''DM Not sent to {member.name}#{member.discriminator}''' ''' :x: ''',colour=0x142c9c)
			embed.set_image(url="https://cdn.discordapp.com/attachments/568829761531543582/573936305495605269/animated-line-image-0379.gif")
			embed.set_footer(text="Made ❤️ By ˢᵖ༒❤P⃠𝙖 𝙧 𝙖 𝙢⍟#4217",icon_url="https://cdn.discordapp.com/attachments/713095989593899068/720095371753291797/JPEG_20200606_170941.jpg")
			await ctx.send(embed=embed)
				
			embed=discord.Embed(title="DM sent to all",description=f" :white_check_mark: ",colour=0x142c9c)
			embed.set_image(url="https://cdn.discordapp.com/attachments/568829761531543582/573936305495605269/animated-line-image-0379.gif")
			embed.set_footer(text="Made ❤️ By ˢᵖ༒❤P⃠𝙖 𝙧 𝙖 𝙢⍟#4217",icon_url="https://cdn.discordapp.com/attachments/713095989593899068/720095371753291797/JPEG_20200606_170941.jpg")
			await ctx.send(embed=embed)


@bot.command(name="say",hidden=True)
#@commands.check(fetch)
async def say(ctx, *, content:str):
	author=ctx.message.author
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		await ctx.send(content)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
		
		
bot.run('NzU2MTA4NTUwNzY5NzM3NzQ4.X2NC9g.b1dNxiccIbKsTqUKgZ4g__2pcg0')
