from clean import clean_file
from collections import Counter
import matplotlib.pyplot as plt
clean_file("book.txt", "clean.txt")

file = open("clean.txt", "r", encoding = "utf-8")

count = Counter(file.read().split())
print(count)

file.close()


x = []
y = []
for key in count:
    x.append(key)
    y.append(count[key])



s = sorted(zip(x,y),key = lambda pair: pair[1], reverse = True)
s = s[0:20]

x,y = zip(*s)
plt.yticks(rotation = "vertical")
plt.bar(x,y)
plt.show()