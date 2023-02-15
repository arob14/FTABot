import disnake
from disnake.ext import commands
import os
import aiosqlite
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

bot = commands.Bot()

# When the bot is ready, run this code.
@bot.event
async def on_ready():
    async with aiosqlite.connect("main.db") as db:
        async with db.cursor() as cursor:
            await cursor.execute('CREATE TABLE IF NOT EXISTS tribe_registry (user STRING, ign STRING, tribe STRING, gt STRING, spec_id INTEGER )')
    print("The bot is ready!")

bot.load_extension("cogs.register")

# Login to Discord with the bot's token.
bot.run(DISCORD_TOKEN)
