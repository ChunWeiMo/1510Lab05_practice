"""
Step 05.
How do we watch a variable?
"""


def merge_sorted(some_list, some_other_list):
    """
    Return a new sorted list containing all elements from both some_list and some_other_list.

    :param some_list: a list of elements that are sortable
    :param some_other_list: a list of elements that are sortable
    :precondition: the lists are composed of the same type
    :precondition: the lists are pre-sorted
    :postcondition: create a new list containing elements from both lists correctly sorted
    :return: a new sorted list containing elements from the original lists
    """
    result = []

    some_list_index = 0
    some_other_list_index = 0
    while some_list_index < len(some_list) or some_other_list_index < len(some_other_list):
        if some_list_index == len(some_list):
            print(some_other_list[some_other_list_index])
            result.append(some_other_list[some_other_list_index])
            some_other_list_index += 1
        elif some_other_list_index == len(some_other_list):
            print(some_list[some_list_index])
            result.append(some_list[some_list_index])
            some_list_index += 1
        else:
            if some_list[some_list_index] < some_other_list[some_other_list_index]:
                result.append(some_list[some_list_index])
                some_list_index += 1
            else:
                result.append(some_other_list[some_other_list_index])
                some_other_list_index += 1
    return result


def main():
    """
    Drive the program.
    """
    some_names = ['Amy', 'Chloe', 'Emerald', 'George', 'Ina',
                  'Kelvin', 'Nancy', 'Petra', 'Reese']
    more_names = ['Bob', 'David', 'Frances', 'Hertie',
                  'Jacky', 'Moira', 'Ophelia', 'Quinn', "SSS", "TTT"]
    print(len(some_names))
    print(len(more_names))
    all_the_names = merge_sorted(more_names, some_names)
    print(all_the_names)


if __name__ == '__main__':
    main()
