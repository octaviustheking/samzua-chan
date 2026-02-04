import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name}, here to dissolve any disputes, at your service!')


@bot.event
async def on_member_join(member):
    await member.send(f'Welcome to Samueltopia, {member.name} <3 uwu nya meow')
    await member.send('Some server rules: do not type abhay')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "abhay" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention}, his name is banned! Please do not use that word uwu')

    if "fuck you" in message.content.lower():
        await message.reply(f'fuck you {message.author.mention} :joy:')

    if "67" in message.content.lower():
        await message.reply(f'6 7 67 67 67 6776 funy hahahahah funnny :joy:')

    if "scaras" in message.content.lower():
        await message.reply(f'<@1326380607168581733>')

    if message.content.lower() == "wha":
        await message.reply('syfm zhenbo')

    await bot.process_commands(message)


@bot.command()
@commands.has_role("new role")
async def pet3(ctx, target: discord.Member):
    pet3 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+++]")
    pet2 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [++]")
    pet1 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+]")
    pet = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash")
    execution = discord.utils.get(ctx.guild.roles, name="execution")
    negative = discord.utils.get(ctx.guild.roles, name="negative social credit")
    bum = discord.utils.get(ctx.guild.roles, name="bum")
    positive = discord.utils.get(ctx.guild.roles, name="positive social credit")
    if pet3:
        await target.add_roles(pet3)
        await target.remove_roles(pet2)
        await target.remove_roles(pet1)
        await target.remove_roles(pet)
        await target.remove_roles(execution)
        await target.remove_roles(negative)
        await target.remove_roles(bum)
        await target.remove_roles(positive)
        await ctx.send(f'Demoted {target.mention} to Premium Execution Trash [+++]')
    else:
        await ctx.send('Role does not exist!')


@bot.command()
@commands.has_role("new role")
async def pet2(ctx, target: discord.Member):
    pet3 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+++]")
    pet2 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [++]")
    pet1 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+]")
    pet = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash")
    execution = discord.utils.get(ctx.guild.roles, name="execution")
    negative = discord.utils.get(ctx.guild.roles, name="negative social credit")
    bum = discord.utils.get(ctx.guild.roles, name="bum")
    positive = discord.utils.get(ctx.guild.roles, name="positive social credit")
    if pet3:
        await target.add_roles(pet2)
        await target.remove_roles(pet3)
        await target.remove_roles(pet1)
        await target.remove_roles(pet)
        await target.remove_roles(execution)
        await target.remove_roles(negative)
        await target.remove_roles(bum)
        await target.remove_roles(positive)
        await ctx.send(f'Set {target.mention} to Premium Execution Trash [++]')
    else:
        await ctx.send('Role does not exist!')


@bot.command()
@commands.has_role("new role")
async def pet1(ctx, target: discord.Member):
    pet3 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+++]")
    pet2 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [++]")
    pet1 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+]")
    pet = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash")
    execution = discord.utils.get(ctx.guild.roles, name="execution")
    negative = discord.utils.get(ctx.guild.roles, name="negative social credit")
    bum = discord.utils.get(ctx.guild.roles, name="bum")
    positive = discord.utils.get(ctx.guild.roles, name="positive social credit")
    if pet3:
        await target.add_roles(pet1)
        await target.remove_roles(pet3)
        await target.remove_roles(pet2)
        await target.remove_roles(pet)
        await target.remove_roles(execution)
        await target.remove_roles(negative)
        await target.remove_roles(bum)
        await target.remove_roles(positive)
        await ctx.send(f'Set {target.mention} to Premium Execution Trash [+]')
    else:
        await ctx.send('Role does not exist!')


@bot.command()
@commands.has_role("new role")
async def pet(ctx, target: discord.Member):
    pet3 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+++]")
    pet2 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [++]")
    pet1 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+]")
    pet = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash")
    execution = discord.utils.get(ctx.guild.roles, name="execution")
    negative = discord.utils.get(ctx.guild.roles, name="negative social credit")
    bum = discord.utils.get(ctx.guild.roles, name="bum")
    positive = discord.utils.get(ctx.guild.roles, name="positive social credit")
    if pet3:
        await target.add_roles(pet)
        await target.remove_roles(pet3)
        await target.remove_roles(pet2)
        await target.remove_roles(pet1)
        await target.remove_roles(execution)
        await target.remove_roles(negative)
        await target.remove_roles(bum)
        await target.remove_roles(positive)
        await ctx.send(f'Set {target.mention} to Premium Execution Trash')
    else:
        await ctx.send('Role does not exist!')


@bot.command()
@commands.has_role("new role")
async def execution(ctx, target: discord.Member):
    pet3 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+++]")
    pet2 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [++]")
    pet1 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+]")
    pet = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash")
    execution = discord.utils.get(ctx.guild.roles, name="execution")
    negative = discord.utils.get(ctx.guild.roles, name="negative social credit")
    bum = discord.utils.get(ctx.guild.roles, name="bum")
    positive = discord.utils.get(ctx.guild.roles, name="positive social credit")
    if pet3:
        await target.add_roles(execution)
        await target.remove_roles(pet3)
        await target.remove_roles(pet2)
        await target.remove_roles(pet1)
        await target.remove_roles(pet)
        await target.remove_roles(negative)
        await target.remove_roles(bum)
        await target.remove_roles(positive)
        await ctx.send(f'Set {target.mention} to execution')
    else:
        await ctx.send('Role does not exist!')


@bot.command()
@commands.has_role("new role")
async def negative(ctx, target: discord.Member):
    pet3 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+++]")
    pet2 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [++]")
    pet1 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+]")
    pet = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash")
    execution = discord.utils.get(ctx.guild.roles, name="execution")
    negative = discord.utils.get(ctx.guild.roles, name="negative social credit")
    bum = discord.utils.get(ctx.guild.roles, name="bum")
    positive = discord.utils.get(ctx.guild.roles, name="positive social credit")
    if pet3:
        await target.add_roles(negative)
        await target.remove_roles(pet3)
        await target.remove_roles(pet2)
        await target.remove_roles(pet1)
        await target.remove_roles(pet)
        await target.remove_roles(execution)
        await target.remove_roles(bum)
        await target.remove_roles(positive)
        await ctx.send(f'Set {target.mention} to negative social credit')
    else:
        await ctx.send('Role does not exist!')


@bot.command()
@commands.has_role("new role")
async def bum(ctx, target: discord.Member):
    pet3 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+++]")
    pet2 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [++]")
    pet1 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+]")
    pet = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash")
    execution = discord.utils.get(ctx.guild.roles, name="execution")
    negative = discord.utils.get(ctx.guild.roles, name="negative social credit")
    bum = discord.utils.get(ctx.guild.roles, name="bum")
    positive = discord.utils.get(ctx.guild.roles, name="positive social credit")
    if pet3:
        await target.add_roles(bum)
        await target.remove_roles(pet3)
        await target.remove_roles(pet2)
        await target.remove_roles(pet1)
        await target.remove_roles(pet)
        await target.remove_roles(execution)
        await target.remove_roles(negative)
        await target.remove_roles(positive)
        await ctx.send(f'Set {target.mention} to bum')
    else:
        await ctx.send('Role does not exist!')


@bot.command()
@commands.has_role("new role")
async def positive(ctx, target: discord.Member):
    pet3 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+++]")
    pet2 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [++]")
    pet1 = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash [+]")
    pet = discord.utils.get(ctx.guild.roles, name="Premium Execution Trash")
    execution = discord.utils.get(ctx.guild.roles, name="execution")
    negative = discord.utils.get(ctx.guild.roles, name="negative social credit")
    bum = discord.utils.get(ctx.guild.roles, name="bum")
    positive = discord.utils.get(ctx.guild.roles, name="positive social credit")
    if pet3:
        await target.add_roles(positive)
        await target.remove_roles(pet3)
        await target.remove_roles(pet2)
        await target.remove_roles(pet1)
        await target.remove_roles(pet)
        await target.remove_roles(execution)
        await target.remove_roles(negative)
        await target.remove_roles(bum)
        await ctx.send(f'Set {target.mention} to Positive Social Credit')
    else:
        await ctx.send('Role does not exist!')


@bot.command()
@commands.has_role("new role")
async def ping(ctx, target: discord.Member, times: int):
    for i in range(times):
        await ctx.send(f'{target.mention}')


@bot.command()
@commands.has_role("new role")
async def ban(ctx, target: discord.Member, reason):
    await ctx.send(f'Banning {target.mention}')
    await target.ban(reason=reason)


@bot.command()
@commands.has_role("new role")
async def kick(ctx, target: discord.Member, reason):
    await ctx.send(f'Kicking {target.mention}')
    await target.kick(reason=reason)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
