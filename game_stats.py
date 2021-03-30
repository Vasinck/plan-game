class GameStats():
    def __init__(self,game_sets):
        self.game_sets = game_sets
        self.reset_stats()
        self.game_active = False
        self.high_score = self.get_heigh_score()

    def reset_stats(self):
        self.ships_left = self.game_sets.ship_limit
        self.score = 0
        self.level = 1

    def get_heigh_score(self):
        with open("D://python源程序//飞机大战Ver1.0//heigh_score.txt","r") as fp:
                high_scores = fp.read()
        
        return int(high_scores)
    
    def save_heigh_scores(self,heigh_score):
        with open("D://python源程序//飞机大战Ver1.0//heigh_score.txt","r+") as fp:
            fp.write(str(int(heigh_score)))
