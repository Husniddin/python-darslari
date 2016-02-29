import sys

print("Buyruqlar qatori argumentlari:")
for i in sys.argv:
	print(i)

print("\n\n O'zgaruvchi PYTHONPATH qiymati", sys.path, "\n")

| - <некоторый каталог из sys.path>/
| |---- world/
| 		|---- __init__.py
| 		|---- asia/
| 		| 	  |---- __init__.py
| 		| 	  |---- india/
| 		| 		    |---- __init__.py
| 		| 		    |---- foo.py
| 		|---- africa/
| 			  |---- __init__.py
| 			  |---- madagascar/
| 				    |---- __init__.py
| 				    |---- bar.py