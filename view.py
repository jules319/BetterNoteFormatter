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
        main_frame = ttk.Frame(self)
        main_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        # Drag and Drop Area
        self.drop_frame = ttk.Labelframe(main_frame, width=400, height=150)  # Removed the text
        self.drop_frame.grid(row=0, column=0, pady=20, sticky="ew", columnspan=2)
        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_label = ttk.Label(self.drop_frame, text="Drag & Drop PDFs here or")
        self.drop_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.folder_btn = ttk.Button(self.drop_frame, text="Select Folder")
        self.folder_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # Text above the Listbox file queue
        queue_label = ttk.Label(main_frame, text="Files to be processed:")
        queue_label.grid(row=1, column=0, sticky="w", padx=10)

        # Queue Listbox with Scrollbar
        self.queue_frame = ttk.Frame(main_frame)
        self.queue_frame.grid(row=2, column=0, pady=20, sticky="nsew", columnspan=2)
        self.scrollbar = ttk.Scrollbar(self.queue_frame, orient="vertical")
        self.queue_listbox = tk.Listbox(self.queue_frame, yscrollcommand=self.scrollbar.set, height=10, width=50)
        self.scrollbar.config(command=self.queue_listbox.yview)
        self.queue_listbox.grid(row=0, column=0, sticky="ew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.queue_frame.columnconfigure(0, weight=1)

        # Buttons Frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=3, column=0, pady=20, sticky="ew", columnspan=2)
        self.remove_btn = ttk.Button(btn_frame, text="Remove Selected")
        self.remove_btn.pack(side=tk.LEFT, padx=10, pady=5)
        self.clear_btn = ttk.Button(btn_frame, text="Clear Queue")
        self.clear_btn.pack(side=tk.RIGHT, padx=10, pady=5)

        # Output Frame
        output_frame = ttk.Labelframe(main_frame, text= "Output Folder:")
        output_frame.grid(row=4, column=0, pady=20, sticky="ew", columnspan=2)
        self.output_entry = ttk.Entry(output_frame, width=40)
        self.output_entry.grid(row=0, column=1, padx=10, sticky="ew")
        self.output_btn = ttk.Button(output_frame, text="Browse")
        self.output_btn.grid(row=0, column=2, padx=10)

        # Process PDFs button
        self.process_btn = ttk.Button(main_frame, text="Process PDFs")
        self.process_btn.grid(row=5, column=0, columnspan=2, pady=10)

        # Text above Progress bar
        progress_label = ttk.Label(main_frame, text="Processing Files...")
        progress_label.grid(row=6, column=0, columnspan=2, pady=10, sticky="w", padx=10)

        # Progress Bar
        self.progress = ttk.Progressbar(main_frame, orient="horizontal", length=300, mode="determinate")
        self.progress.grid(row=7, column=0, columnspan=2, pady=20, padx=10, sticky="ew")
        main_frame.columnconfigure(0, weight=1)
        output_frame.columnconfigure(1, weight=3)
