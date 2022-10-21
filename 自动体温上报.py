import requests
import random
post_url = 'http://k8n.cn/student/course/49623/covid19d3'
t1 = '36.' + str(random.randint(0,10))
t2 = '36.' + str(random.randint(0,10))
t3 = '36.' + str(random.randint(0,10))
t = 't1=' + t1 +'&t2=' + t2 + '&t3=' + t3
data = t
header ={
'Host': '',
'Connection':'',
'Content-Length' : '',
'Cache-Control': '',
'Upgrade-Insecure-Requests': '',
'Origin': '',
'Content-Type': '',
'User-Agent' : '',
'Accept': '',
'X-Requested-With': '',
'Referer': '',
'Accept-Encoding' : 'gzip, deflate',
'Accept-Language' : 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie': ''
}
response = requests.post(post_url,data=data,headers=header)


#以下为请求示例
# POST /student/cours HTTP/1.1
# Host: k8n.cn
# Connection: keep-alive
# Content-Length: 2
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# Origin: http://k8n.cn
# Content-Type: application/x-www-form
# User-Agent: Mozilla/5.0 (40.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/398 MicroMessengeretType/WIFI Language/zh_CN ABI/arm64
# Accept: text/html,application/xhtmlxchange;v=b3;q=0.9
# X-Requested-With: com.tencent.mm
# Referer: http://k8n.cn/student/cou3/covid19d3
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
# Cookie: wxis%7C%242y%2410%24UTlxTs0B.jVcsBFyrtLg0u81nZYR%2FllpueWPiLSOXO1rtig360

# t1=36.3&t2=36.5&t3=36.5
