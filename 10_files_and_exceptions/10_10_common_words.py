with open("workfiles/chapter_10/moby_dick.txt", encoding='utf-8') as moby_dick:
    moby_dick = moby_dick.read()
    print(moby_dick.lower().count("john"))