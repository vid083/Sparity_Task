# empty list to append terms in series
percent_list = [] 

# num --> first term of percentage series i.e, 10.5
# diff --> difference of first and second percentage, (12-10.5)= 1.5
# count --> number of terms of percentage series (Jan to Dec) = 12
def series(num, diff, count): # function to obtain series
    percent_list.append(num)
    num += diff 
    diff += 1
    count -= 1
    
    if count > 0:
        return series(num, diff, count)

# calling function
series(10.5, 1.5, 12)

#empty dictionary to assign terms of percentage series to month numbers respectively
month_dict = {}
for i in range(1,13): 
    month_dict[i] = percent_list[i-1]

# user input
ip = int(input("Enter the month number:"))

# check if month number is in month_dict
if ip in month_dict:
    print(f"Percentage of vaccinated people in month number:{ip} is {month_dict[ip]}%")
else:
    print("Enter a valid month number from 1 to 12")



'''
percent_list = [10.5, 12.0, 14.5, 18.0, 22.5, 28.0, 34.5, 42.0, 50.5, 60.0, 70.5, 82.0]

month_dict = {1: 10.5, 2: 12.0, 3: 14.5, 4: 18.0, 5: 22.5, 6: 28.0, 7: 34.5, 8: 42.0, 9: 50.5, 10: 60.0, 11: 70.5, 12: 82.0}

'''