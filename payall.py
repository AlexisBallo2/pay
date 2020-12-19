list_of_people = {'baba': 14,
                  'neely': 14,
                  'babi': 14,
                  'victoria': 13,
                  'penny': 13,
                  'george': 2,
                  "jacob": 9,
                  'rory': 11,
                  'greg': 1,
                  'tracey': 1,
                  'john': 0,
                  'gail': 0,
                  'peggy': 6,
                  'alexis': 11,
                  'cyrus': 14,
                  'michael': 8,
                  'joanna': 14,
                  'thea': 14,
                  'derek': 14,
                  'andrea': 14,
                  'sofie': 12,
                  'anneke': 1,
                  'stevan': 13,
                  'mika': 12,
                  "bct": 0}

ballo = ['alexis', 'cyrus', 'michael', 'joanna']
vandernoo = ['sofie', 'mika', 'stevan', 'anneke']
skill = ['rory', 'jacob', 'greg', 'tracey']
trelstad = ['thea', 'derek', 'andrea']
abbot = ['victoria', 'penny', 'george']
pisunyer = ['baba', 'babi']
john = ['john', 'gail']
peggy = ['peggy']
neely = ['neely']

ballo_total_days = 0
vandernoo_total_days = 0
skill_total_days = 0
trelstad_total_days = 0
pisunyer_total_days = 0
abbot_total_days = 0
john_total_days = 0
peggy_total_days = 0
neely_total_days = 0
bct_total_days = 0

for x in ballo:
    ballo_total_days = ballo_total_days + list_of_people[x]
for x in vandernoo:
    vandernoo_total_days = vandernoo_total_days + list_of_people[x]
for x in skill:
    skill_total_days = skill_total_days + list_of_people[x]
for x in trelstad:
    trelstad_total_days = trelstad_total_days + list_of_people[x]
for x in pisunyer:
    pisunyer_total_days = pisunyer_total_days + list_of_people[x]
for x in abbot:
    abbot_total_days = abbot_total_days + list_of_people[x]
for x in john:
    john_total_days = john_total_days + list_of_people[x]
for x in peggy:
    peggy_total_days = peggy_total_days + list_of_people[x]
for x in neely:
    neely_total_days = neely_total_days + list_of_people[x]
bct_total_days = 0
"""
print(ballo_total_days)
print(vandernoo_total_days)
print(skill_total_days)
print(trelstad_total_days)
print(pisunyer_total_days)
"""
trelstad_money = -694
abbot_money = -490
vandernoo_money = -511
pisunyer_money = 0
ballo_money = 0
skill_money = 0
john_money = 0
peggy_money = 0
neely_money = 0
bct_money = 0

total_days = bct_total_days + neely_total_days + peggy_total_days + vandernoo_total_days + skill_total_days + pisunyer_total_days + john_total_days + abbot_total_days + trelstad_total_days

total_cost = abs(trelstad_money) + abs(abbot_money) + abs(vandernoo_money)
bct_cost = 120+300+20+80
print("total cost is: ", total_cost)
cost_per_day = total_cost / total_days
print(cost_per_day)

full = bct_total_days + ballo_total_days + vandernoo_total_days + trelstad_total_days + pisunyer_total_days + neely_total_days + john_total_days + peggy_total_days + skill_total_days + abbot_total_days
daily = total_cost / full
print('daily cost is: ', daily)
bct_daily = bct_cost / full
print("bct daily cost", bct_daily)
ballo_money = round(ballo_money + ballo_total_days * daily)
abbot_money = round(abbot_money + abbot_total_days * daily)
trelstad_money = round(trelstad_money + trelstad_total_days * daily)
skill_money = round(skill_money + skill_total_days * daily)
pisunyer_money = round(pisunyer_money + pisunyer_total_days * daily)
vandernoo_money = round(vandernoo_money + vandernoo_total_days * daily)
peggy_money = round(peggy_money + peggy_total_days * daily)
john_money = round(john_money + john_total_days * daily)
neely_money = round(neely_money + neely_total_days * daily)


#bct costs
ballo_bctmoney = round(ballo_total_days * bct_daily)
abbot_bctmoney = round(abbot_total_days * bct_daily)
trelstad_bctmoney = round(trelstad_total_days * bct_daily)
skill_bctmoney = round(skill_total_days * bct_daily)
pisunyer_bctmoney = round(pisunyer_total_days * bct_daily)
vandernoo_bctmoney = round(vandernoo_total_days * bct_daily)
peggy_bctmoney = round(peggy_total_days * bct_daily)
john_bctmoney = round(john_total_days * bct_daily)
neely_bctmoney = round(neely_total_days * bct_daily)

print('\nballo owe:', ballo_money)
print('abbot owe:', abbot_money)
print('trelstad owe:', trelstad_money)
print('skill owe:', skill_money)
print('pisunyer owe:', pisunyer_money)
print('vandernoo owe:', vandernoo_money)
print('john owe:', john_money)
print('peggy owe:', peggy_money)
print('neely owe:', neely_money)
everyone = {'ballo': ballo_money, 'john': john_money, 'abbot': abbot_money, 'trelstad': trelstad_money,
            'peggy': peggy_money, 'skill': skill_money, 'pisunyer': pisunyer_money, 'neely': neely_money,
            'vandernoo': vandernoo_money}
everyone_bct_money = {'ballo': ballo_bctmoney, 'john': john_bctmoney, 'abbot': abbot_bctmoney, 'trelstad': trelstad_bctmoney,
            'peggy': peggy_bctmoney, 'skill': skill_bctmoney, 'pisunyer': pisunyer_bctmoney, 'neely': neely_bctmoney,
            'vandernoo': vandernoo_bctmoney}
print('\n')

# beginning of the price deal
positives = {}
negatives = {}
for k, v in everyone.items():
    if v >= 0:
        positives[str(k)] = v

    else:
        negatives[str(k)] = v

# print(positives)
# print("\n")
# print(negatives)

# print(positives.i\tems())
postup = [(k, v) for k, v in positives.items()]
negup = [(k, v) for k, v in negatives.items()]
newnegup = list(negup)
newnegup = [list(ele) for ele in newnegup]
newpostup = list(postup)
newpostup = [list(ele) for ele in newpostup]
# print(postup,"\n",negup)
test = {tuple(negup): tuple(postup)}
# print('\nthis is the full dict',test)
# print("\nthis is the group who deserves money: ", negup)
# print("\nthis is the group who owes money: ",postup)
# for neg,pos in test.items():
# print("neg", neg)
# print('pos', pos)
print("new negup", newnegup)
print('new postup', newpostup)

# opperation 1
for x in range(0,len(newnegup)):
    newnegup[x][0]
for a in range(0, len(newnegup)):
    for x in range(0, (len(newpostup))):
        if (newpostup[x][1]) < abs((newnegup[a][1])) and (newpostup[x][1]) > 0:
            newnegup[a][1] = newnegup[a][1] + newpostup[x][1]
            print(newpostup[x][0], " pay ", newnegup[a][0], ": ", newpostup[x][1])
            newpostup[x][1] = 0
for y in range(0, len(newpostup)):
    if newpostup[y][1] > 0:
        #print(newpostup[y][1])
        for z in range(0, len(newnegup)):
            if abs(newnegup[z][1]) > 0:
                newnegup[z][1] = newnegup[z][1] + newpostup[y][1]
                print(newpostup[y][0], ' pay ', newnegup[z][0], ": ", newnegup[z][1])
                newnegup[z][1] = 0

    newpostup[y][1] = 0
#print(newnegup)
#print(newpostup)
print(everyone_bct_money)