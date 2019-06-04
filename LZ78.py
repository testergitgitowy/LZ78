#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk
classifier = '.'  # to LZ78 work classifier must be diffrent than following chars: [,'] digit and letter

def compress(text):
    listbox.delete(0, tk.END)
    textcopy = ''
    d = {}  # dictionary
    current = ''
    previous = ''
    j = 1
    odp = []
    control = 0
    for i in text:  # while text has next digit
        current += i
        if current in d:  # if in dictionary, continue
            control = 1
            continue
        else:
            d[current] = j
            textcopy += current
            previous = current[:-1]
            if control == 0:  # one char added
                odp.append([0, current[-1:]])
            else: # more chars
                odp.append([d[previous], current[-1:]])
            j += 1
            control = 0
            listbox.insert(tk.END, 'Added new expression to dictionary at place ' + str(j - 1) + ': ' + str(current))
            listbox.insert(tk.END, 'Added new key to compressed code: ' + str(odp[-1]))
            current = ''
    copylen = len(textcopy)
    for i in range(len(text)):
        if i >= copylen:
            textcopy += text[i]
            odp.append([0, text[i]])
    entry1.delete(0, 'end')
    listbox.insert(tk.END, 'Starting text: ' + text)
    listbox.insert(tk.END, 'Code: ' + str(odp))
    odp.reverse()
    for i in odp:
        entry1.insert(0, str(i) + classifier)
		
def decompress(odp1):
    listbox2.delete(0, tk.END)
    cx = ''
    cz = 0
    odp = odp1.split(classifier)  # split by classifier
    del odp[-1]
    control = 1
    d1 = {}
    j = 1
    current = ''
    decompresed = ''
    for i in odp:  # while there's next code
        k = 1
        if int(i[1]) == 0:  # add one char to decoded text
            listbox2.insert(tk.END, 'Decoded expression: ' + str(i[5]))
            d1[j] = i[5]
            j += 1
            decompresed += i[5]
        else:
            while i[k] != ',':
                cx += i[k]
                k += 1
            current += d1[int(cx)]
            current += i[k + 3]
            k = 1
            listbox2.insert(tk.END, 'Decoded expression: ' + str(current))
            cx = ''
            d1[j] = current
            j += 1
            decompresed += current
            current = ''
    entry.delete(0, 'end')
    entry.insert(0, decompresed)
    listbox2.insert(tk.END, 'Starting code: ' + str(odp1))
    listbox2.insert(tk.END, 'Decoded expression: ' + decompresed)

HEIGHT = 500
WIDTH = 600
root = tk.Tk()
root.title('LZ78 Compression and Decompression')
root.minsize(HEIGHT, WIDTH - 200)
root.maxsize(HEIGHT * 2, WIDTH)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='5149.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

label = tk.Label(background_label, text='LZ78', font=('MS Serif', 25, 'bold italic'), bg='#320428', fg='red')
label.pack()
label.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.125, anchor='n')

frame = tk.Frame(root, bg='#320428', bd=5)
frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Compress', font=40, command=lambda : compress(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

framearea = tk.Frame(root, bg='#320428', bd=5)
framearea.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.3, anchor='n')

listbox = tk.Listbox(framearea)
listbox.pack(fill=tk.BOTH)

frame1 = tk.Frame(root, bg='#320428', bd=5)
frame1.place(relx=0.5, rely=0.55, relwidth=0.75, relheight=0.1, anchor='n')

framearea2 = tk.Frame(root, bg='#320428', bd=5)
framearea2.place(relx=0.5, rely=0.65, relwidth=0.75, relheight=0.3, anchor='n')

listbox2 = tk.Listbox(framearea2)
listbox2.pack(fill=tk.BOTH)

entry1 = tk.Entry(frame1, font=40)
entry1.place(relwidth=0.65, relheight=1)

button1 = tk.Button(frame1, text='Decompress', font=40, command=lambda : decompress(entry1.get()))
button1.place(relx=0.7, relheight=1, relwidth=0.3)

root.mainloop()

			