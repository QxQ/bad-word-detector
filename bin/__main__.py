import options_file, string_stuff, list_stuff

options = options_file.Options_file(default_file=True,directory='bin')

''' #methods
simular-chars
remove-symbols
sounds-simular
repeated-chars
silent-sounds
scramble
'''

def find_bad_words(line): #this looks for bad words, and tells you if it can find any
	if line in get_badwords():
		return True
	return False
	line = string_stuff.String_stuff(line) #we are going to be doing all sorts of complecated stuff, so lets use this library to help out.
	bad_words = list_stuff.List_stuff( get_badwords() )
	
	'''
	formulas=[]
	for formula_class in formulas_classes:
		formulas.append( formula_class(line,bad_words) )
	formulas.sort()
	
	for i in formulas:
		pass
	'''
		

def print_found_bad_words(line): #tells you if it found bad words or not. (this uses print instead of return)
	if find_bad_words(line):
		print('BAD!!')
	else:
		print('ok')

def get_badwords():
	return options.value['bad-words']

def show_badwords():
	print('\n'.join(options.value['bad-words']))

def test():
	print(string_stuff.String_stuff(' starting test ').center(fill='-'))
	
	print('testing bad cases\n')
	bad_success = 0
	for testcase in options.value['bad-test-values']:
		val = find_bad_words(testcase)
		if val!=True:
			print('FAILED (should be a bad word): '+testcase)
		else:
			bad_success+=1
	bad_total = len(options.value['bad-test-values'])
	print('\nbad test over: {}/{} succeeded ({}%)'.format(bad_success, bad_total, round(bad_success/bad_total*100,1)) )
	
	print('\ntesting good cases\n')
	good_success = 0
	for testcase in options.value['good-test-values']:
		val = find_bad_words(testcase)
		if val!=False:
			print('FAILED (should not be a bad word): '+testcase)
		else:
			good_success+=1
	good_total = len(options.value['good-test-values'])
	print('\ngood test over: {}/{} succeeded ({}%)'.format(good_success, good_total, round(good_success/good_total*100,1)) )
	
	total = bad_total+good_total
	success = bad_success+good_success
	if total!=success:
		print('TEST FAILED!')
	print(string_stuff.String_stuff( ' test over: {}/{} succeeded ({}%) '.format(success,total,round(success/total*100,1)) ).center(fill='-'))
	print('\n')

def ui():
	import simple_ui
	default_command = simple_ui.ui_command([],print_found_bad_words,'to test it for bad words')
	
	get_badwords_command = simple_ui.ui_command(['l','list'],show_badwords,'to get the list of bad words')
	test_command = simple_ui.ui_command('test',test,'to test many different pre-made words')
	commands=[get_badwords_command, test_command]
	
	note = string_stuff.String_stuff('*note that this program doesn\'t know any real bad words, so don\'t go typing in real bad words').wrap()
	extra_help = string_stuff.String_stuff('''\
   type anything in, and this program will search through it for a bad word. however, this program is smarter then the average bad-word-detector. it doesn't just look for an exact match, but anything that could look like a bad word to the user. the primary purpose of this program is to prove it is possible, and to try to get people to start implementing similar programs into online chats.

   note that this program doesn't actually have any bad words stored in it. instead it uses a fake list of bad words, so things like "brick" is a bad word, but a real bad word will actually not be detected.

   this program, along with all the little libraries it uses are licensed under the mit lisense, unless a library says so otherwise.

''').wrap()
	options={'before-small-help':note,'before-help':extra_help,
			'small-help-commands':['help',get_badwords_command,'quit']}
	ui = simple_ui.Simple_ui('welcome to the bad word detector',commands,default_command,options)
	ui.start_ui()

if options.value['run-test']:
	test()
if options.value['use-ui-by-default']:
	ui()

def remove_repeated(line):
	repeated_char = ''
	count=0
	for i in range(len(line.value)):
		if line.value[i]['char']==repeated_char:
			count+=1
		else:
			if count>1:
				for j in range(count):
					line.value[i-j]
			repeated_char=0
			count=0
		
