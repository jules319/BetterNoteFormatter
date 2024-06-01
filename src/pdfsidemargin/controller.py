from pdf_processor import PDFProcessor
import re
import os
import tkinter as tk

class PDFProcessorController:

    def __init__(self, view):
        self.view = view
        self.full_paths = {}
        self._update_ui_state()
        # Connecting the widgets to their respective methods
        self.view.drop_frame.dnd_bind('<<Drop>>', self.files_or_folders_on_drop)
        self.view.folder_btn.config(command=self.select_folder)

        self.view.remove_btn.config(command=self.remove_selected)
        self.view.clear_btn.config(command=self.clear_queue)


        self.view.output_btn.config(command=self.browse_output_folder)
        self.view.process_btn.config(command=self.process_files)

    def _update_ui_state(self):
        # Disable/Enable buttons based on the queue
        if not self.full_paths:
            self.view.remove_btn.config(state=tk.DISABLED)
            self.view.clear_btn.config(state=tk.DISABLED)
        else:
            self.view.remove_btn.config(state=tk.NORMAL)
            self.view.clear_btn.config(state=tk.NORMAL)
        
        # Disable/Enable process button based on output folder entry
        if not self.view.output_entry.get():
            self.view.process_btn.config(state=tk.DISABLED)
        else:
            self.view.process_btn.config(state=tk.NORMAL)

    # This method will handle the dropped files into the application
    def files_or_folders_on_drop(self, event):
        data_str = event.data  # Getting the list of files/folders dropped
        paths = self._parse_dropped_data(data_str)
        
        for full_path in paths:
            if full_path.endswith(".pdf") and os.path.isfile(full_path) and full_path not in self.full_paths:  # If it's a file, add directly
                self._add_file_to_queue(full_path)
            elif os.path.isdir(full_path):  # If it's a directory, add all PDF files in it
                for root, dirs, files in os.walk(full_path):
                    for file in files:
                        if file.endswith(".pdf") and file not in self.full_paths:
                            filepath = os.path.join(root, file)
                            self._add_file_to_queue(filepath, file)
        self._update_ui_state()

    # This method will open a dialog for folder selection
    def select_folder(self):
        folder_path = tk.filedialog.askdirectory()  # Open a dialog to choose a folder

        if folder_path:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".pdf") and file not in self.full_paths:
                        filepath = os.path.join(root, file)
                        self._add_file_to_queue(filepath, file)
        self._update_ui_state()

    def _parse_dropped_data(self, data_str):
        # This regex pattern will match either words without spaces or words enclosed within curly brackets
        pattern = re.compile(r'{[^}]*}|[^{ }\n]+')
        paths = pattern.findall(data_str)
        # If paths are enclosed within brackets, remove them
        paths = [path[1:-1] if path.startswith("{") and path.endswith("}") else path for path in paths]
        
        return paths
    
    def _add_file_to_queue(self, filepath, filename=None):
            if not filename:
                filename = os.path.basename(filepath)
            self.view.queue_listbox.insert(tk.END, filepath)
            self.full_paths[filepath] = filename

    # This method will remove the selected items from the queue
    def remove_selected(self):
        selected_indices = self.view.queue_listbox.curselection()
        
        # Deleting from the end to avoid index shifting problems
        for index in reversed(selected_indices):
            filepath = self.view.queue_listbox.get(index)
            del self.full_paths[filepath]  # Remove from the full_paths dictionary

            
            self.view.queue_listbox.delete(index)  # Remove from the Listbox
        self._update_ui_state()

    # This method will clear the queue
    def clear_queue(self):
        self.view.queue_listbox.delete(0, tk.END)  # Remove all items from the Listbox
        self.full_paths.clear()  # Clear the full_paths dictionary
        self._update_ui_state()

    # This method will open a dialog for output folder selection
    def browse_output_folder(self):
        # Open a dialog to choose a folder and store the selected path
        output_folder_path = tk.filedialog.askdirectory()

        # Check if a folder was selected
        if output_folder_path:
            # Update the Entry widget with the selected folder path
            self.view.output_entry.delete(0, tk.END)  # Clear the existing text in the Entry
            self.view.output_entry.insert(0, output_folder_path)  # Insert the new folder path
        self._update_ui_state()

    # This method will process the files
    def process_files(self):
        self.view.create_processing_overlay(self.cancel_processing)  # Show the overlay
        self.view.overlay.progress_bar.start()  # Start the progress bar

        output_folder = self.view.output_entry.get()  # TODO: Check output folder is valid
        if not os.path.isdir(output_folder):
            print("invalid output folder") # TODO: Implement error handling/logging/view message
        else:
            for file_name in self.full_paths:
                output_file = self.create_output_filepath(output_folder, file_name)
                error = PDFProcessor.add_whitespace(file_name, output_file)
                if error:
                    # TODO: Implement error handling/logging/view message
                    print(error)
                    break

        self.clear_queue()
        self.view.overlay.progress_bar.stop()  # Stop the progress bar
        self.view.show_completion_message(self.close_overlay)
        self._update_ui_state()

    def create_output_filepath(self, output_folder, filepath):
        basename = os.path.basename(filepath)
        filename, file_extension = os.path.splitext(basename)

        # Define the initial modified filename
        modified_filename = f"{filename}_mod{file_extension}"
        output_filepath = os.path.join(output_folder, modified_filename)

        # Check if the file already exists and modify the filename if it does
        counter = 1
        while os.path.exists(output_filepath):
            modified_filename = f"{filename}_mod({counter}){file_extension}"
            output_filepath = os.path.join(output_folder, modified_filename)
            counter += 1

        return output_filepath


    def cancel_processing(self):
        # TODO: add code to actually stop the processing 

        self.view.overlay.progress_bar.stop()  # Stop the progress bar
        self.close_overlay()  # Close the overlay


    def close_overlay(self):
        self.view.overlay.destroy()

