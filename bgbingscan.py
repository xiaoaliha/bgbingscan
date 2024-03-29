import os
import sys
import argparse

parser = argparse.ArgumentParser(description='bgbingscan help')
parser.add_argument('-v','--vuln', help='Please Input a vuln number!',default='')
parser.add_argument('-u','--url', help='Please Input a url!',default='')
args=parser.parse_args()
if args.vuln!="":
    number=args.vuln
    number=int(number)
    if number==13579:
        langling='"蓝凌OA custom.jsp 任意文件读取漏洞.py"'
        os.system("cd payload &&"+langling)
    elif number==135791:
        langling='"蓝凌OA custom.jsp 任意文件读取漏洞批量扫描.py"'
        os.system("cd payload &&"+langling)
    elif number==45972:
        ruijie='"锐捷云课堂主机目录遍历漏洞.py"'
        os.system("cd payload &&"+ruijie)
    elif number==459721:
        ruijie='"锐捷云课堂主机目录遍历漏洞批量扫描.py"'
        os.system("cd payload &&"+ruijie)
elif args.url!="":
    url=args.url
    all='"allpayload.py"'
    os.system("cd payload &&"+all+" "+url)
else:
    print("""
\033[1;36m  __               __                               \033[0m
\033[1;36m [  ]             [  ]                              \033[0m
\033[1;36m |  |             |  |     \     _ .--.  ------     \033[0m
\033[1;36m |  |.--..------  |  |.--.----- [ `.-. | /     \    \033[0m
\033[1;36m |      \/      \ |      \    / | |  | | |           \033[0m 
\033[1;36m |      ||        |      |   /  | |  | |  \__ _ _| scan \033[0m
\033[1;36m |.__ _/  \__ _ _||.__ _/   /__[___| [__]        |   \033[0m
\033[1;36m                 |                               |    \033[0m
\033[1;36m                 |                         \__ _ /      \033[0m    
\033[1;36m           \__ _ /           """)
    print("\n")
    print('\033[1;36m   验证漏洞\033[0m')
    print('\033[1;36m           python3 bgbingscan.py -u http://xxx.xxx.xxx.xxx\033[0m')
    print("\n")
    print('\033[1;36m   利用漏洞\033[0m')
    print('\033[1;36m           python3 bgbingscan.py -v xxxx\033[0m')
    print('\033[1;36m            or\033[0m')
    print('\033[1;36m           python3 bgbingscan.py --vuln xxxx\033[0m')
    print("\n")
    print('\033[1;36m目前更新漏洞\033[0m')
    print(' \033[1;36m          2021/5/1 蓝凌OA custom.jsp 任意文件读取漏洞 (13579)\033[0m ')
    print(' \033[1;36m          2021/5/1 蓝凌OA custom.jsp 任意文件读取漏洞批量扫描 (135791)\033[0m ')
    print(' \033[1;36m          2021/5/1 锐捷云课堂主机目录遍历漏洞 (45972)\033[0m ')
    print(' \033[1;36m          2021/5/1 锐捷云课堂主机目录遍历漏洞批量扫描 (459721)\033[0m ')
    sys.exit()

