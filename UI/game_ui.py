from UI.interactions import Interactions
import discord

class GameUI(Interactions):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="1️⃣ Call Uno", style=discord.ButtonStyle.success)
    async def call_uno(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await interaction.response.send_message("this command is a work in progress")

    @discord.ui.button(label="👀 View Cards", style=discord.ButtonStyle.blurple)
    async def view_cards(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await interaction.response.send_message("this command is a work in progress")