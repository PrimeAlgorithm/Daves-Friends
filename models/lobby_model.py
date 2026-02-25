from dataclasses import dataclass
from models.game_state import GameState
from discord.interactions import User


@dataclass
class Lobby:
    user: User
    game: GameState
    main_message: int | None
