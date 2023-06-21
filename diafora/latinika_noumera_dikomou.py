class Solution:
    
    
    def roman_to_int(self, s):
        resoltes = []
        list_of_letters = [letter for letter in s]
        list_index = [x for x in range(len(list_of_letters))]
        for index in list_index:
            if list_of_letters [index] == "M"and index == 0:
                resoltes.append(1000)
            elif list_of_letters[index] == "M" and index > 0 and list_of_letters[index-1] != "C":
                resoltes.append(1000)
            elif list_of_letters[index] == "M" and index > 0 and list_of_letters[index-1] == "C":
                resoltes.append(900)
            
            elif list_of_letters[index] == "D"and index == 0:
                resoltes.append(500)
            elif list_of_letters[index] == "D" and index > 0 and list_of_letters[index-1] != "C":
                resoltes.append(500)
            elif list_of_letters[index] == "D" and index > 0 and list_of_letters[index-1] == "C":
                resoltes.append(400)
            
            elif list_of_letters[index] == "C" and index < (len(list_of_letters)-1) and index > 0  and list_of_letters[index+1] == "M":
                resoltes.append(0)
            elif list_of_letters[index] == "C" and index < (len(list_of_letters)-1) and index > 0  and list_of_letters[index+1] == "D":
                resoltes.append(0)            
            elif list_of_letters[index] == "C" and index == 0:
                resoltes.append(100)
            elif list_of_letters[index] == "C" and index > 0 and list_of_letters[index-1] != "X":
                resoltes.append(100)
            elif list_of_letters[index] == "C" and index > 0 and list_of_letters[index-1] == "X":
                resoltes.append(90)
                       
            elif list_of_letters[index] == "L" and index == 0:
                resoltes.append(50)
            elif list_of_letters[index] == "L" and index > 0 and list_of_letters[index-1] != "X":
                resoltes.append(50)
            elif list_of_letters[index] == "L" and index > 0 and list_of_letters[index-1] == "X":
                resoltes.append(40)

            elif list_of_letters[index] == "X" and index < (len(list_of_letters)-1) and index > 0 and list_of_letters[index+1] == "C":
                resoltes.append(0)   
            elif list_of_letters[index] == "X" and index < (len(list_of_letters)-1) and index > 0 and list_of_letters[index+1] == "L":
                resoltes.append(0)                         
            elif list_of_letters[index] == "X" and index == 0:
                resoltes.append(10)
            elif list_of_letters[index] == "X" and index > 0 and list_of_letters[index-1] != "I":
                resoltes.append(10)
            elif list_of_letters[index] == "X" and index > 0 and list_of_letters[index-1] == "I":
                resoltes.append(9)

            elif list_of_letters[index] == "V" and index == 0:
                resoltes.append(5)
            elif list_of_letters[index] == "V" and index > 0 and list_of_letters[index-1] != "I":
                resoltes.append(5)
            elif list_of_letters[index] == "V" and index > 0 and list_of_letters[index-1] == "I":
                resoltes.append(4)

            elif list_of_letters[index] == "I" and index < (len(list_of_letters)-1) and index > 0 and list_of_letters[index+1] == "X":
                resoltes.append(0)   
            elif list_of_letters[index] == "I" and index < (len(list_of_letters)-1) and index > 0 and list_of_letters[index+1] == "V":
                resoltes.append(0)                         
            elif list_of_letters[index] == "I" :
                resoltes.append(1)

          


        print(sum(resoltes))
        



number = "MCMXCIX"
example = Solution()
example.roman_to_int(number)