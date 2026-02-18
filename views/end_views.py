from views.base_views import BaseViews

class EndViews(BaseViews):
    def end_embed(self):
        return self._build_embed(title="End of Game", desc="someone won", color=self.get_random_color())