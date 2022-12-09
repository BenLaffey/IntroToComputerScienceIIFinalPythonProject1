from PyQt5.QtWidgets import *
from view import *
from filemethods import *
import os.path


class Controller(QMainWindow, Ui_MainWindow):
    """
    A QMainWindow and Ui_MainWindow class representing the main logic controller for a 'Controller' object.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Function to initialize the 'Controller' object by setting up the user interface, creating '__inputfile', '__outputfile', and '__output' strings, setting the 'filenotfound', 'outputfile', and 'outputcheck' labels to "", connecting the three radio buttons to the 'fileCheck()' function, and setting the push button to the 'buttonOutput()' function respectively.
        :param args: A tuple used to pass a variable number of non-key worded arguments to this function.
        :param kwargs: A dictionary used to pass a keyworded variable-length argument list to this function.
        :return: None
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.__inputfile: str = ""
        self.__outputfile: str = ""
        self.__output: str = ""
        self.label_filenotfound.setText("")
        self.label_outputfile.setText("")
        self.label_outputcheck.setText("")
        self.radioButton_1.clicked.connect(lambda: self.fileCheck())
        self.radioButton_2.clicked.connect(lambda: self.fileCheck())
        self.radioButton_3.clicked.connect(lambda: self.fileCheck())
        self.pushButton_setoutput.clicked.connect(lambda: self.buttonOutput())

    def buttonOutput(self) -> None:
        """
        Function to determine if the push button's activation is permitted to update the specified output file.
        :return: None
        """
        self.fileCheck()
        if self.radioButton_1.isChecked() or self.radioButton_2.isChecked() or self.radioButton_3.isChecked():
            file = open(self.__outputfile, "w")
            file.write(self.__output)
            file.close()
            self.label_filenotfound.setText("")
            self.label_outputfile.setText("")
            self.label_outputcheck.setText("                  Data Stored!")
            self.textBrowser_outputpreview.setText("")
            self.lineEdit_input.setText("")
            self.lineEdit_output.setText("")
            self.lineEdit_replacer.setText("")
            self.lineEdit_replacing.setText("")
            self.radioButton_1.setCheckable(False)
            self.radioButton_1.setCheckable(True)
            self.radioButton_2.setCheckable(False)
            self.radioButton_2.setCheckable(True)
            self.radioButton_3.setCheckable(False)
            self.radioButton_3.setCheckable(True)
        else:
            self.label_outputcheck.setText("<html><head/><body><p><span style=\" color:#ff0000;\">Cannot Output With No Selection Made</span></p></body></html>")
            self.textBrowser_outputpreview.setText("")

    def fileCheck(self) -> None:
        """
        Function to check if an input file has been specified, an output file has been specified, and whether or not the selected file method can be done.
        :return: None
        """
        try:
            file = open(f"{self.lineEdit_input.text().strip()}.txt", "r")
            file.close()
            self.label_filenotfound.setText("      Found This File")
            self.__inputfile: str = f"{self.lineEdit_input.text().strip()}.txt"
        except FileNotFoundError:
            self.label_filenotfound.setText("<html><head/><body><p><span style=\" color:#ff0000;\">This File Cannot Be Found</span></p></body></html>")
            self.textBrowser_outputpreview.setText("")
            self.radioButton_1.setCheckable(False)
            self.radioButton_1.setCheckable(True)
            self.radioButton_2.setCheckable(False)
            self.radioButton_2.setCheckable(True)
            self.radioButton_3.setCheckable(False)
            self.radioButton_3.setCheckable(True)
        if len(self.lineEdit_output.text().strip()) > 0:
            if os.path.isfile(f"{self.lineEdit_output.text().strip()}.txt"):
                self.label_outputfile.setText("This Will Override An Existing Output File")
            else:
                self.label_outputfile.setText("  This Will Create A New Output File")
            self.__outputfile: str = f"{self.lineEdit_output.text().strip()}.txt"
        else:
            self.label_outputfile.setText("<html><head/><body><p><span style=\" color:#ff0000;\">Cannot Output With No Output File Name</span></p></body></html>")
            self.textBrowser_outputpreview.setText("")
            self.radioButton_1.setCheckable(False)
            self.radioButton_1.setCheckable(True)
            self.radioButton_2.setCheckable(False)
            self.radioButton_2.setCheckable(True)
            self.radioButton_3.setCheckable(False)
            self.radioButton_3.setCheckable(True)
        if os.path.isfile(f"{self.lineEdit_input.text().strip()}.txt") and len(self.lineEdit_output.text().strip()) > 0:
            if self.radioButton_2.isChecked() and len(self.lineEdit_replacing.text()) > 0 and len(self.lineEdit_replacer.text()) > 0:
                self.updateOutput(2)
            elif not self.radioButton_2.isChecked() and (self.radioButton_1.isChecked() or self.radioButton_3.isChecked()):
                if self.radioButton_1.isChecked():
                    self.updateOutput(1)
                elif self.radioButton_3.isChecked():
                    self.updateOutput(3)
            else:
                self.label_outputcheck.setText("<html><head/><body><p><span style=\" color:#ff0000;\">Cannot Output With No Replacements</span></p></body></html>")
                self.textBrowser_outputpreview.setText("")
                self.radioButton_1.setCheckable(False)
                self.radioButton_1.setCheckable(True)
                self.radioButton_2.setCheckable(False)
                self.radioButton_2.setCheckable(True)
                self.radioButton_3.setCheckable(False)
                self.radioButton_3.setCheckable(True)

    def updateOutput(self, method: int) -> None:
        """
        Function to select which file method will be performed on the file copy to set the output of the final output file.
        :param method: The type of file method as an integer to perform on the file copy for the final output file.
        :return: None
        """
        file = open(self.__inputfile, "r")
        filecopy: list = file.readlines()
        file.close()
        if method == 1:
            self.__output: str = normalOutput(filecopy)
        elif method == 2:
            self.__output: str = replaceOutput(filecopy, self.lineEdit_replacing.text(), self.lineEdit_replacer.text())
        elif method == 3:
            self.__output: str = reverseOutput(filecopy)
        self.textBrowser_outputpreview.setText(self.__output)
        self.label_outputcheck.setText("")