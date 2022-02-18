import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

# Question: is there a correlation between player height and 
# points averaged. 
# To answer this question we will take the average points 
# per season based on the players height and compare. 

all_seasons = pd.read_csv('all_seasons.csv') 

all_seasons.player_height = all_seasons.player_height * 0.393

all_seasons.player_weight = all_seasons.player_weight * 2.2046

all_seasons = all_seasons.round({"player_height":0})


# Give us the tallest player and the shortest player. 
# smallest = all_seasons["player_height"].min(skipna = False)
# print(smallest)
# tallest = all_seasons["player_height"].max(skipna = False)
# print(tallest)
# Shortest = 160, tallest = 231

# Create a new empty Dataframe 
height = pd.DataFrame({'Height':[], 'Points':[]})

# Loop through the possible heights and find the mean points for 
# each height than add the data to the dataframe. 
# Use a try block incase there are no players at the tested height. 
for i in range(0,232):
    try:
        grouped = all_seasons.groupby(all_seasons.player_height)
        set_height = grouped.get_group(i)
        points_avg = set_height['pts'].mean()

        fish = pd.DataFrame({'Height':[i], 'Points':[points_avg]})

        height = pd.concat([height, fish])
         
    except:
        pass
        
# Plot the dataframe and display it. 
chart = height.plot(y = 'Points', x = 'Height', kind = 'scatter')
chart.set_xlabel('Height (Inches)')
chart.set_ylabel('Average Points Per Season')
plt.show()

# There seems to be no correlation between the height of a player 
# and the average points scored. 

######################################################

# Question: Is there a link between the weight of a player 
# and the amount of games played in a season. Often heavier 
# players are viewed as more injury prone due to the extra 
# One of the metrics we can use to judge this is games played 
# per season. If a certian weight class play less games on average 
# then that is a strong indicator that they are injured more often. 

# Round all of the player weights 
all_seasons = all_seasons.round({"player_weight":0})

# Create a new empty Dataframe 
weight = pd.DataFrame({'Weight':[], 'Average games per season':[]})

# Loop through the possible weights and find the mean points for 
# each weight than add the data to the dataframe. 
# Use a try block incase there are no players at the tested weight. 
for i in range(100,450):
    try:
        grouped = all_seasons.groupby(all_seasons.player_weight)
        set_weight = grouped.get_group(i)
        games_avg = set_weight['gp'].mean()

        fish = pd.DataFrame({'Weight':[i], 'Average games per season':[games_avg]})

        weight = pd.concat([weight, fish])
         
    except:
        pass


# Plot the dataframe and display it. 
chart = weight.plot(y = 'Average games per season', x = 'Weight', kind = 'line')
chart.set_xlabel('Weight (lbs)')
plt.show()

# There seems to be a semi strong corelation between weight 
# and games played. It seems to be that having a low or a high 
# impact on a players durability. 