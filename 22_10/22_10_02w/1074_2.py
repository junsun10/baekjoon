# Z
#
#
from gettext import find
import math
n, x, y = map(int, input().split())

find_x = int(math.log2(x))
find_y = int(math.log2(y))
print(find_x, find_y)
