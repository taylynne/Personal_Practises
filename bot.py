import discord
import random
from discord.ext import commands
import _asyncio

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$', '!'))

@bot.event
async def on_ready():
    print("Logged in as ")
    print(bot.user.name)
    print(bot.user.id)
    print("-------")

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(":thinking:")
    await ctx.send(a+b)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello there! :)")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Learning Bot", description="Bestest pupper ever: Patches! Needs home even to this day")

    #my info I guess
    embed.add_field(name="Author", value="SpaceOres")

    await ctx.send(embed=embed)

@bot.command(name='8ball',
             description="Answers a yes or no question",
             brief = "Answers questions from the ~beyond~",
             aliases=['eightball', '8-ball', 'eight_ball', '8_ball'],
             pass_context=True)
async def eightball(ctx):
    possible_responses = [
        'Yeah, no way is that ever happening',
        'The answer is a little foggy, try asking again',
        'Not likely... not likely at all',
        'Oh yeah, I could see that happening',
        'A resounding "Yes!!" for that one',
        'Meh. Maybe',
        'Too hard to tell, sorry',
    ]
    await ctx.send(random.choice(possible_responses) + ', ' + ctx.message.author.mention)

@bot.command(name='FunAnimals',
             description="Just a bunch of random animal photos or gifs!",
             brief="Need a laugh? Have an animal.",
             aliases=["animals", "animalpic", "funnyAnimals", "AnimalPics",])
async def funnyAnimals(ctx):
    pics= [
        "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
        "https://i.imgur.com/pDLHlrb.mp4",
        "https://i.imgur.com/DwbTTa5.mp4",
        "https://i.imgur.com/R7IwCGH.mp4",
        "https://i.imgur.com/nIoLVSZ.jpg",
        "https://i.imgur.com/7YxYVsg.mp4",
        "https://i.imgur.com/85queET.png",
        "https://i.imgur.com/TzRCxS3.mp4",
        "https://i.imgur.com/mvLk8jT.jpg",
        "https://i.imgur.com/BpohKEg.mp4",
        "https://i.imgur.com/g4nZZkv.mp4",
    ]
    await ctx.send(random.choice(pics))
    await ctx.send("That was a cute one! :new_moon_with_face: ")

#@bot.event()
async def shush(ctx):
    if message.author.id == "368967340634669066":
        options = [
            "OMG GATOR BOOTZ!!!",
            "Sick, Gator!",
            "Wow, so badasss man",
            "EYY YAAEYY"
        ]
        await bot.send(random.choice(options))
        await asyncio.sleep(600)
    elif message.author.id != "368967340634669066":
        optns = [
            "Hey there son!",
            "Just testing this shit out man",
            "Stupid ID maybe isn't working :thinking:",
        ]
        await bot.send(random.choice(optns))
        await asyncio.sleep(600)

# async def sush(ctx):
#     if message.author.id == "368967340634669066":
#         options = [
#             "OMG GATOR BOOTZ!!!",
#             "Sick, Gator!",
#             "Wow, so badasss man",
#             "EYY YAAEYY"
#         ]
#         await bot.send(random.choice(options))
#     elif message.author.id != "368967340634669066":
#         optns = [
#             "Hey there son!",
#             "Just testing this shit out man",
#             "Stupid ID maybe isn't working :thinking:",
#         ]
#         await bot.send(random.choice(optns))
#         await asyncio.sleep(600)


bot.run("NDU2OTc4MjkxNjI3MTMwODgw.DgSZ0A.dNB-0kGUD5rydKjER3LZfapa8eE")
