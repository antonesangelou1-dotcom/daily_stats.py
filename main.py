import discord
from discord.ext import commands, tasks
from datetime import datetime

# Daily statistics
daily_messages = 0
daily_joins = 0
daily_leaves = 0
daily_deleted = 0
daily_edited = 0

STATS_CHANNEL_ID = 0
STATS_HOUR = 23
STATS_MINUTE = 45
async def send_daily_stats():
    channel = bot.get_channel(STATS_CHANNEL_ID)

    if channel is None:
        return

    embed = discord.Embed(
        title="📊 DAILY SERVER STATS",
        description="Τα στατιστικά της ημέρας",
        timestamp=datetime.now()
    )

    embed.add_field(name="💬 Messages", value=str(daily_messages), inline=True)
    embed.add_field(name="🟢 Joins", value=str(daily_joins), inline=True)
    embed.add_field(name="🔴 Leaves", value=str(daily_leaves), inline=True)
    embed.add_field(name="🗑️ Deleted", value=str(daily_deleted), inline=True)
    embed.add_field(name="✏️ Edited", value=str(daily_edited), inline=True)

    await channel.send(embed=embed)
e
@tasks.loop(minutes=1)
async def daily_stats_checker():
    now = datetime.now()

    if now.hour == STATS_HOUR and now.minute == STATS_MINUTE:
        await send_daily_stats()


def start_daily_stats():
    if not daily_stats_checker.is_running():
        daily_stats_checker.start()
      def register_message(message):
    global daily_messages

    if not message.author.bot:
        daily_messages += 1
    def register_join():
    global daily_joins
    daily_joins += 1


def register_leave():
    global daily_leaves
    daily_leaves += 
def register_deleted():
    global daily_deleted
    daily_deleted += 1


def register_edited():
    global daily_edited
    daily_edited += 1
def reset_daily_stats():
    global daily_messages
    global daily_joins
    global daily_leaves
    global daily_deleted
    global daily_edited

    daily_messages = 0
    daily_joins = 0
    daily_leaves = 0
    daily_deleted = 0
    daily_edited = 0
import discord
from discord.ext import commands
from daily_stats import (
    register_message,
    register_join,
    register_leave,
    register_deleted,
    register_edited,
    start_daily_stats
)
@bot.event
async def on_ready():
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    start_daily_stats()
@bot.event
async def on_message(message):
  @bot.event
async def on_message(message):
    register_message(message)
    await bot.process_commands(message)
@bot.event
async def on_member_join(member):
    register_join()


@bot.event
async def on_member_remove(member):
    register_leave()
@bot.event
async def on_message_delete(message):
    register_deleted()
@bot.event
async def on_message_edit(before, after):
    register_edited()STATS_CHANNEL_ID = 123456789
STATS_HOUR = 23
STATS_MINUTE = 45

bot_instance = None
channel = bot_instance.get_channel(STATS_CHANNEL_ID)
def start_daily_stats(bot):
    global bot_instance

    if now.hour == STATS_HOUR and now.minute == STATS_MINUTE:
    await send_daily_stats()
    reset_daily_stats()
