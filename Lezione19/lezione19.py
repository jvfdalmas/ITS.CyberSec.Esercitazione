def merge_sort(array: list) -> list:
    if len(array) > 1:
        left: list = array[:len(array)//2]
        right: list = array[len(array)//2:]

        merge_sort(left)
        merge_sort(right)

        i: int = 0 # index left array
        j: int = 0 # index right array
        k: int = 0 # index final array

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
                k += 1
            else:
                array[k] = right[j]
                j += 1
                k += 1
        
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array
    
array1: list = [10, -5, 2, 0, 7]

print(merge_sort(array1))
