#!/usr/bin/python
def element_at(my_list, idx):
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None
