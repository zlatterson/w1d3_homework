def return_10():
    return 10

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2
    
def multiply(num1, num2):
    return num1 * num2

def divide(n1,n2):
    return n1 / n2

def length_of_string(text):
    return len(text)

def join_string(text1,text2):
    return text1 + text2

def add_string_as_number(tn1, tn2):
    return int(tn1) + int(tn2)

def number_to_full_month_name(month):
    if month == 1:
        return "January"
    elif month == 2:
        return "Febuary"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    
def number_to_short_month_name(month):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
    month - 1
    return months[month]

def volume_of_cube(side):
    return side * side * side

def reversed_string(text):
    return text [::-1]

def fh_to_c(farenheit):
    return int((farenheit - 32) * 5/9)

