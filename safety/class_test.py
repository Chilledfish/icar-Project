class My_class:
    def __init__(self, name):
        self.name = name

class Sub_class(My_class):
    def __init__(self):
        self.mame = 'mame'

make = "Audi"

Audi = My_class(make)
print(Audi.name)
sub_moo = Sub_class()

print(sub_moo.mame)
print(sub_moo.name)
# Define the name of the instance and the attribute as strings
instance_name = "my_obj"
attr_name = "attr"

# Use the setattr() function to create the instance and set the attribute
setattr(globals(), instance_name, MyClass(attr_name, "value"))

# The my_obj variable now contains an instance of MyClass with the given attribute
print(my_obj.attr)