class TimeMap:

    def __init__(self):
        self.tMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tMap:
            self.tMap[key] = []
        self.tMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        lis = self.tMap.get(key, [])
        l , r = 0, len(lis)-1
        res = ""
        while l<=r:
            m = (l+r)//2
            if lis[m][1] <= timestamp:
                res = lis[m][0]
                l = m+1
            else:
                r = m-1
        return res
