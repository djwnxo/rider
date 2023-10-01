# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio, datetime, pytz, json
from discord.ext import commands
 
TOKEN = 'MTE1MjgzMDAwMzQwNzUwMzQ1Mg.GoQxlw.J7GRiz6wanktTJqXHdfoufkDBzzBxBxjXGccfU'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_guild_join(guild):
    with open("cogs/jsonfiles/mutes.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role[str(guild.id)] = None
    
    with open("cogs/jsonfiles/mutes.json", "w") as f:
        json.dump(mute_role, f, indent=4)
 
@client.event
async def on_guild_remove(guild):
    with open("cogs/jsonfiles/mutes.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role.pop(str(guild.id))
    
    with open("cogs/jsonfiles/mutes.json", "w") as f:
        json.dump(mute_role, f, indent=4)

class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def 도움말(self, ctx):
        await ctx.send("임베드 (임베드를 보여줍니다.)\n유튜브 (긴적의 유튜브 채널을 보여줍니다.)\n 청소 n (n의 수 만큼 채팅기록을 삭제합니다.)")

    @commands.command()
    async def 유튜브(self,ctx):
        embed = discord.Embed(title="KinJeok", description="official youtube channel",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xccf8ff)

        embed.add_field(name="URL", value="https://www.youtube.com/channel/UC38G1mjjjGAJdRHbbbvIIUw", inline=False)

        embed.set_footer(text="Bot Made by. KinJeok", icon_url="https://cdn.discordapp.com/attachments/1152830894525128816/1157525515339583599/IMG_3426.PNG?ex=6518ed24&is=65179ba4&hm=de68df4c27d5f9ebaa2e486cd806dcc1cf45f49aa9c1eddea3bdd751c41146b2&")
        embed.set_thumbnail(url="https://yt3.googleusercontent.com/D7et0EF7ez2G1Lpws8vQ12EJ9d0VR5eN6E2En6mjBOfpirlo1LqN6W-lqkce9fkUK2VHPCKh2g=s900-c-k-c0x00ffffff-no-rj")
        await ctx.send (embed=embed)
    def __init__(self, client):
        self.client = client        
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setmuterole(self, ctx, role: discord.Role):
        with open("discord/mutes.json", "r") as f:
            mute_role = json.load(f)
            
            mute_role[str(ctx.guild.id)] = role.name
    
        with open("discord/mutes.json", "w") as f:
            json.dump(mute_role, f, indent=4)
            
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Mute role has been set!", value=f"The mute role has been changed to '{role.mention}' for this guild. All members who are muted will be equipped with this role.", inline=False)
            
        await ctx.send(embed=conf_embed)
        
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        with open("discord/mutes.json", "r") as f:
            role = json.load(f)
        
            mute_role = discord.utils.get(ctx.guild.roles, name=role[str(ctx.guild.id)])
 
        await member.add_roles(mute_role)
 
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Muted", value=f"{member.mention} has been muted by {ctx.author.mention}.", inline=False)
        await ctx.send(embed=conf_embed)
        
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        with open("discord/mutes.json", "r") as f:
            role = json.load(f)
        
            mute_role = discord.utils.get(ctx.guild.roles, name=role[str(ctx.guild.id)])
 
        await member.remove_roles(mute_role)
 
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Unmuted", value=f"{member.mention} has been unmuted by {ctx.author.mention}.", inline=False)
        await ctx.send(embed=conf_embed)
        
intents = discord.Intents.default()
intents.message_content = True
 
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("/"),
    description='Relatively simple music bot example',
    intents=intents,
)

async def main():
    async with bot:
        await bot.add_cog(cmd(bot))
        await bot.start(TOKEN)


@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("Run.client")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Vscode"))

@client.event
async def on_message(message):
    if '안녕' in message.content: # 메세지 감지
        await message.channel.send ("어서오세요! {}님!".format( message.author.mention))
    if message.content == "임베드": # 메세지 감지
        embed = discord.Embed(title="Example", description="example description",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xccf8ff)

        embed.add_field(name="ex", value="ex", inline=False)

        embed.set_footer(text="Bot Made by. KinJeok", icon_url="https://cdn.discordapp.com/attachments/1152830894525128816/1157525515339583599/IMG_3426.PNG?ex=6518ed24&is=65179ba4&hm=de68df4c27d5f9ebaa2e486cd806dcc1cf45f49aa9c1eddea3bdd751c41146b2&")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1152830894525128816/1157525515339583599/IMG_3426.PNG?ex=6518ed24&is=65179ba4&hm=de68df4c27d5f9ebaa2e486cd806dcc1cf45f49aa9c1eddea3bdd751c41146b2&")
        await message.channel.send (embed=embed)
        
    if message.content.startswith ("/청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0xccf8ff)
            embed.set_footer(text="Bot Made by. KinJeok", icon_url="https://cdn.discordapp.com/attachments/1152830894525128816/1157525515339583599/IMG_3426.PNG?ex=6518ed24&is=65179ba4&hm=de68df4c27d5f9ebaa2e486cd806dcc1cf45f49aa9c1eddea3bdd751c41146b2&")
            await message.channel.send(embed=embed)

        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

    if message.content == ("/전체청소"):
        i = message.author.guild_permissions.administrator

        if i is True:
            await message.channel.purge(limit=None)  # Clear all messages in the channel
            embed = discord.Embed(
                title="메시지 삭제 알림",
                description="채팅 전체가 관리자 {}님의 요청으로 인해 정상 삭제 조치되었습니다".format(message.author),
                color=0xccf8ff,
            )
            embed.set_footer(
                text="Bot Made by. KinJeok",
                icon_url="https://cdn.discordapp.com/attachments/1152830894525128816/1157525515339583599/IMG_3426.PNG?ex=6518ed24&is=65179ba4&hm=de68df4c27d5f9ebaa2e486cd806dcc1cf45f49aa9c1eddea3bdd751c41146b2&",
            )
            await message.channel.send(embed=embed)

        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send(
                "{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention)
            )
 
    
# 봇을 실행시키기 위한 토큰을 작성해주는 곳
async def run_bot_and_main():
    await asyncio.gather(
        client.start(TOKEN),
        main()
    )

# Run the bot and the main function concurrently
if __name__ == '__main__':
    asyncio.run(run_bot_and_main())
    