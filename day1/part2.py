#!/usr/bin/env python
import sys
print(sum(int(next(filter(str.isdigit, line)) + next(filter(str.isdigit, reversed(line)))) for line in sys.stdin.read().replace("one","o1e").replace("two","t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e").splitlines()))
