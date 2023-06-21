list_of_num = [71, 22, 51, 6, 53, 49, 69, 70, 48, 98, 20, 75, 0, 25, 19, 81, 99, 46, 31, 29, 7, 73, 55, 18, 64, 37, 33, 14, 11, 84, 21]

done = False
for x1 in list_of_num:
    if done:
        break
    for x2 in list_of_num:
        if done:
            break
        for x3 in list_of_num:
            if done:
                break
            for x4 in list_of_num:
                if done:
                    break
                for x5 in list_of_num:
                    if done:
                        break
                    for x6 in list_of_num:
                        if done:
                            break
                        if x1 != x2 != x3 != x4 != x5 != x6:
                            if x1+x2+x3+x4+x5+x6 == 500:
                                print(x1, x2, x3, x4, x5, x6)
                                done = True
                                break
