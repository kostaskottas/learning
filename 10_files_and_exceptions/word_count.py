def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filenames = ['workfiles/chapter_10/alice.txt', "workfiles/chapter_10/moby_dick.txt", "workfiles/chapter_10/little_women.txt", "workfiles/chapter_10/siddhartha.txt"]
for filename in filenames:
    count_words(filename)