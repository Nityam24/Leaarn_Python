# d) Create a base class A with 2 children B and C. class D having 2 parents B and C.
# Create a method named “Call” in every class. Use super in a way that a single call 
# to method of class D execute “Call” method of every class.

class A:
    def __init__(self):
        pass
    
    def Call(self):
        print("Calling Fron A")

class B(A):
    def __init__(self):
        pass
    
    def Call(self):
        super().Call()
        print("Calling Fron B")

class C(A):
    def __init__(self):
        pass
    
    def Call(self):
        super().Call()
        print("Calling Fron C")

class D(B,C):
    def __init__(self):
        pass
    
    def Call(self):
        super().Call()
        print("Calling Fron D")

d1 = D()
d1.Call()
