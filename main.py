# Welcome to the main Python file for the Discord bot "pyramid bot thing"
# The author of this bot hasn't made a bot in 2 years so he's really rusty lol
# Currently all the imports, log commands, events, commands, and token are in this singular file
# In future updates we will make the commands in separate files (they're called cogs I think?)

# imports
try:
    import nextcord
    from nextcord.ext import commands
    import logging
    import random
    import asyncio
except ImportError:
	print("LIBRARIES FAILED TO IMPORT.") # i doubt anything will happen but just in case

# logging - all output in nextcord.log
logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# constants and stuff
MAIN_GUILD_ID = 1113836310529048597



bot = commands.Bot()


# events
@bot.event
async def on_ready():
    activity = nextcord.Game(name="bwomp", type=3)
    await bot.change_presence(status=nextcord.Status.online, activity=activity)
    print()
    print("—————————————————————————————————————————")
    print(f"⎸   {bot.user} is active!   ⎹")
    print("—————————————————————————————————————————")
    print()



# COMMANDS


# test

@bot.slash_command(description = "A test command to check if the bot can send text or not") # ctx test
async def test(interaction: nextcord.Interaction):
    await interaction.send("i is working")
    print("The command \"test\" was called")

@bot.slash_command(description = "a test command to check if the bot can send embeds or not") # embed test
async def embedtest(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title = "yes embeds work")
    embed.add_field(name = "Field 1", value = "Value 1 (inline)", inline=True)
    embed.add_field(name = "Field 2", value = "Value 2 (not inline)", inline=False)
    embed.set_footer(text = "footer thing")
    await interaction.response.send_message(embed=embed)
    print("The command \"embedtest\" was called")


# general commands

@bot.slash_command(description="literally just copies you") # copy
async def copy(interaction: nextcord.Interaction,  *, arg):
    await interaction.send(arg)
    print("The command \"copy\" was called")

@bot.slash_command(description="returns with internet pong") # ping
async def ping(interaction: nextcord.Interaction):
    await interaction.send(f"guess what! your pong is **{round(bot.latency * 1000)} ms**" )
    print("The command \"ping\" was called")


# math things

@bot.slash_command(description = "Generates a random number between two specified numbers") # random number
async def randomnumber(interaction: nextcord.Interaction, first: str = nextcord.SlashOption(description = "The first number"), last: str = nextcord.SlashOption(description = "The last number")):
    await interaction.send(f"The number generated between {first} and {last} is `{random.randint(int(first), int(last)+1)}`.")
    print("The command \"randomnumber\" was called")

@bot.slash_command(description = "Sends the average between two specified numbers") # average
async def average(interaction: nextcord.Interaction, firstInAverage: str = nextcord.SlashOption(description = "The first number"), lastInAverage: str = nextcord.SlashOption(description = "The last number")):
    await interaction.send(f"The average between {firstInAverage} and {lastInAverage} is `{(firstInAverage + lastInAverage) / 2}`.")
    print("The command \"average\" was called")


# discord utility

@bot.slash_command(description = "kicks a user") # kicks user
async def kick(interaction: nextcord.Interaction, user_to_kick: nextcord.Member):
    await interaction.guild.kick(user_to_kick)
    await interaction(f"**{user_to_kick.mention} was kicked by {interaction.author.mention}.** bro gave them the boot")
    print("The command \"kick\" was called")










bot.run('MTA0MTAyNTgxMjEyOTkxMDc5NA.G8zuB9.3E-hPv8v6GVxKttGxBG3RyEvmH-86wbXh0VSvM')