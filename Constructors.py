class Employee:
    def __init__(self,eno,ename,eage,esal):
        self.eno=eno
        self.ename=ename
        self.eage=eage
        self.esal=esal

    def display(self):
        print('Employee number:',self.eno)
        print('Employee name:',self.ename)
        print('Employee age:',self.eage)
        print('Employee salary:',self.esal)

e1=Employee(101,'Rizwan',25,25000)
e2=Employee(102,'Khaleel',24,23000)
e3=Employee(103,'Basha',26,30000)
e1.display()
e2.display()
e3.display()
