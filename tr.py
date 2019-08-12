import csv
final_output = open('name_relative2v2.csv', 'r', encoding='utf-8', newline='')
rows = csv.DictReader(final_output)
data_1 = open('data_2.csv', 'r', encoding='utf-8', newline='')
data_row = csv.DictReader(data_1)
new_data = open('new_data2.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(new_data)
writer.writerow(['True_name', 'Number', 'Gender', 'Group', 'GroupSize', 'class'])
st_dict = {}

for row in rows:
    print(row['Number'])
    print(row["True_name"])
    if st_dict.get(row['True_name'], 'n') == 'n':
        st_dict[row['True_name']] = row['Number']
key_L = list(st_dict.keys())
for data in data_row:
    if data['True_name'] in key_L:
        print(data['True_name'])
        new_number = st_dict.get(data['True_name'])
        writer.writerow([data['True_name'], new_number, data['Gender'], data['Group'], data['GroupSize'], data['class']])
    else:
        writer.writerow(
            [data['True_name'], data['Number'], data['Gender'], data['Group'], data['GroupSize'], data['class']])


