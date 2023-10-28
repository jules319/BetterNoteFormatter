# view.py

import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
# Import other necessary modules and methods...

class PDFView:
    def __init__(self, controller, root):
        self.controller = controller
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        # Drag and Drop Area
        self.drop_frame = tk.Frame(self.root, width=400, height=200, bd=2, relief="ridge")
        self.drop_frame.pack(pady=20)
        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind('<<Drop>>', self.controller.on_drop)
        self.drop_label = tk.Label(self.drop_frame, text="Drag & Drop PDFs here or Select a Folder")
        self.drop_label.pack(pady=80)

        # Queue Listbox with Scrollbar
        self.queue_frame = tk.Frame(self.root)
        self.queue_frame.pack(pady=20)

        self.scrollbar = tk.Scrollbar(self.queue_frame, orient="vertical")
        self.queue_listbox = tk.Listbox(self.queue_frame, yscrollcommand=self.scrollbar.set, height=10, width=50)
        self.scrollbar.config(command=self.queue_listbox.yview)

        self.queue_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Process Button
        self.process_btn = tk.Button(self.root, text="Process PDFs", command=self.controller.process_files)
        self.process_btn.pack(pady=20)

        # Folder Selection Button
        self.folder_btn = tk.Button(self.root, text="Select Folder", command=self.controller.process_folder)
        self.folder_btn.pack(pady=20)

        # Clear Queue Button
        self.clear_btn = tk.Button(self.root, text="Clear Queue", command=self.controller.clear_queue)
        self.clear_btn.pack(pady=20)

        # Status Label
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack(pady=20)

    def update_queue(self, pdf_queue):
        self.queue_listbox.delete(0, tk.END)  # Clear the listbox
        for file in pdf_queue:
            self.queue_listbox.insert(tk.END, file)

    def set_status(self, text):
        self.status_label.config(text=text)

