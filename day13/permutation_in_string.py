
s1 = "ab"
s2 = "eidbaooo"

left = 0
window = {}

for right in range(len(s2)):
    window[s2[right]] = window.get(s2[right], 0) + 1

    if right - left + 1 > len(s1):
        window[s2[left]] -= 1

        if window[s2[left]] == 0:
            del window[s2[left]]

        left += 1

    if right - left + 1 == len(s1):
        if all(window.get(ch, 0) == s1.count(ch) for ch in set(s1)):
            print(True)
            break
else:
    print(False)
