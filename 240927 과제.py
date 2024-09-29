#문제 1
a = input("인사를 먼저하세요<<<")

if a == "안녕하세요" :
    print("반갑습니다")
else:
    print("인사를 먼저하세요")

#문제 2
a = input("숫자를 입력하세요: ")
number = int(a)
result = number + 100

if result >= 150:
    print(result)
else:
    print("값이 부족합니다")

#문제 3
numbers = [100, 200, 300]
for i in numbers :
        print(i)
numbers.append(330)
numbers.append(220)
numbers.append(110)
result = numbers[3:6]
print(result)

#문제 4
number = [3, 100, 23, 33, 72, 94]
result = []
for k in number:
    if k % 3 == 0:
        result.append(k)
print(result)

#문제 5
a = 1
while a < 1000 :
    a = a + 1
    print(a)
    if a == 1000 :
        break

#문제 6
a = 1
sum = 0
while a <= 100:
    if a % 2 != 0:
        sum += a
    a += 1
print(sum)