from typing import Type, Union

import discord
import datetime
from discord.ext import commands

# céeation du bot
bot = commands.Bot(command_prefix='!')


# détecter quand le bot est on
@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(activity=discord.Game("discord"), status=discord.Status.idle)


# créer un commande
@bot.command()
async def regles(ctx):

   await ctx.send("Les règles sont:\n 1.pas spam \n 2.pas d'insultes")

@bot.command()
async def bienvenue(cxt, new_memdre: discord.Member):
    pseudo = new_memdre.mention
    await cxt.send(f"bienvenue a {pseudo} sur le serveur discord n'oublie pas de faire !regles")

@bienvenue.error

async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("La commande est !bienvenue @pseudo")

@bot.command()
async def time(ctx):
    t = datetime.datetime.now()
    await ctx.send(f"il est {t.hour}h {t.minute}min et {t.second} sec")

# jeton pour que le bot se connect (online)
jeton = "ODI2ODg1MTk2OTU4NjYyNjg5.YGS-2Q.iGyy6mZN2nHOy23FqwwLeMSTeKE"

print("Lancement du bot...")

# connecter au serv.
bot.run(jeton)
