class List_stuff():
	def __init__(self, value):
		self.value=value
		
		self.__iter__ = self.value.__iter__
		self.sort = self.value.sort
	
	def to_english(self, conjunction='and',space_after_comma=True, comma_before_conjunction=None): #coma_before_conjuction default is "sometimes" (None), but can be false or true
		if len(self.value)==0:
			return ''
		elif len(self.value)==1:
			return self.value[0]
		comma = ', ' if space_after_comma else ','
		if not conjunction:
			return comma.join(self.value[:-1])
		ans = comma.join(self.value[:-1])
		if comma_before_conjunction:
			ans+=comma
		elif comma_before_conjunction==None and len(self.value)>2: #comma_before_conjuction==sometimes
			ans+=comma
		else:
			ans+=' '
		ans = '{ans}{conjunction} {last}'.format(ans=ans, conjunction=conjunction, last=self.value[-1])
		return ans
		
class Complex_list(): # a list that can have multiple items be in the same index, and more
	def __init__(self, value=[]):
		new_value = []
		for char in value:
			new_value.append(Complex_list_item([char]))
		self.value = new_value

class Complex_list_item(): #an index in a Complex_list
	def __init__(self,items=[]):
		self.value=[]
		for i in items:
			self.append(items[i])
	
	def append(value, condition=None):
		self.insert(-1,value,condition)
	
	def insert(index, value, condition=None):
		self.value.insert(index, {'char':value,'condition':None})
	
	def pop(index=-1):
		return self.value.pop(index)['char']
	
	def get(index=None): #anything you want to do with getting a charcter, use this function, otherwise, use self.value
		if index!=None:
			return [i['char'] for i in items]
		else:
			return items[index]['char']
	
	def loop(func,keep=None,index=0): #func gets passed to parms: keep, and char. char is the char from the iteration. keep is an object to keep information between iterations. keep comes with a value "keep.possibilities" which contains the possibilities object, and keep.past which contains the past accepted possibilities.
		if keep==None:
			class Keep(): pass
			keep=Keep()
		
		keep.possibilities = self.value[i]
		do_break = func(keep,self.value[i]['char'])
		if do_break:
			pass
			#break
			
			
		
		

if __name__=='__main__': #just for testing purpoeses
	a = List_stuff(['hello world'])
