# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio, datetime, pytz
from json import loads
import requests
TOKEN = 'MTE1MjgzMDAwMzQwNzUwMzQ1Mg.GENNfw.EfZMcpTU8q051Ez0oHNFl8GwXsdnp74VNEqVXs'
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("VsCode"))

@client.event
async def on_message(message):
    if message.content == "ㅎㅇ": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))
    if message.content == "임베드": # 메세지 감지
        embed = discord.Embed(title="임베드워즈", description="부제목",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xccf8ff)

        embed.add_field(name="내가 고자라니", value="== 이지안", inline=False)

        embed.set_footer(text="Bot Made by. KinJeok", icon_url="https://discord.com/channels/@me/1152843749337083924/1152847243246841856")
        embed.set_thumbnail(url="https://discord.com/channels/@me/1152843749337083924/1152847243246841856")
        await message.channel.send (embed=embed)

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run(TOKEN)