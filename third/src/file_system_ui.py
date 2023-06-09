# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './file_system.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1172, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.path_label = QtWidgets.QLabel(self.centralwidget)
        self.path_label.setObjectName("path_label")
        self.horizontalLayout_3.addWidget(self.path_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setMaximumSize(QtCore.QSize(116, 45))
        self.return_button.setObjectName("return_button")
        self.horizontalLayout_3.addWidget(self.return_button)
        self.return_root_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_root_button.setMaximumSize(QtCore.QSize(116, 45))
        self.return_root_button.setObjectName("return_root_button")
        self.horizontalLayout_3.addWidget(self.return_root_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_file_button.setMaximumSize(QtCore.QSize(116, 45))
        self.new_file_button.setObjectName("new_file_button")
        self.horizontalLayout.addWidget(self.new_file_button)
        self.new_dir_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_dir_button.setMaximumSize(QtCore.QSize(116, 45))
        self.new_dir_button.setObjectName("new_dir_button")
        self.horizontalLayout.addWidget(self.new_dir_button)
        self.rename_button = QtWidgets.QPushButton(self.centralwidget)
        self.rename_button.setObjectName("rename_button")
        self.horizontalLayout.addWidget(self.rename_button)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setMaximumSize(QtCore.QSize(116, 45))
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.format_button = QtWidgets.QPushButton(self.centralwidget)
        self.format_button.setObjectName("format_button")
        self.horizontalLayout.addWidget(self.format_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.size_label = QtWidgets.QLabel(self.centralwidget)
        self.size_label.setObjectName("size_label")
        self.horizontalLayout.addWidget(self.size_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "file system"))
        self.path_label.setText(_translate("MainWindow", "/"))
        self.return_button.setText(_translate("MainWindow", "返回上一级"))
        self.return_root_button.setText(_translate("MainWindow", "返回根目录"))
        self.new_file_button.setText(_translate("MainWindow", "新建文件"))
        self.new_dir_button.setText(_translate("MainWindow", "新建文件夹"))
        self.rename_button.setText(_translate("MainWindow", "重命名"))
        self.delete_button.setText(_translate("MainWindow", "删除"))
        self.format_button.setText(_translate("MainWindow", "格式化"))
        self.size_label.setText(_translate("MainWindow", "已使用：剩余空间："))
        self.action.setText(_translate("MainWindow", "新建文件"))
        self.action_2.setText(_translate("MainWindow", "新建文件夹"))
        self.action_3.setText(_translate("MainWindow", "删除"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
