# 서로 import를 하면 오류가 발생합니다. (순환 참조)
# [예시]
# a에서 b를 import하고, b에서 a를 import하면, b에서는 바로 a를 import 하니 b가 출력되지않음

print("i am b.py", __name__)  # b.py의 __name__은 "b"입니다. (모듈 이름)

def b_hello():
    print("hello from b.py")

b_hello()