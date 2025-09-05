# # 1부터 10까지

# # 반복문 없이 작성
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# 반복문으로 숫자 출력하기

# i가 0부터 9가 될 때까지
# 총 10번 반복 수행
i=0
while i<11:
    if i%2 == 1:
        i+=1
        continue
    print(i)
    i+=1
# 조건식에 사용되는 i가
# 변경되지 않으면 조건은 계속 참이 되어 
# 무한루프에 빠진다
# 반복횟수:10
# 반복코드:print(?)