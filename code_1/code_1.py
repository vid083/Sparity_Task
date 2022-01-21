import calendar

def covid_vacc_report(n): # n --> month_number
    first = 10.5 #Jan month percentage, first term in series

    if n in range(1,13) :
        result = first + ((n-1)*(n+1)/2)
        return f"Percentage of vaccinated people in {calendar.month_name[n]}: {result}%"
    else:
        return ("Enter a valid month number from 1 to 12")

output = covid_vacc_report(int(input("Enter month number: ")))
print(output)


'''

n=1   10.5
        |  (10.5+1.5) 
n=2    12
        |  (10.5+2.5) 
n=3   14.5
        |  (10.5+3.5)
n=4    18
        |  (10.5+4.5)
n=5   22.5

'''