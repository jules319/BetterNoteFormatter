import tkinter as tk
# from pdf_processor import PDFProcessor
# import PyPDF2

# input_pdf_path = "/Users/juliancolbert/Desktop/temp/14_C_Arrays_Pointers.pdf"

# with open(input_pdf_path, 'rb') as f:
#     reader = PyPDF2.PdfReader(f)
#     writer = PyPDF2.PdfWriter()
#     mbox = reader.pages[0].mediabox
#     for page_num in range(len(reader.pages)):
#         # Extract each page
#         page = reader.pages[page_num]
#         is_portrait = PDFProcessor.check_page_is_portrait(page)
#         print(f"Page {page_num}: width {mbox.width}, height {mbox.height} deg {page.get('/Rotate')}, is_portrait {is_portrait}")


# def create_new_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("New Window")
    
#     frame = tk.Frame(new_window)
#     frame.pack()
    
#     tk.Label(frame, text="Label in New Window").grid(row=0, column=0)
#     tk.Button(frame, text="Button in New Window").grid(row=1, column=0)

# root = tk.Tk()
# root.title("Main Window")

# frame_main = tk.Frame(root)
# frame_main.pack()

# tk.Label(frame_main, text="Label in Main Window").pack()
# tk.Button(frame_main, text="Open New Window", command=create_new_window).pack()

# root.mainloop()

# class MyApp(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Multi-page App")
#         self.geometry("400x300")
        
#         self.frames = {}
#         for F in (HomePage, PageOne):
#             frame = F(self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame(HomePage)

#     def show_frame(self, page):
#         frame = self.frames[page]
#         frame.tkraise()

# class HomePage(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.create_widgets()

#     def create_widgets(self):
#         self.label = tk.Label(self, text="Home Page")
#         self.label.pack()

#         self.button = tk.Button(self, text="Go to Page One", command=lambda: self.master.show_frame(PageOne))
#         self.button.pack()

# class PageOne(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.create_widgets()

#     def create_widgets(self):
#         self.label = tk.Label(self, text="Page One")
#         self.label.pack()

#         self.button = tk.Button(self, text="Go Back Home", command=lambda: self.master.show_frame(HomePage))
#         self.button.pack()

# app = MyApp()
# app.mainloop()

def on_entry_change(*args):
    label_text.set(f"Hello, {name_var.get()}")

root = tk.Tk()

# Creating and setting up StringVar
name_var = tk.StringVar()
name_var.trace_add('write', on_entry_change)  # Tracing changes in the Entry widget

# Creating and setting up Entry widget
entry = tk.Entry(root, textvariable=name_var)  # Associating Entry with StringVar
entry.pack()
entry.insert(0, "Enter your name")  # Default text

# Creating and setting up Label
label_text = tk.StringVar()
label = tk.Label(root, textvariable=label_text)  # Associating Label with StringVar
label.pack()

root.mainloop()
