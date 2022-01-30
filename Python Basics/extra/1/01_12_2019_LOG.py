Python 3.5.2 (default, Oct  8 2019, 13:06:37) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> globals()
{'__package__': None, '__spec__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__name__': '__main__', '__doc__': None, '__builtins__': <module 'builtins' (built-in)>}
>>> for k in globals().keys():
	print(k)

	
__package__
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    for k in globals().keys():
RuntimeError: dictionary changed size during iteration
>>> D = globals().keys()
>>> for k in D.keys():
	print(k)

	
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    for k in D.keys():
AttributeError: 'dict_keys' object has no attribute 'keys'
>>> D = globals()
>>> for k in D.keys():
	print(k)

	
__package__
__spec__
__loader__
k
__name__
__doc__
D
__builtins__
>>> 
=============================== RESTART: Shell ===============================
>>> globals()
{'__name__': '__main__', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__package__': None, '__spec__': None, '__doc__': None, '__builtins__': <module 'builtins' (built-in)>}
>>> def test():
	print(locals())
	n = 10
	print(locals())
	f = 3.14
	print(locals())
	def g():
		print("In g")
	print(locals())
	D = {10:1, 20:2, 30:3}
	print(locals())

	
>>> globals()
{'__name__': '__main__', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__package__': None, '__spec__': None, 'test': <function test at 0xb7a71734>, '__doc__': None, '__builtins__': <module 'builtins' (built-in)>}
>>> test()
{}
{'n': 10}
{'n': 10, 'f': 3.14}
{'n': 10, 'g': <function test.<locals>.g at 0xb633ed64>, 'f': 3.14}
{'D': {10: 1, 20: 2, 30: 3}, 'n': 10, 'g': <function test.<locals>.g at 0xb633ed64>, 'f': 3.14}
>>> 
