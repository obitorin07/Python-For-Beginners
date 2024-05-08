def fact(n):
  if n<0:
    print("Enter positive number")
  elif n ==0:
    print("Enter greather 0")
  elif n ==1:
    return 1
  else:
    for i in range(1,n+1):
      return (n * fact (n-1))
print(fact(5))
