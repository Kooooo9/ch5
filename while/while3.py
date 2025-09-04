# 1부터 10까지 합 구하기
# 1+2+3+4+5+6+7+8+9+10 => 55
# 합을 저장 할 변수를 선언
# sum = +2+3+4+5+6+7+8+9+10
sum = 0
sum = sum + 1
sum = sum + 2
sum = sum + 3
sum = sum + 4
sum = sum + 5
sum = sum + 6
sum = sum + 7
sum = sum + 8
sum = sum + 9
sum = sum + 10

# 반복문을 사용해 합 구하기
i = 1
while i < 11:
    sum = sum + i
    i += 1
    print('합:', sum)
