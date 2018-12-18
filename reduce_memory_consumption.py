#! python3
'''
Activating __slots__ in the creation of classes to reduce memory consumption.
http://www.techort.com/how-to-reduce-memory-consumption-by-half-by-adding-just-one-line-of-code-habr/
'''

import sys, optparse, os
class DataItem(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

d1 = DataItem("Alex", 42, "-")
print("sys.getsizeof(d1):", sys.getsizeof(d1))
print(getattr(d1, "__dict__"))
print(d1.__dict__)

d2 = DataItem("Boris", 24, "In the middle of nowhere")
print("sys.getsizeof(d2):", sys.getsizeof(d2))

'''
However, Python is a very flexible language with dynamic typing, 
and for its work it stores a considerable amount of additional data, 
which in themselves occupy a lot of memory.
'''


# output the entire contents of the class at a lower level
def dump(obj):
    for attr in dir(obj):
        print("obj.%s === %r" %(attr, getattr(obj, attr)))  

# dump(d1)

# compute memory consumption the entire contents of the class take up
def get_size(obj, seen = None):
    # From https://goshippo.com/blog/measure-real-size-any-python-object/
    # Recursively finds size of objects
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Important mark as seen * before * entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
      size += sum([get_size(v, seen) for v in obj.values()])
      size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
      size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj,(str, bytes, bytearray)):
      size += sum([get_size(i, seen) for i in obj])
    return size

print()
print("get_size(d1):", get_size(d1))
print("get_size(d2):", get_size(d2))

'''
Python is an interpreter, and we can expand our class at any time.
'''
# d1 = DataItem("Alex", 42, "-")
print()
print("get_size(d1) before adding new field:", get_size(d1))
d1.weight = 66
print("get_size(d1) after adding new field:", get_size(d1))

'''
If we do not need this functionality, 
we can force the interpreter to specify a list of class objects using the __slots __ directive,
such process has significant decrease in memory consumption, and objects are created faster.
'''

class DataItem(object):
    __slots__ = ['name', 'age', 'address']
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

d1 = DataItem("Alex", 42, "-")
print("sys.getsizeof(d1):", sys.getsizeof(d1))
print("get_size(d1):", get_size(d1))

# print(dir(d1))

'''
Activating __slots__ prohibits the creation of some elements, including __dict__, 
which means, for example, such a code for translating structure in json will not work:

def toJSON(self):
    return json.dumps(self .__ dict__)

But it is easy to fix by generating dict programmatically,
i.e. going through all the elements in the loop
'''
import json

def toJSON(self):
        data = dict()
        for var in self.__slots__:
            data[var] = getattr(self, var)
        return json.dumps(data)

jsonfile = toJSON(d1)
print(jsonfile)

'''
Also, it will not be possible to dynamically add new variables to the class.

To save more memory, the use of the library numpy will allows you to create structures in the C-style,
but require a deeper refinement of the code
'''

