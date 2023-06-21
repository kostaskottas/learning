list1 = [1, 2, 3, 4]
list2 = [10,20,30,40]
list3 = [8, 7, 6, 5]
list4 = [1,2,3,4,5,6,7,8,9,10]
answers = []

def sequences(list):
    list_length = len(list)
    answers = []
    
    for number in range(1, list_length):
        answer = list[(number - 1)] - list[number]
        answers.append(answer)
    
    number_of_answers = answers.count(answers[1])
    if number_of_answers == (len(answers)):
        return True
    else:
        return False


print(sequences(list4))