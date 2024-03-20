"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    
    time = int(input())
    if time<12:
        print('AM')
    elif time>=12 and time<=23:
        print('PM')
    else:
        print('입력범위는 0시부터 23시까지 입니다.')
   
    return


if __name__ == '__main__':
    main()
