import re

s = 'This is first line.\nThis is second line.'
# re.re.MULTILINE
result = re.findall(r'^This(.*?)line.$', s, re.MULTILINE)
print(result)
