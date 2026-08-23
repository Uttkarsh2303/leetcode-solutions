class Solution:
    def isPalindrome(self, num: int) -> bool:
        num_str=str(num)
        rev_num=num_str[::-1]
        if num_str==rev_num:
            return True
        return False