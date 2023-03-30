# script to update solved problems count
# triggered by github action

solved = 0
total = 0
with open("../README.MD", 'r') as f:
    data = f.read()
    solved = data.count("[x]")
    total = data.count("[")

i = data.index("(")
j = data.index(" problems solved)")

before = data[:i+1]
after = data[j:]

new_num = f"{solved}/{total}"

data = before + new_num + after

print(data[:200])

with open("../README.MD", 'w') as f:
    f.write(data)