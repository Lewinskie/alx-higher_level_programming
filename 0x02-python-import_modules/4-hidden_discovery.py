#!/usr/bin/python3.8

import py_compile
import hidden_4

if __name__ == "__main__":
    py_compile.compile('hidden_4.pyc')
    pass

    module_names = dir(hidden_4)

    for name in sorted(module_names):
        if not name.startswith('__'):
            print(name)

