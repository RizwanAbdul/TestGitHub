class Test:
    a=10
    def __init__(self):
        Test.b=20

    def m1(self):
        Test.c=30

    @classmethod
    def m2(cls):
        Test.d=40
        cls.e=50

    @staticmethod
    def m3():
        f=60

t=Test()
t.m1()
t.m2()
t.m3()
print(Test.__dict__)
