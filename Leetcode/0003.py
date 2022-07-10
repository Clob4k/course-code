class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pres = dict()
        longest, lpointer = 0, 0
        for i in range(len(s)):
            if s[i] not in pres:
                longest = max(longest, i-lpointer+1)
            else:
                if pres[s[i]] < lpointer:
                    longest = max(longest, i-lpointer+1)
                else:
                    lpointer = pres[s[i]] + 1
            pres[s[i]] = i
        return longest

print(Solution().lengthOfLongestSubstring("dvdf"))

'''
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
          ^                  ^
          |                  |
		left               right

		seen = {a : 0, c : 1, b : 2, d: 3} 
		# case 1: seen[b] = 2, current window  is s[0:4] , 
		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
		seen = {a : 0, c : 1, b : 4, d: 3} 

indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
						 ^   ^
					     |   |
				      left  right		

indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
					     ^       ^
					     |       |
				       left    right	
                       	
		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3 
		# we can keep moving right pointer.
'''