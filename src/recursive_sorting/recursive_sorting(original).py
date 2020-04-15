# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(a, b):
    s = []
    a_idx, b_idx = 0,0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            s.append(a[a_idx])
            a_idx += 1
        else:
            s.append(b[b_idx])
            b_idx += 1

    if a_idx == len(a):
        s.extend(b[b_idx:])
    else:
        s.extend(a[a_idx:])
    return s


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #if 1 element is passed its already sorted
    if len(arr) <= 1:
        return arr

    #split array input
    mid = len(arr)//2
    first_h = arr[:mid]
    second_h =arr[mid:]

    return merge(first_h,second_h)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
