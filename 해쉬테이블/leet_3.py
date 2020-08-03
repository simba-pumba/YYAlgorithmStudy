class Solution:

    

    def lengthOfLongestSubstring(self, s: str) -> int:

        self.max_len = 0

        self.s = s

        self.check = len(set(s))

        if  (self.check == 0) or (self.check == 1):

            return self.check

        for i in range(len(s)-1):

            

            temp_len = self.unique_check(i)

            if temp_len>self.max_len:

                self.max_len = temp_len

        

 

        return self.max_len

    

    

    

    def unique_check(self, start_str):

        temp_s = self.s[start_str]

        for i in range(start_str+1, len(self.s)):

            new_sub = temp_s + self.s[i]

            if len(temp_s) == len(set(new_sub)):

                break

            else:

                temp_s = new_sub

        

        return len(temp_s)