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

if __name__=='__main__': #just for testing purpoeses
	a = String_stuff('hello world')
