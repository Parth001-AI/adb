# value = 'Parthu'
# length = len(value)
# revStr = ""
# while length != 0:
#   revStr = revStr + value[length - 1]
#   length = length-1; 

# print(revStr)
 
value = 'Parthu'
revvalue = value[::-1]
if value == revvalue:
    print(f"{value} is a palindrome")