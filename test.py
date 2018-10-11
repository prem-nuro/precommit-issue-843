#!/usr/bin/env python2

from __future__ import print_function

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="*")
    args = parser.parse_args()
    print()
    print("Files:")
    for f in args.file:
        print(" ", f)
    print()

if __name__ == '__main__':
    main()
