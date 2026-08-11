numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# ---------------- IQR METHOD ----------------

numbers.sort()
n = len(numbers)

# Find Q1 and Q3
q1 = numbers[n // 4]
q3 = numbers[(3 * n) // 4]

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

iqr_outliers = []

for x in numbers:
    if x < lower or x > upper:
        iqr_outliers.append(x)

print("IQR Outliers =", iqr_outliers)


# ---------------- Z-SCORE METHOD ----------------

mean = sum(numbers) / len(numbers)

# Standard deviation
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
std = variance ** 0.5

z_outliers = []

for x in numbers:
    z = (x - mean) / std

    if abs(z) > 3:
        z_outliers.append(x)

print("Z-Score Outliers =", z_outliers)