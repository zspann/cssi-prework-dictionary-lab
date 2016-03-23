from basketball_info import game_dictionary

# This method returns the team's status
def home_or_away(team_name):
  return game_dictionary[team_name]['status']

print home_or_away('Brooklyn Nets')

# Write a new method that returns a team's colors
def team_colors(team_name):
  colors = "{} and {}".format(game_dictionary[team_name]['team_colors'][0], game_dictionary[team_name]['team_colors'][1])
  return colors
print team_colors('Brooklyn Nets')

#Write a method that returns a string listing every player and their respective points
def player_points(team_name):
    message = ""
    for player in game_dictionary[team_name]['players'][0:4]:
          message += "{} - {} pts, ".format(player['name'],player['points'])
    message += "{} - {} pts.".format(game_dictionary[team_name]['players'][4]['name'],game_dictionary[team_name]['players'][4]['points'])
    return message
print player_points('Charlotte Hornets')

#This method should return all of the statistics for a player, given that players team and name
def player_stats(team, player_name):
    for player in game_dictionary[team]['players']:
        if player['name']==player_name:
            for stat in player:
                return "{}: {}".format(stat.capitalize(),player[stat])
print player_stats("Charlotte Hornets", "Ben Gordon")

# Return a player's shoe size.
def shoe_size(team, player_name):
    for player in game_dictionary[team]['players']:
        if player['name']==player_name:
            return player['shoe']

print shoe_size("Charlotte Hornets", "DeSagna Diop")

# Find the player on the team with the biggest shoe size and return their steals for the game
def big_shoe_stealer(team):
   biggest_shoe = 0
   steals = 0
   for player in game_dictionary[team]['players']:
       if player['shoe'] > biggest_shoe:
          biggest_shoe = player['shoe']
          steals = player['steals']
   return steals
print big_shoe_stealer('Brooklyn Nets')
