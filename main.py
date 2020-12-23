#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


# Global constants:
APP_PATH = os.path.dirname(os.path.abspath(__file__))

def main():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", type=str, help='A file to load with Ked')
    parser.add_argument("-v", "--version", action="store_true", help="Display Ked current version and exit")

    args = parser.parse_args()

    if args.version:
        from ked.utils.files_manip import get_file_content as gfc
        ver = gfc(f'{APP_PATH}/data/version')
        print(f'Ked current version is: {ver}')
    else:
        from ked.gui import ked

        ufile = None
        if args.file:
            ufile = args.file

        ked.start_ked(APP_PATH, user_file=ufile)

    return 0

if __name__ == '__main__':
    sys.exit(main())
