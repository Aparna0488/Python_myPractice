#Program to check if user input is a palindrome
#Please use anaconda prompt to execute and verify results
userInput = input("Enter a word or phrase: ") 
userInput = userInput.replace(' ','')  #spaces removed in user input
userInput = userInput.upper()  #converted to upper case
lstString = list(userInput) #converting string to list  
lstString.reverse() #reversing the list

#converting reversed list back to a string for comparison with user input

str=""
for i in lstString:
	str+= i
if(str == userInput):
	print("Palindrome") #if reversed string and user input are equal, then it means input is a palindrome
else:
	print("Not a Palindrome")
