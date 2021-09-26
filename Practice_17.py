array = input('Введите последовательность чисел через пробел')
num = int(input('Введите любое число'))

array = list(map(int, array.split(' ')))

def insert(array):
    for i in range(len(array)):
        sort = array[i]
        while i != 0 and sort < array[i-1]:
            array[i] = array[i-1]
            i -= 1
        array[i] = sort
    return array

def search(array, number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] < number and array[middle+1] >= number:
        return middle
    elif number < array[middle]:
        return search(array, number, left, middle - 1)
    else:
        return search(array, number, middle + 1, right)

left = 0
right = int(len(array)) - 1

print(insert(array))
if num < array[1] or num > array[-1]:
    print('В последовательности нет нужного числа')
else:
    print('В последовательности присутствует нужное число с индексом', search(array, num, left, right))