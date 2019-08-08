import csv
# dict_student = {}
# be_judged_man = "受評者 (請輸入組員的姓名)"
# judged_man = '請輸入自己的姓名'
# judged_man_num = '\ufeff回應編號'
# topic_list = ['主動且積極地參與小組活動', '個別發想的題目具有參考價值',
#               '願意分享自己的想法以及相關的資源等訊息', '願意接受小組的分工安排並負責任完成',
#               '有助於提升小組的團隊精神', '尊重組員間不同的背景與意見，且願意跟大家一起討論、商量，達成共識', '有必要時，願意提供小組團隊適當的支援',
#               '能欣賞其他成員產出的成品，並給予正向的回饋', '願意為了達成小組共同的任務，而跟大家協同合作', '小組在討論時，能夠友善地溝通與表達意見',
#               '跟小組成員保持聯繫，讓彼此都知道目前的小組進度', '產出有品質的成品', '能在小組約定的截止日期前，完成應該完成的工作項目', '對其他組員的需求與感受能夠有所覺察',
#               '了解小組討論內容的重點，且能給予有助益的建議', '願意讓小組成員了解自己的需要與感受'
#               ]
# score_list = ['非常不同意', '不同意', '中等', '同意', '非常同意']
#
# time_name = ['1st', '2nd', '3rd']
# student_num = 287
# csf = open('output10.csv', 'w', newline='', encoding='utf-8')
# writer = csv.writer(csf)
# writer.writerow(["評測索引", "評論ID", '評論人', "受評人", "受評ID", '主動且積極地參與小組活動', '個別發想的題目具有參考價值',
#               '願意分享自己的想法以及相關的資源等訊息', '願意接受小組的分工安排並負責任完成',
#               '有助於提升小組的團隊精神', '尊重組員間不同的背景與意見，且願意跟大家一起討論、商量，達成共識', '有必要時，願意提供小組團隊適當的支援',
#               '能欣賞其他成員產出的成品，並給予正向的回饋', '願意為了達成小組共同的任務，而跟大家協同合作', '小組在討論時，能夠友善地溝通與表達意見',
#               '跟小組成員保持聯繫，讓彼此都知道目前的小組進度', '產出有品質的成品', '能在小組約定的截止日期前，完成應該完成的工作項目', '對其他組員的需求與感受能夠有所覺察',
#               '了解小組討論內容的重點，且能給予有助益的建議', '願意讓小組成員了解自己的需要與感受', "組別", '總分'])
# for j in time_name:
#     with open('G:/1072Mon/'+j+'/group10.csv', 'r', newline='', encoding='utf-8') as csvfile:
#         rows = csv.DictReader(csvfile)
#         for row in rows:
#             j_name = row[judged_man]
#             b_name = row[be_judged_man]
#             if dict_student.get(row[judged_man]) == None:
#                 # if row[judged_man] not in dict_student:
#                 #     dict_student.update({row[judged_man]: new_name})
#                 # print(t)
#                 new_name = 'student_00' + str(student_num)
#                 dict_student[row[judged_man]] = {'group10': new_name}
#                 print(dict_student)
#                 student_num += 1
#             else:
#                 pass
#             person_score = 0
#             seperate_list = []
#             for i in topic_list:
#                 # print(row[i])#同一個人的全部評論,橫的
#                 if row[i] in score_list:
#                     # print(score_list.index(row[i])+1)
#                     person_score = person_score + score_list.index(row[i]) + 1
#                     seperate_list.append(score_list.index(row[i]) + 1)
#             num = dict_student.get(j_name).get('group10')  # 本名的編號
#             writer.writerow(
#                 [j, num, row[judged_man], row[be_judged_man], dict_student.get(row[be_judged_man])] + seperate_list + [
#                     "group10", person_score])
# s = open('group10relative.csv', 'w', newline='', encoding='utf-8')
# s_w = csv.writer(s)
# s_w.writerow(['True_name', 'Number', 'Group'])
# for name, groups in dict_student.items():
#     # print(name)
#     for group in groups:
#         # print(group + ':', groups[group])
#         s_w.writerow([name, groups[group], group])
# s.close()

name_me = open('group10relative.csv', 'r', newline='', encoding='utf-8')
rows2 = csv.DictReader(name_me)
dict_2 = {}
for row in rows2:
    if dict_2.get(row['True_name'], 'n') == 'n':
        dict_2[row['True_name']] = row['Number']

print(dict_2)
go = open('output10.csv', 'r', encoding='utf-8').read().split('\n')
key_L = list(dict_2.keys())
row = 0
result = []
for sent in go:
    result.append(sent.split(','))
    row += 1
    # if '\,\,' in sent:
    #     index.append(row)

saveFile = '\ufeff'
for sent in result:
    saveFile += '\n'
    try:
        if sent[3] in key_L:
            sent[4] = dict_2.get(sent[3])
        for value in sent:
            saveFile += '%s,' % value
    except IndexError:
        pass

open('output10v2.csv', 'w', encoding='utf-8', newline='').write(saveFile)