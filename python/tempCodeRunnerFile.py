def quick(lis):
  left,right=[],[];
  mid=len(lis)//2;
  p=lis[mid];
  for i in lis:
    if i>p:
      right+=[i];
    elif i<p:
      left+=[i];
  return quick(left)+[p]+quick(right)

print(quick([1,5,3,2,5,1,4]))

