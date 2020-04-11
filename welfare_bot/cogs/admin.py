from discord.ext import commands

import welfare_bot.core.permissions as permissions
import welfare_bot.core.util as util


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="load",
        description="Loads a new cog into Hannah Bot",
        usage="name"
    )
    @commands.check(permissions.is_owner)
    async def load(self, context, name: str):
        try:
            self.bot.load_extension(f"welfare_bot.cogs.{name}")
        except Exception as e:
            return await context.send(util.error(e))

        await context.send(f"✅ Successfully loaded extension: {name}")

    @commands.command(
        name="unload",
        description="Unloads a cog from Hannah Bot",
        usage="name"
    )
    @commands.check(permissions.is_owner)
    async def unload(self, context, name: str):
        try:
            self.bot.unload_extension(f"welfare_bot.cogs.{name}")
        except Exception as e:
            return await context.send(util.error(e))

        await context.send(f"✅ Successfully unloaded extension: {name}")

    @commands.command(
        name="reload",
        description="Reloads a cog a loaded cog",
        usage="name"
    )
    @commands.check(permissions.is_owner)
    async def reload(self, context, name: str):
        try:
            self.bot.unload_extension(f"welfare_bot.cogs.{name}")
            self.bot.load_extension(f"welfare_bot.cogs.{name}")
        except Exception as e:
            return await context.send(util.error(e))

        await context.send(f"✅ Successfully reloaded extension: {name}")


def setup(bot):
    bot.add_cog(Admin(bot))
