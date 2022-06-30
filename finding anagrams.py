# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


'''def find_anagram(word, anagram):
    # [assignment] Add your code here
    sorted(word) == sorted(anagram);
    return False
word = "hello";
anagram = "check";
print(find_anagram(word, anagram))
def find_anagram(word, anagram):
    # [assignment] Add your code here
    sorted(word) == sorted(anagram);
    return True
word = "below";
anagram = "elbow";
print(find_anagram(word, anagram))
'''

word = str(input("Please type in a word: "));
anagram = str(input("Please type in another word: "));
if word == anagram :
    print ("Correct")
     
else :
    print ("Try again")

