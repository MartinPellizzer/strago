from tkinter import *
import pyperclip

from urllib.request import urlopen
from bs4 import BeautifulSoup
from googlesearch import search

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


keyword = "subtle workplace bullying"
title = "Exposing Subtle Workplace Bullying: 27 Signs To Watch Out"

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
        write a 200 words or less blog post section about {content}",
        write the first sentence as a though-provoking one-liner,
        add 3-5 examples in list format,
        do NOT repeat yourself and add synonyms when it makes sense,
        use an engaging and casual style of writing
        use an angry and frustrated tone of voice,
        make it relatable to the employees,
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

root.mainloop()