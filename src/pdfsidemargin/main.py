from controller import PDFProcessorController
from view import PDFProcessorView

if __name__ == "__main__":
    view = PDFProcessorView()
    controller = PDFProcessorController(view)
    view.mainloop()
