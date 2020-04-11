import discord
from discord.ext import commands

from welfare_bot.core.util import read_json

owners = read_json("config.json").owners


def is_owner(context):
    return context.author.id in owners


async def check_permissions(context, permissions, *, check=all):
    if context.author.id in owners:
        return True

    resolved = context.channel.permissions_for(context.author)
    return check(getattr(resolved, k, None) == v for k, v in permissions.items())


def has_permissions(*, check=all, **permissions):
    async def pred(context):
        return await check_permissions(context, permissions, check=check)

    return commands.check(pred)


def is_dm(context):
    return isinstance(context.channel, discord.DMChannel)


def can_send(context):
    return is_dm(context) or context.channel.permissions_for(context.guild.me).send_messages


def can_react(context):
    return is_dm(context) or context.channel.permissions_for(context.guild.me).add_reactions
