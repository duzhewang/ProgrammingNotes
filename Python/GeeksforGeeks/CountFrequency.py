# Counting the frequencies in a list using dictionary in Python

def CountFrequency(my_list):
    freq={}
    for item in my_list:
        if item in freq:
           freq[item]+=1
        else:
            freq[item]=1
    for key, value in freq.items():
        print("{}:{}".format(key, value))


my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
CountFrequency(my_list)


# using list.count()

def CountFrequency2(my_List):
    freq={}
    for item in my_list:
        freq[item]=my_list.count(item)

    for key, value in freq.items():
        print("{}:{}".format(key, value))
