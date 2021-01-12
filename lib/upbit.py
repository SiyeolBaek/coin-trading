import json
from os.path import dirname, abspath

config = json.loads(open(dirname(abspath(__file__)) + "/config.json").read())

class Upbit(object):
	def __init__(self):
		pass