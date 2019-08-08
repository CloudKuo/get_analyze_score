import re
import csv
import pandas as pd


def find(man):
    true_id = ''
    for key in key_L:
        count = 0
        for word in man:
            if word in key:
                count += 1
                if count >= 2:
                    true_id = name_dict.get(key)
                    break
    return true_id


df = pd.read_csv('output3.csv')
# print(df['評論人'][2], df['受評人'][2])
name = open('name_relative2.csv', 'r', newline='', encoding='utf-8')
out = open('output3.csv', 'r', encoding='utf-8').read().split('\n')
rows = csv.DictReader(name)
name_dict = {}
result = []
for row in rows:
    if name_dict.get(row['True_name'], 'n') == 'n':
        name_dict[row['True_name']] = row['Number']
# print(name_dict.keys())
key_L = list(name_dict.keys())
# df['test'] = df['受評ID']
# df.loc[df['受評ID'].isna(), 'test'] = 'test'
na_list = []
for i in range(df.__len__()):
    if pd.isna(df['受評ID'][i]):#找是nan值
        # print(i)
        na_list.append(i+1)
        # for key in key_L:
        #     count = 0
        #     for word in df['受評人'][i]:
        #             if word in key:
        #                 count += 1
        #                 if count >= 2:
        #                     print("一樣", df['受評人'][i], key)
        #                     df.loc[df['受評ID'][i], '受評ID2'] = df['受評人'][i]
        #                     break
# print(na_list)
b = [i+1 for i in na_list]
print(b)
na_txt = open('na.txt', 'w', encoding="utf-8").write(str(b))
saveFile = '\ufeff'
for column in out:
    result.append(column.split(','))
for sent in result:
    saveFile += '\n'
    try:
        if result.index(sent) in na_list:
            sent[4] = find(sent[3])

        for value in sent:
            saveFile += '%s,' % value
    except IndexError:
        pass

open('output3.csv', 'w', encoding='utf-8').write(saveFile)
name.close()





