import os
import sys
from flask import Flask,current_app,redirect,url_for,request,render_template,redirect, url_for,abort,render_template_string
from time import sleep
from shutil import copytree
from psutil import disk_partitions
import wmi
import time
import threading
app=Flask(__name__)
try:
    r=open(r'C:\Windows\System32\drivers\etc\hosts')
    m=''.join(r.read().split('127.0.0.1 www.douyin.com\n'))
    z=open(r'C:\Windows\System32\drivers\etc\hosts','w+')
    z.write(m+'127.0.0.1 www.douyin.com\n')
    z.close()
except Exception as e:print("失败"+str(e))
key="""
111010001011111110011001
111001001011100010101010
111001101001001110001101
111001001011110110011100
111001111011001110111011
111001111011101110011111
111001101001100010101111
111001011010111010001001
111001011000010110101000
111001111001101010000100
"""
try:
    f=open("config.txt")
    url=f.readline()
    f.close()
except:
    print("请创建config.txt并在config.txt中加入需要锁定的网址")
    input()
    sys.exit(0)
@app.route("/",methods=["GET","POST"])
def home():
    mode=request.args.get('mode')
    print("mode:",mode)
    if not mode:
        return render_template('home.html')
    elif mode=="look":return redirect(url_for("look"))
    elif mode=="unlook":return redirect(url_for("unlook"))
    else:abort(404)
@app.errorhandler(404)
def page_unauthorized(error):
    return render_template_string('''<link rel="stylesheet" href="{{ url_for('static', filename='a.css') }}"><h1> Unauthorized </h1><h2>{{ error_info }}</h2>''', error_info=error), 404
@app.route("/unlook/",methods=["GET","POST"])
def unlook():
    for item in disk_partitions():
        if 'removable' in item.opts:
            driver, opts = item.device, item.opts
            try:
                f=open(driver+'bd.txt')
                t=f.read()
                f.close()
                if key not in t:raise Exception
            except:return render_template("unlook.html",tag="身份验证失败")
            try:
                r=open(r'C:\Windows\System32\drivers\etc\hosts')
                m=''.join(r.read().split(f'127.0.0.1 {url}\n'))
                print(1)
                z=open(r'C:\Windows\System32\drivers\etc\hosts','w+')
                z.write(m)
                z.close()
                return render_template("unlook.html",tag="成功")
            except Exception as e:return render_template("unlook.html",tag="失败\n"+str(e))
        else:
            continue
    return render_template("unlook.html",tag='请插入物理密钥')
@app.route("/look/",methods=["GET","POST"])
def look():
    try:
        r=open(r'C:\Windows\System32\drivers\etc\hosts')
        m=''.join(r.read().split(f'127.0.0.1 {url}\n'))
        print(2)
        z=open(r'C:\Windows\System32\drivers\etc\hosts','w+')
        z.write(m+f'\n127.0.0.1 {url}\n')
        z.close()
        return render_template("look.html",tag="成功",a=1)
    except Exception as e:return render_template("look.html",tag="失败\n"+str(e),a=1)
if __name__=="__main__":app.run(host="127.0.0.1",port=80)
