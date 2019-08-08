import re
import csv

if __name__ == '__main__':
    name = '評測索引'
    index = []
    judged_man = []
    be_judged_man = []
    score = []
    se_gender_list = []
    re_gender_list = []
    gr_size_list = []
    class_list = []
    self_list = []
    gr_list = []
    data_dict = {}
    final_output = open('finaloutput.csv', 'r', encoding='utf-8', newline='')
    rows = csv.DictReader(final_output)
    # row1 = next(rows)#第一行
    data_1 = open('data_1.csv', 'r', encoding='utf-8', newline='')
    data_row = csv.DictReader(data_1)
    for data in data_row:
        if data_dict.get(data['Number'], 'n') == 'n':
            data_dict[data['Number']] = {'Gender': data['Gender'], 'Group Size': data['Group Size'], 'class': data['class']}
    # print(data_dict)
    # print(data_dict['student_000'].get('Gender'))
    for row in rows:
        i = int(''.join(re.findall('\d', row['評測索引'])))#轉成純數字的index
        j = int(''.join(re.findall('\d', row['評論ID'])))
        be_j = int(''.join(re.findall('\d', row['受評ID'])))
        gr = int(''.join(re.findall('\d', row['組別'])))
        score.append(row['總分'])
        index.append(i)
        judged_man.append(j)
        be_judged_man.append(be_j)
        gr_list.append(gr)
        if row['評論ID'] == row['受評ID']:
            self_list.append(1)
        else:
            self_list.append(0)

        if data_dict[row['評論ID']].get('Gender') == 'F':
            se_gender_list.append(0)
        else:
            se_gender_list.append(1)
        if data_dict[row['受評ID']].get('Gender') == 'F':
            re_gender_list.append(0)
        else:
            re_gender_list.append(1)
        gr_size_list.append(data_dict[row['評論ID']].get('Group Size'))
        class_list.append(data_dict[row['評論ID']].get('class'))
    w = open('transform.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(w)
    writer.writerow(['Score ID', 'Grp ID', 'Ratee ID', 'Rater ID', 'Score', 'Self', 'ReGen', 'SeGen', 'GrpSize', 'Class'])
    for x in range(len(index)):
        writer.writerow([index[x], gr_list[x], be_judged_man[x], judged_man[x], score[x], self_list[x],
                         re_gender_list[x], se_gender_list[x], gr_size_list[x], class_list[x]])

    # print(len(re_gender_list))
    # print(re_gender_list)

    # print(len(gr_size_list))
    # print(len(class_list))
    # print(re_gender_list)
    # print(len(se_gender_list))

    # print(len(index))
    # print(len(score))
    # print(len(judged_man))




