def safe_print_list_integers(my_list=[], x=0):
    integers = 0
    try:
        for item in my_list:
            if integers >= x:
                break

            if isinstance(item, int):
                print("{:d}".format(item), end="\n")
                integers += 1
    except (ValueError, TypeError, IndexError):
        pass

    return integers
