class GameStats:
    """跟踪游戏的统计信息"""
    # 游戏启动时处于活动状态
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True
        self.high_score = 0
        # 让游戏一开始处于非活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ships_limit
        self.score = 0
        self.level = 1
