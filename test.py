import re

line = "上午11:22	P.Luo	題目可以再長一點..."
x = re.split("\s", line)

print(x[1])