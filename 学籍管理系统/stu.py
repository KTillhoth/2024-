from PyQt5.QtWidgets import QMainWindow, QGraphicsPixmapItem, QWidget, QInputDialog, QFileDialog, QGraphicsScene
from ui.Ui_stumain import Ui_MainWindow  # 导入你写的界面类
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem,  QPushButton
from PyQt5 import QtGui
import pymysql 
from ui.Ui_studisplay import Ui_Stuinfo
from PyQt5.QtCore import Qt


# 奖惩查看界面类
class RewardTable(QWidget):
    def __init__(self, stu_id, cursor):
        super().__init__()

        self.setWindowTitle('奖惩查看')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
        self.stu_id = stu_id
        self.cursor = cursor
        # 创建一个5*6的表格
        self.table = QTableWidget(10, 4)
        column_headers = ["编号", "类型", "描述", "学院"]
        self.table.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.table)
        sql = 'select * from '
        sql = 'select rp_id,type, description,name from RewardsPunishments r,\
        departments where student_id=%s and departments.department_id = r.department_id '
        self.cursor.execute(sql, self.stu_id)
        result = self.cursor.fetchall()
        x = 0
        for i in result:
            y = 0
            for j in range(4):
                self.table.setItem(x, y, QTableWidgetItem(str(result[x][y])))
                y = y + 1
            x = x+1
        self.general_button = QPushButton('退出')
        self.general_button.clicked.connect(self.close)
        self.layout.addWidget(self.general_button)
        self.setLayout(self.layout)


# 成绩查看界面类
class GRADETable(QWidget):
    def __init__(self, stu_id, cursor):
        super().__init__()

        self.setWindowTitle('成绩查看')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
        self.stu_id = stu_id
        self.cursor = cursor
        # 创建一个5*6的表格
        self.table = QTableWidget(10, 3)
        column_headers = ["课程号", "课程名", "成绩"]
        self.table.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.table)
        
        sql = 'select grades.course_id,courses.name, grades.grade from grades,\
        courses where courses.course_id=grades.course_id and student_id=%s'
        self.cursor.execute(sql, self.stu_id)
        result = self.cursor.fetchall()
        x = 0
        for i in result:
            y = 0
            for j in range(3):
                self.table.setItem(x, y, QTableWidgetItem(str(result[x][y])))
                y = y + 1
            x = x+1
        self.general_button = QPushButton('退出')
        self.general_button.clicked.connect(self.close)
        self.layout.addWidget(self.general_button)
        self.setLayout(self.layout)


# 选课界面类
class COURSETable(QWidget):
    def __init__(self, stu_id):
        super().__init__()

        self.setWindowTitle('选课')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
        self.stu_id = stu_id
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
        self.table = QTableWidget(7, 8)
        column_headers = ["课程号", "课程名", "描述", "学分数", "学院", "教师", "状态", "选课"]
        self.table.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.table)
        
        sql = "select * from courses where is_passed ='1'"
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
            # 是否已选课
            sql = 'select student_id from grades where student_id = %s and course_id = %s'
            self.cursor.execute(sql, (self.stu_id, result[x][0]))
            result1 = self.cursor.fetchone()
            if result1:
                self.table.setItem(x, 6, QTableWidgetItem(("已选")))
                btn = QPushButton('退课')
            else:
                self.table.setItem(x, 6, QTableWidgetItem(("未选")))
                btn = QPushButton('选课')
            btn.clicked.connect(lambda ch, r=result[x][0], l=x: self.on_row_button_click(r, l))
            self.table.setCellWidget(x, 7, btn)
            x = x + 1

        # 在表格下方添加退出按钮
        self.general_button = QPushButton('退出')
        self.general_button.clicked.connect(self.on_general_button_click)
        self.layout.addWidget(self.general_button)

        self.setLayout(self.layout)

    def on_row_button_click(self, cid, x):
        item = self.table.item(x, 6)
        if item.text() == '未选':
            sql = "insert grades values(%s,%s,null) "
        else:
            sql = "delete from grades where student_id = %s and course_id = %s "
        self.cursor.execute(sql, (self.stu_id, cid))
        self.conn.commit()
        return
        
    def on_general_button_click(self):
        self.close()
        return


class INFODISPLAY(QMainWindow, Ui_Stuinfo): 
    def __init__(self, parent=None, stu_id='0'):
        super(INFODISPLAY, self).__init__(parent)
        self.setupUi(self)
        self.sid = stu_id
        self.conn = pymysql.connect(
            host='localhost',  # 主机名（或IP地址）
            port=3306,  # 端口号，默认为3306
            user='root',  # 用户名
            password='0205be',  # 密码
            charset='utf8mb4',  # 设置字符编码
            database='SchoolManagement'
        )
        self.cursor = self.conn.cursor()
        self.quit.clicked.connect(self.close)
        sql = 'select * from Students where student_id=%s'
        self.cursor.execute(sql, self.sid)
        result = self.cursor.fetchone()
        self.stu_id.setText(result[2])
        self.id.setText(result[3])
        self.gender.setText(result[4])
        self.place.setText(result[5])
        self.nation.setText(result[6])
        self.name.setText(result[7])
        self.e_date.setText(result[8])
        self.l_date.setText(result[9])
        sql = 'select findmajor(%s)'
        self.cursor.execute(sql, result[10])
        result1 = self.cursor.fetchone()
        self.major.setText(result1[0])
        sql = "select department_id from majors where major_id = %s"
        self.cursor.execute(sql, result[10])
        result1 = self.cursor.fetchone()
        sql = 'select finddepart(%s)'
        self.cursor.execute(sql, result1[0])
        result1 = self.cursor.fetchone()
        self.depart.setText(result1[0])
        pixmap = QtGui.QPixmap(result[11])
        self.image.setFixedSize(200, 200)
        vsize = self.image.size()
        scaled_pixmap = pixmap.scaled(vsize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.scene = QGraphicsScene()
        self.scene.addItem(QGraphicsPixmapItem(scaled_pixmap))
        self.image.setScene(self.scene)
       
       
class STUMAIN(QMainWindow, Ui_MainWindow): 
    def __init__(self, parent=None, user='admin1'):
        super(STUMAIN, self).__init__(parent)
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
        self.change.clicked.connect(self.changef)
        self.info.clicked.connect(self.infof)
        self.course.clicked.connect(self.coursef)
        self.changemajor.clicked.connect(self.changemajorf)
        self.grade.clicked.connect(self.gradef)
        self.reward.clicked.connect(self.rewardf)
        sql = 'select student_id from Students where username=%s'
        self.cursor.execute(sql, self.user)
        result = self.cursor.fetchone()
        self.stu_id = result[0]  

    def changef(self):
        if self.image.isChecked():
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
            sql = "Update Students set image=%s WHERE username = %s;"
            self.cursor.execute(sql, (fileName, self.user))
            self.conn.commit()   
        else:
            text, ok_pressed = QInputDialog.getText(self, 'Input Dialog', 'Enter new password:')
            if ok_pressed == 0 or text == '':
                return
            sql = "Update Students set password=%s WHERE username = %s;"
            self.cursor.execute(sql, (text, self.user))
            self.conn.commit()
        return

    def infof(self):
        self.shop = INFODISPLAY(stu_id=self.stu_id)
        self.shop.show()
        return
    
    def coursef(self):
        self.shop = COURSETable(self.stu_id)
        self.shop.show()
        return
    
    def changemajorf(self):
        text, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入转入专业:')
        if ok_pressed == 0 or text == '':
            return
        sql = 'select major_id from majors where name =%s'
        self.cursor.execute(sql, text)
        result = self.cursor.fetchone()
        if result:
            sql = "Update Students set new_major=%s WHERE username = %s;"
            self.cursor.execute(sql, (result[0], self.user))
            self.conn.commit()
        return
    
    def gradef(self):
        self.shop = GRADETable(self.stu_id, self.cursor)
        self.shop.show()
        return
    
    def rewardf(self):
        self.shop = RewardTable(self.stu_id, self.cursor)
        self.shop.show()
        return