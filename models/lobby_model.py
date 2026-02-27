"""
Provides a model to represent a lobby.
"""

from dataclasses import dataclass

from discord.interactions import User

from models.game_state import GameState


@dataclass
class Lobby:
    """
    A lobby, including the user that created it, the game state, and the message ID.
    """

    user: User
    game: GameState
    main_message: int | None
