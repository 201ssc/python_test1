import numpy as np

arr1 = [10,20,11,28,14]
arr2 = [12,21,14,4,5]
n = 5

def get_22(arr, n):
    ar = []
    for i in arr:
        a = np.binary_repr(i, width=n)
        ar.append(a)
    return ar

ar = get_22(arr1, 5)
a1 = list(np.int_(ar))
#
ar2 = get_22(arr1,5)
a2 = list(np.int_(ar2))
#
bb = [x+y for x,y in zip(a1, a2)]
#cc = [ar[i] + ar2[i] for i in range(len(ar))]
def get_div():

    pass

#
# for i in bb:
#     num = list(map(int, str(i)))
#     print(num_list)
#
num = [0,2,0,2,0]
num2 = []
for i in num:
    if i > 0:
        a= 1
    else:
        a= 0
    num2.append(a)
