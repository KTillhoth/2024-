from PyQt5.QtWidgets import QMainWindow, QGraphicsPixmapItem, QWidget, QInputDialog, QFileDialog, QGraphicsScene
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem,  QPushButton
from ui.Ui_teachmain import Ui_MainWindow  # 导入你写的界面类
import pymysql
from ui.Ui_teacherdisplay import Ui_teacherinfo
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


# 成绩赋予功能窗口类
class GradeTable(QWidget):
    def __init__(self, tid):
        super().__init__()

        self.setWindowTitle('Table with Buttons')
        self.setGeometry(100, 100, 800, 600)
        self.tid = tid
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
        sql = 'select department_id from teachers where teacher_id = %s'
        self.cursor.execute(sql, self.tid)
        result = self.cursor.fetchone()
        self.did = result[0]
        # 创建一个5*6的表格
        self.table = QTableWidget(5, 5)
        column_headers = ["课程号", "课程名", "学号", "成绩", "成绩赋予"]
        self.table.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.table)
        
        sql = 'select grades.course_id,courses.name,grades.student_id, grades.grade from grades,courses where courses.course_id=grades.course_id and teacher_id=%s'
        self.cursor.execute(sql, self.tid)
        result = self.cursor.fetchall()
        x = 0
        for i in result:
            y = 0
            for j in range(4):
                self.table.setItem(x, y, QTableWidgetItem(str(result[x][y])))
                y = y + 1
            btn = QPushButton('给成绩')
            btn.clicked.connect(lambda ch, r=result[x][2], l=result[x][0]: self.on_row_button_click(r, l))
            self.table.setCellWidget(x, 4, btn)
            x = x + 1

    
        # 在表格下方添加一个按钮
        self.general_button = QPushButton('退出')
        self.general_button.clicked.connect(self.on_general_button_click)
        self.layout.addWidget(self.general_button)

        self.setLayout(self.layout)

    def on_row_button_click(self, sid, cid):
        text, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '成绩:')
        if ok_pressed == 0:
            return
        sql = "update grades set grade=%s where student_id=%s and course_id =%s"
        self.cursor.execute(sql, (text, sid, cid))
        self.conn.commit()

    def on_general_button_click(self):
        self.close()
        return


# 开课表类
class TableWithButtons(QWidget):
    def __init__(self, tid):
        super().__init__()

        self.setWindowTitle('Table with Buttons')
        self.setGeometry(100, 100, 800, 600)
        self.tid = tid
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
        sql = 'select department_id from teachers where teacher_id = %s'
        self.cursor.execute(sql, self.tid)
        result = self.cursor.fetchone()
        self.did = result[0]
        # 创建一个5*6的表格
        self.table = QTableWidget(10, 6)
        column_headers = ["课程号", "课程名", "描述", "学分数", "是否通过", "取消"]
        self.table.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.table)
        
        sql = 'select * from courses where teacher_id = %s'
        self.cursor.execute(sql, self.tid)
        result = self.cursor.fetchall()
        x = 0
        for i in result:
            y = 0
            for j in range(4):
                self.table.setItem(x, y, QTableWidgetItem(str(result[x][y])))
                y = y + 1
            if result[x][6] == '0':
                self.table.setItem(x, y, QTableWidgetItem(str("未通过")))
            else:
                self.table.setItem(x, y, QTableWidgetItem(str("通过")))
            btn = QPushButton('取消')
            btn.clicked.connect(lambda ch, r=result[x][0]: self.on_row_button_click(r))
            self.table.setCellWidget(x, 5, btn)
            x = x + 1

    
        # 在表格下方添加一个按钮
        self.general_button = QPushButton('开课')
        self.general_button.clicked.connect(self.on_general_button_click)
        self.layout.addWidget(self.general_button)

        self.setLayout(self.layout)

    def on_row_button_click(self, cid):
        sql = "call deletecourse(%s)"
        self.cursor.execute(sql, cid)
        self.conn.commit()
        return 

    def on_general_button_click(self):
        id, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入课程号:')
        if ok_pressed == 0:
            return
        name, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入课程名:')
        if ok_pressed == 0:
            return
        desp, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入课程描述')
        if ok_pressed == 0:
            return
        credit, ok_pressed = QInputDialog.getText(self, 'Input Dialog', '输入学分数')
        if ok_pressed == 0:
            return
        sql = "INSERT INTO courses VALUES(%s,%s,%s,%s,%s,%s,0) "
        self.cursor.execute(sql, (id, name, desp, credit, self.did, self.tid))
        self.conn.commit()
        return
        

# 基本信息显示窗口类
class INFODISPLAY(QMainWindow, Ui_teacherinfo): 
    def __init__(self, parent=None, t_id='0', cursor=None):
        super(INFODISPLAY, self).__init__(parent)
        self.setupUi(self)
        self.tid = t_id
        self.cursor = cursor
        self.quit.clicked.connect(self.close)
        sql = 'select * from Teachers where teacher_id=%s'
        self.cursor.execute(sql, self.tid)
        result = self.cursor.fetchone()
        self.teacher_id.setText(result[2])
        self.id.setText(result[3])
        self.gender.setText(result[4])
        self.place.setText(result[5])
        self.nation.setText(result[6])
        self.name.setText(result[7])
        sql = 'select finddepart(%s)'
        self.cursor.execute(sql, result[8])
        result1 = self.cursor.fetchone()
        self.depart.setText(result1[0])
        pixmap = QtGui.QPixmap(result[9])
        self.image.setFixedSize(200, 200)
        vsize = self.image.size()
        scaled_pixmap = pixmap.scaled(vsize, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.scene = QGraphicsScene()
        self.scene.addItem(QGraphicsPixmapItem(scaled_pixmap))
        self.image.setScene(self.scene)
       

#老师端主窗口类 
class TEACHMAIN(QMainWindow, Ui_MainWindow): 
    def __init__(self, parent=None, user='admin1'):
        super(TEACHMAIN, self).__init__(parent)
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
        sql = 'select teacher_id from teachers where username = %s'
        self.cursor.execute(sql, self.user)
        result = self.cursor.fetchone()
        self.tid = result[0]
        self.cursor = self.conn.cursor()
        self.course.clicked.connect(self.coursef)
        self.grade.clicked.connect(self.gradef)
        self.change.clicked.connect(self.changef)
        self.info.clicked.connect(self.infof)

    def changef(self):
        if self.image.isChecked():
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
            sql = "Update Teachers set image=%s WHERE username = %s;"
            self.cursor.execute(sql, (fileName, self.user))
            self.conn.commit()   
        else:
            text, ok_pressed = QInputDialog.getText(self, 'Input Dialog', 'Enter new password:')
            if ok_pressed == 0 or text == '':
                return
            sql = "Update Teachers set password=%s WHERE username = %s;"
            self.cursor.execute(sql, (text, self.user))
            self.conn.commit()
        return
    
    def infof(self):
        self.shop = INFODISPLAY(t_id=self.tid, cursor=self.cursor)
        self.shop.show()
        return
    
    def coursef(self):
        self.shop = TableWithButtons(self.tid)
        self.shop.show()
        return 
    
    def gradef(self):
        self.shop = GradeTable(self.tid)
        self.shop.show()
        return 