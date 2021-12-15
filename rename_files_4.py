import os

def rename_file():
    path = "/home/anahit_p/Downloads/20_10_2021_5"
    os.chdir(path)
    for i, file_name in enumerate(os.listdir(path)):
        #print(i, file_name)
        if  file_name.endswith(".txt"):
            os.rename(src = file_name, dst = f'renamed{i}.txt')


rename_file()
