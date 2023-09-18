# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio, datetime, pytz
import yt_dlp as youtube_dl
from json import loads
from discord.ext import commands
import requests
TOKEN = 'MTE1MjgzMDAwMzQwNzUwMzQ1Mg.Gw6rVz.nss0z6tmAul8HuPctob7_TSUtgHR0mGhH-m5vA'

client = discord.Client(intents=discord.Intents.all())

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}
 
ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}
 
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
 
 
# youtube 음악과 로컬 음악의 재생을 구별하기 위한 클래스 작성.
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
 
        self.data = data
 
        self.title = data.get('title')
        self.url = data.get('url')
 
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
 
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
 
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
 
 
# 음악 재생 클래스. 커맨드 포함.
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""
 
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
 
        await channel.connect()
 
    @commands.command()
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""
 
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
 
        await ctx.send(f'Now playing: {query}')
 
    @commands.command()
    async def yt(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""
 
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
 
        await ctx.send(f'Now playing: {player.title}')
 
    @commands.command()
    async def stream(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""
 
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
 
        await ctx.send(f'Now playing: {player.title}')
 
    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""
 
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")
 
        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")
 
    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""
 
        await ctx.voice_client.disconnect()
 
    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("음성 채널에 접속하시지 않았습니다!")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
 
 
intents = discord.Intents.default()
intents.message_content = True
 
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
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
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("VsCode"))

@client.event
async def on_message(message):
    if '안녕' in message.content: # 메세지 감지
        await message.channel.send ("어서오세요! {}님!".format( message.author.mention))
    if message.content == "명령어": # 메세지 감지
        await message.channel.send ("임베드 / 추가예정")
    if message.content == "임베드": # 메세지 감지
        embed = discord.Embed(title="임베드워즈", description="부제목",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xccf8ff)

        embed.add_field(name="내가 고자라니", value="== 이지안", inline=False)

        embed.set_footer(text="Bot Made by. KinJeok", icon_url="https://discord.com/channels/@me/1152843749337083924/1152847243246841856")
        embed.set_thumbnail(url="https://discord.com/channels/@me/1152843749337083924/1152847243246841856")
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
