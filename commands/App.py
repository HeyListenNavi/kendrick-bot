import discord
from discord.ext import commands, tasks
from utils import update_token
import requests
import json
import time

class Main(commands.Cog):
    def __init__(self, ctx):
        self.ctx = ctx 
        self.auth_token_time = time.time()
        self.auth_token = ""
        self.ran_once = False
        self.update_channel = ""
        self.latest_song = "Not Like Us"
        self.vc_channel = None
        self.check_release.start()

    @commands.command()
    async def drake(self, ctx):
        await ctx.send("Drake tryna strike a chord and it's probably A-minooorrrr")
    
    @commands.command()
    async def owner(self, ctx):
        await ctx.send("Véronica (naviheylisten) owns me")
    
    @commands.command()
    async def damn(self, ctx):
        await ctx.send("https://i.scdn.co/image/ab67616d0000b2738b52c6b9bc4e43d873869699")

    @commands.command()
    async def ovo(self, ctx):
        await ctx.send("more like OV-hoe")
        time.sleep(10)
        await ctx.send("OV-HOE")
        await ctx.send("ov-hoeee")

    @commands.command()
    async def braids(self, ctx):
        await ctx.send("WHAT IS IT THE BRAIDS??")

    @commands.command()
    async def ask(self, ctx, question: str):
        if question == "who's the biggest hater?":
            await ctx.send("let me say i'm the biggest hater")
            time.sleep(5)
            await ctx.send("i hate the way that you walk, the way that you talk, i hate the way that you dress")
            await ctx.send("i hate the way that you sneak diss, if i catch a flight it's gon' be direct")
        elif question == "who's the biggest bitch?":
            await ctx.send("<@679857034702618637>")
        elif question == "what's your latest song?":
            await ctx.send(f"{self.latest_song}")
        elif question == "who are the big three?":
            await ctx.send("motherfuck the big three, it's just big me")

    @commands.command()
    async def loverboy(self, ctx):
        await ctx.send("certified loverboy? certified pedophile")
        await ctx.send("WOP WOP WOP WOP")
    
    @commands.command()
    async def wop(self, ctx):
        await ctx.send("WOP WOP WOP WOP !!! dot fuck 'em up")
        await ctx.send("wop wop wop wop !!!! i'ma do my stuff")

    @commands.command()
    async def join(self, ctx):
        try:
            self.vc_channel = await ctx.author.voice.channel.connect()
            await ctx.send("listop")
        except:
            await ctx.send("uhm, please join a vc first ;-; or maybe something went wrong who knows")

    @commands.command()
    async def euphoria(self, ctx):
        if self.vc_channel != None:
            self.vc_channel.stop()
            await ctx.send("playing gaby's favorite!! euphoria")
            self.vc_channel.play(discord.FFmpegPCMAudio("euphoria.mp3"))
        else:
            await ctx.send("sorryyy, i couldn't play the song")

    @commands.command()
    async def notlikeus(self, ctx):
        if self.vc_channel != None:
            self.vc_channel.stop()
            await ctx.send("wop wop wop wop i'ma do my stuff")
            self.vc_channel.play(discord.FFmpegPCMAudio("Not Like Us.mp3"))
        else:
            await ctx.send("sorryyy, i couldn't play the song")
    
    @commands.command()
    async def grahams(self, ctx):
        if self.vc_channel != None:
            self.vc_channel.stop()
            await ctx.send("dear adonis") 
            self.vc_channel.play(discord.FFmpegPCMAudio("meet the grahams.mp3"))
        else:
            await ctx.send("sorryyy, i couldn't play the song")
    
    @commands.command()
    async def leave(self, ctx):
        try:
            await self.vc_channel.disconnect()
            await ctx.send("bai baii")
        except:
            await ctx.send("couldn't disconnect")

    @commands.command()
    async def pause(self, ctx):
        if self.vc_channel.is_playing():
            self.vc_channel.pause()
        else:
            self.vc_channel.resume()
    
    @tasks.loop(seconds = 1)
    async def check_release(self):
        if self.ran_once == False:
            self.auth_token = update_token(3600)
            self.ran_once = True
        else:
            update = update_token(self.auth_token_time)
            if update != None:
                self.auth_token = update
                self.auth_token_time = time.time()
        
        url = "https://api.spotify.com/v1/artists/2YZyLoL8N0Wb9xBt1NhZWg/albums?include_groups=single&limit=1"
        headers = {
            "Authorization": f"Bearer {self.auth_token}",
        }

        response = requests.get(url, headers=headers)
        latest_song = response.json()["items"][0]["name"]

        channel = self.ctx.get_channel(975279824585240586)

        if latest_song != self.latest_song:
            self.latest_song = latest_song
            for ping in range(0, 20): 
                await channel.send(f"<@679857034702618637> <@416383743041863680>")
                time.sleep(1)
            await channel.send("<@679857034702618637> YOOO NEW KENDRICK SONGGGG <@416383743041863680>")
            await channel.send("DRUM ROLL PLEASEEEEEEEE")
            await channel.send(f"||{self.latest_song}||")
                
async def setup(ctx):
    await ctx.add_cog(Main(ctx))
