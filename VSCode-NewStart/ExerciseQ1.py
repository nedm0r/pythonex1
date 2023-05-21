def grep(word,path):
    i = open(path, "r")
    lines = i.readlines()
    for line in lines:
        if word in line:
                print(line)
    i.close()

file_path = "C:/Users/dioni/OneDrive/Рабочий стол/Exercise30.txt"
w = "AAS"

grep(w,file_path)