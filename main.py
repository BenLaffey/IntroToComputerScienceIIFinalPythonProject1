#Requires the PyQt5 Package to be installed in order to run
#Project 1: Lab 5 from this class, improved by making a file changer
#uses "The Raven" and "Lorem Ipsum" as inputs

#Feedback Implemented: Made Errors Red
from controller import *


def main() -> None:
    """
    Function to act as the main graphical window creator and updater.
    :return: None
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()