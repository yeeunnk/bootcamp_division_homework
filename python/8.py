"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    n=int(input())
    sum=0
    mul=1
    if n<=12:
        for i in range(1,n+1):
            sum=sum+i
            mul=mul*i
        print('1에서 n까지의 정수의 합: ',sum)
        print('n!= ',mul)
    else:
        print('n<=12이 되도록 입력하세요') 
        return


if __name__ == '__main__':
    main()
