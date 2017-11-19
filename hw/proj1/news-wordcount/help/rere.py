#!/usr/bin/python3

import sys
import re

patterns = re.compile('\d\d:\d\d(.*?)http://')

for line in sys.stdin:
    print(re.search(patterns, line).group(1).strip())
    #print(re.search(patterns, line).group(1).strip().replace(':', ' ').split())

