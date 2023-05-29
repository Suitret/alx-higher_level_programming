#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    if my_list == []:
        return 0

    num = 0
    for i in range(x):

        try:
            print("{:d}".format(my_list[i]), end="")
        except Exception:
            continue
#        except IndexError:
#            break

        num += 1

    print()
    return num
