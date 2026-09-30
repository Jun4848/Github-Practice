print("안냥하쇼")

score = input("점수를 5개 입력 : ").split()
sum = 0

for i in score:
    sum += float(i)

print("평균 점수 : %.2f" %(sum/5))