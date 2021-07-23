def print_upper_words(words, starts_with):
    for word in words:
        if word[0] in starts_with:
            print(word.upper())



















# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], starts_with={"h", "y"})
