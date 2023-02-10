import sys
import time

write, flush = sys.stdout.write, sys.stdout.flush
list = [i for i in range(10)]
for i in list:
    write(f'\r{i}')
    flush()
    time.sleep(0.2)