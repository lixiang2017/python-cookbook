# 解压序列赋给多个变量

p = (4, 5)
x, y = p
# z, y, z = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)

year, month, day = date
print(year, month, day)

s = 'hello'
a, b, c, d, e = s
print(a, b, c, d, e)
