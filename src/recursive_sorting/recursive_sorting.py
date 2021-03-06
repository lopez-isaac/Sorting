def merge(arrA, arrB):
    s = []
    #set index start point
    arrA_idx, arrB_idx = 0, 0
    #compare arrA and arrB index values, store, increment index for next camparison
    while arrA_idx < len(arrA) and arrB_idx < len(arrB):
        if arrA[arrA_idx] < arrB[arrB_idx]:
            s.append(arrA[arrA_idx])
            arrA_idx += 1
        else:
            s.append(arrB[arrB_idx])
            arrB_idx += 1
    # for the left over uncompared value in either list manually add last index
    if arrA_idx == len(arrA):
        s.extend(arrB[arrB_idx:])
    else:
        s.extend(arrA[arrA_idx:])
    return s

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    result = arr
    #if 1 element is passed its already sorted
    if len(arr) > 1:
        mid = len(arr) // 2
        first_h = arr[:mid]
        second_h = arr[mid:]

        X = merge_sort(first_h)
        Y = merge_sort(second_h)

        result = merge(X, Y)

    return result

merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])