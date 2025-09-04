# 반복문으로 1부터 10까지 출력하기
# 단, 숫자가 짝수일때만 출력하기
# 홀수는 건너뛰기

i = 1
while i < 11:
    if i%2 == 1:
        i += 1
        continue
    print(i) 
    i += 1

print(i)