def S_i(data, i):
    i += 1
    result = 0

    for d in data:
        result += d % i

    return result


def solution(data, col, row_begin, row_end):
    answer = 0
    new_data = []

    while data:
        compare_data = data.pop()
        index = 0
        equal = False

        if not new_data:
            new_data.append(compare_data)
        else:
            for d in new_data:
                if equal:
                    break
                if d[col - 1] < compare_data[col - 1]:
                    index += 1
                elif d[col - 1] > compare_data[col - 1]:
                    break
                else:
                    index = 0

                    for d2 in new_data:
                        if d2[col - 1] != compare_data[col - 1]:
                            if equal:
                                break
                            index += 1
                        else:
                            equal = True
                            if d2[0] > compare_data[0]:
                                index += 1
                            else:
                                break

                    else:
                        equal = True

            new_data.insert(index, compare_data)

    for i in range(row_begin - 1, row_end):
        answer ^= S_i(new_data[i], i)

    return answer
