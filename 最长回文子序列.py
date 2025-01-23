class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s=="":
            return ""
        def huiwenxulie(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        longest=""
        for i in range(len(s)):
            odd=huiwenxulie(i,i)
            even=huiwenxulie(i,i+1)
            longest=max(longest,odd,even,key=len)
        return longest