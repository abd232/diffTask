import tkinter as tk
from tkinter import Entry
from tkinter import Frame
from tkinter import Label
from tkinter import Text
from tkinter import Button
from tkinter import DISABLED
from tkinter import WORD
from tkinter import Canvas
import os
import Pmw
def init(first_file,second_file,d):
    root = tk.Tk()
    root.resizable(False, False)
    canvas = Canvas()
    v = tk.IntVar()
    root.title("tkdiff")
    frame1 = Frame(root, padx=5, pady=5)
    frame2 = Frame(root, padx=5, pady=5)
    frame1.grid(row=0,column=0)
    frame2.grid(row=0,column=1)

    label1 = Label(frame1, text="File1")
    label2 = Label(frame2, text="File2")
    label1.grid(row=0,column=0)
    label2.grid(row=0,column=0)

    path1 = Entry(frame1, width=45, borderwidth=2)
    path2 = Entry(frame2, width=45, borderwidth=2)
    path1.grid(row=2,column=0)
    path2.grid(row=2, column=0)
    path1.insert(0, os.getcwd()+"/"+first_file)
    path2.insert(0, os.getcwd()+"/"+second_file)
    file_lines1=Pmw.ScrolledText(frame1,borderframe = 1,
         text_width =60, text_height=25,
         hscrollmode ="static",  text_wrap='none' ,vscrollmode="static")
    file_lines1.grid(row=5,column=0)

    file_lines2=Pmw.ScrolledText(frame2,borderframe = 1,
         text_width =60, text_height=25,
         hscrollmode ="static",  text_wrap='none' ,vscrollmode="static")
    file_lines2.grid(row=5,column=0)

    file_lines1.tag_configure('yellow', background='yellow')
    file_lines2.tag_configure('yellow', background='yellow')
    file_lines1.tag_configure('green', background='green')
    file_lines2.tag_configure('green', background='green')
    file_lines1.tag_configure('red', background='red')
    file_lines2.tag_configure('red', background='red')
    file_lines1.tag_configure('blue', background='blue')
    file_lines2.tag_configure('blue', background='blue')
    file_lines1.tag_configure('orange', background='orange')
    file_lines2.tag_configure('orange', background='orange')
    frame3 = Frame(root, padx=5, pady=5)
    frame3.grid(row=1,column=0,columnspan=2)
    label3 = Label(frame3, text="green:same	", fg="green")
    label3.grid(row=1, column=0)
    label4 = Label(frame3, text="yellow:changed	", fg="yellow")
    label4.grid(row=1, column=1)
    label5 = Label(frame3, text="red:deleted	",fg="red")
    label5.grid(row=1,column=2)
    label6 = Label(frame3, text="blue:added	",fg="blue")
    label6.grid(row=1,column=3)
    label7 = Label(frame3, text="orange:chars changed	",fg="orange")
    label7.grid(row=1,column=4)
    try:
        r = next(d)
        no_empty_file = True
    except StopIteration:
        no_empty_file = False
    flag = False
    next_in_r2 = False
    f1_line_counter = 1
    f2_line_counter = 1
    while no_empty_file:
        if r[0] == ' ':
            file_lines1.insert("end", r[2::])
            file_lines1.tag_add("green", ''.join((str(f1_line_counter),".0")), ''.join((str(f1_line_counter+1)
                                                                                                    ,".0")))
            f1_line_counter = f1_line_counter+1
            file_lines2.insert("end", r[2::])
            file_lines2.tag_add("green", ''.join((str(f2_line_counter), ".0")), ''.join((str(f2_line_counter+1), ".0")))
            f2_line_counter = f2_line_counter + 1
            flag = True
        else:
            try:
                if next_in_r2:
                    r1 = r2
                    next_in_r2 = False
                else:
                    r1 = next(d)
                flag = False
                if r1[0] != '?':
                    if r[0] == '-':
                        try:
                            r2 = next(d)
                            next_in_r2 = True
                            if r2[0] == '?':
                                file_lines1.insert("end", r[2::])
                                file_lines1.tag_add("yellow", ''.join((str(f1_line_counter), ".0")),
                                                    ''.join((str(f1_line_counter + 1)
                                                             , ".0")))
                                f1_line_counter = f1_line_counter + 1
                            else:
                                file_lines1.insert("end", r[2::])
                                file_lines1.tag_add("red", ''.join((str(f1_line_counter), ".0")),
                                                    ''.join((str(f1_line_counter + 1)
                                                             , ".0")))
                                f1_line_counter = f1_line_counter + 1
                        except StopIteration:
                            file_lines1.insert("end", r[2::])
                            file_lines1.tag_add("red", ''.join((str(f1_line_counter),".0")), ''.join((str(f1_line_counter+1)
                                                                                                        ,".0")))
                            f1_line_counter = f1_line_counter + 1
                    else:
                        file_lines2.insert("end", r[2::])
                        file_lines2.tag_add("blue", ''.join((str(f2_line_counter), ".0")),
                                            ''.join((str(f2_line_counter+1), ".0")))
                        f2_line_counter = f2_line_counter + 1
                    r = r1
                else:
                    if r[0] == '-':
                        file_lines1.insert("end", r[2::])
                        file_lines1.tag_add("yellow", ''.join((str(f1_line_counter),".0")), ''.join((str(f1_line_counter+1)
                                                                                                    ,".0")))
                        f1_line_counter = f1_line_counter + 1
                    else:
                        file_lines2.insert("end", r[2::])
                        file_lines2.tag_add("yellow", ''.join((str(f2_line_counter), ".0")),
                                            ''.join((str(f2_line_counter+1), ".0")))
                        f2_line_counter = f2_line_counter + 1
                    k=2
                    l=0
                    for i in r1[2::]:
                        k = l
                        if i == '+':
                            if r[0] == '-':
                                file_lines1.tag_add("blue", ''.join((str(f1_line_counter - 1), ".", str(k))),
                                                    ''.join((str(f1_line_counter - 1), ".", str(k + 1))))
                            else:
                                file_lines2.tag_add("blue", ''.join((str(f2_line_counter - 1), ".", str(k))),
                                                    ''.join((str(f2_line_counter - 1), ".", str(k + 1))))
                        if i == '-':
                            if r[0] == '-':
                                file_lines1.tag_add("red", ''.join((str(f1_line_counter - 1), ".", str(k))),
                                                        ''.join((str(f1_line_counter - 1), ".", str(k + 1))))
                            else:
                                file_lines2.tag_add("red", ''.join((str(f2_line_counter - 1), ".", str(k))),
                                                        ''.join((str(f2_line_counter - 1), ".", str(k + 1))))
                        if i == '^':
                            if r[0] == '-':
                                file_lines1.tag_add("orange", ''.join((str(f1_line_counter - 1), ".", str(k))),
                                                        ''.join((str(f1_line_counter - 1), ".", str(k + 1))))
                            else:
                                file_lines2.tag_add("orange", ''.join((str(f2_line_counter - 1), ".", str(k))),
                                                        ''.join((str(f2_line_counter - 1), ".", str(k + 1))))
                        l = l + 1
                    r = next(d)

            except StopIteration:
                break
        if flag:
            try:
                r = next(d)
            except StopIteration:
                break
    root.mainloop()

