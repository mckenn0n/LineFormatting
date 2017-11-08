import sys

def format(M, w):
	max_num = M
	words = w
	sum_char = 0
	line = ''
	for x in words:
		print(x,end=" ")
	print("\n-------------------------------------------------")
	for x in words:
		if len(x) + 1 + sum_char < max_num:
			sum_char += len(x)+1
			line += x + ' '
		elif len(x) + sum_char == max_num:
			line += x
			print(line, " \t\tnumber of char (including space) = ",len(line))
			line = ''
			sum_char = 0
		else:
			print(line, " \n\tnumber of char (including space) = ",len(line))
			if len(x) == max_num:
				print(x, " \n\tnumber of char (including space) = ",len(x))
				sum_char = 0
				line = ''
			else:
				line = x+' '
				sum_char = len(x)+1
	if sum_char != 0:
		print(line, " \n\tnumber of char (including space) = ",len(line))

def main():
	wl = ['physics', 'chemistry','spam', 'Spam', 'to', 'SPAM!','Hi!', 'Hi!','YAY','533','ALGORITHMS!', 'Hi!', 'Hi!',"two", "four", "six", "eight","spam", "bungee", "swallow",'apples', 'cherries', 'pears',"Alejandro", "Ed", "Kathryn", "Presila", "Sean", "Peter",'apples', 'bananas', 'blueberries', 'oranges', 'mangos','this', 'that', 'these', 'those']
	wlr = wl[::-1]
	new_wl = wl + wlr + wl + wlr
	format(int(sys.argv[1]), new_wl)


if __name__ == '__main__':
		main()