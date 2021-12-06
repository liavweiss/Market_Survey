class Distribution:

    def __init__(self, values: list[int]):
        self.values = values

    def F(self, x: int) -> float:
        min_value = min(self.values)
        max_value = max(self.values)
        if x > max_value: return 1
        if x < min_value: return 0
        return (x - min_value) / (max_value - min_value)

    def r(self, x: int) -> float:
        return x - ((1 - self.F(x)) / self.f())

    # The derivative of F(x).
    def f(self):
        return 1 / (max(self.values) - min(self.values))


if __name__ == '__main__':
    values = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    d = Distribution(values)
    for i in d.values:
        print("F({}) = {}  ,  r({}) = {}".format(i, d.F(i), i, d.r(i)))
