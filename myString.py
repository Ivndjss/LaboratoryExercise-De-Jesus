# myString.py
from collections import Counter

myString = "To understand the need for creating a class let us consider an example: Let us say that you wanted to track the number of dogs which may have different attributes like breed, and age. If a list is used, the first element could be the dog’s breed while the second element could represent its age. Let's suppose there are 100 different dogs, then how would you know which element is supposed to be which? What if you wanted to add other properties to these dogs? This lacks organization and it’s the exact need for classes."

words = myString.split()
ivndjss = Counter(words)

# Display the number of the word occurrences and the first 5 most common words mentioned in myString.
print(ivndjss.most_common(5))

# Display the total number of words in myString
print(len(words))

# Display all the items sets (keywords and values) of all words in myString
print(ivndjss.items())

# Display the count of a specific word from myString
print(ivndjss['word'])