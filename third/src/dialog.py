from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


class NewItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 创建标签和输入框
        self.label = QLabel("请输入名称：")
        self.input_line = QLineEdit()

        # 创建确定和取消按钮
        self.ok_button = QPushButton("确定")
        self.cancel_button = QPushButton("取消")

        # 连接按钮的点击事件到槽函数
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        # 创建垂直布局，并将标签、输入框和按钮添加到其中
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_line)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.ok_button)
        h_layout.addWidget(self.cancel_button)

        layout.addLayout(h_layout)

        # 设置对话框的布局
        self.setLayout(layout)

    def get_input_text(self):
        # 返回输入框中的文本
        return self.input_line.text()
