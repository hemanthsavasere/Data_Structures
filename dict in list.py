listed = []
name = dict()
name["hemanth"] = 100
listed.append(name)
name = {"John": 200}
listed.append(name)

print listed
total = 0
for i in listed:
    total += sum(i.values())
print total


