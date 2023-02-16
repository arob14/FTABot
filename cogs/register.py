import disnake
from disnake.ext import commands
import aiosqlite


# TODO, /update tribe, /update ign, updateGT, updateSpecID, /info

class RegisterCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name="register",
        description="idk figure it out"
    )
    async def register(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User, in_game_name: str,
                       tribe: str, gamertag: str, spec_id: int = 0):
        async with aiosqlite.connect("main.db") as db:
            async with db.cursor() as cursor:
                await cursor.execute('SELECT user FROM tribe_registry WHERE user = ?', (str(user),))
                data = await cursor.fetchone()
                if data:
                    await cursor.execute('UPDATE tribe_registry '
                                         'SET ign=?, tribe=?, gt=?, spec_id=? '
                                         'WHERE user=?',
                                         (in_game_name, tribe, gamertag, spec_id, str(user),))
                    await inter.response.send_message("Registry Updated")
                else:
                    await cursor.execute('INSERT INTO tribe_registry (user, ign, tribe, gt, spec_id) '
                                         'VALUES(?, ?, ?, ?, ?)',
                                         (str(user), in_game_name, tribe, gamertag, spec_id))
                    role = disnake.utils.get(inter.guild.roles, name="Survivor")
                    await user.add_roles(role)
                    await inter.response.send_message("Registered")

                await db.commit()

    @commands.slash_command(
        name="info",
        description="gives player info"
    )
    async def info(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User):
        async with aiosqlite.connect("main.db") as db:
            async with db.cursor() as cursor:
                await cursor.execute('SELECT user FROM tribe_registry WHERE user = ?', (str(user),))
                data = await cursor.fetchone()
                if data:
                    await cursor.execute('SELECT ign, tribe, gt, spec_id FROM tribe_registry WHERE user = ?',
                                         (str(user),))
                    data = await cursor.fetchone()
                    await inter.response.send_message(data)
                else:
                    await inter.response.send_message("User is not registered")

    @commands.slash_command(
        description="Update player tribename"
    )
    async def update_tribe(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User, tribe: str):
        async with aiosqlite.connect("main.db") as db:
            async with db.cursor() as cursor:
                await cursor.execute('SELECT user FROM tribe_registry WHERE user = ?', (str(user),))
                data = await cursor.fetchone()
                if data:
                    await cursor.execute('UPDATE tribe_registry SET tribe=? WHERE user = ?', (tribe, str(user),))
                    await inter.response.send_message("Registry updated")
                    await db.commit()
                else:
                    await inter.response.send_message("User not registered")

    @commands.slash_command(
        description="Update player name"
    )
    async def update_ign(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User, ign: str):
        async with aiosqlite.connect("main.db") as db:
            async with db.cursor() as cursor:

                await cursor.execute('SELECT user FROM tribe_registry WHERE user = ?', (str(user),))
                data = await cursor.fetchone()
                if data:
                    await cursor.execute('UPDATE tribe_registry SET ign=? WHERE user = ?', (ign, str(user),))
                    await inter.response.send_message("Registry updated")
                    await db.commit()
                else:
                    await inter.response.send_message("User not registered")
    @commands.slash_command(
        description="Update player gamertag"
    )
    async def update_gt(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User, gamertag: str):
        async with aiosqlite.connect("main.db") as db:
            async with db.cursor() as cursor:
                await cursor.execute('SELECT user FROM tribe_registry WHERE user = ?', (str(user),))
                data = await cursor.fetchone()
                if data:
                    await cursor.execute('UPDATE tribe_registry SET gt=? WHERE user = ?', (gamertag, str(user),))
                    await inter.response.send_message("Registry updated")
                    await db.commit()
                else:
                    await inter.response.send_message("User not registered")

    @commands.slash_command(
        description="Update player specimen implant number"
    )
    async def update_spec_id(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User, spec_id: int):
        async with aiosqlite.connect("main.db") as db:
            async with db.cursor() as cursor:
                await cursor.execute('SELECT user FROM tribe_registry WHERE user = ?', (str(user),))
                data = await cursor.fetchone()
                if data:
                    await cursor.execute('UPDATE tribe_registry SET spec_id=? WHERE user = ?', (spec_id, str(user),))
                    await inter.response.send_message("Registry updated")
                    await db.commit()
                else:
                    await inter.response.send_message("User not registered")


def setup(bot: commands.Bot):
    bot.add_cog(RegisterCommand(bot))
