import requests
import random
post_url = 'http://k8n.cn/student/course/49623/covid19d3'
t1 = '36.' + str(random.randint(0,10))
t2 = '36.' + str(random.randint(0,10))
t3 = '36.' + str(random.randint(0,10))
t = 't1=' + t1 +'&t2=' + t2 + '&t3=' + t3
data = t
header ={
'Host': 'k8n.cn',
'Connection':'keep-alive',
'Content-Length' : '23',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': '1',
'Origin': 'http://k8n.cn',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent' : 'Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/398 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'X-Requested-With': 'com.tencent.mm',
'Referer': 'http://k8n.cn/student/course/49623/covid19d3',
'Accept-Encoding' : 'gzip, deflate',
'Accept-Language' : 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie': 'wxid=ollOC0WibnYK4NgJEvohginVigqU$1665902118$c28ec991a07533fd308a9a0940e48d49; remember_student_59ba36addc2b2f9401580f014c7f58ea4e30989d=1491967%7Cex3jUu3KaIxslgKbzeRElYZWo8YWgHPUaMqWlk6UShVXMKDdCFZZJukDakbs%7C%242y%2410%24UTlxTs0B.jVcsBFyrtLg0u81nZYR%2FllpueWPiLSOX7Q3FIVhNhfqq; s=nS5ZJFBkzWt2zgM5OHPPnaS06SDeel9O1rtig360'
}
response = requests.post(post_url,data=data,headers=header)


#以下为请求
# POST /student/course/49623/covid19d3 HTTP/1.1
# Host: k8n.cn
# Connection: keep-alive
# Content-Length: 23
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# Origin: http://k8n.cn
# Content-Type: application/x-www-form-urlencoded
# User-Agent: Mozilla/5.0 (Linux; Android 12; M2007J3SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/398 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# X-Requested-With: com.tencent.mm
# Referer: http://k8n.cn/student/course/49623/covid19d3
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
# Cookie: wxid=ollOC0WibnYK4NgJEvohginVigqU$1665902118$c28ec991a07533fd308a9a0940e48d49; remember_student_59ba36addc2b2f9401580f014c7f58ea4e30989d=1491967%7Cex3jUu3KaIxslgKbzeRElYZWo8YWgHPUaMqWlk6UShVXMKDdCFZZJukDakbs%7C%242y%2410%24UTlxTs0B.jVcsBFyrtLg0u81nZYR%2FllpueWPiLSOX7Q3FIVhNhfqq; s=nS5ZJFBkzWt2zgM5OHPPnaS06SDeel9O1rtig360

# t1=36.3&t2=36.5&t3=36.5