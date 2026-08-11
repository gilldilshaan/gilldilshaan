realoutputs = [10, 20, 30, 40, 50]
predictedoutputs = [12, 18, 33, 37, 52]

sum_error = 0

for i in range(len(realoutputs)):
    error = realoutputs[i] - predictedoutputs[i]
    squared_error = error ** 2
    sum_error = sum_error + squared_error

mse = sum_error / len(realoutputs)

print("Mean Squared Error =", mse)