#add cases to return 0 when no number is possible

def create_num_array(number):
	#creates an array of digits from a number

def find_rep(num):
	#returns the index of first occurence of a repetition in a number

def minimize(num,index):
	#return number with part from "index" to end minimized 
	digit=1
	for i in range(index,len(num)):
		while digit in num:
			digit=digit+1
		num[i]=digit
	return num


def get_next_repfree():
	#returns the first repetition-free number bigger than num
	#num is an array of integers
	num=create_num_array(input())
	rep_index=find_rep(num)
	if num[rep_index] !=9:
		num[rep_index]+=1
	else:
		#complete

	if rep_index+1<len(num):
		num=minimize(num,rep_index+1)

	return num

print get_next_repfree()

