#!/usr/bin/env python
import sys
print(sum(int(next(filter(str.isdigit, line)) + next(filter(str.isdigit, reversed(line)))) for line in sys.stdin.read().splitlines()))
