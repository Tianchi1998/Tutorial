unique_word_list = []
def list_of_unique_word():
    sentence = input("Sentence: ")
    sentence = sentence.lower()

    word_list = sentence.split()
    times = 0
    for i in word_list:
        times = times + 1
        punctuation = [",",".","?","!"]
        for letter in i:
            if letter in punctuation:
                word_list[times-1]=i.replace(letter," ")
                i=word_list[times-1]

    for i in word_list:
        if i not in unique_word_list:
            unique_word_list.append(i)


    print("Unique words: ",end="")
    for i in unique_word_list:
        print(i,end=" ")
    print("\n")
    list_of_unique_word()

list_of_unique_word()
