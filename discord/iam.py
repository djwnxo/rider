# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio, datetime, pytz

from json import loads
from discord.ext import commands
import requests
TOKEN = 'MTE1MjgzMDAwMzQwNzUwMzQ1Mg.GEqLUq.FcfHR8NfXUfX46wo1ki1obtEy4TUDGt96BGeYI'

client = discord.Client(intents=discord.Intents.all())


 
# youtube 음악과 로컬 음악의 재생을 구별하기 위한 클래스 작성.
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def 명령어(self, ctx):
        await ctx.send("임베드 / 유튜브")

    @commands.command()
    async def 유튜브(self,ctx):
        embed = discord.Embed(title="KinJeok", description="official youtube channel",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xccf8ff)

        embed.add_field(name="URL", value="https://www.youtube.com/channel/UC38G1mjjjGAJdRHbbbvIIUw", inline=False)

        embed.set_footer(text="Bot Made by. KinJeok", icon_url="https://yt3.googleusercontent.com/D7et0EF7ez2G1Lpws8vQ12EJ9d0VR5eN6E2En6mjBOfpirlo1LqN6W-lqkce9fkUK2VHPCKh2g=s900-c-k-c0x00ffffff-no-rj")
        embed.set_thumbnail(url="https://yt3.googleusercontent.com/D7et0EF7ez2G1Lpws8vQ12EJ9d0VR5eN6E2En6mjBOfpirlo1LqN6W-lqkce9fkUK2VHPCKh2g=s900-c-k-c0x00ffffff-no-rj")
        await ctx.send (embed=embed)
intents = discord.Intents.default()
intents.message_content = True
 
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("/"),
    description='Relatively simple music bot example',
    intents=intents,
)
 
 
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
 
 
async def main():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.start(TOKEN)


@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("Run.client")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Vscode"))

@client.event
async def on_message(message):
    if '안녕' in message.content: # 메세지 감지
        await message.channel.send ("어서오세요! {}님!".format( message.author.mention))
    if message.content == "납작복숭아": # 메세지 감지
        await message.channel.send ("뭐")
    if message.content == "긴적": # 메세지 감지
        await message.channel.send ("양진중학교대표씹존잘")
    if message.content == "임베드": # 메세지 감지
        embed = discord.Embed(title="Example", description="example description",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xccf8ff)

        embed.add_field(name="ex", value="ex", inline=False)

        embed.set_footer(text="Bot Made by. KinJeok", icon_url="https://yt3.googleusercontent.com/D7et0EF7ez2G1Lpws8vQ12EJ9d0VR5eN6E2En6mjBOfpirlo1LqN6W-lqkce9fkUK2VHPCKh2g=s900-c-k-c0x00ffffff-no-rj")
        embed.set_thumbnail(url="https://yt3.googleusercontent.com/D7et0EF7ez2G1Lpws8vQ12EJ9d0VR5eN6E2En6mjBOfpirlo1LqN6W-lqkce9fkUK2VHPCKh2g=s900-c-k-c0x00ffffff-no-rj")
        await message.channel.send (embed=embed)
        

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
async def run_bot_and_main():
    await asyncio.gather(
        client.start(TOKEN),
        main()
    )

# Run the bot and the main function concurrently
if __name__ == '__main__':
    asyncio.run(run_bot_and_main())
    