import discord
from discord.ext import commands

from welfare_bot.core.util import read_json

import os
from random import choice


class Welfare(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.messages = read_json("./resources/messages.json")

    @commands.command(
        name="cheermeup",
        description="I'll send a message to try cheer you up or make you feel better :smiling_face_with_3_hearts:"
    )
    async def cheer_me_up(self, context):
        await context.send(choice(self.messages.cheermeup))

    @commands.command(
        name="compliment",
        description="I'll send you a compliment to make you happy :heart:"
    )
    async def compliment(self, context):
        await context.send(choice(self.messages.compliment).format(user=context.author.display_name))

    @commands.command(
        name="quote",
        description="I'll send a random inspirational quote"
    )
    async def quote(self, context):
        await context.send(choice(self.messages.quote))

    @commands.command(
        name="wholesome",
        description="I'll send you a wholesome message"
    )
    async def wholesome(self, context):
        await context.send(choice(self.messages.wholesome))

    @commands.command(
        name="tally",
        description="I'll send you a pictures of a v cute doggo :dog: :heart_exclamation:"
    )
    async def tally(self, context):
        img = choice(os.listdir("./resources/tally"))
        await context.send(file=discord.File(f"./resources/tally/{img}"))

    @commands.command(
        name="hugs",
        description="I'll give you a hug :hugging:"
    )
    async def hugs(self, context):
        await context.send(choice(self.messages.hugs).format(user=context.author.display_name))

    @commands.command(
        name="hotchocolate",
        description="Lets have some whittards hot chocolate"
    )
    async def hotchocolate(self, context):
        await context.send(choice(self.messages.hotchocolate).format(user=context.author.display_name))

    @commands.command(
        name="selfcare",
        description="Some tips and ideas on how to care for yourself and be happy :)"
    )
    async def selfcare(self, context):
        await context.send(choice(self.messages.selfcare))


def setup(bot):
    bot.add_cog(Welfare(bot))



