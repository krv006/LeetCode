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



