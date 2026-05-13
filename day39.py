# Access modifiers in Python

# In Python, there are three types of access modifiers: public, protected, and private.
# 1. Public: Public members are accessible from anywhere in the program. They are defined without any leading underscores.
# 2. Protected: Protected members are intended to be accessed only within the class and its

    # subclasses. They are defined with a single leading underscore (e.g., _protected_member).

# 3. Private: Private members are intended to be accessed only within the class. They are defined with a double leading underscore (e.g., __private_member).
class MyClass:
    def __init__(self):
        self.public_member = "I am public"
        self._protected_member = "I am protected"
        self.__private_member = "I am private"
my_object = MyClass()
print(my_object.public_member)  # Output: I am public
print(my_object._protected_member)  # Output: I am protected
# The following line will raise an AttributeError because __private_member is not accessible outside the class
# print(my_object.__private_member)  # Uncommenting this line will cause an error
# However, you can access the private member using name mangling
print(my_object._MyClass__private_member)  # Output: I am private
