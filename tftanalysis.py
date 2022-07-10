import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns #
import plotly.express as px #
import matplotlib.pyplot as plt #
import json #convert json format into dictionaries
import math #mathematical functions



challenger = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_Challenger_MatchData.csv")
challenger2 = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_Challenger_MatchData_2.csv")
grandmaster = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_GrandMaster_MatchData.csv")
grandmaster2 = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_GrandMaster_MatchData_2.csv")
master = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_Master_MatchData.csv")
master2 = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_Master_MatchData_2.csv")
diamond = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_Diamond_MatchData.csv")
diamond2 = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_Diamond_MatchData_2.csv")
plat = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_Platinum_MatchData.csv")
plat2 = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_Platinum_MatchData_2.csv")

#join the different matches for analysis of all games
allgames = pd.concat([challenger,grandmaster,master],ignore_index = True)
items = pd.read_csv("C:/Users/kenne/tftanalysis_set3/data/TFT_Item_CurrentVersion.csv")

set3 = allgames.head(200)
items = items.set_index('id')
print(set3.tail(5))


#convert json files (str) into ordered dictionaries
for i in set3.index:
    dic = json.loads(set3['combination'][i].replace("'",'"'))
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    set3.at[i,'combination'] = dic
    dic = str(set3['champion'][i]).replace("'",'"')
    dic = json.loads(dic)
    #order in terms of item count then star level
    dic = sorted(dic.items(), key=lambda x: (len(x[1]['items']),x[1]['star']), reverse=True)
    champ_count = 0
    item_count = 0
    for x in range(0,len(dic)):
        champ_count += 1
        for y in range(0,len(dic[x][1]['items'])):
            item_num = dic[x][1]['items'][y]
            if (item_num >= 10):
                item_count += 1
            #replacing the itemid with the item name so it is clear
            dic[x][1]['items'][y] = items['name'][item_num]
    if champ_count >= 8 and item_count >= 4:  #if there are 4 items or more and 8 champions or more
        set3.at[i,'champion'] = dic
    else:
        set3 = set3.drop([i])

set3 = set3.sort_values("gameId", ascending = False).reset_index().drop(columns = ['index'])
set3.head(5)
print(set3['combination'][0])

#Most played, successful comp (Using Ranked to judge successfulness)
#most successful is determined by winrate, so do count of composite rank divided by
#success is based on rank/number of occurances, essentially mean rank

most_played_comp = pd.DataFrame(columns = ['comp','comp2'])
for i in range(0,len(set3['combination'])):
    most_played_comp = pd.concat([most_played_comp, pd.DataFrame.from_records([{'comp': set3['combination'][i][0], 'comp2': set3['combination'][i][1]}])])

most_success_comp = most_played_comp.groupby(['comp','comp2']).size().reset_index().rename(columns={0:'count'})
most_success_comp['rank'] = 0

#only based on first comp, primary combination
for x in range(0,len(set3['combination'])):
    for y in range(0,len(most_success_comp['comp'])):
        if (set3['combination'][x][0][0]==most_success_comp['comp'][y][0] and
              set3['combination'][x][0][1]==most_success_comp['comp'][y][1] and
              set3['combination'][x][1][0]==most_success_comp['comp2'][y][0] and
              set3['combination'][x][1][1]==most_success_comp['comp2'][y][1]):
            #Higher the rank, the higher the number (0 is last place and 7 is a furst)
            rank = 8 - set3['Ranked'][x]
            most_success_comp.at[y,'rank'] += rank

most_success_comp['winrate'] = most_success_comp['rank'] / most_success_comp['count']
most_success_comp = most_success_comp[most_success_comp['count']>1]
most_success_comp = most_success_comp.sort_values("winrate", ascending = False).reset_index().drop(columns = ['index'])
print("Most Played Comps")
print(most_played_comp.value_counts().head(10))
print("Most Successful Comps")
print(most_success_comp[most_success_comp['count']>1].head(5))
print("Least Successful Champions")
print(most_success_comp[most_success_comp['count']>1].tail(5))

#Most played, successful champ (Using Ranked to judge successfulness)

most_played_champ = pd.DataFrame(columns = ['champ'])
for i in range(0,len(set3['champion'])):
    for j in range(0,len(set3['champion'][i])):
        most_played_champ = pd.concat([most_played_champ, pd.DataFrame.from_records
                            ([{'champ': set3['champion'][i][j][0]}])])

most_success_champ = most_played_champ.groupby(['champ']).size().reset_index().rename(columns={0:'count'})
most_success_champ['rank'] = 0

#only based on first comp, primary combination
for x in range(0,len(set3['champion'])):
    for y in range(0,len(set3['champion'][x])):
        for z in range(0,len(most_success_champ['champ'])):
            if (set3['champion'][x][y][0]==most_success_champ['champ'][z]):
                #Higher the rank, the higher the number (0 is last place and 7 is a furst)
                rank = 8 - set3['Ranked'][x]
                most_success_champ.at[z,'rank'] += rank
                break

most_success_champ['winrate'] = most_success_champ['rank'] / most_success_champ['count']
most_success_champ = most_success_champ.sort_values("winrate", ascending = False).reset_index().drop(columns = ['index'])
print("Most Played Champions")
print(most_played_champ.value_counts().head(10))
print("Most Successful Champions")
print(most_success_champ[most_success_champ['count']>1].head(10))
print("Least Successful Champions")
print(most_success_champ[most_success_champ['count']>1].tail(10))

#Most used, successful item (Using Ranked to judge successfulness, might not be too correlated)
#maybe remove spat items and do seperately?

most_played_item = pd.DataFrame(columns = ['item'])
for i in range(0,len(set3['champion'])):
    for j in range(0,len(set3['champion'][i])):
        for k in range(0,len(set3['champion'][i][j][1]['items'])):
            most_played_item = pd.concat([most_played_item, pd.DataFrame.from_records
            ([{'item': set3['champion'][i][j][1]['items'][k]}])])

most_success_item = most_played_item.groupby(['item']).size().reset_index().rename(columns={0:'count'})
most_success_item['rank'] = 0

#only based on first comp, primary combination
for a in range(0,len(set3['champion'])):
    for b in range(0,len(set3['champion'][a])):
        for c in range(0,len(set3['champion'][a][b][1]['items'])):
            for d in range(0,len(most_success_item['item'])):
                if (set3['champion'][a][b][1]['items'][c]==most_success_item['item'][d]):
                #Higher the rank, the higher the number (0 is last place and 7 is a furst)
                    rank = 8 - set3['Ranked'][a]
                    most_success_item.at[d,'rank'] += rank
                    break

most_success_item['winrate'] = most_success_item['rank'] / most_success_item['count']
most_success_item = most_success_item.sort_values("winrate", ascending = False).reset_index().drop(columns = ['index'])
print("Most Used Items")
print(most_played_item.value_counts().head(10))
print("Most Successful Items")
print(most_success_item[most_success_item['count']>1].head(10))
print("Least Successful Items")
print(most_success_item[most_success_item['count']>1].tail(10))

#Highest item-character correlation, most common and best items on champion (runtime kinda long)
champ_item_pair = pd.DataFrame(columns = ['champ','item'])
for i in range(0,len(set3['champion'])):
    for j in range(0,len(set3['champion'][i])):
        for k in range(0,len(set3['champion'][i][j][1]['items'])):
            champ_item_pair = pd.concat([champ_item_pair, pd.DataFrame.from_records
            ([{'champ':set3['champion'][i][j][0],'item': set3['champion'][i][j][1]['items'][k]}])])


most_success_champ_item_pair = champ_item_pair.groupby(['champ','item']).size().reset_index().rename(columns={0:'count'})
most_success_champ_item_pair['rank'] = 0

#only based on first comp, primary combination
for a in range(0,len(set3['champion'])):
    for b in range(0,len(set3['champion'][a])):
        for c in range(0,len(set3['champion'][a][b][1]['items'])):
            for d in range(0,len(most_success_champ_item_pair['item'])):
                if (set3['champion'][a][b][1]['items'][c]==most_success_champ_item_pair['item'][d] and
                    set3['champion'][a][b][0] == most_success_champ_item_pair['champ'][d]):
                #Higher the rank, the higher the number (0 is last place and 7 is a furst)
                    rank = 8 - set3['Ranked'][a]
                    most_success_champ_item_pair.at[d,'rank'] += rank
                    break

most_success_champ_item_pair['winrate'] = most_success_champ_item_pair['rank'] / most_success_champ_item_pair['count']
most_success_champ_item_pair = most_success_champ_item_pair.sort_values("winrate", ascending = False).reset_index().drop(columns = ['index'])
print("Most Frequent Champ-Item Pairings")
print(champ_item_pair.value_counts().head(10))
print("Most Successful Champ-Item Pairings")
print(most_success_champ_item_pair[most_success_champ_item_pair['count']>1].head(10))
print("Least Successful Champ-Item Pairings")
print(most_success_champ_item_pair[most_success_champ_item_pair['count']>1].tail(10))

#Most successful spat for comp character (all spat items have 8's, so must be tens and not 88 but 89)
print(most_success_item[most_success_item.item.isin(
                  ['Celestial Orb','Blade of the Ruined King',
                   '''Infiltrator's Talon''','Rebel Medal','''Demolitionist's Charge''',
                  '''Star Guardian's Charm''','''Protector's Chestguard''','''Dark Star's Heart'''])])

#Most common item combinations, what items go together the most (map items together)
item_combo = pd.DataFrame(columns = ['champ','item1','item2','item3'])
for i in range(0,len(set3['champion'])):
    for j in range(0,len(set3['champion'][i])):
            if len(set3['champion'][i][j][1]['items'])==3:
                item_combo = pd.concat([item_combo, pd.DataFrame.from_records([{'champ':set3['champion'][i][j][0],
                            'item1': set3['champion'][i][j][1]['items'][0],'item2': set3['champion'][i][j][1]['items'][1],
                            'item3': set3['champion'][i][j][1]['items'][2]}])],ignore_index=True)
            elif len(set3['champion'][i][j][1]['items'])==2:
                item_combo = pd.concat([item_combo, pd.DataFrame.from_records([{'champ':set3['champion'][i][j][0],
                            'item1': set3['champion'][i][j][1]['items'][0],
                            'item2': set3['champion'][i][j][1]['items'][1]}])],ignore_index=True)

item_combo = item_combo.replace(np.nan, '', regex=True)
print("Popular Item Combos")
print(item_combo[item_combo['item1']!='''Thief's Gloves'''].value_counts().head(10))

#X values is single of list of champs, Y value is the rest of the champions in the comp and what comp
#Given one or multiple champion in the comp, determine the comp and champions to have for highest winrate, what you should go
#highest winrate
import string
import sklearn
from sklearn.metrics.pairwise import cosine_similarity


#Use cosine similarity function to determine how similar two arrays of champions are
def cosine_similarity(X,Y):
    l1 = []
    l2 =[]
    rvector = X + list(set(Y) - set(X))
    for w in rvector:
        if w in X: l1.append(1) # create a vector
        else: l1.append(0)
        if w in Y: l2.append(1)
        else: l2.append(0)
    c = 0
    for i in range(len(rvector)):
        c+= l1[i]*l2[i]
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    return cosine

def champ_to_comp(test):
    comp_champ = pd.DataFrame(columns = ['combination','champions','similarity','winrate'])
    comp_champ['combination'] = set3['combination']
    for i in range(0,len(set3['champion'])):
        champ = list()
        for j in range(0,len(set3['champion'][i])):
            champ.append(set3['champion'][i][j][0])
        comp_champ['champions'][i] = champ
    #lower case all names
    champs = list()
    champs = comp_champ['champions']
    similarity = list()
    for i in range(0,len(champs)):
        for j in range(0,len(champs[i])):
            champs[i][j] = champs[i][j].lower()
        similarity.append(cosine_similarity(test,champs[i]))
    #use winrate of comp to order the output
    comp_champ['similarity'] = similarity
    #only taking comps that have a similarity score of above 0.3
    comp_champ = comp_champ[comp_champ['similarity']>=0.3].reset_index().drop(columns = ['index'])

    for x in range(0,len(comp_champ)):
        for y in range(0,len(most_success_comp)):
            if (comp_champ['combination'][x][0][0]==most_success_comp['comp'][y][0] and
                  comp_champ['combination'][x][0][1]==most_success_comp['comp'][y][1] and
                  comp_champ['combination'][x][1][0]==most_success_comp['comp2'][y][0] and
                  comp_champ['combination'][x][1][1]==most_success_comp['comp2'][y][1]):
                comp_champ.at[x,'winrate'] = most_success_comp['winrate'][y]
    #how to convert to string
    for x in range(0,len(comp_champ)):
        comp_champ.at[x,'combination'] = str(comp_champ['combination'][x])
    comp_champ.drop_duplicates(subset =['similarity'],keep = 'first', inplace = True)
    comp_champ = comp_champ.reset_index().drop(columns = ['index'])
    comp_champ = comp_champ.sort_values(by=['winrate','similarity'],ascending =False).reset_index().drop(columns = ['index'])
    return comp_champ
#end results shows a table of possible comps and champions in the comp to go given that you have number of champions


#X value is the item and champion?, Y value is the Champion(or not) and other items to put on champ
#Given item, what is the ideal item-combo you should put in and on which champion for highest winrate,

from itertools import product

def champ_item_pairing(value):
    value = [x.lower() for x in value]
    test = pd.DataFrame(columns=['name','type'])
    test['name'] = value

    item_count = 0
    #go through items
    for i in test.index:
        for j in items.index:
            if test['name'][i]==items['name'][j].lower():
                item_count+=1
                test.at[i,'type'] = 'item'
    #go through champions
    for i in test.index:
        for j in range(0,len(most_success_champ)):
            if test['name'][i]==most_success_champ['champ'][j].lower():
                test.at[i,'type'] = 'champ'

    #mapping of every champion to every item
    test_champ = pd.DataFrame(columns=['name','item','type'])
    test_item = pd.DataFrame(columns=['name','item','type'])
    test_item = test[test['type']=='item'].reset_index().drop(columns = ['index'])
    test_champ = test[test['type']=='champ']
    test = product(list(test_champ['name']),list(test_item['name']))
    test = pd.DataFrame(test,columns=['champ','item1'])
    test['winrate'] = None

    #Get respective winrates for combinations
    for i in most_success_champ_item_pair.index:
        for j in test.index:
            if (test['champ'][j]==most_success_champ_item_pair['champ'][i].lower() and
                test['item1'][j]==most_success_champ_item_pair['item'][i].lower()):
                test['winrate'][j] = most_success_champ_item_pair['winrate'][i]
                break

    test = test.dropna(subset=['winrate']).reset_index().drop(columns = ['index'])

    #get the item combos for each row and append row if item and champ is found in test
    test['item2'] = ''
    test['item3'] = ''
    for i in test['champ'].index:
        for j in item_combo.index:
            #check champ name and all item slots (3 is max)
            if (item_combo['champ'][j].lower() in test['champ'][i] and
                    (not item_combo['item3'][j] == 0) and
                    ((item_combo['item1'][j].lower() == test['item1'][i]) or
                     (item_combo['item2'][j].lower() == test['item1'][i]) or
                     (item_combo['item3'][j].lower() == test['item1'][i]))):
                if not item_combo['item3'][j]:
                    test = pd.concat([test, pd.DataFrame.from_records([{'champ':item_combo['champ'][j],
                            'item1': item_combo['item1'][j],'item2': item_combo['item2'][j],'item3':
                            item_combo['item3'][j],'winrate':test['winrate'][i]}])])
                else:
                    test = pd.concat([test, pd.DataFrame.from_records([{'champ':item_combo['champ'][j],
                        'item1': item_combo['item1'][j],'item2': item_combo['item2'][j],'winrate':test['winrate'][i]}])])
    test = test.sort_values(by=['champ','winrate'],ascending =False)
    test = test.replace('', np.nan, regex=True)
    test = test[['champ','item1','item2','item3','winrate']].dropna(subset=['item2']).reset_index().drop(columns = ['index'])
    test = test.replace(np.nan, '', regex=True)
    output = pd.DataFrame(np.sort(test[['champ','item1','item2','item3']].values, axis=1), index=test.index, columns=['champ','item1','item2','item3'])
    test = test[~output.duplicated()]
    return test

#test = ['malphite','yasuo','masteryi','sona']
#print(champ_to_comp(test))

test = ['lucian','xinzhao','leona','''titan's resolve''','Morellonomicon','''giant slayer''']
print(champ_item_pairing(test))


#output is a DataFrame Table with a list of champions and the possible builds they can go, determine who to put items on and which other items that complement them