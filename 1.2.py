

# 星号表达式
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


def avg(grades):
    sum = 0
    n = 0
    for item in grades:
        sum += item
        n += 1
    return sum / n


scores = [80, 90, 92, 100]
print(drop_first_last(scores))

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)
print(type(phone_numbers) == type([]))
print(type([]))


def cmp(sales_record):
    *trailing_qtrs, current_qtr = sales_record
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    return avg_comparison(trailing_avg, current_qtr)


def avg_comparison(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0