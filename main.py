import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}! Я буду расказывать тебе об Экологии в виде мемов')

@bot.command()
async def eco(ctx):
    await ctx.send(f'не просто эко а экология!О которой я:{bot.user} буду расказывать тебе в виде мемов')

@bot.command()
async def info(ctx):
    await ctx.send(f'Меня зовут{bot.user} создан для подрастковой аудитории.Я хочю чтобы молодёжь берегла природу')

@bot.command()
async def slogan(ctx):
    await ctx.send(f'Экология важнее заводов')    

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

bot.run("token")
