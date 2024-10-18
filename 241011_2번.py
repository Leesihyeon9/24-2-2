a=input("메시지를 입력하세요")
def check_length_of_message(message):
    Q=len(message)
    if Q <= 20:
        return "메시지 요금은 50원 입니다"
    elif Q > 20:
        return "메시지 요금은 100원입니다"
print(check_length_of_message(a))