import textwrap
CHARS_PER_LINE=80 #how many characters can fit in one line

class String_stuff():
	def __init__(self, value, line_size=CHARS_PER_LINE):
		self.value=value
		self.line_size = line_size
		
	def left(self,fill='',line_size=None): #left aligns
		if line_size==None:
			line_size = self.line_size
		return '{string:{fill}<{size}}'.format(fill=fill,size=line_size,string=self.value)
	def center(self,fill='',line_size=None): #center aligns
		if line_size==None:
			line_size = self.line_size
		return '{string:{fill}^{size}}'.format(fill=fill,size=line_size,string=self.value)
	def right(self,fill='',line_size=None): #right aligns
		if line_size==None:
			line_size = self.line_size
		return '{string:{fill}>{size}}'.format(fill=fill,size=line_size,string=self.value)
	
	def wrap(self,line_size=None): #this will wrap the text, and preserv new line characters
		if line_size==None:
			line_size = self.line_size
		result = self.value.splitlines()
		for i in range(len(result)):
			result[i] = textwrap.fill(result[i], width=line_size)
		return '\n'.join(result)
		
class Complex_string(): # a string that can have multiple items be in the same index, and more
	def __init__(self, value=[]):
		new_value = [] #example: [Complex_list_item, Complex_list_item, ...]
		for char in value:
			new_value.append(Complex_string_item([char]))
		self.value = new_value #you can access self.value directly
	
	def append(self, items): #items is a list of possible items for this index.
		self.value.append( Complex_string_item(items) )
	
	def find(self, key):
			
		def findInIndex(index):
			keyPoss = [0]
			for valueIndex in range(index,len(self.value)):
				newKeyPoss=[]
				for keyPossIndex,keyPos in enumerate(keyPoss):
					for possible in self.value[valueIndex]:
						if len(possible)+keyPos<=len(key) and key[keyPos:len(possible)+keyPos]==possible:
							newKeyPos = keyPoss[keyPossIndex]+len(possible)
							if newKeyPos==len(key):
								return True
							if newKeyPos not in newKeyPoss:
								newKeyPoss.append(newKeyPos)
				keyPoss = newKeyPoss
				if len(keyPoss)==0:
					return False
			return False
		
		for valueIndex in range(len(self.value)):
			if findInIndex(valueIndex):
				return valueIndex
	
	def get(self, index=None):
		if index==None:
			return self.value
		else:
			return self.value[index]
	
	def __contains__(self,key):
		return self.find(key)!=None
	
	def __iter__(self):
		for i in self.value:
			yield i
	
	def __repr__(self):
		return '[complex string: '+str(self.value)[1:-1]+']'
				
				
					

class Complex_string_item(object): #an index in a Complex_string. this index can containt multiple items unlike a normal string.
	def __init__(self,items=[], raw_items=[]):
		if raw_items:
			items = raw_items
		else:
			self.value=[] #example: [{'char':a,...}, {...}]
			for item in items:
				self.add(item)
	
	def add(self, value, condition=lambda: True): #adds an item and returns id. If the item is already there, returns the id of that item instead.
		for i in self.value:
			if value==i['char']:
				return i['id']
		obj = {'char':value,'condition':condition}
		obj['id']=id(obj)
		self.value.append(obj)
		return obj['id']
	
	def remove(self, Id): #removes an item by id
		for i in range(len(self.value)):
			if self.value[i]['id']==Id:
				return self.value.pop(i)
	
	def get(index=None): #anything you want to do with getting a charcter, use this function. otherwise, use self.value to get the raw stuff.
		if index==None:
			return [i['char'] for i in self.value]
		else:
			return self.value[index]['char']
	
	def __contains__(self,key):
		return key in [i['char'] for i in self.value]
	
	def __iter__(self):
		for i in self.value:
			yield i['char']
	
	def __repr__(self):
		val = str([i['char'] for i in self.value])[1:-1]
		val = val.replace(', ','|')
		return val
	__eq__ = __contains__
