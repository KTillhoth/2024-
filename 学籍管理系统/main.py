import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui.Ui_login import Ui_MainWindow  # 导入你写的界面类
import pymysql
from stu import STUMAIN
from admin import ADMINMAIN
from teacher import TEACHMAIN


class MyMainWindow(QMainWindow, Ui_MainWindow): 
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.login.clicked.connect(self.loginf)
        self.logout.clicked.connect(self.logoutf)
        self.conn = pymysql.connect(
            host='localhost',  # 主机名（或IP地址）
            port=3306,  # 端口号，默认为3306
            user='root',  # 用户名
            password='0205be',  # 密码
            charset='utf8mb4',  # 设置字符编码
            database='SchoolManagement'
        )

    def loginf(self):
        username = self.user.text().strip()
        password = self.key.text().strip()
        if self.stu.isChecked():
            table = "Students"
        elif self.teach.isChecked():
            table = "Teachers"
        else:
            table = "Administrators"
        sql = f"select password from {table} where username = %s;"
       
        with self.conn.cursor() as cursor:
            cursor.execute(sql, username)
            result = cursor.fetchone()
            if result and result[0] == password:
                # 假设Shopmain是进入的主界面
                if self.stu.isChecked():
                    self.shop = STUMAIN(user=username)
                elif self.teach.isChecked():
                    self.shop = TEACHMAIN(user=username)
                else:
                    self.shop = ADMINMAIN(user=username)
                self.conn.close()
                self.shop.show()
            else:
                QMessageBox.warning(self, "错误", "账号或密码输入错误", QMessageBox.Yes)
                return
        self.close()
        return

    def logoutf(self):
        self.close()
        return
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())    