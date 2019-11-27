# get dataset from csv 
# convert to pandas dataframe

# 1. remove asterisks from names
# 2. go through csv and see if there are any empty cells, if empty, then 0
# 3. 

import pandas as pd
import numpy as np
import csv

data = pd.read_csv('Seasons_Stats.csv')
#print(data.head())

# remove asterisks
data['Player'] = data['Player'].str.replace("*","")
data.fillna(0, inplace=True)

teams = data['Tm'].unique()
west = ['SAC', 'DAL', 'POR', 'SEA', 'HOU',
        'UTA', 'DEN', 'NOK', 'MEM', 'GSW', 
        'PHO', 'SAS', 'MIN', 'LAC', 'LAL', 
        'NOH', 'NOP', 'OKC']
east = ['NJN', 'CHI', 'BOS', 'PHI', 'CHA', 
        'WAS', 'ORL', 'IND', 'NYK', 'TOR', 
        'MIA', 'ATL', 'MIL', 'DET', 'CLE', 
        'BRK', 'CHO']
invalid = ['TOT', 0]
conferences = []
# get conference
for i in range(len(data)):
    # get team
    team = data.loc[i]['Tm']
    if team in west:
        conferences.append('W')
    elif team in east:
        conferences.append('E')
    else:
        conferences.append('N')

data['conference'] = conferences


all_star_rosters = {}
# get prev all star appearances
with open('allstardata copy.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2017'] = []
        elif counter != 1:
            all_star_rosters['2017'].append(row[0])
            all_star_rosters['2017'].append(row[1])
        counter += 1
        if counter == 15:
            break

    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2016'] = []
        elif counter != 1:
            all_star_rosters['2016'].append(row[0])
            all_star_rosters['2016'].append(row[1])
        counter += 1
        if counter == 16:
            break

    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2015'] = []
        elif counter != 1:
            all_star_rosters['2015'].append(row[0])
            all_star_rosters['2015'].append(row[1])
        counter += 1
        if counter == 17:
            break

    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2014'] = []
        elif counter != 1:
            all_star_rosters['2014'].append(row[0])
            all_star_rosters['2014'].append(row[1])
        counter += 1
        if counter == 15:
            break

    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2013'] = []
        elif counter != 1:
            all_star_rosters['2013'].append(row[0])
            all_star_rosters['2013'].append(row[1])
        counter += 1
        if counter == 14:
            break

    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2012'] = []
        elif counter != 1:
            all_star_rosters['2012'].append(row[0])
            all_star_rosters['2012'].append(row[1])
        counter += 1
        if counter == 15:
            break

    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2011'] = []
        elif counter != 1:
            all_star_rosters['2011'].append(row[0])
            all_star_rosters['2011'].append(row[1])
        counter += 1
        if counter == 15:
            break

    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2010'] = []
        elif counter != 1:
            all_star_rosters['2010'].append(row[0])
            all_star_rosters['2010'].append(row[1])
        counter += 1
        if counter == 17:
            break

    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2009'] = []
        elif counter != 1:
            all_star_rosters['2009'].append(row[0])
            all_star_rosters['2009'].append(row[1])
        counter += 1
        if counter == 16:
            break
        
    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2008'] = []
        elif counter != 1:
            all_star_rosters['2008'].append(row[0])
            all_star_rosters['2008'].append(row[1])
        counter += 1
        if counter == 16:
            break
    
    counter = 0
    for row in spamreader: 
        if counter == 0:
            all_star_rosters['2007'] = []
        elif counter != 1:
            all_star_rosters['2007'].append(row[0])
            all_star_rosters['2007'].append(row[1])
        counter += 1
        if counter == 19:
            break




players = data[['Year', 'Player']]

prev_all_star_appearances = pd.DataFrame(columns=['Player', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'])

prev_all_star_appearances['Player'] = data['Player']

for year, roster in all_star_rosters.items():
    year_data = []
    for index,row in players.iterrows():
        player = row['Player']
        if player in roster:
            year_data.append(1)
        else:
            year_data.append(0)
    prev_all_star_appearances[year] = year_data


years = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']


cumulative_all_star_appearances = pd.DataFrame(columns=['Player', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'])

for index, row in prev_all_star_appearances.iterrows():
    counter = 0
    for year in years:
        data_point = row[year]
        if data_point == 1:
            row[year] = data_point + counter
            counter += 1
    cumulative_all_star_appearances[index] = row

print(cumulative_all_star_appearances.loc[6390])



        
        