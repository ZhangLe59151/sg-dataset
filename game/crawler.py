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
item_dict = [''] * 1500
item_dict[1] = 'blink dagger'
item_dict[9] = 'platemail'
item_dict[16] = 'iron branch'
item_dict[21] = 'ogre axe'
item_dict[29] = 'boots of speed'
item_dict[30] = 'gem of the sight'
item_dict[33] = 'cheese'
item_dict[34] = 'magic stick'
item_dict[36] = 'magic wand'
item_dict[40] = 'dust of apperance'
item_dict[42] = 'observer ward'
item_dict[43] = 'sentry ward'
item_dict[48] = 'boots of travel'
item_dict[50] = 'phase boots'
item_dict[61] = 'vitality booster'
item_dict[63] = 'power treads'
item_dict[96] = 'scythe of vyse'
item_dict[102] = 'froce staff'
item_dict[108] = 'aghanims scepter'
item_dict[110] = 'refresher orb'
item_dict[112] = 'assault cuirass'
item_dict[116] = 'black king bar'
item_dict[119] = 'shivas guard'
item_dict[117] = 'aegis of the immortal'
item_dict[123] = 'linkens sphere'
item_dict[131] = 'hood of defiance'
item_dict[139] = 'butterfly'
item_dict[141] = 'daedalus'
item_dict[143] = 'skull basher'
item_dict[145] = 'battle fury'
item_dict[156] = 'satanic'
item_dict[160] = 'eye of skadi'
item_dict[174] = 'diffusal blade'
item_dict[178] = 'soul ring'
item_dict[185] = 'drum of endurance'
item_dict[188] = 'smoke of deceit'
item_dict[208] = 'abyssal blade'
item_dict[214] = 'tranquil boots'
item_dict[218] = 'observer and sentry wards'
item_dict[235] = 'octarine core'
item_dict[249] = 'silver edge'
item_dict[250] = 'bloodthorn'
item_dict[252] = 'echo sabra'
item_dict[254] = 'glimmer cape'
item_dict[256] = 'aeon disk'
item_dict[267] = 'spirit vessel'
item_dict[273] = 'kaya and sange'
item_dict[534] = 'witch blade'
item_dict[610] = 'wind waker'
item_dict[635] = 'helm of the overlord'
item_dict[908] = 'wraith pact'
item_dict[931] = 'boots of bearing'
item_dict[1466] = 'gleipnir'


###############################
#     Get Match         #######
###############################
mid_list = ['6576116877','6576223979']
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
  print(data['match_id'])
  for record in data['players']:
    print(heros_array[record['hero_id']], record['item_0'], record['item_1'], record['item_2'], record['item_3'], record['item_4'], record['item_5'], record['win'])
    mid.append(data['match_id'])
    hero.append(heros_array[record['hero_id']].split(',')[0])
    hero_type.append(heros_array[record['hero_id']].split(',')[1])
    item1.append(item_dict[record['item_0']])
    item2.append(item_dict[record['item_1']])
    item3.append(item_dict[record['item_2']])
    item4.append(item_dict[record['item_3']])
    item5.append(item_dict[record['item_4']])
    item6.append(item_dict[record['item_5']])
    result.append(record['win'])

csv_data = {
  'mid': mid,  'hero': hero, 'hero_type': hero_type, 'item1': item1, 'item2': item2, 'item3': item3, 'item4': item4, 'item5': item5, 'item6': item6, 'result': result
}

pd_data = pd.DataFrame(csv_data)
pd_data.to_csv('match_info.csv')
print(pd_data)


