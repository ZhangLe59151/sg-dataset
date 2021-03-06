import requests
import json
import pandas as pd


###########################
#      Get Heros          #
###########################
response = requests.get('https://api.opendota.com/api/heroes')
data = json.loads(response.text)
heros_array = [''] * (data[-1]['id'] + 1)
for heros in data:
  heros_array[heros['id']] = heros['localized_name']+','+heros['attack_type']

############################
#      Item Dict           #
############################
response = requests.get('https://api.opendota.com/api/constants/item_ids')
data = json.loads(response.text)
item_array = [''] * 1566
for item in data:
  item_array[int(item)] = data[item]

###############################
#     Get Match         #######
###############################
mid_list = ['6576116877','6576223979','6575811382','6575974930',
'6575685774','6575589562','6575506610',
'6574848748','6574739883',
'6574603408','6574482766','6574385083',
'6574188575','6574108422',
'6573503063','6573568264','6579091075','6579165262',
'6573407404','6573291227','6578909443','6578799684','6578674296',
'6573182161','6573058524','6572937926',
'6571843720','6571843204','6571965781','6572937926','6573058524','6573182161',
'6571442714','6571582160','6571446779','6571554679','6571738707','6571732248',
'6571201844','6571305244','6571200692','6571306390','6571204733','6571280989',
'6570284918','6570398588','6571966593','6572659357','6572725458','6572822253',
'6580625364','6580732041','6580245004','6580376211','6580504708','6579931950','6580016442',
'6579165262','6579091075'
]

mid_list = set(mid_list)

mid = []
hero = []
hero_type = []
item1 = []
item2 = []
item3 = []
item4 = []
item5 = []
item6 = []
result = []

for id in mid_list:
  response = requests.get('https://api.opendota.com/api/matches/'+id)
  data = json.loads(response.text)
  print(id)
  # print(data['match_id'])
  for record in data['players']:
    mid.append(data['match_id'])
    hero.append(heros_array[record['hero_id']].split(',')[0])
    hero_type.append(heros_array[record['hero_id']].split(',')[1])
    item1.append(item_array[record['item_0']])
    item2.append(item_array[record['item_1']])
    item3.append(item_array[record['item_2']])
    item4.append(item_array[record['item_3']])
    item5.append(item_array[record['item_4']])
    item6.append(item_array[record['item_5']])
    result.append(record['win'])

csv_data = {
  'mid': mid,  'hero': hero, 'hero_type': hero_type, 'item1': item1, 'item2': item2, 'item3': item3, 'item4': item4, 'item5': item5, 'item6': item6, 'result': result
}

pd_data = pd.DataFrame(csv_data)
pd_data.to_csv('match_info.csv')

