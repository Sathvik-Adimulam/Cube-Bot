import discord 
import dotenv 
import os    

from discord.ext import commands 

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

class CubingBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix=".", intents=intents)

        @self.command()
        async def hi(ctx):
            await ctx.channel.send(f"Hi {ctx.author.display_name}!")

    async def on_ready(self):
        print("--------------------------------------------------")
        print(f"Logged in as {self.user} <{self.user.id}>")
        print("--------------------------------------------------")

    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to the Cubing Place!'
        )


bot = CubingBot()
bot.run(TOKEN)