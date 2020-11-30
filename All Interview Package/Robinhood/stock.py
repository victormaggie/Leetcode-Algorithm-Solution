def maxRevenueFromStocks(prices, algo, k):
    if not prices:
        return 0
    # mk sure k <= len(prices) ** 
    runSum = 0
    n = len(algo)
    for i in range(n):
        if algo[i] == 0:
            runSum -= prices[i]
        elif algo[i] == 1:
            runSum += prices[i]
    
    # change the buy into sell and get another value
    # consecutive sell

    for j in range(k):
        if algo[j] == 0:
            runSum += 2 * prices[j]

    # sliding window here
    mx = runSum 
    for j in range(k, n):
        if algo[j] == 0:
            runSum += 2 * prices[j]
        if algo[j-k] == 0:
            runSum -= 2 * prices[j-k]
        mx = max(mx, runSum)
    return mx 


prices =  [2, 4, 1, 5, 2, 6, 7]

algo =    [0, 1, 0, 0, 1, 0, 0]

k = 4

print(maxRevenueFromStocks(prices, algo, k))


