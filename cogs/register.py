import disnake
from disnake.ext import commands


class RegisterCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name="register",
        description="idk figure it out"
    )
    async def register(self, inter: disnake.ApplicationCommandInteraction, member: disnake.User, in_game_name: str, tribe: str, gamertag: str, spec_id: int = -1):
        await inter.response.send_message("Member: " + member + " IGN: " + in_game_name + " Tribe: " + tribe + " GT: " + gamertag + " spec id: " + str(spec_id))


def setup(bot: commands.Bot):
    bot.add_cog(RegisterCommand(bot))
