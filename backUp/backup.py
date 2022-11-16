#! /usr/bin/env python

import yaml
import argparse
import re
import os
import subprocess

def main():
    fileExt = re.search(r'\.(\w+)', args.specs)
    if fileExt.group(1) != 'yaml':
        print ("Inserted file is not in yaml format!!")

    with open(args.specs) as file:
        document = yaml.load(file, Loader=yaml.FullLoader)

    for i in range(0, len(document)):
     for key,value in document[i].items():
      # print (key,":",value)
      if key == 'path_pattern':
         os.chdir(value)
         # sp = subprocess.run(['cp','*'])
         # sp.stdout

      if key == 'dest':
          sp = subprocess.run(['cp','*',f'{value}'])
          sp.stdout




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Backup files in paths matching a pattern')
    parser.add_argument(
        '--specs','-s',
        help='file to read paths and destinations from, default is backup.yaml',
        metavar='SPECS',
        type=str
    )
    parser.add_argument(
        '--dry-run',
        help='do not perform backup, only print the operations about to be performed for every file',
        # metavar=" ",
        action='store_true',
        default=False
    )

    args = parser.parse_args()
    main()