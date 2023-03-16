from tkinter import *
import pyperclip

from urllib.request import urlopen
from bs4 import BeautifulSoup
from googlesearch import search

import random
import os
import shutil


keyword = "subtle workplace bullying"
title = "Exposing Subtle Workplace Bullying: 27 Signs To Watch Out"




def scrape_headers():
    keyword = e1.get()
    urls = [url for url in search(keyword, tld="co.in", num=10, stop=10, pause=2)]

    for url in urls:
        try: html = urlopen(url)
        except: continue
        soup = BeautifulSoup(html, "html.parser")
        titles = soup.find_all(['h1', 'h2','h3','h4','h5','h6'])

        for title in titles:
            s = ''
            for content in title.contents:
                soup = BeautifulSoup(str(content), "html.parser")
                s += str(soup.text.strip())
            print(title.name + ' ' + s.strip())

        print('\n\n\n')



def click():
    keyword = e1.get()
    prompt = ''
    if prompt_type.get() == 1:
        prompt = f'write 10 blog post titles for this keyword "{keyword}"'
    elif prompt_type.get() == 2:
        prompt = f'write 10 blog post titles for this keyword "{keyword}"'
    elif prompt_type.get() == 3:
        prompt = f'write an outline for a blog post with this title "{keyword}"'
    print(prompt)
    pyperclip.copy(prompt)

    
def generate_list():
    content = list_entry.get()
    prompt = f'''
            write a crazy big, huge, and exhaustive list of "{content}",
            do NOT repeat yourself, 
        '''
    print(prompt)
    pyperclip.copy(prompt)


def generate_section():
    content = section_entry.get()
    prompt = f'''
            rewrite the content above so that it is not detected as AI content by AI content detectors
        '''
    prompt = f'''
        DELETE PREVIOUS CONVERSATIONS,
        write a 200 words or less blog post section about {content},
        use very short paragraphs,
        add examples in unordered list,
        add actionable advice in unordered list,
        conclude with a blast,
        do NOT repeat yourself,
        use an engaging and casual style of writing,
        be angry, frustrated, and empathic,
        write in active form and refer to the reader as you,
        '''
    print(prompt)
    pyperclip.copy(prompt)


root = Tk()

f1 = LabelFrame(root, text='General', padx=10, pady=10)
f1.pack(padx=10, pady=10)
f3 = LabelFrame(root, text='Type', padx=10, pady=10)
f3.pack(padx=10, pady=10)
f2 = LabelFrame(root, text='Prompt', padx=10, pady=10)
f2.pack(padx=10, pady=10)


list_frame = LabelFrame(root, text='List', padx=10, pady=10)
list_frame.pack(padx=10, pady=10)
list_entry = Entry(list_frame, width=60)
list_entry.pack()
list_button = Button(list_frame, text="Generate Prompt", command=generate_list)
list_button.pack()




section_frame = LabelFrame(root, text='Section', padx=10, pady=10)
section_frame.pack(padx=10, pady=10)
section_entry = Entry(section_frame, width=60)
section_entry.pack()
section_button = Button(section_frame, text="Generate Prompt", command=generate_section)
section_button.pack()




f4 = LabelFrame(root, text='Scraper', padx=10, pady=10)
f4.pack(padx=10, pady=10)
scraper_button = Button(f4, text="Scrape Headers", command=scrape_headers)
scraper_button.pack()



l1 = Label(f1, text="Keyword")
l1.pack()
e1 = Entry(f1, width=60)
e1.pack()
e1.insert(0, keyword)

title_label = Label(f1, text="Title")
title_label.pack()
title_entry = Entry(f1, width=60)
title_entry.pack()
title_entry.insert(0, title)

b1 = Button(f2, text="Generate Prompt", command=click)
b1.pack()
# l1.grid(row=0, column=0)
# e1.grid(row=1, column=0)
# b1.grid(row=0, column=1)
prompt_type = IntVar()
prompt_type.set(1)
r1 = Radiobutton(f3, text='Title', variable=prompt_type, value=1)
r1.pack()
r2 = Radiobutton(f3, text='Intro', variable=prompt_type, value=2)
r2.pack()
outline_radio = Radiobutton(f3, text='Outline', variable=prompt_type, value=3)
outline_radio.pack()





def md_to_html():
    keyword_dashed = keyword.replace(' ', '-')
    if not os.path.exists(f'./article/assets/{keyword_dashed}'): 
        os.makedirs(f'./article/assets/{keyword_dashed}')

    with open('article.md') as f: lines = f.readlines()

    html = ''
    is_ul = False
    i = 1
    added_toc = False
    k = 1
    for line in lines:
        line = line.strip()
        if not line: pass
        elif line.strip() == '@ stop':
            break
        elif line.startswith('### '):
            line = line.replace('### ', '')
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<h3 id="{k}">{i}. {line}</h3>'
            i += 1
            k += 1
        elif line.startswith('## '):
            if not added_toc:
                added_toc = True
                html += '[insert-toc-here]'
            line = line.replace('## ', '')
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<h2 id="{k}">{line}</h2>'
            k += 1
            if 'conclusion' not in line.lower():
                images = [x for x in os.listdir(f'./article/assets/{keyword_dashed}')]
                line_formatted = line.lower().strip()
                if line_formatted[0].isdigit() and line_formatted[1] == '.':
                    line_formatted = line_formatted[2:].strip()    
                img_src = line_formatted.replace(' ', '-') + '.jpg'
                if img_src not in images:
                    random_image = random.choice(os.listdir(f'F:/images/768x512-good/'))
                    shutil.copy2(f'F:/images/768x512-good/{random_image}', f'./article/assets/{keyword_dashed}/{img_src}')
                html += f'<img class="post-img" alt="{line}" title="{line}" src="./assets/{keyword_dashed}/{img_src}" />'
        elif line.startswith('# '):
            line = line.replace('# ', '')
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<h1>{line}</h1>'
            keyword_formatted = keyword.strip().replace(' ', '-') + '.jpg'
            # html += f'<img class="post-img" alt="{keyword}" title="{keyword}" src="./assets/{keyword_dashed}/{img_src}" />'
        elif line.startswith('- '):
            line = line.replace('- ', '')
            if not is_ul:
                html += f'<ul>'
                is_ul = True
            html += f'<li>{line}</li>'
        else:
            if is_ul:
                html += f'</ul>'
                is_ul = False
            html += f'<p>{line}</p>'

    toc = ''
    toc += f'<div class="toc">'
    toc += f'<p><strong>Table of Contents</strong></p>'
    toc += f'<ul>'
    new_subsection = False
    i = 1
    k = 1
    for line in lines:
        if 0: pass
        elif line.startswith('### '):
            line = line.replace('### ', '')
            if not new_subsection:
                new_subsection = True
                toc += f'<ul>'
            toc += f'<li><a href="#{i}">{k}. {line}</a></li>'
            i += 1
            k += 1
        elif line.startswith('## '):
            if new_subsection:
                new_subsection = False
                toc += f'</ul>'
            line = line.replace('## ', '')
            toc += f'<li><a href="#{i}">{line}</a></li>'
            i += 1
    toc += f'</ul>'
    toc += f'</div>'
    
    html = html.replace('[insert-toc-here]', toc)

    keyword_formatted = keyword.strip().replace(' ', '-')
    with open(f'article/content.html', 'w') as f: f.write(html)


html_button = Button(root, text="MD to HTML", command=md_to_html)
html_button.pack()



root.mainloop()