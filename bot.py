import discord
from discord.ext import commands
# from itertools import cycle
import asyncio
import time
prefix = "×"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
BOT_OWNER_ROLE= "Runner" #change which role you need!



@bot.event
async def on_ready():
    print('Online')
    print(bot.user.name)
    print("Everything's all ready to go~")
    while True:
    	await bot.change_presence(activity=discord.Activity(type=1,name="with YAHOO TRIVIA...!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with ÃmìT RØY®#8848"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with HQ GOOGLE BOT...!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with HQ TRIVIA....!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with QUIPP GERMANY....!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with SWAG IQ..!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with MAIL+BOT...!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with  AMIT ROY...!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=2,name="with PARKASH..."))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'''{len(bot.guilds)} servers'''))
    	await asyncio.sleep(5)
 
 
@bot.command(name="ping")
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command()
async def start(ctx,game:str):
	await ctx.message.delete()
	author = ctx.message.author
	# if BOT_OWNER_ROLE in [role.name for role in author.roles]:
	# 	BOT_OWNER_ROLE="Access"
	if game== 'loco':
		url="https://cdn.discordapp.com/attachments/596710160035217408/597750968528142337/giphy.gif"
	elif game== 'hq':
		url="https://cdn.discordapp.com/attachments/557650994897485834/594847560863186945/IMG_20190426_203610.jpg"
	elif game== 'trivaa':
		url="https://cdn.discordapp.com/attachments/557650994897485834/594847560326447126/IMG_20190426_203621.jpg"
	elif game== 'jeetoh':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594861943454564352/new_mascot_elephant.png"
	elif game== 'karma':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594865537939668992/IMG_20190630_175306_281.JPG"
	elif game== 'confetti':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547395/IMG_20190630_233005_747.JPG"
	elif game== 'swagiq':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547393/IMG_20190630_233031_734.JPG"
	elif game== 'theq':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950648764825600/18vDC_cU_400x400.jpg"
	elif game== 'brainbaazi':
		url="https://is3-ssl.mzstatic.com/image/thumb/Purple118/v4/fc/da/17/fcda17ed-f0b6-6067-ecc4-d9641fed234c/AppIcon-0-1x_U007emarketing-0-0-sRGB-85-220-0-5.png/246x0w.jpg"
	elif game== 'qureka':
		url="https://cdn.discordapp.com/attachments/572922639039856645/595214144060391450/IMG_20190701_165822_749.JPG"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		# BOT_OWNER_ROLE="Access"
		embed = discord.Embed(title='Join Fast :wink:',description='**Game is starting!**',colour=0x98FB98)
		embed.add_field(name='Game', value=f'**{game}**',inline=True)
		embed.set_thumbnail(url=url)
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text=f"KESHAV RAJ ᴳᵒᵈ#7735", \
            icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone Game Alert :alarm_clock:",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
        
   

@bot.command()
async def end(ctx,game:str):
	await ctx.message.delete()
	author=ctx.message.author
	if game== 'loco':
		url="https://cdn.discordapp.com/attachments/596710160035217408/597750968528142337/giphy.gif"
	elif game== 'hq':
		url="https://cdn.discordapp.com/attachments/557650994897485834/594847560863186945/IMG_20190426_203610.jpg"
	elif game== 'trivaa':
		url="https://cdn.discordapp.com/attachments/557650994897485834/594847560326447126/IMG_20190426_203621.jpg"
	elif game== 'jeetoh':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594861943454564352/new_mascot_elephant.png"
	elif game== 'karma':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594865537939668992/IMG_20190630_175306_281.JPG"
	elif game== 'confetti':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547395/IMG_20190630_233005_747.JPG"
	elif game== 'swagiq':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547393/IMG_20190630_233031_734.JPG"
	elif game== 'theq':
		url="https://cdn.discordapp.com/attachments/578965576651898890/594950648764825600/18vDC_cU_400x400.jpg"
	elif game== 'brainbaazi':
		url="https://is3-ssl.mzstatic.com/image/thumb/Purple118/v4/fc/da/17/fcda17ed-f0b6-6067-ecc4-d9641fed234c/AppIcon-0-1x_U007emarketing-0-0-sRGB-85-220-0-5.png/246x0w.jpg"
	elif game== 'qureka':
		url="https://cdn.discordapp.com/attachments/572922639039856645/595214144060391450/IMG_20190701_165822_749.JPG"  
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed = discord.Embed(title='Game End! :wink:',
                              description='**Game is Ended!**',
                              colour=0x98FB98)
		embed.add_field(name='Game',value=f'**{game}.upper()**',inline=True)
		embed.set_thumbnail(url=url)
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone :warning:",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
   




@bot.command(name="say",hidden=True)
#@commands.check(fetch)
async def say(ctx, *, content:str):
	author=ctx.message.author
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		await ctx.send(content)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#brainbaazi
@bot.command(name="brainbaazi",description="")
async def brainbaazi(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" <:right:604146670862598158>"
	else:
		check=" <:wrong:604147533043990528> "
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Brain Baazi",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://is3-ssl.mzstatic.com/image/thumb/Purple118/v4/fc/da/17/fcda17ed-f0b6-6067-ecc4-d9641fed234c/AppIcon-0-1x_U007emarketing-0-0-sRGB-85-220-0-5.png/246x0w.jpg")
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone <:emoji_16:606076148371292160>",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
	   
#loco
@bot.command(name="loco",description="")
async def loco(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" <:right:604146670862598158> "
	else:
		check=" <:wrong:604147533043990528>"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Loco",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/596710160035217408/597750968528142337/giphy.gif")
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone <:emoji_16:606076148371292160>",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#hq
@bot.command(name="hq",hidden=True)
async def hq(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" <:right:604146670862598158>"
	else:
		check=" <:wrong:604147533043990528>"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="HQ Trivia",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/595173694670635019/SAVE_20190426_203902.gif")
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone <:emoji_16:606076148371292160>",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
		
#trivaa	
@bot.command(name="trivaa",hidden=True)
async def trivaa(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" <:right:604146670862598158>"
	else:
		check=" <:wrong:604147533043990528>"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Trivaa",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/557650994897485834/594847560326447126/IMG_20190426_203621.jpg")
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone <:emoji_16:606076148371292160>",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#jeetoh
@bot.command(name="jeetoh",hidden=True)
async def jeetoh(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" <:emoji_3:609588150976905216>"
	else:
		check=" <:emoji_4:609588641358151698>"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Jeetoh",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/594861943454564352/new_mascot_elephant.png")
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone <:emoji_15:609593009213931540>",embed=embed)
	else:
		await ctx.send("you not have permisson "+ctx.author.mention)
#karma
@bot.command(name="karma",hidden=True)
async def karma(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" <:right:604146670862598158>"
	else:
		check=" <:wrong:604147533043990528> "
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="My karma",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/594865537939668992/IMG_20190630_175306_281.JPG")
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone <:emoji_16:606076148371292160>",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)

#confeeti
@bot.command(name="confetti",hidden=True)
async def confetti(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" <:right:604146670862598158>"
	else:
		check=" <:wrong:604147533043990528> "
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game  Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Confetti-India",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547395/IMG_20190630_233005_747.JPG")
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone <:emoji_14:609592717013680138>",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#swagiq
@bot.command(name="swagiq",hidden=True)
async def swagiq(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" <:emoji_3:609588150976905216>"
	else:
		check=" <:emoji_4:609588641358151698> "
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game  Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Swag-IQ",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/594950473375547393/IMG_20190630_233031_734.JPG")
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg.jpg")
		await ctx.send(content="@everyone <:emoji_16:606076148371292160>",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#the q
@bot.command(name="theq",hidden=True)
async def theq(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" <:right:604146670862598158>"
	else:
		check=" <:wrong:604147533043990528>"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game  Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="The-Q",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/578965576651898890/594950648764825600/18vDC_cU_400x400.jpg")
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone <:emoji_16:606076148371292160>",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#qureka
@bot.command(name="qureka",hidden=True)
async def qureka(ctx,accuracy:str,prize_won:str,last_question_status:str,result:str):
	await ctx.message.delete()
	author=ctx.message.author
	if last_question_status== 'correct':
		check=" <:right:604146670862598158>"
	else:
		check=" <:wrong:604147533043990528>"
	if result=='won':
		emoji =":tada:"
	else:
		emoji=":sob:"
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Game  Results",description=f"**{ctx.guild.name}**",color=0x142c9c)
		embed.add_field(name="Qureka",value=f"**Accuracy: {accuracy}{check}\nPrize Won: {prize_won} :moneybag:\nLast Question status: {last_question_status}{check}\nGame Status: {result} {emoji}**")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/572922639039856645/595214144060391450/IMG_20190701_165822_749.JPG")
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
		await ctx.send(content="@everyone <:emoji_16:606076148371292160>",embed=embed)
	else:
		await ctx.send("**Lol You Not Have Permission To use this commands**:joy: "+ctx.author.mention)
#q1		
@bot.command(name="q")
async def q(ctx,qnumber:int):
	await ctx.message.delete()
	author=ctx.message.author
		
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		embed=discord.Embed(title="Questions", description=f"**Q.{qnumber} is coming on your mobile screen**", colour=0x142c9c)
		embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
		embed.set_footer(text="Made By KESHAV RAJ ᴳᵒᵈ#7735")
		await ctx.send(embed=embed)
		
@bot.command(name="ban")
async def ban(ctx,member:discord.Member,*,reason=None):
	await ctx.message.delete()
	author=ctx.message.author
	
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		await member.ban(reason=reason)
		embed=discord.Embed(title="Ban:",description=f"**{member.name}#{member.discriminator} got banned!,Reason={reason}**",colour=0x142c9c)
	await ctx.send(embed=embed)

@bot.command(name="warn")
async def ban(ctx,member:discord.Member,*,reason=None):
	await ctx.message.delete()
	author=ctx.message.author
	
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		await member.ban(reason=reason)
		embed=discord.Embed(title="Warned:",description=f"**{member.name}#{member.discriminator} got Warned!,Reason={reason}**",colour=0x142c9c)
	await ctx.send(embed=embed)
		
@bot.command(name="kick")
async def ban(ctx,member:discord.Member,*,reason=None):
	await ctx.message.delete()
	author=ctx.message.author
	
	if BOT_OWNER_ROLE in [role.name for role in author.roles]:
		await member.ban(reason=reason)
		embed=discord.Embed(title="Kicked:",description=f"**{member.name}#{member.discriminator} Got Kicked!,Reason={reason}**",colour=0x142c9c)
	await ctx.send(embed=embed)
	
@bot.command(name="n")
@commands.has_role('owner')
async def f(ctx,*,msg):
	await ctx.message.delete()
	author=ctx.message.author
	
	for member in ctx.guild.members:
		try:
			await member.send(msg)
			embed=discord.Embed(title="Mass DM",description=f"DM sent to {member.name}#{member.discriminator} \n:white_check_mark:",colour=0x142c9c)
			embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
			embed.set_footer(text="Made By KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
			await ctx.send(embed=embed)
		except:
			embed=discord.Embed(title='''Mass DM''',description=f'''DM Not sent to {member.name}#{member.discriminator}''' ''' :x: ''',colour=0x142c9c)
			embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
			embed.set_footer(text="Made By KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
			await ctx.send(embed=embed)
				
			embed=discord.Embed(title="DM sent to all",description=f" :white_check_mark: ",colour=0x142c9c)
			embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
			embed.set_footer(text="Made By KESHAV RAJ ᴳᵒᵈ#7735",icon_url="")
			await ctx.send(embed=embed)
@f.error
async def f_error(ctx,error):
    if isinstance(error,commands.CheckFailure):
    	embed=discord.Embed(title="Mass DM",description="**Lol You Not Have Permission To Use This Cmd!** :joy: ",colour=0x142c9c)
    	embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
    	embed.set_footer(text="Made By KESHAV RAJ ᴳᵒᵈ#7735")
    	await ctx.send(embed=embed)
    if isinstance(error,commands.MissingRequiredArgument):
    	await ctx.send(f"Please say a message to send!")
		
@bot.command(name="help",hidden=True) 
async def suggest(ctx):
	await ctx.message.delete()
	embed=discord.Embed(title="Help Commands",description="**×<game_name> <accuracy> <prize_won> <last_question_status> <result>\nExample: +loco 10/10 10rs correct/wrong won**",colour=0xf81703)
	embed.add_field(name="×say",value="Use Like This ×say <text>")
	embed.add_field(name="Game Alert",value="Use Like This \n1.×start<game_name>\n2.×end<game_name>")
	embed.add_field(name="Check Ping",value='×ping')
	embed.add_field(name="Questions:",value="×q<q number>")
	embed.add_field(name="Mods Command:",value="Use Like This \n1. ×ban <Mention_User>\n2. ×kick <Mention_User>\n3.×warn <Mention_User>")
	embed.add_field(name="Mass DM Command:",value="×s <content>")
	embed.add_field(name="Permisson For Bot User",value="`NATION COMMAND` Role Required")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
	embed.set_image(url="https://cdn.discordapp.com/attachments/610979650394390528/610980511006851083/animated-chain-line.gif")
	embed.set_footer(text="KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609581613155876884/JPEG_20190810_062642.jpg")
	await ctx.send(embed=embed)
	# else:
	# 	await ctx.send("**Lol You Not Have Permission To use this commands**:wink: "+ctx.author.mention)
		

bot.run("NDk0NDY0NDM3MzE1NTY3NjM2.XzSQug.rM8yNCgsX7ivIh42NXzxdNtEXtY") # Where 'TOKEN' is 
