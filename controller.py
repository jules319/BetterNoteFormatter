from pdf_processor import PDFProcessor
import os
import tkinter as tk
from tkinter import filedialog

class PDFProcessorController:

    def __init__(self, view):
        self.view = view
        self.pdf_queue = set()
        self.full_paths = {}

        # Connecting the widgets to their respective methods
        # self.view.drop_frame.dnd_bind('<<Drop>>', self.on_drop)
        # self.view.folder_btn.config(command=self.process_folder)

        # self.view.clear_btn.config(command=self.clear_queue)
        # self.view.remove_btn.config(command=self.remove_selected)

        # self.view.output_btn.config(command=self.browse_output_folder)
        # self.view.process_btn.config(command=self.process_files)

    # This method will handle the dropped files into the application
    def files_or_folders_on_drop(self, event):
        data = event.data.strip().split()  # Getting the list of files/folders dropped
        for datum in data:
            if os.path.isfile(datum):  # If it's a file, add directly
                self.pdf_queue.add(datum)
                self.view.queue_listbox.insert(tk.END, os.path.basename(datum))
                self.full_paths[os.path.basename(datum)] = datum
            elif os.path.isdir(datum):  # If it's a directory, add all PDF files in it
                for root, dirs, files in os.walk(datum):
                    for file in files:
                        if file.endswith(".pdf"):
                            filepath = os.path.join(root, file)
                            self.pdf_queue.add(filepath)
                            self.view.queue_listbox.insert(tk.END, file)
                            self.full_paths[file] = filepath

    # This method will open a dialog for folder selection
    def select_folder(self):
        folder_path = filedialog.askdirectory()  # Open a dialog to choose a folder
        if folder_path:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".pdf"):
                        filepath = os.path.join(root, file)
                        self.pdf_queue.add(filepath)
                        self.view.queue_listbox.insert(tk.END, file)
                        self.full_paths[file] = filepath


    # This method will clear the queue
    def clear_queue(self):
        pass  # TODO: Implement the method

    # This method will remove the selected items from the queue
    def remove_selected(self):
        pass  # TODO: Implement the method

    # This method will open a dialog for output folder selection
    def browse_output_folder(self):
        pass  # TODO: Implement the method

    # This method will process the files
    def process_files(self):
        pass  # TODO: Implement the method

