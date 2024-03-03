
from timer import Timer
import numpy as np
from datetime import datetime

# 素数判定問題
# 67,280,421,310,721 は素数であるかどうかを判定する
# 答えは素数である

# 2からn-1までの数で割り切れるかどうかを調べる
@Timer
def divide_all(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# speedtest.txt に記録
with open('speedtest.txt', 'a') as f:
    f.write(f'Divide all number: {divide_all(67280421310721)}\n')
