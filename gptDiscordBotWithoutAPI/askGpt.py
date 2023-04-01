import pyautogui as pg
import time
import apiManager
import pyautogui as pg 
import time
from colorama import Style, Fore
import re

def log():
    while True:
        time.sleep(0.3)
        print(pg.position())
        #browser pos: x= 963, y = 1057
        #browser exit pos: x = 1895, y= 14
        #gpt chatbox pos: x = 722, y = 956

def close_browser():
    time.sleep(2)
    pg.moveTo(963, 1057, 0.01)
    pg.click()
    pg.moveTo(1895, 14, 0.1)#browser exit pos: x = 1895, y= 14
    pg.click()
    

def open_browser():
    pg.moveTo(955, 1057, 0.01)#browser pos: x= 963, y = 1057
    pg.click()
    time.sleep(2)

def open_gpt():
    pg.write("https://chat.openai.com/chat")
    pg.press("Enter")
    time.sleep(3)
    pg.moveTo(722, 956, 0.1)#gpt chatbox pos: x = 722, y = 956
    pg.click()



def ask_gpt():
    question = apiManager.getter("question")
    time.sleep(0.5)
    pg.write(question)
    pg.press("Enter")

def write_to_text():
    pg.moveTo(1314, 1058, 0.3)
    pg.click()
    pg.moveTo(111,345)
    pg.click()
    pg.moveTo(623, 289)
    pg.click()
    pg.hotkey("ctrl", "v")
    pg.hotkey("ctrl", "s")


def get_to_answer():
    
    pg.moveTo(1535, 200)
    pg.scroll(-720)
    time.sleep(0.1)
    pg.rightClick()
    pg.moveTo(1598, 769, 0.3)
    pg.click()
    pg.moveTo(1416, 370, 0.3)
    time.sleep(0.5)
    pg.click()
    pg.moveTo(1427, 413, 0.3)
    time.sleep(0.5)
    pg.click()
    pg.moveTo(1438, 458)
    pg.rightClick()
    pg.moveTo(1509, 644, 0.2)
    pg.click()
    pg.moveTo(1746, 643, 0.2)
    pg.click()
    write_to_text()
    

def write_copy():
    with open("copy.txt", "r", encoding="utf-8") as f:
        ans = f.read()
        ans = parser(html=ans, data="<p>", attr="", tale= "</p")
        apiManager.setter("answer", ans)
        print("checkpoint")
        f.close()
    with open("copy.txt", "w") as f:
        f.write("")
        f.close()

def code_parser(html):
    if "<code" in html:
        print("code in html")

    print("excepted error.")
    span = re.search('<code class="!whitespace-pre hljs language-',html)
    span = span.span()[0]
    span2 = re.search("</code>", html)
    span2 = span2.span()[0]
    html = html[span:span2]
    
    tags = ["</span", '<span class="hljs-built_in"','<span class="hljs-string"', '>','<span class="hljs-variable language_"' ,'<span class="hljs-title function_"', '<code class="!whitespace-pre hljs language-' ]
    for tag in tags:
        html = html.replace(tag, "")
    html = html.replace('<span class="hljs-built_in"', "")
    html = html.replace('</span>', "")
    html = html.replace('<span class="hljs-string"', "")
    html = html.replace('>', "")
    html = html.replace('<code class="!whitespace-pre hljs language-','')
    span3 = re.search('"', html)
    span3 = span3.span()[1]
    html = html[span3:]
    print(html)
    return html

def parser(html, data, attr, tale):
    #debug
    if "<code" in html:
        return code_parser(html)
    print("function name --> parser")
    value = ""
    return_value = []
    tag_list = []
    tmp_start = html
    tmp_end = html
    for_loop = re.findall(data, tmp_start)
    for i in range(len(for_loop)):
        src_start = re.search(data, tmp_start)
        tmp_start = tmp_start[src_start.span()[1]:]
        tmp_end = tmp_start.split("<")
        tmp_end = tmp_end[0]
        tag_list.append(tmp_end)
    #print(tag_list)
    for tag in tag_list:
        tmp_head = tag.find(attr)
        tag = tag[tmp_head:]
        tag = tag.replace(tale, "")
        print(f"{Fore.LIGHTRED_EX}    parser log --> {Style.RESET_ALL}{tag}")
        print(tag)
        return_value.append(tag)
    for val in return_value:
        value = value + val + "\n"
    print(value)
    return value

def run():
    close_browser()
    open_browser()
    open_gpt()
    ask_gpt()
    time.sleep(20)
    get_to_answer()
    write_copy()
    time.sleep(3)

