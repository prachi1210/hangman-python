import turtle, random
file_path='C:\Udacity\Hangman\wordlist.txt'
stage=[0]

def wordlist():
	file_obj=open(file_path, 'r')
	lst=file_obj.readlines()
	file_obj.close()
	return lst[random.randint(0,len(lst))]
