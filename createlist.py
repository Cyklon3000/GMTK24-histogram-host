num = float(input("Enter a number: "))

# Create a list of 10 dictionaries
result = []
for i in range(10):
    min_val = i * (num / 1000)
    max_val = (i + 1) * (num / 1000)
    result.append({"min": round(min_val, 3), "max": round(max_val, 3), "count": 0})

print(str(result).replace("'", '"'))