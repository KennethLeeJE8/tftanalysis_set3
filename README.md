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

# Data Cleaning

<img width="717" alt="image" src="https://user-images.githubusercontent.com/71307669/178202992-3398ac3d-14da-477b-94be-8f535451321f.png">


Working throught the dataset, I noticed that many of the champion columns for players where scarce, less than 7 champions on the board, max being 9(not including Force of Nature(+1 unit on board)). Because we want quality data, we will only be taking end-game comps, these are the following assumptions on end game comps:

- Player needs to be at least level 7
- Need at least 8 units on board (use FON to have 8 units but lv7)
- At least 4 full items on board

Because to the time constraints, we are only going to explore fully developed compositions, this is okay due to the abundance of data in this dataset, we will be liberal in choosing only fully developed team compositions to explore.

<img width="756" alt="image" src="https://user-images.githubusercontent.com/71307669/178202003-aac8e095-6fab-4c5a-92a9-b55d220e1079.png">

This is the data after being cleaned, where the conditions mentioned above are met and the following adjustments were made to the remainding rows:

- Combination column sorted in terms of number, then traits, this is done to quickly determine which comp they are playing
- The items were converted from numbers to item names


# Data Analysis

There are many websites that aim to find out what the best comps to build are and what items you should have for these comps, my data analysis attempt to uncover some insight that will help people make more infored decisions when playing the game

Meta Analysis (What is the most popular and most successful)
- Most played, successful comp (Using Ranked to judge successfulness)
- Most played, successful champ (Using Ranked to judge successfulness)
- Most used, successful item (Using Ranked to judge successfulness, might not be too correlated)
- Highest item-character correlation (Make a list of tuples, where each row is a character-item pair)
- Most successful spat for comp character (all spat items have 8's, so must be tens and not 88 but 89)
- Most common item pair, what 2 items go together the most (map items together)

For all of these show the top and bottom 5, so we get a good idea of which comps and items to build and which to avoid. 

Given the processing constraints of my laptop, I have decided to only use 10000 challanger games for this analysis. 

### Most played, successful comp (Using Ranked to judge successfulness)

<img width="313" alt="image" src="https://user-images.githubusercontent.com/71307669/178213738-2b064c1c-ee34-4a52-986e-e1afeaedf326.png">

<img width="413" alt="image" src="https://user-images.githubusercontent.com/71307669/178213840-4cf51d21-bd1e-4e22-92ee-d712ed7ff60d.png">

<img width="425" alt="image" src="https://user-images.githubusercontent.com/71307669/178214028-3d18eec6-f3ab-436f-9579-83b43498f24c.png">



### Most played, successful champions (Using Ranked to judge successfulness)

<img width="176" alt="image" src="https://user-images.githubusercontent.com/71307669/178213320-1f75797c-0e7d-4b0f-a865-74629ecbd182.png">

<img width="218" alt="image" src="https://user-images.githubusercontent.com/71307669/178213565-b75ea52a-2ee8-4ffa-aa2f-d705fb1e2524.png">

<img width="239" alt="image" src="https://user-images.githubusercontent.com/71307669/178213639-219f9172-f764-4219-9273-727726eb4d88.png">

### Most played, successful items (Using Ranked to judge successfulness)

<img width="159" alt="image" src="https://user-images.githubusercontent.com/71307669/178235814-660148d8-dbef-4529-940d-8ce647b13cd4.png">

<img width="318" alt="image" src="https://user-images.githubusercontent.com/71307669/178235892-5f4d0420-49c7-4245-aeed-117d14c11d4c.png">

### Most common champion-item pairing

<img width="207" alt="image" src="https://user-images.githubusercontent.com/71307669/178236045-f8d61455-96ea-455a-90b8-8b69892f08a4.png">

### Best performing Spatula Items

<img width="325" alt="image" src="https://user-images.githubusercontent.com/71307669/178236307-2b7242d7-2c8a-4b49-a24a-f465e06e5ccb.png">

### Most Common Builds for champion

<img width="368" alt="image" src="https://user-images.githubusercontent.com/71307669/178236480-38f16731-fc18-432c-ad73-353352b6385a.png">



