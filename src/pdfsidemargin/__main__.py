from view import PDFProcessorView
from controller import PDFProcessorController


if __name__ == '__main__':
    view = PDFProcessorView()
    controller = PDFProcessorController(view)
    view.mainloop()
    