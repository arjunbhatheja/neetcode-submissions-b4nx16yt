class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for r in strs:
           enc += str(len(r)) + "#" + r
        return enc

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while(s[j]!="#"):
                j= j+1
            length = int(s[i:j])
            end = j+1+length
            s1 = s[j+1:end]
            ans.append(s1)
            i = end
        return ans