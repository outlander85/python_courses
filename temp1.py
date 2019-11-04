# from pprint import pprint
# pprint('Hello World!')

from textwrap import wrap


width = 100

print('+-' + '-' * width + '-+')

for line in wrap(pr, width):
    print('| {0:^{1}} |'.format(line, width))

print('+-' + '-' * width + '-+')