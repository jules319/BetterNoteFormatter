from controller import PDFProcessorController
from view import PDFProcessorView


def main():
    view = PDFProcessorView()
    controller = PDFProcessorController(view)
    view.mainloop()


if __name__ == "__main__":
    main()
