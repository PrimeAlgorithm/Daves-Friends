import discord
from models.lobby_model import Lobby
from utils.utils import mention
from views.base_views import BaseViews
from models.deck import (
    NUMBER_EMOJIS, COLOR_EMOJIS,
    Number, Skip, Reverse, DrawTwo, Wild, DrawFourWild, Card
)

def _card_display(card: Card) -> str:
    if isinstance(card, Number):
        return f"{COLOR_EMOJIS[card.color]}{NUMBER_EMOJIS[card.number]}"
    if isinstance(card, Skip):
        return f"{COLOR_EMOJIS[card.color]}⏭️"
    if isinstance(card, Reverse):
        return f"{COLOR_EMOJIS[card.color]}🔄"
    if isinstance(card, DrawTwo):
        return f"{COLOR_EMOJIS[card.color]}➕2"
    if isinstance(card, Wild):
        return f"🌈{COLOR_EMOJIS[card.color] if card.color else ''}"
    if isinstance(card, DrawFourWild):
        return f"➕4🌈{COLOR_EMOJIS[card.color] if card.color else ''}"
    return str(card)

class GameViews(BaseViews):
    def game_embed(self, lobby: Lobby) -> discord.Embed:
        embed = self._build_embed(title="Game by " + lobby.user.name, desc="A game of UNO is in progress!", color=self.get_random_color(), gif=False)

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
        card = lobby.game.top_card()
        embed.add_field(name="Card On Top", value=_card_display(card) if card else "(none)", inline=False)

        return embed