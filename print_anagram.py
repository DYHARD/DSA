class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        s=dict()
        for i in words:
            w=''.join(sorted(i))
            if w in s:
                s[w].append(i)
            else:
                s[w]=[]
                s[w].append(i)
        return s
   # s have all the keys i.e set of differnt values and stored together to print in lexographical smallest sort each of the array of key value
