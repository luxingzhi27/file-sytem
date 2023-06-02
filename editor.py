import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QPushButton, QVBoxLayout, QMessageBox, QShortcut
from editor_ui import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QKeySequence


class TextEditor(QMainWindow, Ui_MainWindow):
    text_saved = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit.setText("")
        self.save_button.clicked.connect(self.save_file)
        self.textEdit.textChanged.connect(self.modified)
        self.is_saved = True
        self.file_name = ""
        self.shortcut_save = QShortcut(QKeySequence("Ctrl+S"), self)
        self.shortcut_save.activated.connect(self.save_file)

    def modified(self):
        self.is_saved = False
        self.setWindowTitle(f"{self.file_name} *")

    def open_file(self, text):
        self.textEdit.setText(text)
        self.setWindowTitle(self.file_name)

    def save_file(self):
        if self.is_saved:
            return
        self.text_saved.emit(self.textEdit.toPlainText())
        self.is_saved = True
        self.setWindowTitle(self.file_name)

    def closeEvent(self, event):
        if self.textEdit.document().isModified() and not self.is_saved:
            reply = QMessageBox.question(
                self, "保存文件", "是否保存文件？", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                self.save_file()
            elif reply == QMessageBox.Cancel:
                event.ignore()
                return
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
