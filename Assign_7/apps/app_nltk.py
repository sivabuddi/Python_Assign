name = ['1', '2', '3']
value = ['charan', 'aravind', 'Sir']
years = [2, 2, 5]

mapped = zip(name, value, years)
print("mapped values")
print("mapped values", end="")

for i in mapped:
    print(i[0], i[1], i[2])
