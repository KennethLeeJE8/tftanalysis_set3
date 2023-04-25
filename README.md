# tftanalysis_set3

This is an analysis done on Set 3 of Teamfight Tactics, a game made by Riot Games.
![Teamfight Tactics Set 3](https://github.com/KennethLeeJE8/tftanalysis_set3/blob/main/images/tftset3.jpg)

League of Legends Teamfight Tactics(TFT) is a game I have been playing since 2019 and decided to start this analysis on set 3, which I played briefly during 2020. Riot Games releases a new set, which is a new version of the game with different champions, mechanics and traits, every few months.

Some terms to note:

- Meta: The most effective composition in this version of the game
- Slam: When you forced to make an item because you need to improve your team's power in hopes of winning a fight
- Comp: Short for team composition, commonly used in the game

The questions I aim to answer are:

- To know which comps were the most popular and had the highest winrate, in other words, the meta during set 3
- To know which comp to build given the champions or items you currently have
- Best champions to buy that are in the most successful comps (Highest winrate)
- To know which items go on which champions and which champions go with an item, so you can achieve the most optimal item combination (know which items are an okay slam)

The dataset I am using tracks games played in high level play, which is in the top 1% of players, consisting of Challenger, Grandmaster and Master rank. I will be using this data to determine what the optimal level of play was during set 3.

## Data Structure (What the raw data looks like):

Here is some information about the variables collected in the dataset.

gameId: Unique identifier of game, all 8 players in the same game have the same identifier

gameDuration: How long the game lasted, which ends when someone gets 1st place

level: level

lastRound: The last round you participated in

ranked: The rank you obtained in the game, 1st is the best and 8th is the worst

inGameDuration: how long you were in game

combination: A list of key values showing traits or origin and count

key: Trait or Origin Name

value: the count of the trait or origin

champion: json file, list of key values

key : Champion name

value : Item, Stars

Item : Champion's items

Stars : Enhance Champion n (Min 1 Star, Max 3 Star)

1 Star : 1-star champion,

2 Star : 1-star champion three

3 Star : 2-star champion three


## Purpose(Business Goal):

- To know what the meta was at the time and what team compositions would yield the best results overall
- To know what to do in certain situations, given the champions you have or components you have what to build
- Best champions to hold that are in the most successful comps, good champions across the board
- To know which items go on which champions and which champions go with an item, given already built or need to slam

The application for this is to apply this data analysis to future sets to better understand the game and understand what is meta at the moment.

# Data Cleaning

<img width="717" alt="image" src="https://user-images.githubusercontent.com/71307669/178202992-3398ac3d-14da-477b-94be-8f535451321f.png">


Working throught the dataset, I noticed that many of the champion columns for players where scarce, less than 7 champions on the board, max being 9(not including Force of Nature(+1 unit on board)). As we are looking for endgame comps, these following assumptions are made for consistency in data:

- Player needs to be at least level 7
- Need at least 8 units on board (use FON to have 8 units but lv7)
- At least 4 full items on board

Because to the time constraints, we will be dropping any rows that do not meet the criteria above, we can do this in this project due to the abundance of data we have access to.

<img width="756" alt="image" src="https://user-images.githubusercontent.com/71307669/178202003-aac8e095-6fab-4c5a-92a9-b55d220e1079.png">

This is the data after being cleaned, where the conditions mentioned above are met and the following adjustments were made to the remainding rows:

- Combination column sorted in terms of number, then traits, this is done to quickly determine which comp they are playing
- The items were converted from numbers to item names


# Data Analysis

There are many websites that aim to find out what the best comps to build are and what items you should have for these comps, my data analysis aims to uncover some insight that will help people make more informed decisions when playing the game

Meta Analysis (What is the most popular and most successful)
- Most played, successful comp (Using Ranked to judge successfulness)
- Most played, successful champ (Using Ranked to judge successfulness)
- Most used, successful item (Using Ranked to judge successfulness, might not be too correlated)
- Highest item-character correlation (Best performing set of items on a given champion)
- Most successful spat for comp character (all spat items have 8's, so must be tens and not 88 but 89)
- Most common item pair, what 2 items go together the most (map items together)

For all of these show the top and bottom 5, so we get a good idea of which comps and items to build and which to avoid. Winrate represents the average position of the comp/champ/item, this ranges from 0-7 with 0 getting 8th place and 7 getting 1st place.

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

# Tools

I have produced 2 tools that can be used during gameplay, these tools will help you make the best decision given your position in the game.

1. Champion-Comp Pairing

The first tool takes in a list of champions and outputs the possible comps that you could play from that position.

The comp is determined by 2 main factors:
- Similarity: A comp is easier to achieve if you have more champions that make up the comp, there are less champions you need to look for and thus less gold can be spent to look for the champions that make up this team comp
- Winrate: A comp is more desirable if it has a higher winrate overall, so winrate is important to consider when recommending the best comp to run

Example:


2. BIS Tools

BIS stands for "Best in Slot", it describes the best items for a given champion in the game. This tool aims to find the BIS for each champion, taking what items and champions you currently have into consideration.

This tool takes in a list of champions and items, and outputs how you should arrange the items onto your champions based on their performance in the dataset. 


# Problems with this project

- The runtime is really long as the number of rows processed increases, as it iterates through the dataset many times, I could try to reduce this by reusing DataFrames used and changing them instead of creating new ones for each functions.

- There are currently only 2 tools, one to determine optimal team comp and another to determine optimal item-champion pairing.

- Some of the code is very inefficient, could work on improving runtime by changing the structure.

# Future Implications

1. Building more tools in the future

One tool to explore is taking in item components and champions as an input and figuring out which items to build and who they go on, it is one step above the BIS tool I built

The hope for this project is to be able to import data from other sets, Riot comes up with new TFT sets approximately every 3 months, this can be used to get an objective picture of the current state of the set.
