def covid_vacc_report(month_number):
    n = month_number
    
    if n in range(1,13) :
        result = 10+((n**2)/2)
        print(f"Percentage of vaccinated people in month number:{n} is {result}%")
    else:
        print("Enter a valid month number from 1 to 12")

covid_vacc_report(int(input("Enter month number: ")))


'''

n=1   10.5
        |  (10+2) 
n=2    12
        |  (10+4.5) 
n=3   14.5
        |  (10+8)
n=4    18
        |  (10+12.5)
n=5   22.5

'''
