class Secretive:
    def __inacccessablel(self):
        print("bet you cannot see me")
        pass
    def accceessable(self):
        print("the secete mess is ")
        self.__inacccessablel()
        pass
    def test(self):
        print("test Secete class")


class A(Secretive):
    def test(self):
        print("test A super class")
class B(A,Secretive):
    print("test class b")
    pass


s = Secretive()
s.accceessable()
s._Secretive__inacccessablel()

a = A()
print(issubclass(Secretive,A))
print(issubclass(A,Secretive))

print(isinstance(a,Secretive))
print(isinstance(a,A))
print(s.__class__)
print(a.__class__)

b = B()
b.test()
print(hasattr(b,"test"))
