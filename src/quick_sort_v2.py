
def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    less, greater = [], []
    for i in array[1:]:
        if i <= pivot:
            less.append(i)
        else:
            greater.append(i)
    return quickSort(less) + [pivot] + quickSort(greater)
    
        # pivot = array[0]
        # less = [i for i in array[1:] if i <= pivot]
        # greater = [i for i in array[1:] if i > pivot]
        # return quickSort(less) + [pivot] + quickSort(greater)