class Math:
    note = 'this is the class variable'
    # note is a class variable coz we define it under a calss Math

    # functions below are called methods in object oriented programming
    def add(self, num1, num2):
        print('addition: ', num1 + num2)

    def multiply(self, num1, num2):
        print('multiplication: ', num1 * num2)

# on terminal type python & enter
# >>> from oop import Math - oop is a module from which we import Math class

# to access the property and methods  we need to create an instances of the class

# >>> inst = Mat()
# >>> dir(inst) - list the properties & methods avaiable _xxx_ to be used by python
# to access properties and methods we use object.attribute notation
# here the varible inst is an object & the attribute is anything inside the Math class
# inst.note, inst.add(2,4
# type(inst)
