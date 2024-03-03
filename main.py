
from timer import Timer
import numpy as np

# 1~10までの平方を計算する関数
# expected result: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# シンプルにループで計算
@Timer
def simple_loop():
    result = []
    for i in range(1, 11):
        result.append(i ** 2)
    return result

# pow を使って計算
@Timer
def use_pow():
    return [pow(i, 2) for i in range(1, 11)]

# numpyを使って計算
@Timer
def use_numpy():
    return np.square(np.arange(1, 11))

# それぞれの関数を実行
print('simple_loop')
simple_loop()
print('use_pow')
use_pow()
print('use_numpy')
use_numpy()
