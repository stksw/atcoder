def selection_sort(numbers: list):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        if min_index != i:
            numbers[min_index], numbers[i] = numbers[i], numbers[min_index]

array = [9, 4, 5, 1, 8, 7, 3] 
result = selection_sort(array) 
print(result)