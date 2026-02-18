import discord
from models.lobby_model import Lobby
from utils.utils import mention
from views.base_views import BaseViews
from models.deck import NUMBER_EMOJIS, COLOR_EMOJIS

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
        card_display = COLOR_EMOJIS[card.color] + NUMBER_EMOJIS[card.number]

        embed.add_field(name="Card On Top", value=card_display, inline=False)

        return embed