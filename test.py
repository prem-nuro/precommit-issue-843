#!/usr/bin/env python2

from __future__ import print_function

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="*")
    args = parser.parse_args()
    print("Files:")
    for f in args.file:
        print(" ", f)
