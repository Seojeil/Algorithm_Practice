# 식료품 가게


T = int(input())

for test_case in range(1, T + 1):
    _ = input()
    sales = list(map(int, input().split()))

    sales_2 = sales[:]
    result = []

    for sale in sales_2:
        sale_75 = int(sale * 3 / 4)
        if sale % 4 == 0 and sale_75 in sales:
            sales.remove(sale)
            sales.remove(sale_75)
            result.append(sale_75)

    result.sort()
    result = " ".join([str(elem) for elem in result])

    print(f"#{test_case} {result}")
