def finding_the_maximum_value(arr: list) -> int:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            max_item = arr[i]
            return max_item


array = [4, 5, 6, 7, 9, 12, 0, 1, 2, 3]
print(finding_the_maximum_value(array))
