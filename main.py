def calculate_lists(user_input):
    """ Calculates the number of occurences of certain character in a string."""
    input_list = []
    for i in user_input:
        input_list.append(i)

    occurence_list = []
    for i in set(input_list):
        occurence_list.append((i, user_input.count(i)))

    sorted_by_first = sorted(occurence_list, key=lambda tup: tup[1])
    sorted_list = list(reversed(sorted_by_first))

    propability_list = []
    for i in range(len(sorted_list)):
        propability_list.append(sorted_list[i][1])

    print("Input list is: ", input_list)
    print("Input list is: ", input_list)
    print("Occurence list: ", occurence_list)
    print("Sorted list is: ", sorted_list)
    print("Probility list is: ", propability_list)


def main():
    user_input = str(input("Please enter a text: "))
    calculate_lists(user_input)


if __name__ == "__main__":
    main()
