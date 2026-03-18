"""
Tests that Discord component views can be restored after a restart.
"""

from types import SimpleNamespace

from ui.game_ui import GameUI
from ui.lobby_ui import LobbyUI


def test_lobby_view_is_persistent():
    """
    Lobby buttons should be persistent so the bot can reattach them on startup.
    """
    view = LobbyUI(renderer=None, lobby_service=None, lobby_views=None)

    assert view.is_persistent()


def test_game_view_is_persistent():
    """
    Game buttons should be persistent so the bot can reattach them on startup.
    """
    view = GameUI(
        renderer=None,
        lobby=SimpleNamespace(user=SimpleNamespace(id=1), game=None),
        game_service=None,
    )

    assert view.is_persistent()
