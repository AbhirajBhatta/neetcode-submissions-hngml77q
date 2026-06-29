class CountSquares:

    def __init__(self):
        self.pointsMap = defaultdict(int)
        self.pointsArr = []

    def add(self, point: List[int]) -> None:
        self.pointsMap[tuple(point)]+=1
        self.pointsArr.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.pointsArr:
            if abs(px-x) != abs(py-y) or px-x==0 or py-y==0:
                continue
            res += self.pointsMap[(px, y)] * self.pointsMap[(x, py)]
        return res
