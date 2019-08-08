import re
import csv


def write_student(dict):
    st = open("student_new_name.txt", 'w', encoding='utf-8')
    st.write(str(dict_student))
    st.close()

def first_generate():
    initial_count = 0
    student_num = 0
    csf = open('output3.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(csf)
    writer.writerow(["評測索引", "評論ID", '評論人', "受評人", "受評ID", '主動且積極地參與小組活動', '個別發想的題目具有參考價值',
                  '願意分享自己的想法以及相關的資源等訊息', '願意接受小組的分工安排並負責任完成',
                  '有助於提升小組的團隊精神', '尊重組員間不同的背景與意見，且願意跟大家一起討論、商量，達成共識', '有必要時，願意提供小組團隊適當的支援',
                  '能欣賞其他成員產出的成品，並給予正向的回饋', '願意為了達成小組共同的任務，而跟大家協同合作', '小組在討論時，能夠友善地溝通與表達意見',
                  '跟小組成員保持聯繫，讓彼此都知道目前的小組進度', '產出有品質的成品', '能在小組約定的截止日期前，完成應該完成的工作項目', '對其他組員的需求與感受能夠有所覺察',
                  '了解小組討論內容的重點，且能給予有助益的建議', '願意讓小組成員了解自己的需要與感受', "組別", '總分'])
    # csf.close()
    for c in class_name:
        print(c)
        last_file_num = 48
        j_name = ''
        b_name = ''
        for t in time_name:
            for ff in range(0, last_file_num):
                # print("time_name: ", t, "file_num:", ff + 1)
                if ff < 10:
                    file_num = '0' + str(ff + 1)
                else:
                    file_num = str(ff + 1)

                try:
                    print("time_name: ", t, "file_num:", ff + 1)
                    with open('G:/' + c + '/' + t + '/group' + file_num + '.csv', 'r', newline='',
                              encoding='utf-8') as csvfile:
                        rows = csv.DictReader(csvfile)
                        for row in rows:
                            j_name = row[judged_man]
                            b_name = row[be_judged_man]
                            new_name = 'student_00' + str(student_num)
                            if dict_student.get(row[judged_man]) == None:
                                # if row[judged_man] not in dict_student:
                                #     dict_student.update({row[judged_man]: new_name})
                                # print(t)
                                dict_student[row[judged_man]] = {'group'+file_num: new_name}
                                print(dict_student)
                                student_num += 1
                            else:
                                pass
                            # print(row[judged_man] + ':')
                            person_score = 0
                            seperate_list = []
                            for i in topic_list:
                                # print(row[i])#同一個人的全部評論,橫的
                                if row[i] in score_list:#她評分的分數
                                    # print(score_list.index(row[i])+1)
                                    person_score = person_score + score_list.index(row[i]) + 1
                                    seperate_list.append(score_list.index(row[i]) + 1)
                                # print("--")
                                # dict_student[row[judged_man]].update({i: row[i]})
                                # print(dict_student.get(row[judged_man]))
                                # 要顧慮到不同class同個名子的問題
                            num = dict_student.get(j_name).get('group'+file_num)# 本名的編號
                            # num = dict_student[row[judged_man]].get(file_num)
                            # print("評測索引", t, num, "組別:", ff + 1, '總分:', person_score, "受評人: ", row[be_judged_man])
                            # print(num)
                            # writer.writerow(["評測索引", "new_name", '評論人', "組別", '總分', "受評人"])
                            writer.writerow(
                                [t, num, row[judged_man], row[be_judged_man], dict_student.get(row[be_judged_man])] + seperate_list+["group" + str(ff + 1), person_score])
                            # print('-------------')

                        # print(dict_student)
                        # print("now length", len(dict_student))
                        # for i in topic_list:
                        #     print(row[i])
                except FileNotFoundError:
                    # if t == '4th':
                    #     if c != 'class05':
                    #         initial_count = ff
                    #     else:
                    #         break
                    pass
                # except KeyError:
                #     # wrong = open('wrong.txt', 'w+', encoding='utf-8')
                #     # wrong.write(t+j_name+b_name+str(ff + 1))
                #     # wrong.close()
                #     print(t+j_name+b_name+str(ff + 1))
                # except TypeError:
                #     pass
    # write_student(dict_student)
    csf.close()
    print(dict_student)
    s = open('name_relative2.csv', 'w', newline='', encoding='utf-8')
    s_w = csv.writer(s)
    s_w.writerow(['True_name', 'Number', 'Group'])
    for name, groups in dict_student.items():
        # print(name)
        for group in groups:
            # print(group + ':', groups[group])
            s_w.writerow([name, groups[group], group])
    s.close()


if __name__ == '__main__':
    class_name = ['1072Mon', '1072Tue', '1072Wed', '1072Thu', '1072Fri']
    time_name = ['1st', '2nd', '3rd']
    dict_student = {}
    be_judged_man = "受評者 (請輸入組員的姓名)"
    judged_man = '請輸入自己的姓名'
    judged_man_num = '\ufeff回應編號'
    topic_list = ['主動且積極地參與小組活動', '個別發想的題目具有參考價值',
                  '願意分享自己的想法以及相關的資源等訊息', '願意接受小組的分工安排並負責任完成',
                  '有助於提升小組的團隊精神', '尊重組員間不同的背景與意見，且願意跟大家一起討論、商量，達成共識', '有必要時，願意提供小組團隊適當的支援',
                  '能欣賞其他成員產出的成品，並給予正向的回饋', '願意為了達成小組共同的任務，而跟大家協同合作', '小組在討論時，能夠友善地溝通與表達意見',
                  '跟小組成員保持聯繫，讓彼此都知道目前的小組進度', '產出有品質的成品', '能在小組約定的截止日期前，完成應該完成的工作項目', '對其他組員的需求與感受能夠有所覺察',
                  '了解小組討論內容的重點，且能給予有助益的建議', '願意讓小組成員了解自己的需要與感受'
                  ]
    score_list = ['非常不同意', '不同意', '中等', '同意', '非常同意']
    # s = open('name_relative.csv', 'r', newline='', encoding='utf-8')
    # row_rows = csv.DictReader(s)
    # yo_dict = {}
    # for yo in row_rows:
    #     yo_dict[yo['True_name']] = yo['Number']
    # s.close()
    # print(yo_dict)
    first_generate()
    # with open("output.csv", 'r', newline='', encoding='utf-8') as cc:
    #     every_rows = csv.DictReader(cc)
    #     new_csv = open("finaloutput.csv", 'w', newline='', encoding='utf-8' )
    #     new_writer = csv.writer(new_csv)
    #     new_writer.writerow(["評測索引", "評論ID", "受評ID", '主動且積極地參與小組活動', '個別發想的題目具有參考價值',
    #                '願意分享自己的想法以及相關的資源等訊息', '願意接受小組的分工安排並負責任完成',
    #                '有助於提升小組的團隊精神', '尊重組員間不同的背景與意見，且願意跟大家一起討論、商量，達成共識', '有必要時，願意提供小組團隊適當的支援',
    #                '能欣賞其他成員產出的成品，並給予正向的回饋', '願意為了達成小組共同的任務，而跟大家協同合作', '小組在討論時，能夠友善地溝通與表達意見',
    #                '跟小組成員保持聯繫，讓彼此都知道目前的小組進度', '產出有品質的成品', '能在小組約定的截止日期前，完成應該完成的工作項目', '對其他組員的需求與感受能夠有所覺察',
    #                '了解小組討論內容的重點，且能給予有助益的建議', '願意讓小組成員了解自己的需要與感受', "組別", '總分'])
    #     for rr in every_rows:
    #         print(yo_dict.get(rr['受評人']))
    #         new_writer.writerow(
    #             [rr["評測索引"], rr["評論ID"], yo_dict.get(rr['受評人']), rr["主動且積極地參與小組活動"], rr['個別發想的題目具有參考價值'],
    #                rr['願意分享自己的想法以及相關的資源等訊息'], rr['願意接受小組的分工安排並負責任完成'],
    #                rr['有助於提升小組的團隊精神'], rr['尊重組員間不同的背景與意見，且願意跟大家一起討論、商量，達成共識'], rr['有必要時，願意提供小組團隊適當的支援'],
    #                rr['能欣賞其他成員產出的成品，並給予正向的回饋'], rr['願意為了達成小組共同的任務，而跟大家協同合作'], rr['小組在討論時，能夠友善地溝通與表達意見'],
    #                rr['跟小組成員保持聯繫，讓彼此都知道目前的小組進度'], rr['產出有品質的成品'], rr['能在小組約定的截止日期前，完成應該完成的工作項目'], rr['對其他組員的需求與感受能夠有所覺察'],
    #                rr['了解小組討論內容的重點，且能給予有助益的建議'], rr['願意讓小組成員了解自己的需要與感受'], rr["組別"], rr['總分']])
    #
    #     new_csv.close()

        # check = []
        # last_thing = '1st'
        # for rr in every_rows:
        #     # print(rr['new_name'])
        #
        #     if rr['評測索引'] == last_thing:
        #         # print("same", rr['評測索引'])
        #         for st, ask in check:
        #             # print(st, ask)
        #             if rr['評論ID'] == st and re.findall(ask, rr['受評人']):
        #                 print(st, rr['評論人']+','+rr['受評人'])
        #
        #         check.append((rr['評論ID'], rr['受評人']))
        #     else:
        #         check = []
        #
        #     last_thing = rr['評測索引']
    # cc.close()

