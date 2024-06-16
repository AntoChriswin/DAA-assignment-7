def max_num_of_palindromes(s, k):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            nonlocal max_count
            max_count = max(max_count, len(path))
            return

        for end in range(start + k, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):
                path.append(sub)
                backtrack(end, path)
                path.pop()

    max_count = 0
    backtrack(0, [])
    return max_count

# Example 1
s1 = "abaccdbbd"
k1 = 3
print(max_num_of_palindromes(s1, k1))  # Output: 2

# Example 2
s2 = "adbcda"
k2 = 2
print(max_num_of_palindromes(s2, k2))  # Output: 0
