import re

def clean_word(word):
    """make every element in the list clear word"""
    return re.sub(r'\W+', '', word).lower()

def compare_word_files(file1_path, file2_path, fault_range):
    """compare 2 text files for common text"""
    #making the text files lists of words
    with open(file1_path, encoding='utf-8') as md:
        file1_content = md.read()
    file1_wordlist = [clean_word(word) for word in file1_content.split()]

    with open(file2_path, encoding='utf-8') as lw:
        file2_content = lw.read()
    file2_wordlist = [clean_word(word) for word in file2_content.split()]
    #a loop to binary search
    end = True
    sectums1 = 2
    while end:
        sectum_len1 = len(file1_wordlist) // sectums1
        sectum_len2 = sectum_len1 // 2
        sectum_start1 = 0
        print(sectum_len1)
        print(sectum_len2)
        if sectum_len1 < 20:
            end = False
        
        for i in range(sectums1):
            sectum_end1 = sectum_start1 + sectum_len1
            sectum_start2 = 0
            
            while sectum_start2 + sectum_len2 <= len(file2_wordlist):
                sectum_end2 = sectum_start2 + sectum_len2
                #check if all the words on the sectum are in the other sectum
                if all(word in file1_wordlist[sectum_start1:sectum_end1] for word in file2_wordlist[sectum_start2:sectum_end2]):
                    print("found")
                    print(file2_wordlist[sectum_start2:sectum_end2])
                    counter1 = 0
                    counter2 = 0
                    total_counter = counter1 + counter2
                    
                    #a loop to search if there is more common words out of the sectum but stop at 30 uncommon
                    while total_counter<(fault_range+1):

                        total_counter = counter1 + counter2
                        if counter1 < ((fault_range//2)+1) and sectum_start2 > 0:
                            sectum_start2 -= 1
                            if file2_wordlist[sectum_start2] not in file1_wordlist[sectum_start1:sectum_end1]:
                                print(file2_wordlist[sectum_start2])
                                counter1 +=1
                        if counter2 < ((fault_range//2)+1) and sectum_end2 < len(file2_wordlist):                                
                            sectum_end2 +=1
                            if file2_wordlist[sectum_end2] not in file1_wordlist[sectum_start1:sectum_end1]:
                                print(file2_wordlist[sectum_end2])
                                counter2 +=1
                        if sectum_start1 > 0:
                            sectum_start1 -=1
                        if sectum_end1 < len(file1_wordlist):
                            sectum_end1 +=1
                        if total_counter == fault_range:
                            end = False
                            print(file2_wordlist[sectum_start2:sectum_end2])
                            
                        
                sectum_start2 = sectum_end2
            sectum_start1 = sectum_end1
        sectums1 *= 2


moby_dick = "10_files_and_exceptions/moby_dick.txt"
little_women = "10_files_and_exceptions/little_women.txt"

text = compare_word_files(moby_dick, little_women, 30)
