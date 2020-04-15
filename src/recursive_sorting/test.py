def test(arr):
    for x in arr:
        print("hello")

test([1,2,3])

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

merge([1,3,5],[2,4,6])