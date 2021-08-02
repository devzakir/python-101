print(list(range(1, 5)))
print(list(range(3, 15, 3)))

# range with for
for num in range(20):
    print(num)
for num in range(3, 6):
    print(num)
for num in range(3, 15, 3):
    print(num)


z = {
    'a': 10,
    'b': 20,
    'c': 30,
}

print(z.keys())
print(z.values())
print(z.items())

for item in z.items():
    print(f"the number is - {item[1]}")

for key, value in z.items():
    print("key:", key,  ' value: ', value)
