array = input("Введите числа от 1 до 10 через пробел: ").split()
L = list(map(int, array))
for i in range(len(L)):
    idx_min = i
    for j in range(i, len(L)):
        if L[j] < L[idx_min]:
            idx_min = j
    if i != idx_min:
        L[i], L[idx_min] = L[idx_min], L[i]
print(L)
print(len(L))
element = int(input("Введите число: "))
def binary_search(L, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if L[middle] == element:
        return middle
    elif element < L[middle]:
        return binary_search(L, element, left, middle - 1)
    else:
        return binary_search(L, element, middle + 1, right)

print(binary_search(L, element, 0, len(L)))