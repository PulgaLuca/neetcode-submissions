class TimeMap:

    def __init__(self):
        self.mmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mmap:
            self.mmap[key] = []
        self.mmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.mmap.get(key, [])
        l, r = 0, len(values)-1
        while l <= r:
            m = (l+r)//2
            if timestamp >= values[m][1]:
                res = values[m][0]
                l = m+1
            else:
                r=m-1
        return res
