num = float(input("Enter a number: "))

# Create a list of 10 dictionaries
result = []
for i in range(10):
    min_val = i * (num / 10)
    max_val = (i + 1) * (num / 10)
    result.append({"count": 0 , "max": round(max_val, 3), "min": round(min_val, 3)})

print(
    str(result)\
        .replace('[{', '[\n {')\
        .replace("'", '"')\
        .replace(' {"count":', '    {"count":')
        .replace('},', '},\n')\
        .replace('}]', '}\n]')
)