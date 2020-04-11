import time
import discord
from discord.ext import commands


class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="ping",
        description="The ping command"
    )
    async def ping(self, context):
        before = time.monotonic()

        message = await context.send("🏓 Pong")

        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 Pong: {int(ping)}ms")

    @commands.command(
        name='help',
        description='The help command!',
        aliases=['commands', 'command'],
        usage='cog'
    )
    async def help(self, context, cog:str="all"):

        help_embed = discord.Embed(
            title="Help",
            color=0x006400
        )
        help_embed.set_thumbnail(url=self.bot.user.avatar_url)
        help_embed.set_footer(
           text=f'Requested by {context.message.author.display_name}',
           icon_url=context.message.author.avatar_url
        )

        cogs = [c for c in self.bot.cogs.keys()]

        if cog == "all":
            for c in cogs:
                cog_commands = self.bot.get_cog(c).get_commands()
                commands_list = ""
                for comm in cog_commands:
                    commands_list += f"**{comm.name}** - *{comm.description}*\n"

                help_embed.add_field(
                    name=c,
                    value=commands_list,
                    inline=False
                ).add_field(
                    name='\u200b', value='\u200b', inline=False
                )

        else:
            lower_cogs = [c.lower() for c in cogs]
            if cog.lower() in lower_cogs:
                commands_list = self.bot.get_cog(cogs[lower_cogs.index(cog.lower())]).get_commands()
                help_text = ''
                for command in commands_list:
                    help_text += f'```{command.name}```\n' \
                                 f'**{command.description}**\n\n'
                    if len(command.aliases) > 0:
                        help_text += f'**Aliases :** `{"`, `".join(command.aliases)}`\n'
                    else:
                        help_text += '\n'

                    help_text += f'Format: `' \
                                 f'{command.name} {command.usage if command.usage is not None else ""}`\n\n'

                help_embed.description = help_text
            else:
                # Notify the user of invalid cog and finish the command
                await context.send('Invalid cog specified.\nUse `help` command to list all cogs.')
                return

        await context.send(embed=help_embed)


def setup(bot):
    bot.add_cog(Basic(bot))
