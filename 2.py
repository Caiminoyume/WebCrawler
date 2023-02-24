import re

# 定义要匹配的模式
pattern = r'hello\s(\w+)'

# 定义要匹配的字符串
string = 'hello world'

# 使用 re 模块进行匹配
match = re.search(pattern, string)

# 如果匹配成功，输出匹配到的字符串
if match:
    print('Match found: ', match.group(0))
    print('Match found: ', match.group(1))
else:
    print('No match')
