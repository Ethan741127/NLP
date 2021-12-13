#刪除操作
input_str = '  今天天氣不錯，挺風和日麗的   '
print(input_str)
print(input_str.strip())
print(input_str.lstrip())
input_str = 'AAAA今天天氣不錯，挺風和日麗的AAAA'
print(input_str)
print(input_str.strip('A'))
print(input_str.lstrip('A'))

#替換操作
print(input_str.replace('A','B'))
print(input_str.replace('今天',''))

#查找操作
print(input_str.find('不錯'))

#判斷操作
input_str='123'
print(input_str.isdigit())
input_str='apple'
print(input_str.isalpha())

#分割合併操作
input_str = '今天 天氣 不錯 挺風 和 日麗 的'
input_str1 = input_str.split(' ')
print(input_str1)
print(''.join(input_str1))





