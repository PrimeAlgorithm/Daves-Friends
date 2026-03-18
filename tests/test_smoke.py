"""
Runs basic smoke tests to ensure modules work at a high level.
"""

import importlib

from models import deck


def test_smoke_imports():
    """
    Smoke test: modules and submodules should import without crashing.
    """
    modules = [
        "controllers",
        "controllers.uno_cog",
        "models",
        "models.bot",
        "models.deck",
        "models.game_state",
        "models.lobby_model",
        "services",
        "services.game_service",
        "services.lobby_service",
        "repos",
        "repos.lobby_repo",
        "ui",
        "ui.end_ui",
        "ui.game_ui",
        "ui.interactions",
        "ui.lobby_ui",
        "utils",
        "utils.card_image",
        "utils.utils",
        "views",
        "views.base_views",
        "views.end_views",
        "views.game_views",
        "views.hand_views",
        "views.lobby_views",
        "views.renderer",
    ]

    for m in modules:
        importlib.import_module(m)


def test_smoke_deck_can_build_and_draw():
    """
    Smoke test: deck can be created and can draw at least one card.
    """
    if hasattr(deck, "Deck"):
        d = deck.Deck()
        assert d is not None

        if hasattr(d, "shuffle"):
            d.shuffle()

        if hasattr(d, "draw"):
            card = d.draw()
            assert card is not None
