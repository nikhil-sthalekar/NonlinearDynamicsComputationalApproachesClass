def logistic_map(n, x_0, r):
    i = 0
    x_n = x_0
    while i < n: 
      x_n = r * x_n * (1.0 - x_n)
      i += 1

    print(x_n)

logistic_map(10, 0.2, 2.6)   
