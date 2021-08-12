# 최초 submit
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {
            'a':0,
            'b':1,
            'c':2,
            'd':3,
            'e':4,
            'f':5,
            'g':6,
            'h':7,
            'i':8,
            'j':9,
            'k':10,
            'l':11,
            'm':12,
            'n':13,
            'o':14,
            'p':15,
            'q':16,
            'r':17,
            's':18,
            't':19,
            'u':20,
            'v':21,
            'w':22,
            'x':23,
            'y':24,
            'z':25
        }
        ansDict = dict()
        for st in strs:
            temp = [0]*26
            for s in st:
                temp[word_dict[s]] += 1 
            str_temp = tuple(temp)
            if not ansDict.get(str_temp):
                ansDict[str_temp] = [] 
            ansDict[str_temp].append(st)
        return [v for v in ansDict.values()]

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""