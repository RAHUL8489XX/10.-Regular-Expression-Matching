

# 🔍 10. Regular Expression Matching

> LeetCode Problem 10 — Implement regular expression matching with support for `.` and `*`.

## 🧠 Problem Statement

Given an input string `s` and a pattern `p`, implement regular expression matching with support for:
- `.` — Matches any single character
- `*` — Matches zero or more of the preceding element

The match must cover the **entire input string**.

---

## 📌 Constraints

- `1 <= len(s), len(p) <= 20`
- `s` contains only lowercase English letters
- `p` contains lowercase letters, `.` and `*`
- `*` will not be the first character in `p`

---

## 🚀 Approach

We use **Dynamic Programming** to build a 2D table `dp[i][j]`:
- `dp[i][j] = True` means `s[0..i-1]` matches `p[0..j-1]`
- Handle `*` by checking both:
  - Zero occurrence: `dp[i][j-2]`
  - One or more occurrence: `dp[i-1][j]` if preceding character matches

---

## 🧪 Example Cases

| Input     | Pattern   | Output | Explanation                                  |
|-----------|-----------|--------|----------------------------------------------|
| `"aa"`    | `"a"`     | False  | `"a"` doesn't match full `"aa"`              |
| `"aa"`    | `"a*"`    | True   | `*` allows multiple `"a"`                    |
| `"ab"`    | `".*"`    | True   | `.` matches any char, `*` allows repetition  |
| `"aab"`   | `"c*a*b"` | True   | `c*` → "", `a*` → "aa", `b` → "b"             |

---

## 🧑‍💻 Code

```python
class Solution(object):
    def isMatch(self, s, p):
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True

        for j in range(2, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (
                        dp[i-1][j] if p[j-2] == '.' or p[j-2] == s[i-1] else False
                    )

        return dp[len(s)][len(p)]
