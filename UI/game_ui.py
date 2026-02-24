from UI.interactions import Interactions
import discord

class GameUI(Interactions):
    def __init__(self, lobby):
        super().__init__()
        self.lobby = lobby

    @discord.ui.button(label="1️⃣ Call Uno", style=discord.ButtonStyle.success)
    async def call_uno(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await interaction.response.send_message("this command is a work in progress")

    @discord.ui.button(label="👀 View Cards", style=discord.ButtonStyle.blurple)
    async def view_cards(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        from models.game_state import Phase
        from models.deck import format_card

        user_id = interaction.user.id
        game = self.lobby.game

        if game.phase() != Phase.PLAYING:
            await interaction.response.send_message("Game is not currently active.", ephemeral=True)
            return

        hand = game.hand(user_id)

        if not hand:
            await interaction.response.send_message("You are not in this game.", ephemeral=True)
            return

        cards_display = []
        for index, card in enumerate(hand):
            cards_display.append(f"**{index}**  →  {format_card(card)}")

        embed = discord.Embed(
            title="Your Hand",
            description="\n".join(cards_display),
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)