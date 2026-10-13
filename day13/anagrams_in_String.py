
s = "cbaebabacd"
p = "abc"

result = []
left = 0
window = {}

for right in range(len(s)):
    window[s[right]] = window.get(s[right], 0) + 1

    if right - left + 1 > len(p):
        window[s[left]] -= 1

        if window[s[left]] == 0:
            del window[s[left]]

        left += 1

    if right - left + 1 == len(p):
        if all(window.get(ch, 0) == p.count(ch) for ch in set(p)):
            result.append(left)

print(result)
