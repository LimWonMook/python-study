def checkWin(user, com):
    print(f'나: {user} / 컴퓨터: {com}')

    if user == com:
        print("비겼습니다.")
        return False
    elif (user == '가위' and com == '보') or \
         (user == '바위' and com == '가위') or \
         (user == '보' and com == '바위'):
        print("이겼습니다.")
        return True
    else:
        print("졌습니다.")
        return True

def continueComfirm():
    answer = input("게임을 계속하시겠습니까? (y/n) : ")

    if answer.lower() == 'y':
        return True
    else: 
        return False