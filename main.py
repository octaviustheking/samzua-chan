import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random

load_dotenv()
token = os.getenv('TOKEN')

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

ball_answers = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes, definitely.', 'You may rely on it', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes', 'Signs point to yes.',
                "Don't count on it.", 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.',
                'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Reply hazy, try again.']


@bot.event
async def on_ready():
    print(f'{bot.user.name}, here to dissolve any disputes, at your service!')


@bot.event
async def on_member_join(member):
    await member.send(f'Welcome to Samueltopia, {member.name} <3 uwu nya meow')
    await member.send('Type "augusta sucks" in the server to get started!')
    await member.send('Type "!commands" to learn commands!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "abhay" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention}, his name is banned! Please do not mention that name uwu')

    if "fuck you" in message.content.lower():
        await message.reply(f'fuck you {message.author.mention} :joy:')

    if "67" in message.content.lower():
        await message.reply(f'6 7 67 67 67 6776 funy hahahahah funnny :joy:')

    if "scaras" in message.content.lower():
        await message.reply(f'<@1326380607168581733>')

    if message.content.lower() == "wha":
        await message.reply('syfm zhenbo')

    if "augusta sucks" in message.content.lower():
        await message.reply('you fucking idiot why did you have to be so mean')

    if "masha" in message.content.lower():
        await message.reply('syfm abhay')

    if discord.utils.get(message.guild.roles, name='Premium Execution Trash [+++]') in message.author.roles:
        await message.add_reaction('🤡')

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
    await target.add_roles(pet3)
    await target.remove_roles(pet2)
    await target.remove_roles(pet1)
    await target.remove_roles(pet)
    await target.remove_roles(execution)
    await target.remove_roles(negative)
    await target.remove_roles(bum)
    await target.remove_roles(positive)
    await ctx.send(f'Demoted {target.mention} to Premium Execution Trash [+++]')


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
    await target.add_roles(pet2)
    await target.remove_roles(pet3)
    await target.remove_roles(pet1)
    await target.remove_roles(pet)
    await target.remove_roles(execution)
    await target.remove_roles(negative)
    await target.remove_roles(bum)
    await target.remove_roles(positive)
    await ctx.send(f'Set {target.mention} to Premium Execution Trash [++]')
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
    await target.add_roles(pet1)
    await target.remove_roles(pet3)
    await target.remove_roles(pet2)
    await target.remove_roles(pet)
    await target.remove_roles(execution)
    await target.remove_roles(negative)
    await target.remove_roles(bum)
    await target.remove_roles(positive)
    await ctx.send(f'Set {target.mention} to Premium Execution Trash [+]')


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
    await target.add_roles(pet)
    await target.remove_roles(pet3)
    await target.remove_roles(pet2)
    await target.remove_roles(pet1)
    await target.remove_roles(execution)
    await target.remove_roles(negative)
    await target.remove_roles(bum)
    await target.remove_roles(positive)
    await ctx.send(f'Set {target.mention} to Premium Execution Trash')


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
    await target.add_roles(execution)
    await target.remove_roles(pet3)
    await target.remove_roles(pet2)
    await target.remove_roles(pet1)
    await target.remove_roles(pet)
    await target.remove_roles(negative)
    await target.remove_roles(bum)
    await target.remove_roles(positive)
    await ctx.send(f'Set {target.mention} to execution')


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
    await target.add_roles(negative)
    await target.remove_roles(pet3)
    await target.remove_roles(pet2)
    await target.remove_roles(pet1)
    await target.remove_roles(pet)
    await target.remove_roles(execution)
    await target.remove_roles(bum)
    await target.remove_roles(positive)
    await ctx.send(f'Set {target.mention} to negative social credit')


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
    await target.add_roles(bum)
    await target.remove_roles(pet3)
    await target.remove_roles(pet2)
    await target.remove_roles(pet1)
    await target.remove_roles(pet)
    await target.remove_roles(execution)
    await target.remove_roles(negative)
    await target.remove_roles(positive)
    await ctx.send(f'Set {target.mention} to bum')


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
    await target.add_roles(positive)
    await target.remove_roles(pet3)
    await target.remove_roles(pet2)
    await target.remove_roles(pet1)
    await target.remove_roles(pet)
    await target.remove_roles(execution)
    await target.remove_roles(negative)
    await target.remove_roles(bum)
    await ctx.send(f'Set {target.mention} to Positive Social Credit')


@bot.command()
@commands.has_role("new role")
async def ping(ctx, target: discord.Member, times: int):
    if times > 25:
        await ctx.send('Please do not ping someone more than 25 times, unlike SOME mod abusers...')
    for i in range(times):
        await ctx.send(f'{target.mention}')


@bot.command()
@commands.has_role("new role")
async def ban(ctx, target: discord.Member, *, reason):
    await ctx.send(f'Banning {target.mention}, reason: {reason}')
    await target.ban(reason=reason)


@bot.command()
@commands.has_role("new role")
async def kick(ctx, target: discord.Member, *, reason):
    await ctx.send(f'Kicking {target.mention}, reason: {reason}')
    await target.kick(reason=reason)


@bot.command()
@commands.has_role("new role")
async def nick(ctx, target: discord.Member, *, nickname):
    await target.edit(nick=nickname)
    await ctx.send(f"Changed {target.mention}'s nickname to {nickname}")


@bot.command()
async def purge(ctx, number: int):
    await ctx.channel.purge(limit=number + 1)


@bot.command()
async def ball(ctx):
    answer = random.randint(0, 19)
    await ctx.reply(ball_answers[answer])
    

@bot.command()
async def commands(ctx):
    await ctx.send("COMMANDS\nall parameters are required\n*=new role required\n!commands\n!positive (user)*\n!bum (user)*\n!negative (user)*\n!execution (user)*\n!pet (user)*\n!pet1 (user)*\n!pet2 (user)*\n!pet3 (user)*\n!ping (user) (times)*\n!ban (user) (reason)*\n!kick (user) (reason)*\n!nick (user) (nickname)*\n!purge (number of messages)\n!ball (question)")



bot.run(token, log_handler=handler, log_level=logging.DEBUG)
