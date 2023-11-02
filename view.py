import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD

class PDFProcessorView(TkinterDnD.Tk):

    def __init__(self):
        super().__init__()
        self.title("PDF Processor")
        self.geometry("500x750")  
        self.minsize(500, 750)  
        self._setup_style()
        self._build_ui()

    def _setup_style(self):
        style = ttk.Style(self)
        pass

    def _build_ui(self):
        # Main frame
        self.window = ttk.Frame(self)
        self.window.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        # Drag and Drop Area
        self.drop_frame = ttk.Labelframe(self.window, width=400, height=150)  # Removed the text
        self.drop_frame.grid(row=0, column=0, pady=20, sticky="ew", columnspan=2)
        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_label = ttk.Label(self.drop_frame, text="Drag & Drop PDFs here or")
        self.drop_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.folder_btn = ttk.Button(self.drop_frame, text="Select Folder")
        self.folder_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # Text above the Listbox file queue
        queue_label = ttk.Label(self.window, text="Files to be processed:")
        queue_label.grid(row=1, column=0, sticky="w", padx=10)

        # Queue Listbox with Scrollbar
        self.queue_frame = ttk.Frame(self.window)
        self.queue_frame.grid(row=1, column=0, pady=20, sticky="nsew", columnspan=2)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)

        self.v_scrollbar = ttk.Scrollbar(self.queue_frame, orient="vertical")
        self.h_scrollbar = ttk.Scrollbar(self.queue_frame, orient="horizontal")

        self.queue_listbox = tk.Listbox(self.queue_frame, yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set, height=10, width=50, selectmode=tk.MULTIPLE)
        
        self.v_scrollbar.config(command=self.queue_listbox.yview)
        self.h_scrollbar.config(command=self.queue_listbox.xview)

        self.queue_listbox.grid(row=0, column=0, sticky="nsew")
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")
        self.h_scrollbar.grid(row=1, column=0, sticky="ew")

        self.queue_frame.columnconfigure(0, weight=1)
        self.queue_frame.rowconfigure(0, weight=1)  # ensure Listbox expands vertically


        # Buttons Frame
        btn_frame = ttk.Frame(self.window)
        btn_frame.grid(row=3, column=0, pady=20, sticky="ew", columnspan=2)
        self.remove_btn = ttk.Button(btn_frame, text="Remove Selected")
        self.remove_btn.pack(side=tk.LEFT, padx=10, pady=5)
        self.clear_btn = ttk.Button(btn_frame, text="Clear Queue")
        self.clear_btn.pack(side=tk.RIGHT, padx=10, pady=5)

        # Output Frame
        output_frame = ttk.Labelframe(self.window, text= "Output Folder:")
        output_frame.grid(row=4, column=0, pady=20, sticky="ew", columnspan=2)
        self.output_entry = ttk.Entry(output_frame, width=40)
        self.output_entry.grid(row=0, column=1, padx=10, sticky="ew")
        self.output_btn = ttk.Button(output_frame, text="Browse")
        self.output_btn.grid(row=0, column=2, padx=10)

        # Process PDFs button
        self.process_btn = ttk.Button(self.window, text="Process PDFs")
        self.process_btn.grid(row=5, column=0, columnspan=2, pady=10)

    def create_processing_overlay(self, cancel_command):
        self.overlay = tk.Toplevel(self)
        self.overlay.title("Processing")
        self.overlay.geometry("300x150")
        self.overlay.resizable(False, False)

        # Progress bar
        self.overlay.progress_bar = ttk.Progressbar(self.overlay, mode='indeterminate')
        self.overlay.progress_bar.pack(pady=20, padx=20)

        # Status label
        self.overlay.status_label = ttk.Label(self.overlay, text="Processing files...")
        self.overlay.status_label.pack()

        # Cancel button
        self.overlay.cancel_btn = ttk.Button(self.overlay, text="Cancel", command=cancel_command)
        self.overlay.cancel_btn.pack(pady=10)


    def show_completion_message(self, ok_command):
        # Clear all widgets from the overlay
        for widget in self.overlay.winfo_children():
            widget.destroy()

        # Completion label
        self.overlay.completion_label = ttk.Label(self.overlay, text="Processing Completed!")
        self.overlay.completion_label.pack(pady=20)

        # OK button
        self.overlay.ok_button = ttk.Button(self.overlay, text="OK", command=ok_command)
        self.overlay.ok_button.pack(pady=10)

