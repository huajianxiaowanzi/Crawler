import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests
from lxml import etree
# 测试git上传
# 测试2
# 测试3

def sendmessage():
    from_addr = ''  # 邮件发送账号
    to_addrs = ''  # 接收邮件账号
    qqCode = ''  # 授权码（这个要填自己获取到的）
    smtp_server = ''  # 固定写死
    smtp_port = 465  # 固定端口
    # 配置服务器
    stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    stmp.login(from_addr, qqCode)

    # 组装发送内容
    b = '今天' + a + "哦"
    message = MIMEText(b, 'plain', 'utf-8')  # 发送的内容
    message['From'] = Header('还没起床？', 'utf-8')  # 发件人
    message['To'] = Header("掉毛", 'utf-8')  # 收件人
    subject = a
    message['Subject'] = Header(subject, 'utf-8')  # 邮件标题

    try:
        stmp.sendmail(from_addr, to_addrs, message.as_string())
    except Exception as e:
        print('邮件发送失败--' + str(e))
    print('邮件发送成功')

headers = {
    "User-Agent": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
}

html = 'https://weather.cma.cn/web/weather/58606.html'
try:
    #/ html / body / div[1] / div[2] / div[1] / div[1] / div[2] / div[1] / div[3]
    response = requests.get(html, headers=headers)
    response.encoding = "utf-8"
    if response.status_code == 200:
        #soup = BeautifulSoup(response.text, "lxml")
        #print(soup)
        tree = etree.HTML(response.text)
        div_list = tree.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/text()')

        a = div_list[0].strip()

        if '雨' in a:
            sendmessage()
        else:
            print(a)


            # prin
except Exception as e:
    # 访问异常的错误编号和详细信息
    print(e.args)
    print(str(e))
    print(repr(e))
