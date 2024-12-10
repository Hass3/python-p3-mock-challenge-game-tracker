class Game:
    all = []
    def __init__(self, title):
        if not isinstance(title,str) and len(title) == 0:
            raise ValueError("Must be a type of string and greater than 0") 
        self._title = title
        Game.all.append(self)
    @property
    def title(self):
        return self._title
   
    @title.setter
    def title(self,title):
        if hasattr(self, "._title"):
            raise AttributeError("title cannot be changed")
        

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results() if isinstance(result.player, Player)]))

    def average_score(self, player):
        total_score = sum([result.score for result in player.results() ])
        num_of_results = len(player.results())
        return total_score/num_of_results

class Player:
    all = []
    def __init__(self, username):
        self.username = username
        Player.all.append(self)
    @property
    def username(self):
        return self._username
   
    @username.setter
    def username(self,username):
        if isinstance(username, str) and (2 <= len(username) <=16):
            self._username = username                                                                  
           
    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in self.results() if isinstance(result.game, Game)]))

    def played_game(self, game):
        return True if self in game.players() else False

    def num_times_played(self, game):
        return len([result.game for result in self.results() if result.game == game])

    @classmethod
    def highest_scored(cls,game):
        players = [player for player in cls.all if player in game.players()]
        if not players:
            return None
        return max(players, key=lambda player: game.average_score(player))
        
class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        if not isinstance(score,int) and not (1<= score <= 5000):
            raise ValueError("must be an integer and between 1- 5000")
        self._score = score
        Result.all.append(self)
 
    @property
    def score(self):
        return self._score
 
    @score.setter
    def score(self,score):
        if hasattr(self,"._score"):
            raise AttributeError("The score cannot be changed")
 
    @property
    def player(self):
        return self._player
   
    @player.setter                                                               
    def player(self,player):
        if not isinstance(player,Player):
            raise Exception("Must be in the player class")
        self._player = player
        
    @property
    def game(self):
        return self._game
   
    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise Exception("Must be in the Game class")
        self._game = game
