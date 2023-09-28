x = input("Enter your Sentence: ")
l = list(x)
y = [l.count(ele) for ele in l]
d = dict(zip(l, y))
print(d)