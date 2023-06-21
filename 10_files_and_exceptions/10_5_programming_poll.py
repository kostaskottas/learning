while True:
    print("If you want to stop at any time insert the word: stop")
    reason = input("Write the reason you like programming: ")
    if reason == "stop":
        break
    with open("10_files_and_exceptions/reasons_to_programming.txt", "a") as file:
        file.write(f"{reason}.\n")