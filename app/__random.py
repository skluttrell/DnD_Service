import random
import string
import urllib3

class RandomOrg:
	def __init__(self):
		self.data = None
		self.code = None
		self.alert = None
		self._http = urllib3.PoolManager()
		self._dontResetVariables = False

	def __gen_url(self, type: str='integers', num: int=1, min: int=1, max: int=2, col: int=1, len: int=10, digits: str='on', upperalpha: str='on', loweralpha: str='on', unique: str='on', base: int=10, format: str='plain', rnd: str='new') -> str:
		# PRIVATE METHOD: Returns a random.org url for the requested data

		if type == 'int': type = 'integers'
		elif type == 'seq': type = 'sequences'
		elif type == 'str': type = 'strings'
		if not type[-1] == 's': type += 's'
		if type != 'integers' and type != 'strings' and type != 'sequences': raise Exception('That is not a valid type!')
		if type == 'integers': # Integer generator
			return 'https://www.random.org/{}/?num={}&min={}&max={}&col={}&base={}&format={}&rnd={}'.format(type, num, min, max, col, base, format, rnd)
		elif type == 'sequences': # Sequence generator
			return 'https://www.random.org/{}/?min={}&max={}&col={}&format={}&rnd={}'.format(type, min, max, col, format, rnd)
		elif type == 'strings': # String generator
			return 'https://www.random.org/{}/?num={}&len={}&digits={}&upperalpha={}&loweralpha={}&unique={}&format={}&rnd={}'.format(type, num, len, digits, upperalpha, loweralpha, unique, format, rnd)

	def get_true_random(self, type: str='integers', num: int=1, min: int=1, max: int=2, col: int=1, len: int=10, digits: str='on', upperalpha: str='on', loweralpha: str='on', unique: str='on', base: int=10, format: str='plain', rnd: str='new') -> int or str:
		"""Generates a true random number from random.org

		Parameters
		----------
		num : int
			Possible values: [1,1e4]
			The number of strings requested. (Defaults to 1)
		min : int
			Possible values: [-1e9,1e9]
			The lower bound of the interval (inclusive). (Defaults to 1)
		max : int
			Possible values: [-1e9,1e9]
			The upper bound of the interval (inclusive). (Defaults to 2)
		col : int
			Possible values: [1,1e9]
			The number of columns in which the integers will be arranged. The /
			integers should be read (or processed) left to right across columns. /
			(Defaults to 1)
		len : int
			Possible values: [1,20]
			The length of the strings. All the strings produced will have the same /
			length. (defaults to 10)
		digits : str
			Possible values: on | off
			Determines whether digits (0-9) are allowed to occur in the strings.
			(Defaults to on)
		upperalpha : str
			Possible values: on | off
			Determines whether uppercase alphabetic characters (A-Z) are allowed /
			to occur in the strings. (Defaults to on)
		loweralpha : str
			Possible values: on | off
			Determines lowercase alphabetic characters (a-z) are allowed to occur /
			in the strings. (Defaults to on)
		unique : str
			Possible values: on | off
			Determines whether the strings picked should be unique (as a series of /
			raffle tickets drawn from a hat) or not (as a series of die rolls). If /
			unique is set to on, then there is the additional constraint that the /
			number of strings requested (num) must be less than or equal to the /
			number of strings that exist with the selected length and characters. /
			(Defaults to on)
		base : int
			Possible values: 2 | 8 | 10 | 16
			The base that will be used to print the numbers, i.e., binary, octal, /
			decimal or hexadecimal. (Defaults to 10)
		format : str
			Possible values: html | plain
			Determines the return type of the document that the server produces as /
			its response. If html is specified, the server produces a nicely /
			formatted XHTML document (MIME type text/html), which will display /
			well in a browser but which is somewhat cumbersome to parse. If plain /
			is specified, the server produces as minimalistic document of type /
			plain text (MIME type text/plain) document, which is easy to parse. If /
			you are writing an automated client, you probably want to specify plain here. (Defaults to plain)
		rnd : str
			Possible values: new | id.identifier | date.iso-date
			Determines the randomization to use to generate the strings. If new is /
			specified, then a new randomization will created from the truly random /
			bitstream at RANDOM.ORG. This is probably what you want in most cases. /
			If id.identifier is specified, the identifier is used to determine the /
			randomization in a deterministic fashion from a large pool of /
			pregenerated random bits. Because the numbers are produced in a /
			deterministic fashion, specifying an id basically uses RANDOM.ORG as a /
			pseudo-random number generator. The third (date.iso-date) form is /
			similar to the second; it allows the randomization to be based on one /
			of the daily pregenerated files. This form must refer to one of the /
			dates for which files exist, 
			so it must be the current day (according to UTC) or a day in the past. /
			The date must be in ISO 8601 format (i.e., YYYY-MM-DD) or one of the /
			two shorthand strings today or yesterday. (Defaults to new)
		"""

		# Random.org has a limit of 100,000 bytes and will not allow requests if this number is negative
		# Each IP is given at least 20,000 top-up bytes at midnight
		# If the quota is below zero (0) bytes than this method calls a local pseudo random generator by default
		if not self.get_quota():
			self.code = 601
			self.alert = 'Error: random.org is unable to fulfill the request, defaulting to pseudo random.'
			self._dontResetVariables = True
			return self.get_pseudo_random(type, num, min, max, col, len, digits, upperalpha, loweralpha, unique, base)

		# Resets the class variables
		self.data = None
		self.code = None
		self.alert = None
		requestURL = self.__gen_url(type, num, min, max, col, len, digits, upperalpha, loweralpha, unique, base, format, rnd)
		request = self._http.request('GET', requestURL)
		self.code = request.status
		self.data = request.data.decode('utf-8').split()
		if self.code != 200:
			self.alert = ''.join(map(str, self.data)) # Something went wrong
			self.data = None

	def get_pseudo_random(self, type: str='integers', num: int=1, min: int=1, max: int=2, col: int=1, len: int=10, digits: str='on', upperalpha: str='on', loweralpha: str='on', unique: str='on', base: int=10) -> int or str:
		"""Generates a pseudo random number from a local resource

		Parameters
		----------
		num : int
			Possible values: [1,1e4]
			The number of strings requested. (Defaults to 1)
		min : int
			Possible values: [-1e9,1e9]
			The lower bound of the interval (inclusive). (Defaults to 1)
		max : int
			Possible values: [-1e9,1e9]
			The upper bound of the interval (inclusive). (Defaults to 2)
		col : int
			Possible values: [1,1e9]
			The number of columns in which the integers will be arranged. The /
			integers should be read (or processed) left to right across columns. /
			(Defaults to 1)
		len : int
			Possible values: [1,20]
			The length of the strings. All the strings produced will have the same /
			length. (defaults to 10)
		digits : str
			Possible values: on | off
			Determines whether digits (0-9) are allowed to occur in the strings.
			(Defaults to on)
		upperalpha : str
			Possible values: on | off
			Determines whether uppercase alphabetic characters (A-Z) are allowed /
			to occur in the strings. (Defaults to on)
		loweralpha : str
			Possible values: on | off
			Determines lowercase alphabetic characters (a-z) are allowed to occur /
			in the strings. (Defaults to on)
		unique : str
			Possible values: on | off
			Determines whether the strings picked should be unique (as a series of /
			raffle tickets drawn from a hat) or not (as a series of die rolls). If /
			unique is set to on, then there is the additional constraint that the /
			number of strings requested (num) must be less than or equal to the /
			number of strings that exist with the selected length and characters. /
			(Defaults to on)
		"""

		self.data = None
		if self._dontResetVariables:
			self._dontResetVariables = False
		else:
			self.code = None
			self.alert = None

		if type == 'integers':
			integers = []
			for i in range(num): integers.append(random.randint(min, max))
			self.data = integers
		elif type == 'sequences':
			seqIn = list(range(min, max+1))
			seqOut = []
			while seqIn:
				i = random.choice(seqIn)
				seqOut.append(i)
				seqIn.remove(i)
			self.data = seqOut
		elif type == 'strings':
			alphaNum = ''
			if digits == 'on': alphaNum += string.digits
			if upperalpha == 'on': alphaNum += string.ascii_uppercase
			if loweralpha == 'on': alphaNum += string.ascii_lowercase
			strings = []
			for i in range(0, num): strings.append(''.join(random.choice(alphaNum) for x in range(len)))
			self.data = strings

	def get_quota(self) -> bool:
		"""Checks to see if random.org is available"""

		request = self._http.request('GET', 'https://www.random.org/quota/?format=plain')
		if request.status != 200 or int(request.data.decode('utf-8')) < 0: return False
		return True