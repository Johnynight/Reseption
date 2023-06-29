import json
from datetime import timedelta, datetime

last = datetime.now() - timedelta(days=750)

date = last.strftime('%d.%m.%Y')
date2 = datetime.strptime(date, '%d.%m.%Y')

data = []
with open('data.json', mode='r', encoding='utf-8') as file:
    j = json.load(file)
iskl = ['', 'null']
for i in j:
    try:
        abc = (datetime.strptime(i['RepairFinishMonthDate'], '%d.%m.%Y'))
        if abc >= date2:
            data.append(i)

    except:
        continue
with open('new_crh.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file)

# print(data)
# firs_dict = [x for x in j if '_handle#' in x['WOOpenDate'] ]

# output_dict = [x for x in j if datetime.strptime(x['RepairFinishMonthDate'].replace('_handle#', ''),'%d.%m.%Y') >= date2]
