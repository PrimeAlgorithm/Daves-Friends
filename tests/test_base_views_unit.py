"""
Tests shared Discord view helper behavior.
"""

import asyncio
from types import SimpleNamespace

from models.game_state import GameError
from views.base_views import BaseViews


def _make_interaction(response_done: bool = False):
    calls: list[tuple[str, bool]] = []
    state = {"done": response_done}

    async def send_response(*, embeds, ephemeral):
        assert embeds
        calls.append(("response", ephemeral))
        state["done"] = True

    async def send_followup(*, embeds, ephemeral):
        assert embeds
        calls.append(("followup", ephemeral))

    interaction = SimpleNamespace(
        response=SimpleNamespace(
            is_done=lambda: state["done"], send_message=send_response
        ),
        followup=SimpleNamespace(send=send_followup),
    )

    return interaction, calls


def test_render_error_uses_initial_response_when_interaction_is_new():
    """
    Error rendering should use the initial interaction response before deferring.
    """
    interaction, calls = _make_interaction()

    asyncio.run(
        BaseViews().render_error(
            "Join Error", GameError("Already joined", private=True), interaction
        )
    )

    assert calls == [("response", True)]


def test_render_error_uses_followup_after_interaction_is_acknowledged():
    """
    Error rendering should fall back to a follow-up after an interaction is acknowledged.
    """
    interaction, calls = _make_interaction(response_done=True)

    asyncio.run(
        BaseViews().render_error(
            "Join Error", GameError("Already joined", private=True), interaction
        )
    )

    assert calls == [("followup", True)]
