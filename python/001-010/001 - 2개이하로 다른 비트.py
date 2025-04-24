def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"

    binary_number = ""

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2

    return binary_number


def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            binary_number = decimal_to_binary(number)
            reversed_binary = binary_number[::-1]
            number_of_one = reversed_binary.find("0")

            if number_of_one == -1:
                len_one = len(binary_number)
            else:
                len_one = number_of_one
            answer.append(number + (2 ** (len_one - 1)))

    return answer
