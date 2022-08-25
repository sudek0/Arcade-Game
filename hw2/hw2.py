

def hw2():
    str_input = input()
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    list = str_input.split()
    word_number = len(list)

    if word_number > 2:
        word_number = str(word_number)
        print(word_number + " words!")
        print(list[0] + " " + list[-1])

    elif word_number == 1:
        print("One word")
        print(list[0])

    elif word_number == 2:
        print("Two words")
        print(list[0] + " " + list[-1])

    else:
        print("No words")

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    return


if __name__ == "__main__":
    hw2()
