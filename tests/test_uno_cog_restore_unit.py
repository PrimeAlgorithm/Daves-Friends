"""
Tests startup restore behavior in the UNO cog.
"""

from datetime import datetime, timezone
from types import SimpleNamespace

from controllers.uno_cog import UnoCog


def test_reset_restored_turn_timer_gives_player_new_afk_window():
    """
    Restored games should get a fresh AFK window instead of expiring immediately.
    """
    save_calls = []
    fake_cog = SimpleNamespace(
        lobby_service=SimpleNamespace(save=lambda: save_calls.append("saved"))
    )
    lobby = SimpleNamespace(game=SimpleNamespace(state={"afk_deadline": None}))

    UnoCog._reset_restored_turn_timer(fake_cog, lobby)  # pylint: disable=protected-access

    assert lobby.game.state["afk_deadline"] > datetime.now(timezone.utc)
    assert save_calls == ["saved"]
