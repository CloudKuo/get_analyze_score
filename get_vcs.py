import re
import csv
if __name__ == '__main__':
    class_name = ['class01', 'class02', 'class03', 'class04', 'class05']
    time_name = ['1st', '2nd', '3rd', '4th']
    student_num = 0
    dict_student = {}
    for c in class_name:
        print(c)
        last_file_num = 50
        for t in time_name:
            for ff in range(last_file_num):
                print("time_name: ", t, "file_num:", ff+1)
                if ff < 10:
                    file_num = '0'+str(ff+1)
                else:
                    file_num = str(ff+1)
                try:
                    with open('G:/'+c+'/'+t+'/group'+file_num+'.csv', 'r', newline='', encoding='utf-8') as csvfile:
                        rows = csv.DictReader(csvfile)
                        be_judged_man = "受評者 (請輸入組員的姓名)"
                        judged_man = '請輸入自己的姓名'
                        judged_man_num = '\ufeff回應編號'
                        topic_list = ['主動且積極地參與小組活動', '個別發想的題目具有參考價值',
                                      '願意分享自己的想法以及相關的資源等訊息', '願意接受小組的分工安排並負責任完成',
                                      '有助於提升小組的團隊精神', '尊重組員間不同的背景與意見，且願意跟大家一起討論、商量，達成共識', '有必要時，願意提供小組團隊適當的支援',
                                      '能欣賞其他成員產出的成品，並給予正向的回饋', '願意為了達成小組共同的任務，而跟大家協同合作', '小組在討論時，能夠友善地溝通與表達意見',
                                      '跟小組成員保持聯繫，讓彼此都知道目前的小組進度', '產出有品質的成品', '能在小組約定的截止日期前，完成應該完成的工作項目', '對其他組員的需求與感受能夠有所覺察',
                                      '了解小組討論內容的重點，且能給予有助益的建議', '願意讓小組成員了解自己的需要與感受',
                                      ]

                        for row in rows:
                            new_name = 'student_00'+str(student_num)
                            if dict_student.get(row[judged_man]) == None:
                                dict_student.update({row[judged_man]: new_name})
                                student_num += 1
                            else:
                                pass
                        # print(dict_student)
                        print("now length", len(dict_student))
                            # for i in topic_list:
                            #     print(row[i])
                except FileNotFoundError:
                    pass

    print(dict_student)


