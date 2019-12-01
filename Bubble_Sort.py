def bubbleSort(list):
    for i in range ( len ( list ) - 1, 0, -1 ):
       for j in range (i):
           if list[j]>list[j+1]:
               temp = list[j]
               list[j] = list[j+1]
               list[j+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
print(f'Lista przed posortowaniem: {nlist}')
bubbleSort(nlist)
print(f'Lista po posortowaniu: {nlist}')