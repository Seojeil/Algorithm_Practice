def solution(book_time):
    time_line = [0] * 24 * 60 + [0] * 10

    for book in book_time:
        start = int(book[0][:2]) * 60 + int(book[0][-2:])
        end = int(book[1][:2]) * 60 + int(book[1][-2:])

        for i in range(start, end + 10):
            time_line[i] += 1

    return max(time_line)
