import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
from pdf_processor import PDFProcessor

def on_drop(event):
    file_path = event.data
    if file_path.endswith('.pdf'):
        file_name = os.path.basename(file_path)
        full_paths[file_name] = file_path
        pdf_queue.add(file_name)
        update_queue()

def update_queue():
    queue_listbox.delete(0, tk.END)  # Clear the listbox
    for file in pdf_queue:
        queue_listbox.insert(tk.END, file)

def clear_queue():
    pdf_queue.clear()
    update_queue()

def process_files():
    process_btn.config(state=tk.DISABLED)  # Disable the button during processing
    status_label.config(text="Processing...")  # Update the status label
    
    for file_name in pdf_queue:
        input_path = full_paths[file_name]
        output_file = os.path.splitext(input_path)[0] + "_modified.pdf"
        
        error = PDFProcessor.add_whitespace(input_path, output_file)
        if error:
            status_label.config(text=f"Error: {error}")
            process_btn.config(state=tk.NORMAL)  # Re-enable the button
            return
    
    clear_queue()
    status_label.config(text="All PDFs processed successfully!")
    tk.messagebox.showinfo("Done", "All PDFs processed successfully!")
    process_btn.config(state=tk.NORMAL)  # Re-enable the button

def process_folder():
    folder_path = tk.filedialog.askdirectory(title="Select Folder")
    if folder_path:
        for file in os.listdir(folder_path):
            if file.endswith('.pdf'):
                full_path = os.path.join(folder_path, file)
                full_paths[file] = full_path
                pdf_queue.add(file)
        update_queue()


root = TkinterDnD.Tk()
root.title("PDF Processor")

pdf_queue = set()  # Using a set to prevent duplicates
full_paths = {}

# Drag and Drop Area
drop_frame = tk.Frame(root, width=400, height=200, bd=2, relief="ridge")
drop_frame.pack(pady=20)
drop_frame.drop_target_register(DND_FILES)
drop_frame.dnd_bind('<<Drop>>', on_drop)
drop_label = tk.Label(drop_frame, text="Drag & Drop PDFs here or Select a Folder")
drop_label.pack(pady=80)

# Queue Label
# Queue Listbox with Scrollbar
queue_frame = tk.Frame(root)
queue_frame.pack(pady=20)

scrollbar = tk.Scrollbar(queue_frame, orient="vertical")
queue_listbox = tk.Listbox(queue_frame, yscrollcommand=scrollbar.set, height=10,\
                           width=50)
scrollbar.config(command=queue_listbox.yview)

queue_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Process Button
process_btn = tk.Button(root, text="Process PDFs", command=process_files)
process_btn.pack(pady=20)

# Folder Selection Button
folder_btn = tk.Button(root, text="Select Folder", command=process_folder)
folder_btn.pack(pady=20)

# Clear Queue Button
clear_btn = tk.Button(root, text="Clear Queue", command=clear_queue)
clear_btn.pack(pady=20)

# Status Label
status_label = tk.Label(root, text="")
status_label.pack(pady=20)

root.mainloop()
