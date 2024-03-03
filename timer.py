import time

# デコレータされた関数を呼び出すと、その関数を1000回実行し、その実行時間を表示する
# コードの実行時間のの平均値、中央値、最小値、最大値を表示する

class Timer:
    def __init__(self, func):
        self.func = func
        self.elapsed = 0
        self.min_time = float('inf')
        self.max_time = float('-inf')
        self.times = []

    def __call__(self, *args, **kwargs):
        for _ in range(100000):
            start = time.time()
            self.func(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            self.elapsed += elapsed
            self.min_time = min(self.min_time, elapsed)
            self.max_time = max(self.max_time, elapsed)
            self.times.append(elapsed)
        avg_time = self.elapsed / 100000
        self.times.sort()
        median_time = self.times[50000]
        min_time = self.min_time
        max_time = self.max_time
        print(f'平均時間: {avg_time:.5f}')
        print(f'中央値: {median_time:.5f}')
        print(f'最小値: {self.min_time:.5f}')
        print(f'最大値: {self.max_time:.5f}')
        self.reset()
        return self.func(*args, **kwargs), avg_time, median_time, min_time, max_time
    
    def reset(self):
        self.elapsed = 0
        self.min_time = float('inf')
        self.max_time = float('-inf')
        self.times = []

  