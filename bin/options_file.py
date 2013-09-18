import os, json
from os import path

'''
use OptionsFile.value to change the settings, then OptionsFile.save() to save the changes.
'''
class Options_file(object): #if no file is found, sets it to default (wich must be a string) unless default_file is provided or default_func is provided. if default_func is provided, sets it to the output of the func (must return a string). if default_file is provided, opens the file's directory provided and uses that, or if default_file is true, uses the directory default_options.json
	def __init__(self, directory=path.abspath('.'), name='options.json', default={},default_file=False,default_func=None):
		self._default = default
		if default_file==True:
			default_file = path.join(directory,'default_options.json')
		self._default_file = default_file
		self._default_func = default_func
		self._path = directory
		self._full_path = path.join(directory,name)
		
		if path.isfile(self._full_path):
			#reads the content of the file and stores it as self.value
			self.refresh()
		else: #no file exists, so stores an empty dictionary in self.value and creates a file, unless one of the defaults are specified.
			self.set_default()
	
	def save(self): #saves any changes made to self.value
		with open(self._full_path, 'w') as json_file:
			json_file.write( json.dumps(self.value, sort_keys=True, indent=4, separators=(',', ': ')) )
	
	def refresh(self): #dumps any unsaved changes and gets content from the saved file (useful if the file changes with other means besides this program, while the program is running)
		json_file = open(self._full_path)
		self.value = json.loads( json_file.read() )
		json_file.close()
	
	def set_default(self): #sets to the default values provided in the init.
		if self._default_file:
			with open(self._default_file) as src_file:
				self.value = json.loads(src_file.read())
		elif self._default_func:
			self.value = json.loads(self._default_func())
		else:
			self.value = json.loads(self._default)
		self.save()	
	
	''' #this is buggy, and I don't actually like the way they are implemented, so maybe some other time I will re-implement them differently
	def modify(self,*args): #modifies an attribute, then saves the changes. syntax: modify('key','subkey'...)('value'). only works with modifying sub dictionaries, not lists.
		obj = self.value
		return self._modify_returned_func
	def _modify_returned_func(self, value):
		if args.length==1:
			obj[args[0]]=value
			self.save()
			return
		first_arg = args.pop(0)
		obj = obj[first_arg]
		self._modify_returned_func(self, value)
	
	def remove(self,*args): #removes an attribute, then saves the changes. syntax: modify('key','subkey'...). only works with modifying sub dictionaries, not lists.
		obj = self.value
		_remove_recursive()
	def _remove_recursive(self):
		if args.length==1:
			obj.pop(args[0],None)
			self.save()
			return
		first_arg = args.pop(0)
		obj = obj[first_arg]
		self._modify_returned_func(self, value)
	'''
	
	def delete_file(self): #deletes the options file.
		os.remove(self._full_path)
		#this object can't do anything without the file, so we remove the object also
		del self #this doesn't actually seem to work. oh well.

if __name__=='__main__': #just for testing purpoeses
	f = Options_file(path.abspath('.'),default_file=True)
