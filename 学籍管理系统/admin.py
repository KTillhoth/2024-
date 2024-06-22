from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem,  QInputDialog
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,  QPushButton
from ui.Ui_adminmain import Ui_MainWindow  
import pymysql
from ui import Ui_stuinfo 
from ui import Ui_teachinfo 
from ui.Ui_majordisplay import Ui_MAJORDISPLAY


# 奖惩窗口类
class RewardTable(QWidget):
    def __init__(self, conn):
        super().__init__()

        self.setWindowTitle('Table with Buttons')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.table = QTableWidget(10, 5)
        column_headers = ["编号", "学号", "类型", "描述", "学院"]
        self.table.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.table)
        
        sql = 'select * from RewardsPunishments'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        x = 0
        for i in result:
            y = 0
            for j in range(4):
                self.table.setItem(x, y, QTableWidgetItem(str(result[x][y])))
                y = y + 1
            sql = "select finddepart(%s)"
            self.cursor.execute(sql, result[x][4])
            result1 = self.cursor.fetchone()
            self.table.setItem(x, 4, QTableWidgetItem(str(result1[0])))
            x = x+1

        # 在表格下方添加一个按钮
        self.general_button = QPushButton('添加奖惩')
        self.general_button.clicked.connect(self.on_general_button_click)
        self.layout.addWidget(self.general_button)

        self.setLayout(self.layout)

    def on_general_button_click(self):
        
        id, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入奖惩号:')
        if ok_pressed == 0:
            return
        sql = "select student_id from students"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        result1 = tuple(row[0] for row in result)
        stu_id, ok_pressed = QInputDialog.getItem(self, 'Input Dialog', '输入学号:', result1, False)
        if ok_pressed == 0:
            return
        type = ('Reward', 'Punishment')
        rtype, ok_pressed = QInputDialog.getItem(self, 'Input Dialog', '输入类型', type, False)
        if ok_pressed == 0:
            return
        desc, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入描述')
        if ok_pressed == 0:
            return
        sql = "select name from departments"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        result1 = tuple(row[0] for row in result)
        depart, ok_pressed = QInputDialog.getItem(self, 'Input Dialog', '输入学院', result1, False)
        if ok_pressed == 0:
            return
        sql = "select department_id from departments where name = %s"
        self.cursor.execute(sql, depart)
        did = self.cursor.fetchone()
        sql = "INSERT INTO RewardsPunishments VALUES(%s,%s,%s,%s,%s)"
        self.cursor.execute(sql, (id, stu_id, rtype, desc, did[0]))
        self.conn.commit()
        return


# 转专业申请窗口类
class CHANGEMAJORTable(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Table with Buttons')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()

        self.conn = pymysql.connect(
            host='localhost',  # 主机名（或IP地址）
            port=3306,  # 端口号，默认为3306
            user='root',  # 用户名
            password='0205be',  # 密码
            charset='utf8mb4',  # 设置字符编码
            database='SchoolManagement'
        )
        self.cursor = self.conn.cursor()

        # 创建一个5*6的表格
        self.table = QTableWidget(7, 5)
        column_headers = ["学号", "姓名", "原专业", "目标专业",  "通过"]
        self.table.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.table)
        
        sql = "select * from students where new_major is not null"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        x = 0
        for i in result:
            self.table.setItem(x, 0, QTableWidgetItem(result[x][2]))
            self.table.setItem(x, 1, QTableWidgetItem(result[x][6]))
            sql = 'select findmajor(%s)'
            self.cursor.execute(sql, result[x][10])
            result1 = self.cursor.fetchone()
            self.table.setItem(x, 2, QTableWidgetItem(result1[0]))
            sql = 'select findmajor(%s)'
            self.cursor.execute(sql, result[x][12])
            result1 = self.cursor.fetchone()
            self.table.setItem(x, 3, QTableWidgetItem((result1[0])))
            btn = QPushButton('通过')
            btn.clicked.connect(lambda ch, r=result[x][2]: self.on_row_button_click(r))
            self.table.setCellWidget(x, 4, btn)
            x = x + 1

    
        # 在表格下方添加一个按钮
        self.general_button = QPushButton('退出')
        self.general_button.clicked.connect(self.on_general_button_click)
        self.layout.addWidget(self.general_button)

        self.setLayout(self.layout)

    def on_row_button_click(self, stu_id):
        sql = "call updatemajor(%s)"
        self.cursor.execute(sql, stu_id)
        self.conn.commit()
        return
        
    def on_general_button_click(self):
        self.close()
        return


# 选课申请窗口类
class COURSETable(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Table with Buttons')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()

        self.conn = pymysql.connect(
            host='localhost',  # 主机名（或IP地址）
            port=3306,  # 端口号，默认为3306
            user='root',  # 用户名
            password='0205be',  # 密码
            charset='utf8mb4',  # 设置字符编码
            database='SchoolManagement'
        )
        self.cursor = self.conn.cursor()

        # 创建一个5*6的表格
        self.table = QTableWidget(7, 7)
        column_headers = ["课程号", "课程名", "描述", "学分数", "学院", "教师", "通过"]
        self.table.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.table)
        
        sql = "select * from courses where is_passed ='0'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        x = 0
        for i in result:
            y = 0
            for j in range(4):
                self.table.setItem(x, y, QTableWidgetItem(str(result[x][y])))
                y = y + 1
            sql = 'select finddepart(%s)'
            self.cursor.execute(sql, result[x][4])
            result1 = self.cursor.fetchone()
            self.table.setItem(x, 4, QTableWidgetItem(result1[0]))
            sql = 'select s_name from teachers where teacher_id = %s'
            self.cursor.execute(sql, result[x][5])
            result1 = self.cursor.fetchone()
            self.table.setItem(x, 5, QTableWidgetItem((result1[0])))
            btn = QPushButton('通过')
            btn.clicked.connect(lambda ch, r=result[x][0]: self.on_row_button_click(r))
            self.table.setCellWidget(x, 6, btn)
            x = x + 1

    
        # 在表格下方添加一个按钮
        self.general_button = QPushButton('退出')
        self.general_button.clicked.connect(self.on_general_button_click)
        self.layout.addWidget(self.general_button)

        self.setLayout(self.layout)

    def on_row_button_click(self, cid):
        sql = "Update courses set is_passed='1' where course_id = %s"
        self.cursor.execute(sql, cid)
        self.conn.commit()
        return
        
    def on_general_button_click(self):
        self.close()
        return


# 专业和学院窗口类
class MAJOR(QMainWindow, Ui_MAJORDISPLAY): 
    def __init__(self, parent=None):
        super(MAJOR, self).__init__(parent)
        self.setupUi(self)
        self.conn = pymysql.connect(
            host='localhost',  # 主机名（或IP地址）
            port=3306,  # 端口号，默认为3306
            user='root',  # 用户名
            password='0205be',  # 密码
            charset='utf8mb4',  # 设置字符编码
            database='SchoolManagement'
        )
        self.cursor = self.conn.cursor()
        self.addmajor.clicked.connect(self.addmajorf)
        self.adddepart.clicked.connect(self.adddepartf)
        sql = 'select * from Departments'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        x = 0
        for i in result:
            y = 0
            for j in i:
                self.departtable.setItem(x, y, QTableWidgetItem(str(result[x][y])))
                y = y + 1
            x = x + 1
        sql = 'select * from Majors'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        sql = 'select finddepart(%s)'
        x = 0
        for i in result:
            self.cursor.execute(sql, result[x][3])
            result1 = self.cursor.fetchone()
            self.majortable.setItem(x, 3, QTableWidgetItem(str(result1[0])))
            x = x+1
        x = 0
        for i in result:
            y = 0
            for j in range(3):
                self.majortable.setItem(x, y, QTableWidgetItem(str(result[x][y])))
                y = y + 1
            x = x + 1

    def addmajorf(self):
        id, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入专业号:')
        if ok_pressed == 0:
            return
        name, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入专业名:')
        if ok_pressed == 0:
            return
        depart, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入所属学院')
        if ok_pressed == 0:
            return
        sql = 'select department_id from departments where name=%s'
        self.cursor.execute(sql, str(depart))
        result = self.cursor.fetchone()
        departid = result[0]
        if not result[0]:
            return 
        sql = "INSERT INTO Majors VALUES(%s,%s,0,%s) "
        self.cursor.execute(sql, (id, name, departid))
        self.conn.commit()
        return
    
    def adddepartf(self):
        id, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入学院号:')
        if ok_pressed == 0:
            return
        name, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入学院名:')
        if ok_pressed == 0:
            return
        sql = "INSERT INTO Departments VALUES(%s,%s,0) "
        self.cursor.execute(sql, (id, name))
        self.conn.commit()
        return


class ADDSTU(QMainWindow, Ui_stuinfo.Ui_MainWindow): 
    def __init__(self, parent=None):
        super(ADDSTU, self).__init__(parent)
        self.setupUi(self)
        self.conn = pymysql.connect(
            host='localhost',  # 主机名（或IP地址）
            port=3306,  # 端口号，默认为3306
            user='root',  # 用户名
            password='0205be',  # 密码
            charset='utf8mb4',  # 设置字符编码
            database='SchoolManagement'
        )
        self.cursor = self.conn.cursor()
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.close)

    def confirm(self):
        username = self.user.text().strip()
        password = self.key.text().strip()
        stu_id = self.stu_id.text().strip()
        id = self.id.text().strip()
        gender = self.gender.text().strip()
        place = self.place.text().strip()
        nation = self.nation.text().strip()
        name = self.name.text().strip()
        l_data = self.l_data.text().strip()
        le_date = self.le_date.text().strip()
        major = self.major.text().strip()
        sql = "SELECT major_id FROM Majors WHERE name = %s;"
        self.cursor.execute(sql, major)
        result = self.cursor.fetchone()
        major_id = result[0]
        sql = "INSERT INTO Students VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,null,null)"
        # 执行插入操作
        self.cursor.execute(sql,  (username, password, stu_id, id, gender, place, nation, name, l_data, le_date,  major_id))
        self.conn.commit()
        self.close()
        return


class ADDTEACH(QMainWindow, Ui_teachinfo.Ui_MainWindow): 
    def __init__(self, parent=None):
        super(ADDTEACH, self).__init__(parent)
        self.setupUi(self)
        self.conn = pymysql.connect(
            host='localhost',  # 主机名（或IP地址）
            port=3306,  # 端口号，默认为3306
            user='root',  # 用户名
            password='0205be',  # 密码
            charset='utf8mb4',  # 设置字符编码
            database='SchoolManagement'
        )
        self.cursor = self.conn.cursor()
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.close)
    
    def confirm(self):
        username = self.user.text().strip()
        password = self.key.text().strip()
        stu_id = self.t_id.text().strip()
        id = self.id.text().strip()
        gender = self.gender.text().strip()
        place = self.place.text().strip()
        nation = self.nation.text().strip()
        name = self.name.text().strip()
        depart = self.depart.text().strip()
        sql = "SELECT department_id FROM Majors WHERE name = %s;"
        self.cursor.execute(sql, depart)
        result = self.cursor.fetchone()
        depart_id = result[0]
        sql = "INSERT INTO Teachers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,null)"
        # 执行插入操作
        self.cursor.execute(sql,  (username, password, stu_id, id, gender, place, nation, name, depart_id))
        self.conn.commit()
        self.close()
        return


class ADMINMAIN(QMainWindow, Ui_MainWindow): 
    def __init__(self, parent=None, user='admin1'):
        super(ADMINMAIN, self).__init__(parent)
        self.setupUi(self)
        self.user = user
        self.conn = pymysql.connect(
            host='localhost',  # 主机名（或IP地址）
            port=3306,  # 端口号，默认为3306
            user='root',  # 用户名
            password='0205be',  # 密码
            charset='utf8mb4',  # 设置字符编码
            database='SchoolManagement'
        )
        self.cursor = self.conn.cursor()
        self.addstu.clicked.connect(self.addstuf)
        self.addteach.clicked.connect(self.addteachf)
        self.reward.clicked.connect(self.rewardf)
        self.major.clicked.connect(self.majorf)
        self.course.clicked.connect(self.coursef)
        self.changemajor.clicked.connect(self.changemajorf)

    def addstuf(self):
        self.shop = ADDSTU()
        self.shop.show()
        return
    
    def addteachf(self):
        self.shop = ADDTEACH()
        self.shop.show()
        return
    
    def rewardf(self):
        self.shop = RewardTable(self.conn)
        self.shop.show()
        return

    def majorf(self):
        self.shop = MAJOR()
        self.shop.show()
        return
    
    def coursef(self):
        self.shop = COURSETable()
        self.shop.show()
        return

    def changemajorf(self):
        self.shop = CHANGEMAJORTable()
        self.shop.show()
        return
