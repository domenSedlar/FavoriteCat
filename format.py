f = open("list_of_cats.txt")
ls = f.readlines()
nls = []

for i in ls:
    nls.append(i.replace("\n", ""))

print(nls)