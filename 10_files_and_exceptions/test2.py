import re

moby_dick = "10_files_and_exceptions/moby_dick.txt"
little_women = "10_files_and_exceptions/little_women.txt"

def clean_word(word):
    return re.sub(r'\W+', '', word).lower()

with open(moby_dick, encoding='utf-8') as md:
    file1_content = md.read()
file1_wordlist = [clean_word(word) for word in file1_content.split()]

with open(little_women, encoding='utf-8') as lw:
    file2_content = lw.read()
file2_wordlist = [clean_word(word) for word in file2_content.split()]
print(file1_wordlist)