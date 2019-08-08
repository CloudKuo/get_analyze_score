import re
import csv
import pandas as pd

# text = open('output3.csv', 'r', encoding='utf-8').read().split('\n')
#
# # name = open('name_relative2.csv', 'r', encoding='utf-8', newline='')
# # rows = csv.DictReader(name)
# # find = []
# name = open('name_relative2.csv', 'r', newline='', encoding='utf-8')
# rows = csv.DictReader(name)
# name_dict = {}
# for row in rows:
#     if name_dict.get(row['True_name'], 'n') == 'n':
#         name_dict[row['True_name']] = row['Number']
# key_L = list(name_dict.keys())
# index = []
# row = 0
# result = []
# for sent in text:
#     result.append(sent.split(','))
#     row += 1
#     # if '\,\,' in sent:
#     #     index.append(row)
#
# saveFile = '\ufeff'
# for sent in result:
#     saveFile += '\n'
#     try:
#         if sent[3] in key_L:
#             sent[4] = name_dict.get(sent[3])
#         for value in sent:
#             saveFile += '%s,' % value
#     except IndexError:
#         pass
#
# open('output3.csv', 'w', encoding='utf-8', newline='').write(saveFile)
def change_num():
    name = open('name_relative2.csv', 'r', encoding='utf-8').read().split('\n')
    initial_num = 148
    row = 0
    result = []
    for sent in name:
        result.append(sent.split(','))
        row += 1
        # if '\,\,' in sent:
        #     index.append(row)

    saveFile = '\ufeff'
    for sent in result:
        # print(result.index(sent))
        saveFile += '\n'
        try:
            if result.index(sent) == 0:
                sent[1] = 'Number'
            else:
                initial_num += 1
                sent[1] = 'student_00'+str(initial_num)
            print(sent[0], sent[1], sent[2])
            for value in sent:
                saveFile += '%s,' % value

        except IndexError:
            pass
    open('name_relative2v2.csv', 'w', encoding='utf-8').write(saveFile)


if __name__ == '__main__':
    name2 = open('name_relative2v2.csv', 'r', newline='', encoding='utf-8')
    rows = csv.DictReader(name2)
    name_dict = {}
    result2 = []
    for row2 in rows:
        # print(row2['\ufeffTrue_name'])
        if name_dict.get(row2['\ufeffTrue_name'], 'n') == 'n':
            name_dict[row2['\ufeffTrue_name']] = row2['Number']
    key_L = list(name_dict.keys())
    ori_output = open('finaloutput2.csv', 'r', newline='', encoding='utf-8').read().split('\n')
    for sent in ori_output:
        result2.append(sent.split(','))
    saveFile = '\ufeff'
    for sent in result2:
        # print(result.index(sent))
        saveFile += '\n'
        try:
            if sent[3] in key_L:
                sent[4] = name_dict.get(sent[3])
            if sent[2] in key_L:
                sent[1] = name_dict.get(sent[2])
            # print(sent[22])
            sent[22] = re.sub('\r', '', sent[22])
            # print(sent)
            for value in sent:
                saveFile += '%s,' % value

        except IndexError:
            pass
    open('finaloutput2v2.csv', 'w', encoding='utf-8').write(saveFile)