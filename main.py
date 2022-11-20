import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication
from main_ui import Ui_MainWindow

con = sqlite3.connect('coffee_list.sqlite')
cur = con.cursor()
result = cur.execute("""SELECT name FROM coffee_name""").fetchall()
COFFEE_NAMES = []
for elem in result:
    COFFEE_NAMES.append(elem[0])
con.close()


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItems(COFFEE_NAMES)
        self.pushButton.clicked.connect(self.get_coffee_info)

    def get_coffee_info(self):
        con1 = sqlite3.connect('coffee_list.sqlite')
        cur1 = con1.cursor()
        seek_for = (self.comboBox.currentText(),)
        result1 = cur1.execute("""SELECT * FROM coffee_info
                    WHERE name LIKE ?""", seek_for).fetchall()
        self.label_7.setText(str(result1[0][1]))
        self.label_12.setText(str(result1[0][2]))
        self.label_11.setText(str(result1[0][3]))
        self.label_10.setText(str(result1[0][4]))
        self.label_8.setText(str(result1[0][5]))
        self.label_9.setText(str(result1[0][6]))
        con1.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
