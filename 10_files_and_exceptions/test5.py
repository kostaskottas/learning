import re

moby_dick = "10_files_and_exceptions/moby_dick.txt"
little_women = "10_files_and_exceptions/little_women.txt"

def clean_word(word):
    return re.sub(r'\W+', '', word).lower()

def compare_word_files(file1_path, file2_path):
    with open(file1_path, encoding='utf-8') as md:
        file1_content = md.read()
    file1_wordlist = [clean_word(word) for word in file1_content.split()]

    with open(file2_path, encoding='utf-8') as lw:
        file2_content = lw.read()
    file2_wordlist = [clean_word(word) for word in file2_content.split()]

    end = True
    sectums1 = 2
    while end:
        sectum_len1 = len(file1_wordlist) // sectums1
        sectum_len2 = sectum_len1 * 2
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
                
                if all(word in file2_wordlist[sectum_start2:sectum_end2] for word in file1_wordlist[sectum_start1:sectum_end1]):
                    print(f"{file1_wordlist[sectum_start1:sectum_end1]}\n")
                    print(file2_wordlist[sectum_start2:sectum_end2])
                    print(sectum_end1)
                    print(sectum_end2)
                    print(len(file1_wordlist))
                    print(len(file2_wordlist))
                    end = False
                sectum_start2 = sectum_end2
            sectum_start1 = sectum_end1
        sectums1 *= 2

moby_dick = "10_files_and_exceptions/moby_dick.txt"
little_women = "10_files_and_exceptions/little_women.txt"
compare_word_files(moby_dick, little_women)