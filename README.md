# Basketball Stats

## Overview
Dictionaries offer an organized way to store a lot of information because of the way that each value can be accessed by a unique key. Many of the APIs you'll be working with send data in the form of nested arrays and dictionaries. Being comfortable iterating through nested data structures will allow you to access and manipulate data from a variety of sources.

## Instructions

In this lab, we've gotten a bunch of data from the Yahoo Sports API. There is a nested dictionary in `basketball_info.py` that defines a game, with two teams, their players, and the players stats.

Using the power of Python, and the game dictionary in `basketball_info.py`, write functions in `basketball.py` to complete the following:

1.Return the name of the home team and the away team. We've done this one for you to get started.

2.Return a team's colors, as a string: `Black and Red` or `Green and White`

3.Return the points scored by each player on a team. There should be a ' - ' between each player and their points. A comma and a space should separate each name.
```
>>> print player_points('Chicago Bulls')
Michael Jordan - 28 pts, Scottie Pippen - 22 pts, Dennis Rodman - 18 pts, Tony Kukoc - 20 pts, Ron Artest - 12 pts.
```

4.Return all the stats for a player, given a player's team and name.
```
>>> print player_stats('Chicago Bulls', 'Scottie Pippen')
Name: Michael Jordan
Slam_dunks: 4
Number: 23
Points: 28
Shoe: 15
Steals: 5
```

5.Given a team and a player's name, return that player's shoe size. Hint: try finding the player first (the same way you did with `player_stats`) then look for his shoe size.


6.For a given team, find the player with the largest shoe size and return their number of steals.
