import discord # For Discord
from discord.utils import get  # For Discord Utils
from discord.ext import commands # For Discord Extensions
import asyncio
import logging # For Logging
from pathlib import Path # For Pathing
import json

# Def imports
import draft # randomization

# Bot Configs
cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

# Definitions
secret_file = json.load(open(cwd+'/bot_config/secrets.json'))
bot = commands.Bot(command_prefix='-', case_insenstive=True)
bot.config_token = secret_file['token']
logging.basicConfig(level=logging.INFO)

#@bot.event
#async def on_ready():
    #print(f"-----\n Logged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")
    #print("----\nLogged in as: {} : {} \n------ \n My current prefix is: -\n-----".format(bot.user.name, bot.user.id))
    #await bot.change_presence(activity=discord.Game(name=f"Hi my names {bot.user.name}. \n Use - to interact with me!")) # Changes the bots activity 
    #await bot.change_presence(activity=discord.Game(name="Hi my names {}. \n Use - to interact with me!".format(bot.user.name))) # Changes the bots activity 

@bot.command(name='draft', alises=['a'])
async def _draft(ctx):
    # Drafting for Pugs
    team1, team2 = draft._6rand(len(ctx.author.voice.channel.members))
    team1Users = []
    team1ID = []
    team2Users = []
    team2ID = []

    guild = ctx.author.guild

    channel1 = bot.get_channel(717548150117761046)
    channel2 = bot.get_channel(717548412823928882)

    for num in team1:
        team1Users.append(ctx.author.voice.channel.members[num].name)
        team1ID.append(ctx.author.voice.channel.members[num].id)

    for num in team2:
        team2Users.append(ctx.author.voice.channel.members[num].name)
        team2ID.append(ctx.author.voice.channel.members[num].id)

    for x in team1ID:
        p1 = guild.get_member(x)
        await p1.move_to(channel1, reason=None )

    for x in team2ID:
        p2 = guild.get_member(x)
        await p2.move_to(channel2, reason=None )

    await ctx.send(f'```Team 1 : {team1Users}\n\nTeam 2 : {team2Users}```')


@bot.command(name='react')
async def _react(ctx):
    msg = await ctx.send("```What game would you like to draft for?\nThe most voted one will be drafted in 15 seconds.```")
    reactions = [':val:716844878537162813','<:OW:716843789896908872>','<:lol:716843790190641223>']
    for x in reactions:
        await msg.add_reaction(x)
    await asyncio.sleep(5) 
    reactions = discord.utils.get(msg.id.reactions)
    await ctx.send(reactions)
    pass


@bot.command(name='test')
async def _test(ctx):
    guild = ctx.author.guild
    p1 = guild.get_member(184857361813340160)
    channel1 = bot.get_channel(717548150117761046)
    print(guild)
    print(p1)
    #print(len(ctx.author.voice.channel.members))
    await p1.move_to(channel1, reason=None)


bot.run(bot.config_token)

