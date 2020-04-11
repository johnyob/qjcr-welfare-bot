import logging

from welfare_bot.core.util import read_json
from welfare_bot.core.bot import Bot, HelpFormat

from welfare_bot.cogs import cogs

config = read_json("config.json")

logging.basicConfig(level=logging.INFO)
logging.info("Logging in...")


bot = Bot(
    command_prefix=config.prefix,
    prefix=config.prefix,
    command_attrs=dict(hidden=True),
    help_command=HelpFormat()
)


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name} - {bot.user.id}")
    bot.remove_command('help')

    for cog in cogs:
        bot.load_extension(f"welfare_bot.cogs.{cog}")

bot.run(config.token)





