from os import system as sys
'''
导入system模块，以运行系统命令
'''
def main():   
    '''
    pyqi主函数
    '''
    version = int(0)
    x = int(0)
    py = int(0)
    '''
    初始化变量
    '''
    print("Pyqi v1.0-beta")
    print("请输入您要安装的Python版本:")
    print("[1]Python3.7")
    print("[2]Python3.8")
    print("[3]Python3.9")
    print("===========================")
    '''
    打印询问消息
    '''
    version = int(input(">>> "))
    '''
    确认安装版本
    '''
    x = input("是否继续?(y/n):")
    '''
    确认，并开始安装进程
    '''
    if x == "y" :
        print("正在下载Python")
        if version == 1 :
            print("开始安装")
        elif x == "n" :
            exit("用户取消进程")
    if version == 1 :
        sys("cd /usr/local/")
        sys("mkdir python3")
        sys("curl -O https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz")
        sys("tar xvf python-3.7.1.tgz")
        sys("cd python-3.7.1")
        sys("./configure --prefix=/usr/local/python3")
        sys("sudo make install")
    elif version == 2 :
        sys("cd /usr/local/")
        sys("mkdir python3")
        sys("curl -O https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz")
        sys("tar xvf python-3.8.1.tgz")
        sys("cd python-3.8.1")
        sys("./configure --prefix=/usr/local/python3")
        sys("sudo make install")
    elif version == 3 :
        sys("cd /usr/local/")
        sys("mkdir python3")
        sys("curl -O https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz")
        sys("tar xvf python-3.9.1.tgz")
        sys("cd python-3.9.1")
        sys("./configure --prefix=/usr/local/python3")
        sys("sudo make install")
if __name__ == '__main__' :
    main()
    '''
    执行主函数
    '''