from project.player import Player


class Guild:
    def __init__(self, name:str, ):
        self.name = name
        self.players = []

    def assign_player(self,new_player: Player):
        if new_player.guild != self.name and new_player.guild != "Unaffiliated":
            return f"Player {new_player.name} is in another guild."

        elif new_player.guild == self.name:
            return f"Player {new_player.name} is already in the guild."

        else:
            self.players.append(new_player)
            new_player.guild = self.name
            return  f"Welcome player {new_player.name} to the guild {self.name}"



    def kick_player(self, player_name):
        for new_player in self.players:
            if new_player.name == player_name:
                new_player.guild = "Unaffiliated"
                self.players.remove(new_player)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."


    def guild_info(self):
        all_players = "\n".join(p.player_info() for p in self.players)
        return f"Guild: {self.name}\n" \
                f"{all_players}\n"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
print(guild.kick_player(player))

