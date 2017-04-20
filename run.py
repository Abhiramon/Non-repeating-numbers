#Check with test cases

def run():
	num=create_num_array(input())
	return get_next_repfree(num)	

def create_num_array(number):
	#creates an array of digits from a number
	num_str=str(number)
	lst=[]
	for i in range(len(num_str)):
		lst.append(int(num_str[i]))
	return lst

def convert_to_num(num):
	number=0
	num.reverse()
	for i in range(len(num)):
		number=number+(10**i)*num[i]
	return number

def find_rep(num):
	#returns the index of first occurence of a repetition in a number  
	for i in range(len(num)):
		for j in range(i):
			if num[i]==num[j]:
				return i
	return -1 #when -1 is returned, no repetetion is found


def minimize(num,index):
	#return number with part from "index" to end minimized (with digits excluding 0)
	digit=1
	for i in range(index,len(num)):
		while digit in num[:i]:
			digit=digit+1
		num[i]=digit
	return num

def minimize_from_zero(num):
	#replaces array from the first occurance of zero with min values
	for i in range(len(num)):
		if num[i]==0:
			num=minimize(num,i)
	return num

def nine_rep(num,index):
	i=index
	#find first digit not 9 to the left of "index", say d
	while(i>=0 and num[i]==9):
		i=i-1
	if i!=-1:  #if 9 is not the first digit, increase d found and minimize from d to end
		num[i]+=1
		num=minimize(num,i+1)
		return num
	else:    # if 9 is first digit, add another digit and minimize all
		num.insert(0,1)
		return minimize(num,0)


def get_next_repfree(num):
	#returns the first repetition-free number bigger than num
	#num is an array of integers
	if len(num)>9:
		return 0
	num=minimize_from_zero(num)
	rep_index=find_rep(num)
	if rep_index==-1:  # no repetition is found
		return convert_to_num(num)	
	if num[rep_index] !=9:
		num[rep_index]+=1
	else:
		num=nine_rep(num,rep_index)

	if rep_index+1<len(num):
		num=minimize(num,rep_index+1)

	return get_next_repfree(num)



print(run())



