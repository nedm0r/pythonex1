from random import randint
file_path = "C:/Users/dioni/OneDrive/Рабочий стол/Exercise30.txt"
with open(file_path,"r")as i:
    word=i.read()
    WordList=word.split()
    x=randint(0, len(WordList))
    print(WordList[x])

