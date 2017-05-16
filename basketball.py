from basketball_info import game_dictionary

# This method returns the team's status
def home_or_away(team_name):
  return game_dictionary[team_name]['status']


# Write a new method that returns a team's colors
def team_colors(team_name):
    colors = game_dictionary[team_name]['team_colors']
    colors = " and ".join(colors)
    return colors

#Write a method that returns a string listing every player and their respective points
def player_points(team_name):
    player_list = ""
    for player in game_dictionary[team_name]['players']:
        player_list += player['name'] + " - " + str(player['points']) + " pts, "
    player_list = player_list[:-2]
    player_list += "."
    return player_list

#This method should return all of the statistics for a player, given that players team and name
def player_stats(team, player_name):
    stats_list = ""
    for player in game_dictionary[team]['players']:
        if player['name'] == player_name:
            stats_list += (
            "Name: " + player_name + "\n" +
            "Slam_dunks: " + str(player['slam_dunks']) + "\n" +
            "Number: " + str(player['number']) + "\n" +
            "Points: " + str(player['points']) + "\n" +
            "Shoe: " + str(player['shoe']) + "\n" +
            "Steals: " + str(player['steals'])
            )
    return stats_list

# Return a player's shoe size.
def shoe_size(team, player_name):
    size = ""
    for player in game_dictionary[team]['players']:
        if player['name'] == player_name:
            size  = player['shoe']
    return size

# Find the player on the team with the biggest shoe size and return their steals for the game
def big_shoe_stealer(team):
    shoe_counter = 0
    steals_counter = 0
    for player in game_dictionary[team]['players']:
        if player['shoe'] > shoe_counter:
            shoe_counter = player['shoe']
            steals_counter = player['steals']
    return steals_counter
