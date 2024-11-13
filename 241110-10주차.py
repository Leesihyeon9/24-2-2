#1번 문제
import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50]
y = [40, 70, 80, 75, 64]

plt.plot(x, y, marker = 'x', linestyle = '-', color = 'r', label = 'weight')

plt.title("Average weight for each age ")
plt.xlabel('(age)')
plt.ylabel('(weight)')
plt.legend()

plt.grid(True)
plt.savefig("./idea.png")

#2번 문제
import matplotlib.pyplot as plt

categories = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grape']
values = [5, 10, 15, 20, 25]

plt.clf()

plt.bar(categories, values, color='r')

plt.title('Fruit Sales')

plt.xlabel('Fruit')
plt.ylabel('Sales')

plt.savefig("./idea.png")

#3번 문제
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.clf()

plt.hist(data, bins=20, color='r', edgecolor='b')

plt.title('Histogram chart')

plt.xlabel('Values')
plt.ylabel('Frequency')

plt.savefig("./idea.png")

#4번 문제
import matplotlib.pyplot as plt

labels = ['English', 'Math', 'Science', 'History']
sizes = [45, 30, 15, 10]

plt.clf()

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon'])
plt.title('Subjects Distribution')

plt.savefig("./idea.png")

#5번 문제
import matplotlib.pyplot as plt
import random

x = [random.uniform(0, 100) for _ in range(1000)]
y = [random.uniform(0, 100) for _ in range(1000)]

plt.clf()
plt.scatter(x, y, label='Random Data Points', color='green', marker='o', s=30, alpha=0.5)
plt.title('Scatter Plot Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.savefig("./idea.png")

#6번 문제
import matplotlib.pyplot as plt
import random

x = [random.uniform(0, 100) for _ in range(200)]
y = [2 * val + 1 + random.uniform(-10, 10) for val in x]

plt.clf()

plt.scatter(x, y, label='Scatter Plot', color='blue', marker='o', s=30, alpha=0.5)

plt.title('Scatter Plot Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.savefig("./idea.png")

#7번 문제
import matplotlib.pyplot as plt
import random

x = [random.uniform(0, 100) for _ in range(200)]
y = [2 * val + 1 + random.uniform(-10, 10) for val in x]

plt.clf()

plt.scatter(x, y, label='Scatter Plot', color='blue', marker='o', s=30, alpha=0.5)

x_line = range(101)
y_line = [2 * val + 1 for val in x_line]
plt.plot(x_line, y_line, label='y = 2x + 1', color='red')

plt.title('Scatter Plot Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.savefig("./idea.png")

#8번 문제
import matplotlib.pyplot as plt
import random

data = [random.gauss(0, 1) for _ in range(100)]
outliers = [10, -10]

plt.clf()

plt.boxplot(data + outliers, vert=False, patch_artist=True)

plt.title('Boxplot Example with Outliers')

plt.xlabel('Values')

plt.xticks(range(-15, 16, 5))

plt.savefig("./idea.png")

#9번 문제
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

plt.clf()

heatmap = plt.imshow(data, cmap='YlGnBu', aspect='auto')

plt.colorbar(heatmap)

plt.title('Heatmap Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.savefig("./idea.png")