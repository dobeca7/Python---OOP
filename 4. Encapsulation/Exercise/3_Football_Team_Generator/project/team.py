from project.player import Player


class Team:
    def __init__(self, name:str, rating:int):
        self.__name = name
        self.__rating = rating
        self.__players = []


    def add_player(self, player:Player):

        if player in self.__players:
            return f"Player {player.name} has already joined"
        else:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name:str):
        try:
            our_player = next(filter(lambda x: x.name == player_name , self.__players))

        except StopIteration:
            return f"Player {player_name} not found"

        self.__players.remove(our_player)
        return our_player




