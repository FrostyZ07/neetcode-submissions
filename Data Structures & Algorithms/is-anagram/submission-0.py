class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1={}
        h2={}
        if len(s)!=len(t):
            return False
        for a in range(len(s)):
            h1[s[a]]=1+h1.get(s[a],0)
            h2[t[a]]=1+h2.get(t[a],0)
        return h1==h2