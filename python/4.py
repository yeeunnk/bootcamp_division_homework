"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    score=int(input())

    if score >= 90 and score<100:
        print('A')
    elif score>=80:
        print('B')
    elif score>=70:
        print('C')
    elif score>=60:
        print('D')
    else:
        print('F')

    return


if __name__ == '__main__':
    main()
