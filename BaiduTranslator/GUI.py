import sys
from translator import BaiduTranslator
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QComboBox, QPushButton, QVBoxLayout, QWidget, QMessageBox
)

class TranslatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.translator = BaiduTranslator("", "")
        # 填入百度翻译api的id和密钥
        self.setWindowTitle("智能翻译器")
        self.setGeometry(100, 100, 600, 400)

        # 创建主窗口布局
        self.layout = QVBoxLayout()

        # 输入标签和文本框
        self.input_label = QLabel("输入文本：")
        self.input_text = QTextEdit()

        # 源语言选择
        self.from_lang_label = QLabel("源语言：")
        self.from_lang_combo = QComboBox()
        self.from_lang_combo.addItems(['自动检测', '中文', '英文', '日语', '韩语', '法语', '西班牙语'])

        # 目标语言选择
        self.to_lang_label = QLabel("目标语言：")
        self.to_lang_combo = QComboBox()
        self.to_lang_combo.addItems(['中文', '英文', '日语', '韩语', '法语', '西班牙语'])

        # 翻译按钮
        self.translate_button = QPushButton("翻译")
        self.translate_button.clicked.connect(self.translate_text)

        # 输出标签和文本框
        self.output_label = QLabel("翻译结果：")
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        # 添加控件到布局
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_text)
        self.layout.addWidget(self.from_lang_label)
        self.layout.addWidget(self.from_lang_combo)
        self.layout.addWidget(self.to_lang_label)
        self.layout.addWidget(self.to_lang_combo)
        self.layout.addWidget(self.translate_button)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_text)

        # 创建中央小部件
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def translate_text(self):
        input_content = self.input_text.toPlainText().strip()
        if not input_content:
            QMessageBox.warning(self, "输入为空", "请输入要翻译的文本。")
            return

        from_lang = self.from_lang_combo.currentText()
        to_lang = self.to_lang_combo.currentText()

        lang_map = {
            '自动检测': 'auto',
            '中文': 'zh',
            '英文': 'en',
            '日语': 'jp',
            '韩语': 'kor',
            '法语': 'fra',
            '西班牙语': 'spa',
        }

        from_lang_code = lang_map.get(from_lang, 'auto')
        to_lang_code = lang_map.get(to_lang, 'zh')

        translated = self.translator.translate(input_content, from_lang=from_lang_code, to_lang=to_lang_code)

        self.output_text.setPlainText(translated)

def main():
    app = QApplication(sys.argv)
    translator_gui = TranslatorGUI()
    translator_gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
