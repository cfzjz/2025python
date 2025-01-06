import re


def test_re():
    result = re.match("wangdao", 'wangdao.cn')
    if result:
        print(result.group())


def single_re():
    ret = re.match('.', 'M')
    print(ret.group())

    ret = re.match('t.o', 'too')
    print(ret.group())

    ret = re.match('h', 'hello')
    print(ret.group())

    ret = re.match('[hH]', 'HELLO')
    print(ret.group())

    ret = re.match('[0-9]he', '7hello')
    print(ret.group())

    ret = re.match("[0-35-9]Hello Python", "5Hello Python")
    print(ret.group())

    ret = re.match(r"嫦娥\d号", "嫦娥1号发射成功")
    print(ret.group())


def multiple_re():
    ret = re.match('[A-Z][a-z]*', 'M')
    print(ret.group())
    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())
    ret = re.match("[A-Z][a-z]*", "Aabcdef")
    print(ret.group())

    names = ['name1', '_name', '2_name', '__name__']

    for name in names:
        ret = re.match(r'[a-zA-Z_]\w*', name)
        if ret:
            print(f'{ret.group()} 符合要求')
        else:
            print(f'{name} 非法')

    ret = re.match("[1-9]?[0-9]", "7")
    print(ret.group())
    ret = re.match(r"[1-9]?\d", "33")
    print(ret.group())
    ret = re.match(r"[1-9]?\d", "09")
    print(ret.group())

    ret = re.match(r'[a-zA-Z0-9_]{8,20}', '1jwsifhivbaa_d')
    print(ret.group())

    email_list = ['xiao@163.com', 'xiao@163.comcom', '.com.xiao@qq.com']
    for email in email_list:
        ret = re.match(r'[a-zA-Z0-9_]{4,20}@163\.com', email)
        if ret:
            print(f'{ret.group()}符合')
        else:
            print(f'{email}不符合')


def head_end_re():
    email_list = ['xiao@163.com', 'xiao@163.comcom', '.com.xiao@qq.com']

    for email in email_list:
        ret = re.match(r'\w{4,20}@163\.com$', email)
        if ret:
            print(f'{ret.group()}符合规定')
        else:
            print(f'{email}不符合')

    print('-' * 50)
    ret = re.match(r"[1-9]?\d$", "09")
    if ret:

        print(ret.group())
    else:
        print('不在0-99之间')


def group_re():
    ret = re.match(r'[1-9]?\d$|100', '100')
    print(ret.group())

    email_list = ['xiao@163.com', 'xiao@qq.com', 'xiao@gmail.com']
    for email in email_list:
        ret = re.match(r'\w{4,20}@(qq|163|126)\.com', email)
        if ret:
            print(f'{ret.group()}符合')
        else:
            print(f'{email}不是163，126，qq邮箱')

    tels = ["13100001234", "18912344321", "10086", "18800007777"]
    for tel in tels:
        ret = re.match(r'1\d{9}[0-35-68-9]$', tel)
        if ret:
            print(ret.group())
        else:
            print(f'{tel} no')

    ret = re.match(r'([^-]+)-(\d+)', '010-12345678')
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))

    ret = re.match(r'<[a-zA-z]*>\w*</[a-zA-Z]*>', '<html>hh</html>')
    print(ret.group())

    ret = re.match(r'<([a-zA-Z]*)>\w*</\1>', '<html>hh</htmlasdsd>')
    if ret:
        print(ret.group())
    else:
        print('<html>hh</htmlasdsd>是不正确的标签')

    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]
    for label in labels:
        ret = re.match(r'<([a-zA-Z]*)><([a-zA-Z0-9]*)>.*</\2></\1>', label)
        if ret:
            print(f'{ret.group()}符合')
        else:
            print(f'{label}不符合')

    for label in labels:
        ret = re.match(r'<(?P<n1>\w*)><(?P<n2>\w*)>.*</(?P=n2)></(?P=n1)>', label)
        if ret:
            print(f'{ret.group()}符合')
        else:
            print(f'{label}不符合')


def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)
    try:
        next(matches)
        second_match = next(matches)
        return second_match.group()
    except StopIteration:
        return None


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


def advance_re():
    ret = re.search(r'\d+', '阅读次数999，书本222')
    print(ret.group())

    text = 'abc123def456ghi789'
    pattern = r'\d+'
    second_match = find_second_match(pattern, text)
    print(second_match)

    ret = re.findall(r'\d+', 'python=9999,c=7890,c++=1234')
    print(ret)

    ret = re.sub(r'\d+', '998', 'python=997')
    print(ret)

    ret=re.sub(r'\d+',add,'python=997')
    print(ret)

    ret=re.sub(r'apple','orange','apple apple apple',count=2)
    print(ret)

    s = 'hello world, now is 2020/7/20 18:48, 现在是 2020年7月20日18时48分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)
    ret_s = re.sub(r'时|分', r':', ret_s)
    print(ret_s)
    com = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    ret = com.findall(ret_s)
    print(ret)
    ret1 = com.search(ret_s)
    print(ret1.group())

    long_text = """<div>
            <p>岗位职责：</p>
    <p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
    <p><br></p>
    <p>必备要求：</p>
    <p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
    <p>&nbsp;<br></p>
    <p>技术要求：</p>
    <p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
    <p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
    <p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
    <p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
    <p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
    <p>&nbsp;<br></p>
    <p>加分项：</p>
    <p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

            </div>
        """
    ret=re.sub(r'<[^>]*>|&nbsp;|\n|\s',' ',long_text)
    print(ret)

    ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
    print(ret)


if __name__ == '__main__':
    # test_re()
    # single_re()
    # multiple_re()
    # head_end_re()
    # group_re()
    advance_re()
