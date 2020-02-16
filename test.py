
def out(arr,start,end,res):
  if start==end:
    res+=[arr[:]];
  else:
    for i in range(start,end):
      arr[i],arr[start]=arr[start],arr[i];
      out(arr,start+1,end,res);
      arr[i],arr[start]=arr[start],arr[i];


lis = [1, 2, 3]
res = []
out(lis, 0,len(lis), res)
print(res)


