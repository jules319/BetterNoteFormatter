from pdf_processor import PDFProcessor
import re
import os
import tkinter as tk
from tkinter import filedialog

class PDFProcessorController:

    def __init__(self, view):
        self.view = view
        self.pdf_queue = set()
        self.full_paths = {}

        # Connecting the widgets to their respective methods
        self.view.drop_frame.dnd_bind('<<Drop>>', self.files_or_folders_on_drop)
        self.view.folder_btn.config(command=self.select_folder)

        # self.view.clear_btn.config(command=self.clear_queue)
        # self.view.remove_btn.config(command=self.remove_selected)

        # self.view.output_btn.config(command=self.browse_output_folder)
        # self.view.process_btn.config(command=self.process_files)

    # This method will handle the dropped files into the application
    def files_or_folders_on_drop(self, event):
        data_str = event.data  # Getting the list of files/folders dropped
        paths = self._parse_dropped_data(data_str)
        
        for full_path in paths:
            if full_path.endswith(".pdf") and os.path.isfile(full_path) and full_path not in self.pdf_queue:  # If it's a file, add directly
                self._add_file_to_queue(full_path)
            elif os.path.isdir(full_path):  # If it's a directory, add all PDF files in it
                for root, dirs, files in os.walk(full_path):
                    for file in files:
                        if file.endswith(".pdf") and file not in self.pdf_queue:
                            filepath = os.path.join(root, file)
                            self._add_file_to_queue(filepath, file)

    # This method will open a dialog for folder selection
    def select_folder(self):
        folder_path = filedialog.askdirectory()  # Open a dialog to choose a folder

        if folder_path:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".pdf") and file not in self.pdf_queue:
                        filepath = os.path.join(root, file)
                        self._add_file_to_queue(filepath, file)

    def _parse_dropped_data(self, data_str):
        # This regex pattern will match either words without spaces or words enclosed within curly brackets
        pattern = re.compile(r'{[^}]*}|[^{ }\n]+')
        paths = pattern.findall(data_str)
        # If paths are enclosed within brackets, remove them
        paths = [path[1:-1] if path.startswith("{") and path.endswith("}") else path for path in paths]
        
        return paths
    
    def _add_file_to_queue(self, filepath, filename=None):
            self.pdf_queue.add(filepath)
            if not filename:
                filename = os.path.basename(filepath)
            self.view.queue_listbox.insert(tk.END, filename)
            self.full_paths[filename] = filepath

    # This method will remove the selected items from the queue
    def remove_selected(self):
        pass  # TODO: Implement the method
    
    # This method will clear the queue
    def clear_queue(self):
        pass  # TODO: Implement the method


    # This method will open a dialog for output folder selection
    def browse_output_folder(self):
        pass  # TODO: Implement the method

    # This method will process the files
    def process_files(self):
        pass  # TODO: Implement the method

