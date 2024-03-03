
from timer import Timer
import numpy as np
from datetime import datetime

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


# speedtest.txt に結果を書き込む
with open('./speedtest.txt', 'a') as f:
    f.write(f'実行日時: {datetime.now()}\n')
    f.write(f'シンプルなループ: {simple_loop()}\n')
    f.write(f'powを使って計算: {use_pow()}\n')
    f.write(f'numpyを使って計算: {use_numpy()}\n')
    f.write('\n')
