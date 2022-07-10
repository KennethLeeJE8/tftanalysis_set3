# tftanalysis_set3

This is an analysis done on Set 3 of Teamfight Tactics, a game made by Riot Games. 
![Teamfight Tactics Set 3](https://github.com/KennethLeeJE8/tftanalysis_set3/blob/main/images/tftset3.jpg)

League of Legends Teamfight Tactics(TFT) is a game I have been playing since 2019 and decided to start this analysis on set 3, which I played briefly during 2020. Riot, the maker of the game, releases a new set, which is a new version of the game with different champions, mechanics and traits.

Some terms to note:

Meta: The most effective composition in this version of the game
Slam: When you forced to make an item because you need to improve your team

The questions I aim to answer are:

- To know which team compositions were the most popular and had the highest winrate, in other words, the meta during set 3
- To know which comp to build given the champions or items you currently have
- Best champions to buy that are in the most successful comps (Highest winrate)
- To know which items go on which champions and which champions go with an item, so you can achieve the most optimal item combination (know which items are an okay slam)
- The dataset I am using tracks games played in high level play, which is in the top 1% of players, consisting of Challenger, Grandmaster and Master rank. I will be using this data to determine what the optimal level of play was during set 3.

## Data Structure (What the raw data looks like):

Here is some information about the variables collected in the dataset. 

gameId: Unique identifier of game, all 8 players in the same game have the same identifier

gameDuration: How long the game lasted, which ends when someone gets 1st place

level: level

lastRound: The last round you participated in 

ranked: The rank you obtained in the game, 1st is the best and 8th is the worst

inGameDuration: how long you were in game

combination: A list of key values showing combination and count

key: Combination

value: the number of combinations

champion: json file, list of key values
key : Champion name

value : Item, Stars

Item : Champion's items

Stars : Enhance Champion n (Min 1 Star, Max 3 Star)

1 Star : 1-star champion,

2 Star : 1-star champion three

3 Star : 2-star champion three


## Purpose(Business Goal):

To know what the meta was at the time and what team compositions would yield the best results overall
To know what to do in certain situations, given the champions you have or components you have what to build
Best champions to hold that are in the most successful comps (Highest winrate)
To know which items go on which champions and which champions go with an item, given already built or need to slam
Plan for TFT Analysis:

## Data Trends:

A game is grouped into 8 rows, where each row is a player in the game, identify game by gameId
combinations are displayed in alphabetical order, not the most helpful
champions are also random order
Items are indexed, consult the table
## Data Prep:

Group games to make it easier, can eliminate id after grouped, list of Dataframes
Group game failed because of inconsistencies in data, only cherry picking rows that meet certain conditions
Turn items id's into item names?
Order the combinations in term of count, Highest Trait count is the comp, right now it is alphabetical
turn json into dictionary
## Data Vis:

Most played, successful comp
Most played, successful champ
Most used, successful item
Distribution of comp, array of traits, putting highest count at the front
Highest item-character correlation
Does in-game duration affect anything
Trait and item combo
Most successful spat for comp character
Most common item pair, what 2 items go together the most
## Pred:

Given one champion in the comp, determine the comp
What does the typical comp look like, the average, ideal?
Given you get a champion, what should I put in for the highest winrate
Given one component and one champion, what is the next component you should go for, based on the most common item for the champion
Given x number of components, what champions and itemss should pick up to play strongest board
Given other ppl's comp, what should you go, best matchups, correlated to the most successful comp I guess

# Pre-processing Data

Working throught the dataset, I noticed that many of the champion columns for players where scarce, less than 7 champions on the board, max being 9(not including Force of Nature(+1 unit on board)). Because we want quality data, we will only be taking end-game comps, these are the following assumptions on end game comps:

Player needs to be at least level 7
Need at least 8 units on board (use FON to have 8 units but lv7)
At least 4 full items on board
Because to the time constraints, we are only going to explore fully developed compositions, this is okay due to the abundance of data in this dataset, we will be liberal in choosing only fully developed team compositions to explore.
