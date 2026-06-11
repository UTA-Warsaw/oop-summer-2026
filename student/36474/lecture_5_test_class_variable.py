# lecture_5_test_class_variable.py
# Hsuh: creating a class with a class variable

class ClassWithVariable:
    class_variable = 10  # Hsuh: class variable, same for all objects

# Hsuh: creating an object of the class
obj_variable = ClassWithVariable()

# Hsuh: print the class variable value
print(obj_variable.class_variable)  # Hsuh: should print 10