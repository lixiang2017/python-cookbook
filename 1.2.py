# 从任意长度的可迭代对象中分解元素
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


*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# cat /etc/shadow | grep nobody
# nobody:*:17647:0:99999:7:::
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# _ ign ignore
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)


# recursive
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print('sum =', sum(items))               # 36
'''
(head + sum(tail)) if tail else head       36
(head + sum(tail)) if tail else head * 2   45
head + (sum(tail) if tail else head)       45
head + (sum(tail) if tail else head * 2)   54
head + sum(tail) if tail else head * 2     45
head * 2 + sum(tail) if tail else head     63
'''
# 递归出口
head, *tail = [9]
print(head)
print(tail)


