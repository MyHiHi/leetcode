
def quicksort(arr):
    left,right=[],[];
    if len(arr)<2:
      return arr;
    n=len(arr)
    point=arr.pop(n//2);
    for k in arr:
      if k<point:
        left+=[k];
      else:
        right+=[k];
    return quicksort(left)+[point]+quicksort(right)


arr = [1, 2, 3, 1, 2, 4, 5322, 1,232,12,1,45,6,45,3453,432,42,31,2312,313,1,434]
print(quicksort(arr))
