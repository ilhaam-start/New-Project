def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1 #This returns the amount of times char is in the dictionary, if char is not in the dictionary, then it returns 0. The +1 adds 1 to the count of char. It's basically counting how many times char is in the text.
    letter = sorted(counter.items(), key=lambda item: -item[1])[0][0] #The first part sorts the items in the dictionary, then the second
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")

# , key=lambda item: item[1])[0][1]

# counter.items() - returns a list of the key value pairs, where each key is the character in the dictionary and each value is the number of occurences of that character
# key=lambda item: item[1] - This is saying that it lambda item: -item[1] is used as the sorting key.
# sorted(counter.items(), key=lambda item: -item[1]) - then sorts the key value pairs from descending order hence the -item...