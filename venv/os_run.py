import os

for dirPath, dirNames, fileNames in os.walk("C:/Users/admin/Desktop/get_analyze_score/venv"):
    # print(type(dirPath))  # os.walk 出來會是一個tuple裡面是([('目前路徑(str)', ['裡面有的資料夾'](list), [檔案名稱](list))])
    # print(dirNames)
    # print(dirPath)
    for f in fileNames:
        # pass
        print(os.path.join(dirPath, f))# 印出所有檔案