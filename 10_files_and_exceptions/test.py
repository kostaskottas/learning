moby_dick = "10_files_and_exceptions/moby_dick.txt"
little_women = "10_files_and_exceptions/little_women.txt"

with open(moby_dick, encoding='utf-8') as md:
#file1 = open(moby_dick, "r")
    file1_content = md.read()
file1_wordlist = file1_content.split()

with open(little_women, encoding='utf-8') as lw:
    file2_content = lw.read()
file2_wordlist = file2_content.split()

end = True
sectums1 = 1
while end:
    sectum_len1 = len(file1_wordlist) // sectums1
    sectum_start1 = 0
    print(sectum_len1)
    if sectum_len1 < 30:
        end = False
    for i in range(sectums1):
        sectum_end1 = sectum_start1 + sectum_len1
        sectum_start2 = 0
        
        while sectum_start2 + sectum_len1 <= len(file2_wordlist):
            sectum_end2 = sectum_start2 + sectum_len1
            
            if file1_wordlist[sectum_start1:sectum_end1] == file2_wordlist[sectum_start2:sectum_end2]:
                print(file1_wordlist[sectum_start1:sectum_end1])
                end = False
            sectum_start2 = sectum_end2
        sectum_start1 = sectum_end1
    sectums1 *= 2