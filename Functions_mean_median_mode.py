import random

def mean(x:list,/) -> float:
	mean = float(sum(x)/len(x))
	return mean

def median(x:list,/) -> float:
	length = len(x)
	x_arranged = sorted(x)	
	if len(x_arranged) % 2 == 0:
		first_index=int((length/2)-1)		
		second_index=int(length/2)		
		median = (x_arranged[first_index]+x_arranged[second_index])/2
	else:
		median = x_arranged[(length-1)/2]
	return median

def mode(x:list,/) -> str:
	num_count_dict={}
	for item in x:
		if item in num_count_dict:
			num_count_dict[item]+=1
		else:
			num_count_dict[item]=1
	mode = [key for key in num_count_dict.keys() if num_count_dict[key] == max(num_count_dict.values())]
	# print(mode)
	if len(mode) == len(x): 
		mode = ["No mode"]
	else:
		return str(mode[0])


def variance(x:list,/) -> float:
	mean = float(sum(x)/len(x))
	y = [(number - mean)**2 for number in x]
	variance = round((sum(y)/len(x)),2)
	return variance

def std(x:list,/) -> float:
	variance_data = variance(x)
	std = round(variance_data  ** 0.5,2)
	return std

def summary(n):
	int_list=[]
	for number in range(0,n): 		
		int_list.append(random.randint(0,100))
	num_file = open("numbers.txt",'w')	
	num_file.writelines(str(int_list))
	num_file.close()

	print("mean: "+ str(mean(int_list)))
	print("median: "+str(median(int_list)))
	print("mode: "+mode(int_list))
	print("variance: "+str(variance(int_list)))
	print("std: "+str(std(int_list)))
	
if __name__ == '__main__':
	summary(50)
