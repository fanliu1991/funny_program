import Ref

call_module = Ref.A("someone", "7","2011")

print("run by Call.py,", call_module.name, call_module.value)
print("also run by Call.py," , call_module.show())
print("run by Call.py and predefined function," , str(call_module))
print("return private number," , call_module.private_num)
print("set private number")
call_module.private_num = 2029
print("return new private number," , call_module.private_num)