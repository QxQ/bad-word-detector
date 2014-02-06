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

