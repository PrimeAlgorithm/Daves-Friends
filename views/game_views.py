"""
Provides a view into the current game state.
"""

from datetime import datetime, timezone
import discord
from models.deck import (
    NUMBER_EMOJIS,
    COLOR_EMOJIS,
    Number,
    Skip,
    Reverse,
    DrawTwo,
    Wild,
    DrawFourWild,
    Card,
)
from models.lobby_model import Lobby
from utils.card_image import get_card_filename
from utils.utils import mention
from views.base_views import BaseViews

def _card_display(card: Card) -> str:
    card = str(card)
    if isinstance(card, Number):
        card = f"{COLOR_EMOJIS[card.color]}{NUMBER_EMOJIS[card.number]}"
    if isinstance(card, Skip):
        card = f"{COLOR_EMOJIS[card.color]}⏭️"
    if isinstance(card, Reverse):
        card = f"{COLOR_EMOJIS[card.color]}🔄"
    if isinstance(card, DrawTwo):
        card = f"{COLOR_EMOJIS[card.color]}➕2"
    if isinstance(card, Wild):
        card = f"🌈{COLOR_EMOJIS[card.color] if card.color else ''}"
    if isinstance(card, DrawFourWild):
        card = f"➕4🌈{COLOR_EMOJIS[card.color] if card.color else ''}"
    return card


class GameViews(BaseViews):
    """
    The game view displaying the current game state.
    """

    def game_embed(self, lobby: Lobby) -> tuple[discord.Embed, discord.File | None]:
        """
        Creates an embed for the game, displaying the game creator, the current players, whose turn
        it is, and the top card.
        """

        embed = self._build_embed(
            title="Game by " + lobby.user.name,
            desc="A game of UNO is in progress!",
            color=self.get_random_color(),
            gif=False,
        )

        players_turn = ""
        current_player_id = lobby.game.current_player()

        for index, player in enumerate(lobby.game.players()):
            if index > 0:
                players_turn += "\n"

            if player == current_player_id:
                players_turn += mention(player) + " ⬅️ Current Turn"
            else:
                players_turn += mention(player)

        embed.add_field(name="Current Turn", value=players_turn, inline=False)

                # AFK Timer (shows remaining seconds, if the game has afk_deadline set)
        afk_deadline = getattr(lobby.game, "afk_deadline", None)

        if afk_deadline is not None:
            now = datetime.now(timezone.utc)

            # If the deadline has no timezone info, assume UTC
            if getattr(afk_deadline, "tzinfo", None) is None:
                afk_deadline = afk_deadline.replace(tzinfo=timezone.utc)

            remaining = int((afk_deadline - now).total_seconds())
            remaining = max(0, remaining)

            embed.add_field(
                name="AFK Timer",
                value=f"⏳ {remaining}s remaining",
                inline=False,
            )

        card = lobby.game.top_card()
        file = None

        if card:
            filename = get_card_filename(card)
            path = f"assets/cards/{filename}"
            file = discord.File(path, filename=filename)
            embed.set_image(url=f"attachment://{filename}")

            if isinstance(card, (Wild, DrawFourWild)) and card.color:
                embed.add_field(
                    name="Chosen Color",
                    value=f"{COLOR_EMOJIS[card.color]}  **{card.color.name.capitalize()}**",
                    inline=False,
                )

        return embed, file
