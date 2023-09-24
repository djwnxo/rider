import discord
import asyncio
import datetime
import pytz
from discord.ext import commands

TOKEN = 'MTE1MjgzMDAwMzQwNzUwMzQ1Mg.GEqLUq.FcfHR8NfXUfX46wo1ki1obtEy4TUDGt96BGeYI'

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("/"),
    description='Relatively simple music bot example',
    intents=discord.Intents.all(),
)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 명령어(self, ctx):
        await ctx.send("임베드 / 유튜브")

    @commands.command()
    async def 유튜브(self, ctx):
        embed = discord.Embed(
            title="KinJeok",
            description="official youtube channel",
            timestamp=datetime.datetime.now(pytz.timezone('UTC')),
            color=0xccf8ff
        )

        embed.add_field(name="URL", value="https://www.youtube.com/channel/UC38G1mjjjGAJdRHbbbvIIUw", inline=False)

        embed.set_footer(text="Bot Made by. KinJeok", icon_url="https://yt3.googleusercontent.com/D7et0EF7ez2G1Lpws8vQ12EJ9d0VR5eN6E2En6mjBOfpirlo1LqN6W-lqkce9fkUK2VHPCKh2g=s900-c-k-c0x00ffffff-no-rj")
        embed.set_thumbnail(url="https://yt3.googleusercontent.com/D7et0EF7ez2G1Lpws8vQ12EJ9d0VR5eN6E2En6mjBOfpirlo1LqN6W-lqkce9fkUK2VHPCKh2g=s900-c-k-c0x00ffffff-no-rj")
        await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if '안녕' in message.content:
        await message.channel.send("어서오세요! {}님!".format(message.author.mention))
    if message.content == "납작복숭아":
        await message.channel.send("뭐")
    if message.content == "임베드":
        embed = discord.Embed(
            title="Example",
            description="example description",
            timestamp=datetime.datetime.now(pytz.timezone('UTC')),
            color=0xccf8ff
        )

        embed.add_field(name="내가 고자라니", value="== 이지안", inline=False)

        embed.set_footer(text="Bot Made by. KinJeok", icon_url="https://yt3.googleusercontent.com/D7et0EF7ez2G1Lpws8vQ12EJ9d0VR5eN6E2En6mjBOfpirlo1LqN6W-lqkce9fkUK2VHPCKh2g=s900-c-k-c0x00ffffff-no-rj")
        embed.set_thumbnail(url="https://yt3.googleusercontent.com/D7et0EF7ez2G1Lpws8vQ12EJ9d0VR5eN6E2En6mjBOfpirlo1LqN6W-lqkce9fkUK2VHPCKh2g=s900-c-k-c0x00ffffff-no-rj")
        await message.channel.send(embed=embed)

@bot.command()
async def 특별명령(ctx):
    # 봇의 특별한 명령어 처리
    await ctx.send("특별한 명령어를 실행합니다.")

async def main():
    bot.add_cog(Music(bot))
    try:
        await bot.start(TOKEN)
    except KeyboardInterrupt:
        await bot.close()
        await bot.logout()
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the bot and the main function concurrently
if __name__ == '__main__':
    asyncio.run(main())
