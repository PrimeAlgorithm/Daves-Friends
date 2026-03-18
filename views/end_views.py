"""
Provides a view into the end of a game.
"""

import discord

from views.base_views import BaseViews
from models.lobby_model import Lobby
from utils.utils import mention


class EndViews(BaseViews):
    """
    The game view displaying the end of a game.
    """

    def end_embed(self, lobby: Lobby) -> discord.Embed:
        """
        Creates an embed for the end of a game, displaying the result and statistics about the
        game.
        """

        winner_id = lobby.game.state["winner"]
        hands = lobby.game.state["hands"]
        turn_count = lobby.game.turn_count()
        ended_in_draw = lobby.game.ended_in_draw()

        desc = "The game ended in a draw."
        if winner_id is not None:
            desc = f"Winner: {mention(winner_id)}"
        elif not ended_in_draw:
            desc = "No winner."

        embed = self._build_embed(
            title="🎉 GAME OVER 🎉",
            desc=desc,
            color=self.get_random_color(),
        )

        results_text = ""

        for player_id, cards in hands.items():
            results_text += f"{mention(player_id)} — {len(cards)} cards remaining\n"

        embed.add_field(name="Final Results", value=results_text, inline=False)
        embed.add_field(name="Total Turns Played", value=str(turn_count), inline=False)

        return embed
