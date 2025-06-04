class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for letter in s:
            my_dict[letter] = my_dict.get(letter, 0) + 1
        
        for otherLetter in t:
            my_dict[otherLetter] = my_dict.get(otherLetter, 0) - 1
         Nyreturn max(my_dict.values()) == 0 and min(my_dict.values()) == 0