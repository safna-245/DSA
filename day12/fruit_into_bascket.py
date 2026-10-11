
fruits = [1, 2, 3, 2, 2]

left = 0
basket = {}
max_fruits = 0

for right in range(len(fruits)):
    fruit = fruits[right]

    if fruit in basket:
        basket[fruit] += 1
    else:
        basket[fruit] = 1

    while len(basket) > 2:
        basket[fruits[left]] -= 1

        if basket[fruits[left]] == 0:
            del basket[fruits[left]]

        left += 1

    max_fruits = max(max_fruits, right - left + 1)

print(max_fruits)
