import tkinter as tk
from tkinter import *
import sqlite3

conn = sqlite3.connect('test3.db')

def select_specific_info(conn,tagName,similarTag,outputType):
    searchTerm = ""
    similarTerm = ""
    print("tag type is {}".format(tagName))
    print("similar tag is {}".format(similarTag))
    print("output type is {}".format(outputType))
    if "good" in tagName:
        searchTerm += "goodTag"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "improve" in tagName:
        searchTerm += "improvedTag"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "simi" in tagName:
        searchTerm += "similarTag"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "loc" in tagName:
        searchTerm += "locationTag"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "feel" in tagName:
        searchTerm += "feelTag"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "id" in tagName:
        searchTerm += "id="
        similarTerm += similarTag

    outputTag = "" 
    if "id" in outputType:
        outputTag = "id"
    elif "stor" in outputType:
       outputTag = "story"
    elif "all" in outputType:
        outputTag = "*"
    elif "sim" in outputType:
        outputTag = "similarTag"
    elif "good" in outputType:
        outputTag = "goodTag"
    elif "loc" in outputType:
        outputTag = "locationTag"
    elif "feel" in outputType:
        outputTag = "feelTag"

    #TODO does not recognise id because it is a number not string
    cur = conn.cursor()
    cur.execute("SELECT {} FROM Review WHERE {} {}".format(outputTag,searchTerm,similarTerm))
    print("SELECT {} FROM Review WHERE {}{}".format(outputTag,searchTerm,similarTerm))
    # cur.execute("SELECT story FROM Review WHERE id=61079".format(outputTag,searchTerm,similarTerm))
    allTag = cur.fetchall()
    for tag in allTag:
        print(allTag)
    return allTag

def search():
    info = select_specific_info(conn,tag_text.get(),spec_text.get(),output_text.get())
    for i in info:
        search_results.insert(END,i)
    print(info)

def clear_search_res():
    search_results.delete(0,END)

def main():
    global spec_text
    global output_text
    global tag_text
    global search_results
    win = tk.Tk()

    DataTypes = [
        "id",
        "story",
        "time Posted",
        "good Tag" ,
        "similar Tag",
        "improved Tag",
        "response Tag",
        "feel Tag",
        "location Tag"
    ]

    #Part title
    part_label = tk.Label
    win.title("DB search")
    win.geometry('700x700')
    # title_label = tk.Label(win,text = "Welcome! Use this to search for reviews in the databse:", font=('bold',10),pady=20,padx=100)
    # title_label.grid()

    #tag label e.g improve,bad,location ect
    tag_text = tk.StringVar()
    tag_text.set(DataTypes[3])
    tag_label = tk.Label(win,text = "Enter Search Tag:", font=('bold',10))
    tag_label.grid(row=1, column=0, sticky=tk.W)
    input_tag = tk.OptionMenu(win,tag_text,*DataTypes)
    input_tag.grid(row=1,column=1)

    #specific search e.g nurse, food, doctors
   
    spec_text = tk.StringVar()
    spec_label = tk.Label(win,text = "Enter Specific Tag:", font=('bold',10))
    spec_label.grid(row=2, column=0, sticky=tk.W)
    input_spec = tk.Entry(win,textvariable=spec_text)
    input_spec.grid(row=2,column=1)

    #which output they would like id,rev
    output_text = tk.StringVar()
    output_text.set(DataTypes[0])
    output_label = tk.Label(win,text = "Enter Output type:", font=('bold',10))
    output_label.grid(row=3, column=0, sticky=tk.W)
    input_output = tk.OptionMenu(win,output_text,*DataTypes)
    input_output.grid(row=3,column=1)

    # Listbox that will show reviewed
    search_results = Listbox(win, height=8, width=50, border=0)
    search_results.grid(row=10, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
    # Create scrollbar
    scrollbar = Scrollbar(win,orient='vertical',command=search_results.yview)
    scrollbar.grid(row=8, column=3,sticky='ns')
    search_results['yscrollcommand'] = scrollbar.set


    scrollbar2 = Scrollbar(win,orient='horizontal',command=search_results.xview)
    scrollbar2.grid(row=15, column=1,sticky='ew')
    # Set scroll to listbox
    # search_results.configure(yscrollcommand=scrollbar.set)
    search_results.configure(xscrollcommand=scrollbar2.set)


    #buttons
    search_but = tk.Button(win,text='Search', width=12,command=search)
    search_but.grid(row=4,column=2)
    #clear
    clear_but = tk.Button(win,text='Clear', width=12,command=clear_search_res)
    clear_but.grid(row=4,column=3)
    # canvas1.create_window(200, 140, window=entry1)
    win.mainloop()
    #In cmd run pyinstaller graphics1.py to get an application

if __name__ == '__main__':
    main()