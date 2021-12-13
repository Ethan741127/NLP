'''
Python正则表达式
指定好匹配的模式-pattern
选择相应的方法-match,search等
得到匹配结果-group
re.match #从开始位置开始匹配，如果开头没有则无
re.search #搜索整个字符串
re.findall #搜索整个字符串，返回一个list
'''

input = '自然语言处理很重要 。 12abc789'
import re
pattern = re.compile(r'.')
print(re.findall(pattern,input))

'''
字符集合
[abc] 指定包含字符
[a-zA-Z] 来指定所以英文字母的大小写
[^a-zA-Z] 指定不匹配所有英文字母
'''
pattern = re.compile(r'[abc]')
print(re.findall(pattern,input))

pattern = re.compile(r'[a-zA-Z]')
print(re.findall(pattern,input))

pattern = re.compile(r'[^a-zA-Z]')
print(re.findall(pattern,input))

'''
或方法
将两个规则并列起来，以‘ | ’连接，表示只要满足其中之一就可以匹配。
[a-zA-Z]|[0-9] 表示满足数字或字母就可以匹配，这个规则等价于 [a-zA-Z0-9]
'''

pattern = re.compile(r'[a-zA-Z]|[0-9]')
print(re.findall(pattern,input))

'''
匹配数字 ‘\d’ 等价于 [0-9]
'''

pattern = re.compile(r'\d')
print(re.findall(pattern,input))

'''
‘\D’ 匹配非数字
'''

pattern = re.compile(r'\D')
print(re.findall(pattern,input))

'''
‘\w’ 匹配字母和数字
'''

pattern = re.compile(r'\w')
print(re.findall(pattern,input))

'''
\W’ 匹配非字母和数字
'''

pattern = re.compile(r'\W')
print(re.findall(pattern,input))

'''
‘\s’ 匹配间隔符
'''

pattern = re.compile(r'\s')
print(re.findall(pattern,input))

'''
‘*’ 0 或多次匹配
'''
pattern = re.compile(r'\d*')
print(re.findall(pattern,input))

'''
‘+’ 1 或多次匹配
'''

pattern = re.compile(r'\d+')
print(re.findall(pattern,input))

'''
‘?’ 0 或1匹配
'''

pattern = re.compile(r'\d?')
print(re.findall(pattern,input))

'''
‘{m}’ 精确匹配 m 次
'''

pattern = re.compile(r'\d{3}')
print(re.findall(pattern,input))

'''
{m,n}’ 匹配最少 m 次，最多 n 次。 (n>m)
'''

pattern = re.compile(r'\d{1,3}')
print(re.findall(pattern,input))

'''
match 与 search
它们的返回不是一个简单的字符串列表，而是一个 MatchObject,可以得到更多的信息。
如果匹配不成功，它们则返回一个 NoneType 。所以在对匹配完的结果进行操作之前，必需先判断一下是否匹配成功了。
match 从字符串的开头开始匹配，如果开头位置没有匹配成功，就算失败了；而 search 会跳过开头，继续向后寻找是否有匹配的字符串。
'''

input2 = '123自然语言处理23'
pattern = re.compile(r'\d')
match=re.match(pattern,input2)
print(match.group())

input2 = '自然语言处理3'
pattern = re.compile(r'\d')
search=re.search(pattern,input2)
print(search.group())

'''
字符串的替换和修改
在目标字符串中规格规则查找匹配的字符串，再把它们替换成指定的字符串。你可以指定一个最多替换次数，否则将替换所有的匹配到的字符串。
sub ( rule , replace , target [,count] )
subn(rule , replace , target [,count] )
第一个参数是正则规则，第二个参数是指定的用来替换的字符串，第三个参数是目标字符串，第四个参数是最多替换次数。
sub 返回一个被替换的字符串
subn 返回一个元组，第一个元素是被替换的字符串，第二个元素是一个数字，表明产生了多少次替换。
'''

input3 = '123自然语言处理'
pattern = re.compile(r'\d')
print(re.subn(pattern,'啥',input3))

'''
split 切片函数。使用指定的正则规则在目标字符串中查找匹配的字符串，用它们作为分界，把字符串切片。
split( rule , target [,maxsplit] )
第一个参数是正则规则，第二个参数是目标字符串，第三个参数是最多切片次数,返回一个被切完的子字符串的列表
'''

input4 = '國家123自然语言处理4444处理3566自然语言'
pattern = re.compile(r'\d+')
print(re.split(pattern,input4))


'''
‘(?P…)’ 命名组
<…>’ 里面是你给这个组起的名字,
'''

pattern = re.compile(r'(?P<lol>\d+)(?P<dota>\D+)')
m = re.search(pattern,input4)
print(m.group('dota'))

'''
例子
'''

# 筛选号码
input5 = 'number 338-343-220'
pattern = re.compile(r'(\d\d\d-\d\d\d-\d\d\d)')
m = re.search(pattern,input5)

print(m.groups())