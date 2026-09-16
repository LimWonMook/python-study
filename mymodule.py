def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

# 모듈 테스트용 실제 적용X
print('__name__', __name__)
if __name__=='__main__':
    print(add(5, 2))
    print(sub(3, 1))