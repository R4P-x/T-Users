try:
	import os
	from os import system as s
	try:
		import requests
	except ModuleNotFoundError:
		os.s('pip install requests')
	try:
		import random
	except ModuleNotFoundError:
		os.s('pip install random')
	try:
		import multiprocessing
	except ModuleNotFoundError:
		os.s('pip install multiprocessing')
		
except ModuleNotFoundError:
	print('\033[1;31m ERROR!!!!')
