dayType = 1

weekend = 1
workday = 2
holiday = 3



if dayType == 1:
    pass
elif dayType == 2:
    pass 
else:
    pass 

dayDescription = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holiday'

print(dayDescription)


bonus_granted = True 
bonus = 23
price = 123 

price  = price - bonus if bonus_granted == False else price
print(price) 