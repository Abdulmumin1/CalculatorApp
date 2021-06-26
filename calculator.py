from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget

class Main(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Calculator')
		self.resize(300, 500)
		self.show()
		self.setStyleSheet('background:#333; font-size:30px;')
		
		main_layout = QVBoxLayout()
		button_layout = QGridLayout()

		self.histryBox = QListWidget()
		self.entryBox = QLineEdit()
		self.entryBox.setStyleSheet('color:white;')

		main_layout.addWidget(self.histryBox)
		main_layout.addWidget(self.entryBox)

		button1 = QPushButton(text='1', clicked=lambda:self.insertNum('1'))
		button2 = QPushButton(text='2', clicked=lambda:self.insertNum('2'))
		button3 = QPushButton(text='3', clicked=lambda:self.insertNum('3'))
		button4 = QPushButton(text='4', clicked=lambda:self.insertNum('4'))
		button5 = QPushButton(text='5', clicked=lambda:self.insertNum('5'))
		button6 = QPushButton(text='6', clicked=lambda:self.insertNum('6'))
		button7 = QPushButton(text='7', clicked=lambda:self.insertNum('7'))
		button8 = QPushButton(text='8', clicked=lambda:self.insertNum('8'))
		button9 = QPushButton(text='9', clicked=lambda:self.insertNum('9'))
		button0 = QPushButton(text='0', clicked=lambda:self.insertNum('0'))
		
		button_dot = QPushButton(text='.', clicked=lambda:self.insertNum('.'))
		button_op = QPushButton(text='(', clicked=lambda:self.insertNum('('))
		button_cp = QPushButton(text=')', clicked=lambda:self.insertNum(')'))
		
		button_add = QPushButton(text='+', clicked=lambda:self.insertNum('+'))
		button_sub = QPushButton(text='-', clicked=lambda:self.insertNum('-'))
		button_mult = QPushButton(text='*', clicked=lambda:self.insertNum('*'))
		button_div = QPushButton(text='/', clicked=lambda:self.insertNum('/'))

		button_clear = QPushButton(text='C', clicked=self.clear_items)
		button_calculate = QPushButton(text='=', clicked=self.calculate)
		
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

	def insertNum(self, num):
		self.entryBox.insert(num)

	def clear_items(self):
		self.entryBox.clear()

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

app = QApplication([])
app.setStyle('fusion')
main = Main()
app.exec_()
