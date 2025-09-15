import abc as abstract

# Single Inheritance
class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    def display(self):
        print(" Parent class method called")
obj = A()
print(obj.b)
#A.display()  


class B(A):
    def __init__(self):
        #super().__init__()
        self.c = 3
        print(" Chlild class method called")

    def show(self):
        print(f"a: {self.a}, b: {self.b}, c: {self.c}")

B = B()
    
# Abstract Class

class C(abstract.ABC):
    @abstract.abstractmethod
    def display(self):
        pass

class D(C):
    def display(self):
        print("Implementation of abstract method")

d = D()
d.display()


# Multiple Inheritance since python supports multiple inheritance

class E:
    def method_e(self):
        print("Method from class E")

class F:
    def method_f(self):
        print("Method from class F")

class G(E, F):
    def method_g(self):
        print("Method from class G")  

g = G()
g.method_e()    
g.method_f()
g.method_g()


# Multilevel Inheritance

class H:
    def method_h(self):
        print("Method from class H")

class I(H):
    def method_i(self):
        print("Method from class I")

class J(I):
    def method_j(self):
        print("Method from class J")

j = J() 
j.method_h()
j.method_i()        
j.method_j()

# Hierarchical Inheritance

class K:
    def method_k(self):
        print("Method from class K")

class L(K):
    def method_l(self):
        print("Method from class L")

class M(K):
    def method_m(self):
        print("Method from class M")

l = L()
m = M()
l.method_k()
l.method_l()
m.method_k()
m.method_m()
           


       


