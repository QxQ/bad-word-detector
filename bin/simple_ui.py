import string_stuff, list_stuff

class Simple_ui():
	'''
	title: what shows at the top of the screen. leave blank to not show a title. you can make a more custamizable by disabling this, and showing your own title in the before-small-help param.
	commands: a list of commands that the user can use. eg: [<command>,<command>]. make the commands with ui_command()
	default_command: a function that will be used if the prompt doesn't match any of the commands. I think you must use ui_command()
	options: some additional options you can configure
	'''
	def __init__(self,title='', commands=[], default_command=None, options={}):
		self._title = string_stuff.String_stuff(' '+title+' ').center(fill='=') if title!='' else ''
		self._default_command = default_command if default_command else ui_command([],self.default_command_handler)
		self._commands = commands
		
		self._use_quit_command= options['use-quit-command'] if ('use-quit-command' in options) else True #wither to have the default quit command or not
		self._use_more_help_command= options['use-help-command'] if ('use-help-command' in options) else True #wither to have the default more help command or not. note that this gets overwritten if there is no additional help.
		
		self._custom_help= options['custom-help'] if ('custom-help' in options) else False #wither or not to use custom help or default help when program first starts (the text that appears right after the title). you probably want to specify custom-help-str with this.
		self._custom_help_str= options['custom-help-str'] if ('custom-help-str' in options) else '' #the string which will be displayed instead of the default help text. you have to set custom-help to true to use this.
		self._prompt= options['prompt'] if ('prompt' in options) else '>> ' #the string used when asking the user to type in a command
		
		self._before_small_help= options['before-small-help'] if ('before-small-help' in options) else '' #some text to put before the small help
		self._after_small_help= options['after-small-help'] if ('after-small-help' in options) else '' #some text to put after the small help
		self._before_help= options['before-help'] if ('before-help' in options) else '' #some text to put before the help
		self._after_help= options['after-help'] if ('after-help' in options) else '' #some text to put after the help
		
		self._quit=False #set this to true to indicate you want to quit the ui
		self._quit_command = self._about_command = self._help_command = None
		small_help_commands_default = []
		
		if self._use_quit_command:
			self._quit_command = ui_command(['q','quit'], self.stop_ui, 'to quit')
			commands.append( self._quit_command )
			small_help_commands_default.append(self._quit_command)
		
		if self._use_more_help_command:
			self._help_command = ui_command(['h','help'], self.show_help, 'for more help')
			commands.append( self._help_command )
			small_help_commands_default.append(self._help_command)
		self._small_help_commands= options['small-help-commands'] if ('small-help-commands' in options) else small_help_commands_default #the commands that show in the small help. you can use the strings 'help' and'quit' for the built in help and quit commands
		
		for i in range( len(self._small_help_commands) ):
			if self._small_help_commands[i]=='help':
				self._small_help_commands[i] = self._help_command
			elif self._small_help_commands[i]=='quit':
				self._small_help_commands[i] = self._quit_command
		
		same_help = True
		for i in self._small_help_commands:
			if i not in self._commands:
				same_help = False
				break
		for i in self._commands:
			if i not in self._small_help_commands:
				same_help = False
				break
		if same_help and self._before_help=='' and self._after_help=='': #if this is true, then there is no additional help, so the help command is useless
			for i in range(len( self._small_help_commands )):
				if self._small_help_commands[i]==self._help_command:
					self._small_help_commands.pop(i)
					break
			for i in range(len( self._commands )):
				if self._commands[i]==self._help_command:
					self._commands.pop(i)
					break
			self._help_command = None
		
		
	def start_ui(self):
		self.show_start_text()
		while not self._quit:
			self.parse_command( input(self._prompt) )
	
	def show_start_text(self):
		if self._title!='':
			print(self._title)
		
		if self._before_small_help:
			print(self._before_small_help)
		self.show_small_help()
		if self._after_small_help:
			print(self._after_small_help)
	
	def show_small_help(self,always_use_default=False): #the help that shows when the program first starts. set always_use_default to ignore the user's custom help
		if self._custom_help and not always_use_default:
			print(self._custom_help_str)
		else:
			if self._default_command['help']!='':
				print('type anything {help}'.format(help=self._default_command['help']))
			for command in self._small_help_commands:
				self.show_help_with(command)			
	
	def show_help_with(self,command): #used when showing the small help and full help
		for word in command['names']:
			if len(word)>1:
				press = 'type'
				break
		else:
			press='press'
		formated_words = list_stuff.List_stuff( ['"'+i+'"' for i in command['names']] ).to_english(conjunction='or')
		optional = 'you can ' if command['help']=='' else ''
		print( '{optional}{press} {words} than press enter {help}'\
				.format(optional=optional, press=press, words=formated_words, help=command['help']) )
	
	def parse_command(self,command):
		for cmd in self._commands:
			if command in cmd['names']:
				val = cmd['func']()
				if val!=None:
					print(val)
				return val
		val = self._default_command['func'](command)
		if val!=None:
			print(val)
		return val
	
	#some default commands
	def stop_ui(self): #used to stop the ui
		self._quit=True
	
	def show_about(self): #used to show the about page
		print(self._about)
	
	def show_help(self): #shows the full help page
		if self._before_help:
			print(self._before_help)
		for command in self._commands:
			if command not in self._small_help_commands:
				self.show_help_with(command)
		print()
		self.show_small_help(always_use_default=True) #we don't want to show the user's custom help because we want it to all be styled the same way, and the user could leave out some of the help if he feels like it.
		if self._after_help:
			print(self._after_help)
	
	def default_command_handler(self,text): #what to do if the user typed something in that didn't match any command.
		print('that didn\'t match any available commands.\n')
		self.show_small_help()

#the help is only used for the auto generated help that shows when the program first starts. the string "press {0} than press enter " will be inserted before your help string, so your help string should probably look something like "to quit the game"
def ui_command(names,func,help=''):
	if isinstance(names,str):
		names=[names]
	return {'names':names,'func':func,'help':help}

if __name__=='__main__': #just for debugging puppoeses
	def pingpong():
		print('pong')
	def default(s):
		print('you said {0}'.format(s))
	commands = [ui_command('ping',pingpong,'to ping pong!')]
	default_command = ui_command([],default,'to know what you said')
	options={'custom-help':False,'custom-help-str':'press H for help','prompt':'command> '}
	Simple_ui('the ping pong example',commands=commands,default_command=default_command,options=options).start_ui()
