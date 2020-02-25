def r(n, myM):
  
  if n == 0 or n == 1:
      return 1
  if n not in myM:
      myM[n] = r(n-1, myM)+r(n-2, myM)
      return myM[n] 
  else:
      return myM[n]


x = r(3, {})
print(x)
