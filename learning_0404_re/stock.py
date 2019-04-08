import requests
import re

response = requests.get('http://quote.stockstar.com/stock/ranklist_a_3_1_1.html')
content = str(response.content, encoding='gb2312')
result = re.findall(r'<tbody class="tbody_right" id="datalist">(.*?)</tbody>', content, re.S)
result = re.findall(r'<tr>(.*?)</tr>', result[0])
with open('stock.txt', 'w', encoding='utf8') as f:
    f.write('股票代码    股票名称    价格\n')
    for r in result:
        code = re.search(r'<a href="//stock.quote.stockstar.com/(\d{6}).shtml">\d{6}</a>', r)
        name = re.search(r'<a href="//stock.quote.stockstar.com/.*?.shtml">(\D*?)</a>', r)
        price = re.search(r'<td class=""><span class="red">(\d*.\d*)</span></td>', r)
        text = '%s    %s    %s\n' % (code.group(1), name.group(1), price.group(1))
        f.write(text)
