class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def mima(i):
            A=[int(i) for i in str(i)]
            length=len(A)
            ans=int(str(max(A))*length)
            return ans
        new_nums=[mima(i) for i in nums]
        return sum(new_nums)