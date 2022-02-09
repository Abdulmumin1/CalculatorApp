from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget

class Main(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Calculator')
		self.setFixedWidth(400)
		self.setFixedHeight(500)
		self.show()
		self.setStyleSheet('background:#333; font-size:25px; color:#F1D4B4;')
		
		main_layout = QVBoxLayout()
		button_layout = QGridLayout()
		self.err = False
		self.histryBox = QListWidget()
		self.histryBox.setStyleSheet('QListWidget::item:selected{'+
		'background:#F1D4B4; color:black; border-radius:5px;}')
		self.entryBox = QLineEdit()

		main_layout.addWidget(self.histryBox)
		main_layout.addWidget(self.entryBox)

		button1 = self.create_button('1')
		button2 = self.create_button('2')
		button3 = self.create_button('3')
		button4 =self.create_button('4')
		button5 =self.create_button('5')
		button6 = self.create_button('6')
		button7 = self.create_button('7')
		button8 = self.create_button('8')
		button9 = self.create_button('9')
		button0 = self.create_button('0')
		
		button_dot = self.create_button('.')
		button_op = self.create_button('(')
		button_cp = self.create_button(')')
		
		button_add =self.create_button('+')
		button_sub = self.create_button('-')
		button_mult =self.create_button('*')
		button_div =self.create_button('/')

		button_clear = QPushButton(text='C', clicked=self.clear_items)
		button_clear.setStyleSheet('background:#F1D4B4; border-radius:6px; padding:5px; color:black;')
		button_calculate = QPushButton(text='=', clicked=self.calculate)
		button_calculate.setStyleSheet('background:#F1D4B4; border-radius:6px; padding:5px; color:black;')
		
		button_layout.addWidget(button1, 0, 0)
		button_layout.addWidget(button2, 0, 1)
		button_layout.addWidget(button3, 0, 2)
		button_layout.addWidget(button4, 1, 0)
		button_layout.addWidget(button5, 1, 1)
		button_layout.addWidget(button6, 1, 2)
		button_layout.addWidget(button7, 2, 0)
		button_layout.addWidget(button8, 2, 1)
		button_layout.addWidget(button9, 2, 2)
		button_layout.addWidget(button0, 3, 0)
		button_layout.addWidget(button_dot, 3, 1)
		button_layout.addWidget(button_op, 4, 0)
		button_layout.addWidget(button_cp, 4, 1)

		button_layout.addWidget(button_add, 1, 3)
		button_layout.addWidget(button_sub, 2, 3)
		button_layout.addWidget(button_mult, 3, 3)
		button_layout.addWidget(button_div, 3, 2)

		button_layout.addWidget(button_clear, 0, 3)
		button_layout.addWidget(button_calculate, 4, 2, 1, 2)



		main_layout.addLayout(button_layout)
		self.setLayout(main_layout)
	def create_button(self, text):
		button = QPushButton(text=text, clicked=lambda:self.insertNum(text))
		button.setStyleSheet('*{background:#F1D4B4; border-radius:6px; padding:5px; color:black;}'+
				'*:hover{background:#F3EDD6;}')
		return button
	def insertNum(self, num):
		if not self.err:
			self.entryBox.insert(num)
		else:
			self.entryBox.clear()
			self.entryBox.setEnabled(True)
			self.err = False
			self.entryBox.insert(num)

	def clear_items(self):
		self.entryBox.clear()
		if self.err:
			self.entryBox.setEnabled(True)
			self.err = False

	def calculate(self):
		items_to_calculte = self.entryBox.text()
		try:
			if items_to_calculte:
				items_to_calculte = str(items_to_calculte)
				result = eval(items_to_calculte)
				self.entryBox.setText(str(result))
				self.histryBox.addItem(f"{items_to_calculte}={result}")

		except:
			self.entryBox.setText('err')
			self.entryBox.setDisabled(True)
			self.err = True

app = QApplication([])
app.setStyle('fusion')
main = Main()
app.exec_()
