numbers = [10, 20, 20, 30, 40, 50, 20]

# Mean
mean = sum(numbers) / len(numbers)

# Median
numbers.sort()
n = len(numbers)

if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

# Mode
mode = max(set(numbers), key=numbers.count)

# Range
range_value = max(numbers) - min(numbers)

# Variance
variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)

# Standard Deviation
standard_deviation = variance ** 0.5

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Range =", range_value)
print("Variance =", variance)
print("Standard Deviation =", standard_deviation)