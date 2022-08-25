def hw3():
    cumulative_sum = 0
    n = int(input())
    x = int(input())
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    list_of_numerals = []

    if x==0 or n==0:
        False

    else:
        for i in range(x):
            numeral = int(input("Enter a numeral"))
            list_of_numerals.append(numeral)

            new_list = list_of_numerals[len(list_of_numerals):0:-1]
            new_list.append(list_of_numerals[0])

        if n <= x:
            str_num = ""
            for a in range(len(new_list)):
                str_num = str(new_list[a]) + str_num
                cumulative_sum += int(str_num)
                if a == n - 1:
                    break

        else:
            str_num =""
            for a in range(n):
                str_num = str(new_list[a % len(new_list)]) + str_num
                cumulative_sum += int(str_num)


    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    print(cumulative_sum)
    return cumulative_sum


if __name__ == "__main__":
    hw3()

