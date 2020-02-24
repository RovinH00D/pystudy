#박씨네 집이라는 동화를 클래스를 통해 만들어 보자
class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def tarvel(self, where):
        print("%s씨, %s로 여행을 떠나다." % (self.fullname, where))
    def __add__(self,other):
        print("%s씨, %s씨와 결혼하다." % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s씨, %s씨와 헤어지다." % (self.fullname, other.fullname))

class HouseKim(HousePark) :
    lastname = "김"
    def tarvel(self, where):
        print("%s님도 %s로 여행을 갔습니다." % (self.fullname, where))

a = HousePark("진영")
b = HouseKim("오찌")
a.tarvel("훗카이도")
b.tarvel("훗카이도")
a+b
a-b
