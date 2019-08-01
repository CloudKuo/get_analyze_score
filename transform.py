import re
import csv

if __name__ == '__main__':
    name = '評測索引'
    index = []
    with open('finaloutput.csv', 'r', encoding='utf-8', newline='') as final_output:
        rows = csv.DictReader(final_output)
        # row1 = next(rows)#第一行
        for row in rows:
            i = int(''.join(re.findall('\d', row['評測索引'])))#轉成純數字的index
            index.append(i)


