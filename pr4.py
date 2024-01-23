from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QTabWidget, QDoubleSpinBox, QLineEdit, QComboBox, QSlider, QProgressBar, QDial)

app = QApplication([])
window = QWidget()

window.resize(250, 250)
window.move(560, 225)

tab1 = QWidget()
slider = QSlider()
progress = QProgressBar()
progress.setValue(0)
v1 = QVBoxLayout()
v1.addWidget(slider)
v1.addWidget(progress)
tab1.setLayout(v1)
slider.valueChanged.connect(lambda value: progress.setValue(value))

tab2 = QWidget()
n = QDoubleSpinBox()
v2 = QVBoxLayout()
v2.addWidget(n)
tab2.setLayout(v2)

tab3 = QWidget()
text = QLabel('Сума:')
text1 = QLabel('У валюту:')
text2 = QLabel('Результат:')
text3 = QLabel(' ')
button1 = QPushButton('Конвертувати')

c = QComboBox()
list1 = ['eur', 'usd', 'frank']
c.addItems(list1)

line = QLineEdit()

v3 = QVBoxLayout()
v3.addWidget(text)
v3.addWidget(line)
v3.addWidget(text1)
v3.addWidget(c)
v3.addWidget(text2)
v3.addWidget(text3)
v3.addWidget(button1)
tab3.setLayout(v3)

def add_task():
    t = line.text()
    f = c.currentText()
    if f == 'eur':
        r = int(t) * 41.45
        text3.setText(str(r))
    elif f == 'usd':
        r = int(t) * 37.80
        text3.setText(str(r))
    elif f == 'frank':
        r = int(t) * 44.33
        text3.setText(str(r))

button1.clicked.connect(add_task)

tab4 = QWidget()
dial = QDial()
label_tab4 = QLabel("Градуси: 0")
v4 = QVBoxLayout()
v4.addWidget(dial)
v4.addWidget(label_tab4)
tab4.setLayout(v4)

def dial_changed(value):
    label_tab4.setText(f"Градуси: {value}")

dial.valueChanged.connect(dial_changed)

tabs = QTabWidget()
tabs.addTab(tab1, 'Вкладка №1')
tabs.addTab(tab2, 'Вкладка №2')
tabs.addTab(tab3, 'Вкладка №3')
tabs.addTab(tab4, 'Вкладка №4')  

v_layout = QVBoxLayout()
v_layout.addWidget(tabs)
window.setLayout(v_layout)

window.show()
app.exec_()
