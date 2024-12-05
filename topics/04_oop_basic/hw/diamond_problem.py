"""
DIAMOND PROBLEM
       A
      / \
     B   C
      \ /
       D
Class A: Base class.
Class B and Class C: Both inherit from Class A.
Class D: Inherits from both Class B and Class C.

When Class D calls a method or accesses an attribute defined in Class A, 
there is ambiguity because Class D could potentially inherit from Class A through either Class B or Class C.

Python uses the C3 Linearization Algorithm to define the Method Resolution Order (MRO) in multiple inheritance.

This ensures a consistent order for method resolution. 
You can view the MRO with the .__mro__ attribute or mro() method.
"""
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")

class C(A):
    def hello(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.hello()  # Resolves using the MRO
print(D.mro())

"""
When you create a class with multiple inheritance (like D(B, C)), 
Python computes the MRO using the C3 linearization algorithm. In this case:

Class D is checked first.
Then, Python looks at Class B.
After that, Python checks Class C.
Finally, it looks at Class A, which is the base class.
So, when d.hello() is called, it first looks for hello in D (but D doesn't define a hello method). 
Then, it looks in B, and since B has a hello method, it uses that and prints "Hello from B".
"""