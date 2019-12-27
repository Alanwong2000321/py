A = [4, 2, 1, 290, 51]   
for i in range(len(A)): 
  min1 = i 
  for j in range(i+1, len(A)): 
    if A[min1] > A[j]:
      min1 = j 
      A[i], A[min1] = A[min1], A[i] 
for i in range(len(A)): 
    print("%d" %A[i]),