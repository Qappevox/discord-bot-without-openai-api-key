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

html = """
<div class="relative flex w-[calc(100%-50px)] flex-col gap-1 md:gap-3 lg:w-[calc(100%-115px)]"><div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start gap-4 whitespace-pre-wrap"><div class="markdown prose w-full break-words dark:prose-invert light"><p>Tabii, işte Python'da "Hello World!" yazdırmak için kullanabileceğiniz basit bir kod:</p><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python"><span class="hljs-built_in">print</span>(<span class="hljs-string">"Hello World!"</span>)
</code></div></div></pre><p>Bu kodu çalıştırdığınızda, Python konsolunda "Hello World!" yazısı görünecektir.</p></div></div></div><div class="flex justify-between lg:block"><div class="text-gray-400 flex self-end lg:self-center justify-center mt-2 gap-2 md:gap-3 lg:gap-1 lg:absolute lg:top-0 lg:translate-x-full lg:right-0 lg:mt-0 lg:pl-2 visible"><button class="p-1 rounded-md hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200 disabled:dark:hover:text-gray-400"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg></button><button class="p-1 rounded-md hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200 disabled:dark:hover:text-gray-400"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"></path></svg></button></div></div></div>
"""
code_parser(html)

def run():
    close_browser()
    open_browser()
    open_gpt()
    ask_gpt()
    time.sleep(20)
    get_to_answer()
    write_copy()
    time.sleep(3)

