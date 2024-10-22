#1번
import random

def numbers():
    result = []
    while len(result) < 6:
        num = random.randint(1,45)
        if num not in result:
            result.append(num)
    return result

print(numbers())

#2번
class math :
    def __init__(self, math_num):
        self.num = math_num
    def output(self):
        print(f"{self.num}단")
        for i in range(1, 10) :
            result = self.num * i
            print(f"{self.num} * {i} = {result}")
a = int(input("몇 단을 해드릴까요?"))
gugudan = math(a)
gugudan.output()

#3번
class Exercise:
    def __init__(self, name, calories_burned):
        self.name = name
        self.calories_burned = calories_burned


class Diet:
    def __init__(self, meal, calories):
        self.meal = meal
        self.calories = calories


class Member:
    def __init__(self, name):
        self.name = name
        self.exercises = []
        self.diets = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def add_diet(self, diet):
        self.diets.append(diet)

    def display_summary(self):
        total_burned = sum(e.calories_burned for e in self.exercises)
        total_intake = sum(d.calories for d in self.diets)
        return (f"\n{self.name}의 총 운동 소모 칼로리: {total_burned}\n"
                f"{self.name}의 총 식단 섭취 칼로리: {total_intake}")


name = input("회원 이름을 입력하세요: ")
member = Member(name)

while True:
    action = input("운동 추가하려면 '1', 식단 추가하려면 '2', 요약 보려면 '3', 종료하려면 'q'를 입력하세요: ")

    if action == '1':
        exercise_name = input("운동 이름을 입력하세요: ")
        calories = int(input("소모 칼로리를 입력하세요: "))
        member.add_exercise(Exercise(exercise_name, calories))
        print(f"{exercise_name}이(가) 추가되었습니다.")

    elif action == '2':
        meal_name = input("식사 이름을 입력하세요: ")
        calories = int(input("칼로리를 입력하세요: "))
        member.add_diet(Diet(meal_name, calories))
        print(f"{meal_name}이(가) 추가되었습니다.")

    elif action == '3':
        print(member.display_summary())

    elif action == 'q':
        print("종료합니다.")
        print(member.display_summary())
        break

    else:
        print("올바른 선택이 아닙니다.")