class FourCal :
    def setdata (self, first, second):      #setdata를 통해 처음 받은 두 숫자로 모든 사칙연산을 한다.
        self.first = first
        self.second = second
    def sum(self):
        return self.first + self.second
    def mul(self):
        return self.first - self.second
    def sub(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second

a = FourCal()
a.setdata(4,2)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())
