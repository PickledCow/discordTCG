#!/user/bin/env python

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import os, sys, random
import mechanics, config
import json

# For cogs when needed
mechanics.initData()
startup_extensions = ['cogs.infocommands', 'cogs.deckbuilding', 'cogs.collecting']
config.matches = {}

# Bot setup
TOKEN = config.TOKEN
activity = discord.Game(name=f"Version {config.VERSION}. Use =help!")
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix='=', activity=activity, intents=intents)


# Load extensions
@bot.event
async def on_ready():
    pass


class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def on_ready(self):
        await tree.synced(guild=discord.Object(id=1031351276736348160))
        self.synced = True
        print("Bot Online!")

class MainMenu(discord.ui.View):
    def __init__(self, author):
        super().__init__()
        self.author = author
        self.value = None
    
    @discord.ui.button(label="🛒 Shop", style=discord.ButtonStyle.success)
    async def main_menu_shop(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Here is a Shop.")
    
    @discord.ui.button(label="📦 Inventory", style=discord.ButtonStyle.primary)
    async def main_menu_inventory(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Here is a Shop.")
    
    @discord.ui.button(label="🛠️ Crafting", style=discord.ButtonStyle.secondary)
    async def main_menu_crafting(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Here is a Shop.")
    
    @discord.ui.button(label="🏦 Bazzar", style=discord.ButtonStyle.secondary)
    async def main_menu_bazzar(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Here is a Shop.")

    @discord.ui.button(label="🌿 Gumtree", style=discord.ButtonStyle.secondary)
    async def main_menu_bazzar(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Here is a Shop.")

    @discord.ui.button(label="💎 Get Gems", style=discord.ButtonStyle.success, disabled=True)
    async def main_menu_getgem(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Here is a Shop.")

    @discord.ui.button(label="🚫 Quit", style=discord.ButtonStyle.danger)
    async def main_menu_quit(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="Goodbye~", embed=None, view=None)
        self.value = False
        self.stop()

    # Make sure only the original person can interact
    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user.id == self.author.id



@bot.command()
async def main(ctx):

    embed=discord.Embed(title="Y.A.T.S. Official Trading Card Game™ (YOTCG™)", color=0x5170dd)
    embed.add_field(name="Select From the Buttons Below!", value="Yo", inline=False)

    view = MainMenu(ctx.author)
    await ctx.reply(view=view, embed=embed)

    
@bot.command()
async def card(ctx, arg):
    embed=discord.Embed(title="You've found a card!", color=0x5170dd)
    arg_list = arg.split(" ")
    print(" ".join(arg_list[1:]))
    embed.add_field(name="Unzan Armour (Holo)", value="Rarity: <:burst:1034848190651973753><:filled:1034848188349304914><:filled:1034848188349304914><:filled:1034848188349304914><:filled:1034848188349304914>", inline=False)
    embed.set_image(url=arg)
    await ctx.send(embed=embed)


bot.run(TOKEN)
