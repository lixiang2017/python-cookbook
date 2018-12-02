# 从字典中提取子集
# 字典推导式(dictionary comprehension)

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

# Make a dictionary of tech stocks  # 选出科技股
tech_name = {'AAPL', 'IBM', "HPQ", 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_name}
print(p2)


# 创建元祖序列 # 慢
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)

# 慢
tech_name = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: prices[key] for key in prices.keys() & tech_name}
print(p2)

'''
{'AAPL': 612.78, 'IBM': 205.55}
{'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2}
{'AAPL': 612.78, 'IBM': 205.55}
{'IBM': 205.55, 'HPQ': 37.2, 'AAPL': 612.78}
'''