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
        print(f'Average: {self.elapsed / 100000}')
        print(f'Min: {self.min_time}')
        print(f'Max: {self.max_time}')
        print(f'Median: {sorted(self.times)[len(self.times) // 2]}')
        print(f'Count: {len(self.times)}')
        self.reset()

    def reset(self):
        self.elapsed = 0
        self.min_time = float('inf')
        self.max_time = float('-inf')
        self.times = []

  