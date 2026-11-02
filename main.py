import os
from random import random

import discord
from discord.ext import commands
import requests
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print("Bot de contaminación conectado")


@bot.command()
async def start(ctx):
    await ctx.send("¡Hola! Soy un bot que te informa sobre la contaminación ambiental.")
    await ctx.send("Usa !contaminacion para aprender sobre el tema.")

@bot.command()
async def definicion(ctx):
    for i in range(4):
        await ctx.send('La contaminación es cuando hay presencia de '
        'sustancias dañinas, como humo, plasticos, etc en el medio ambiente.')

@bot.command()
async def prevencion(ctx):
    mensaje = """
     Medidas para prevenir la contaminación:

    - Reciclar materiales como papel, vidrio y plástico.
    - Reducir el uso de productos de un solo uso.
    - Utilizar transporte público o medios de transporte sostenibles.
    - Evitar arrojar basura en la naturaleza.
    - Apagar luces y electrodomésticos cuando no se estén usando.
    """
    await ctx.send(mensaje)

@bot.command()
async def contaminacion_imagen(ctx):
    archivos = os.listdir('imagenes')
    foto = random.choice(archivos)
    with open(f'imagenes/{foto}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def reciclje(ctx):
    await ctx.send("El reciclaje es el proceso de recolectar, tratar "
    "y transformar materiales usados (como papel, cartón, vidrio, plástico y metales)"
    " para convertirlos en nueva materia prima o producto útil.")


bot.run("")
