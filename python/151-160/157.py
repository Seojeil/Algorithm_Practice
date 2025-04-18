# 너의 평점은


GRADE = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

dividend = 0
divisor = 0

for _ in range(20):
    subject, mark, grade = input().split()

    mark = float(mark)

    if grade == 'P':
        pass
    else:
        dividend += mark * GRADE[grade]
        divisor += mark

print(dividend/divisor)
