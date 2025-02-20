# todo 257
# def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#     res = []
#
#     def dfs(node, path):
#         if not node:
#             return
#
#         if path:
#             path += "->" + str(node.val)
#         else:
#             path = str(node.val)
#         if not node.left and not node.right:
#             res.append(path)
#             return
#         dfs(node.right, path)
#         dfs(node.left, path)
#
#     dfs(root, "")
#     return res


# todo 383
# https://leetcode.com/problems/ransom-note/description/
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         char_counts = {}
#
#         for char in magazine:
#             char_counts[char] = char_counts.get(char, 0) + 1
#
#         for char in ransomNote:
#             if char not in char_counts or char_counts[char] == 0:
#                 return False
#             char_counts[char] -= 1
#
#         return True

# todo 409
# https://leetcode.com/problems/longest-palindrome/description/
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         char_counts = {}
#         for char in s:
#             char_counts[char] = char_counts.get(char, 0) + 1
#
#         length = 0
#         odd_found = False
#
#         for count in char_counts.values():
#             length += count // 2 * 2
#             if count % 2 != 0 and not odd_found:
#                 length += 1
#                 odd_found = True
#
#         return length

# todo 2 usul
#
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         s1=set()
#         for i in s:
#             if i not in s1:
#                 s1.add(i)
#             else:
#                 s1.remove(i)
#         if len(s1)!=0:
#             return len(s)-len(s1)+1
#         else:
#             return len(s)


# todo 412. Fizz Buzz
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         answer = []
#         for i in range(1, n + 1):
#             if i % 3 == 0 and i % 5 == 0:
#                 answer.append("FizzBuzz")
#             elif i % 3 == 0:
#                 answer.append("Fizz")
#             elif i % 5 == 0:
#                 answer.append("Buzz")
#             else:
#                 answer.append(str(i))
#         return answer


# todo 459
# https://leetcode.com/submissions/detail/1546634932/
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         return s in (s + s)[1:-1]



# todo 482
# https://leetcode.com/problems/license-key-formatting/description/

# class Solution:
#     def licenseKeyFormatting(self, s: str, k: int) -> str:
#         string = s.replace('-', '').upper()
#         mod = len(string) % k
#         parts = []
#         if mod > 0:
#             parts.append(string[:mod])
#         for i in range(mod, len(string), k):
#             parts.append(string[i:i + k])
#         return '-'.join(parts)



# todo 521
# https://leetcode.com/problems/longest-uncommon-subsequence-i/
# class Solution:
#     def findLUSlength(self, a: str, b: str) -> int:
#         if a==b :
#             return -1
#         else:
#             return max(len(a), len(b))



# todo 557
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(map(lambda word: word[::-1], s.split()))


# todo 599
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         index_sum = inf
#         list3 = set(list2)
#         for i, word in enumerate(list1):
#             if word in list3:
#                 if (i_sum := i + list2.index(word)) < index_sum:
#                     result = [word]
#                     index_sum = i_sum
#                 elif i_sum == index_sum:
#                     result.append(word)
#         return result


# todo 38
# https://leetcode.com/problems/count-and-say/description/
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         curr = "1"
#
#         for _ in range(n - 1):
#             j = k = 0
#             next_str = ""
#             while j < len(curr):
#                 while k < len(curr) and curr[j] == curr[k]:
#                     k += 1
#                 next_str += str(k - j) + curr[j]
#                 j = k
#             curr = next_str
#
#         return curr

# todo 22
# https://leetcode.com/problems/generate-parentheses/description/
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#
#         def backtrack(s="", open=0, close=0):
#             if len(s) == 2 * n:
#                 res.append(s)
#                 return
#             if open < n:
#                 backtrack(s + "(", open + 1, close)
#             if close < open:
#                 backtrack(s + ")", open, close + 1)
#
#         backtrack()
#         return res


# todo 17
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#         digit_to_chars = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
#         combinations = ['']
#         for digit in digits:
#             letters = digit_to_chars[int(digit) - 2]
#             combinations = [prefix + letter for prefix in combinations for letter in letters]
#         return combinations