import os
 
def geturlPath():
    # 指定路径
    path = r'KawaiiChino.github.io\Gallery\img'
    # 返回指定路径的文件夹名称
    dirs = os.listdir(path)
    # 循环遍历该目录下的照片
    for dir in dirs:
        # 拼接字符串
        pa = './img/'+dir
        # 判断是否为照片
        if not os.path.isdir(pa):
            # 使用生成器循环输出
            yield pa
 
 
if __name__ == '__main__':
    for item in geturlPath():
        print("<div class=\"col-sm-6 col-md-3\">")
        print("<a href=\""+item+"\" class=\"thumbnail\">")
        print("<img src=\""+item+"\" alt=\""+item+"\">")
        print("</a>\n</div>")