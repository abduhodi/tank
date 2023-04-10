from PyQt6 import QtCore, QtGui, QtWidgets
from img import resources
import threading
from time import sleep
from random import randint


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle("MainWindow")
        self.setWindowIcon(QtGui.QIcon(":/icons/me_right.png"))
        self.setMinimumSize(600, 400)
        self.resize(1350, 800)
        self.showMaximized()

        self.bullet = threading.Thread(target=self.fire_func)
        self.demage_enemy = threading.Thread(target=self.demageEnemy)

        self.height = 80
        self.width = 80

        self.up = 16777235
        self.right = 16777236
        self.down = 16777237
        self.left = 16777234
        self.fire = 32
        self.start = 16777220

        self.my_direction = "right"
        self.my_bullet_height = 25
        self.my_bullet_width = 40
        self.my_bullet_pos_x = 0
        self.my_bullet_pos_y = 0
        self.my_x = 0
        self.my_y = 0

        self.enemy_direction = "left"
        self.enemy_bullet_height = 8
        self.enemy_bullet_width = 30
        self.enemy_bullet_pos_x = 0
        self.enemy_bullet_pos_y = 0
        self.enemy_x = self.size().width() // 2 - self.width
        self.enemy_y = 200

        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.statusbar = QtWidgets.QWidget(parent=self.centralwidget)
        self.statusbar.setMinimumSize(QtCore.QSize(0, 40))
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.statusbar.setStyleSheet("background-color: #fff;border-top: 1px solid #333;")
        self.statusbar.setObjectName("statusbar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.statusbar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.score_label = QtWidgets.QLabel(parent=self.statusbar)
        self.score_label.setObjectName("score")
        self.score_label.setText("Score: ")
        self.score_label.setStyleSheet("border: none;")
        self.horizontalLayout.addWidget(self.score_label)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.statusbar, 2, 0, 1, 1)
        self.playground = QtWidgets.QWidget(parent=self.centralwidget)
        self.playground.setObjectName("playground")
        self.Me = QtWidgets.QLabel(parent=self.playground)
        self.Me.setGeometry(QtCore.QRect(self.my_x, self.my_y, self.height, self.width))
        self.Me.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Me.setObjectName("Me")
        self.Me.setStyleSheet("border: none; background-color: transparent;")
        self.Me.setPixmap(QtGui.QPixmap(":/icons/me_right.png").scaled(self.height, self.width))
        self.enemy = QtWidgets.QLabel(parent=self.playground)
        self.enemy.setGeometry(QtCore.QRect(self.enemy_x, self.enemy_y, 60, 60))
        self.enemy.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.enemy.setObjectName("enemy")
        self.enemy.setStyleSheet("border: none; background-color: transparent;")
        self.enemy.setPixmap(QtGui.QPixmap(":/icons/enemy_left.png").scaled(60, 60))
        self.my_bullet = QtWidgets.QLabel(parent=self.playground)
        self.my_bullet.setGeometry(QtCore.QRect(100, 30, self.my_bullet_width, self.my_bullet_height))
        self.my_bullet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.my_bullet.setObjectName("my_right_bullet")
        self.my_bullet.setStyleSheet("border: none; background-color: transparent;")
        self.my_bullet.setPixmap(QtGui.QPixmap(":/icons/my_right_bullet.png").scaled(40, 25))
        self.my_bullet.hide()
        self.enemy_bullet = QtWidgets.QLabel(parent=self.playground)
        self.enemy_bullet.setGeometry(QtCore.QRect(470, 25, 30, 8))
        self.enemy_bullet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.enemy_bullet.setObjectName("enemy_bullet")
        self.enemy_bullet.setStyleSheet("border: none; background-color: transparent;")
        self.enemy_bullet.setPixmap(QtGui.QPixmap(":/icons/enemy_left_bullet.png").scaled(30, 8))
        self.gridLayout.addWidget(self.playground, 1, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        QtCore.QMetaObject.connectSlotsByName(self)


    def demageEnemy(self):
        self.enemy.setPixmap(QtGui.QPixmap(":/icons/explosion.png").scaled(60, 60))
        sleep(1)
        self.enemy.setPixmap(QtGui.QPixmap(":/icons/enemy_left.png").scaled(60, 60))
        self.enemy_x = randint(0, self.playground.size().width() - 60)
        self.enemy_y = randint(0, self.playground.size().height() - 60)
        self.enemy.setGeometry(QtCore.QRect(self.enemy_x, self.enemy_y, 60, 60))
        print("x = ", self.enemy_x)
        print("y = ", self.enemy_y)

    def set_geometry(self):
        pass
    

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        print(a0.size().width())


    def set_bullet_pos(self):
        self.my_bullet_pos_x = self.my_bullet.geometry().x()
        self.my_bullet_pos_y = self.my_bullet.geometry().y()

        
    def fire_func(self, direction: str):
        if direction == "right":
            print('x=', self.enemy_x)
            print('y=', self.enemy_y)
            print(self.my_bullet_pos_y)
            self.set_bullet_pos()
            while self.my_bullet_pos_x < self.playground.size().width():
                print(self.my_bullet_pos_x)
                self.my_bullet_pos_x += 5
                self.my_bullet.setGeometry(QtCore.QRect(self.my_bullet_pos_x, self.my_bullet_pos_y, self.my_bullet_width, self.my_bullet_height))
                if self.my_bullet_pos_x + 30 == self.enemy_x and self.my_bullet_pos_y + self.my_bullet_height // 2 in range(self.enemy_y, self.enemy_y + 61):
                    print("Boom")
                    del self.demage_enemy
                    self.demage_enemy = threading.Thread(target=self.demageEnemy)
                    self.demage_enemy.start()
                    break
                sleep(0.02)
        elif direction == "left":
            self.set_bullet_pos()
            while self.my_bullet_pos_x > -self.my_bullet_width:
                self.my_bullet_pos_x -= 5
                print(self.my_bullet_pos_x)
                self.my_bullet.setGeometry(QtCore.QRect(self.my_bullet_pos_x, self.my_bullet_pos_y, self.my_bullet_width, self.my_bullet_height))
                if self.my_bullet_pos_x == self.enemy_x + 50 and self.my_bullet_pos_y + self.my_bullet_height // 2 in range(self.enemy_y, self.enemy_y + 61):
                    del self.demage_enemy
                    self.demage_enemy = threading.Thread(target=self.demageEnemy)
                    self.demage_enemy.start()
                    break
                sleep(0.02)
        elif direction == "up":
            self.set_bullet_pos()
            while self.my_bullet_pos_y > -self.my_bullet_height:
                self.my_bullet_pos_y -= 5
                print(self.my_bullet_pos_y)
                self.my_bullet.setGeometry(QtCore.QRect(self.my_bullet_pos_x, self.my_bullet_pos_y, self.my_bullet_width, self.my_bullet_height))
                if self.my_bullet_pos_y == self.enemy_y + 50 and self.my_bullet_pos_x + self.my_bullet_width // 2 in range(self.enemy_x, self.enemy_x + 61):
                    del self.demage_enemy
                    self.demage_enemy = threading.Thread(target=self.demageEnemy)
                    self.demage_enemy.start()
                    break
                sleep(0.02)
        elif direction == "down":
            self.set_bullet_pos()
            while self.my_bullet_pos_y < self.playground.size().height():
                self.my_bullet_pos_y += 5
                print(self.my_bullet_pos_y)
                self.my_bullet.setGeometry(QtCore.QRect(self.my_bullet_pos_x, self.my_bullet_pos_y, self.my_bullet_width, self.my_bullet_height))
                if self.my_bullet_pos_y == self.enemy_y - 30 and self.my_bullet_pos_x + self.my_bullet_width // 2 in range(self.enemy_x, self.enemy_x + 61):
                    del self.demage_enemy
                    self.demage_enemy = threading.Thread(target=self.demageEnemy)
                    self.demage_enemy.start()
                    break
                sleep(0.02)
        self.my_bullet.hide()
                

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        key = event.key() 
        print(key)
        if key == self.right:
            if self.my_direction != "right":
                self.Me.setPixmap(QtGui.QPixmap(":/icons/me_right.png").scaled(self.height, self.width))
                self.my_direction = "right"
            elif self.my_direction == "right":
                if self.my_x < self.playground.size().width() - self.width:
                    self.my_x += 5 
                self.Me.setGeometry(QtCore.QRect(self.my_x, self.my_y, self.height, self.width))
        elif key == self.up:
            if self.my_direction != "up":
                self.Me.setPixmap(QtGui.QPixmap(":/icons/me_up.png").scaled(self.height, self.width))
                self.my_direction = "up"
            elif self.my_direction == "up":
                if self.my_y > 0:
                    self.my_y -= 5 
                self.Me.setGeometry(QtCore.QRect(self.my_x, self.my_y, self.height, self.width))
        elif key == self.down:
            if self.my_direction != "down":
                self.Me.setPixmap(QtGui.QPixmap(":/icons/me_down.png").scaled(self.height, self.width))
                self.my_direction = "down"
            elif self.my_direction == "down":
                if self.my_y < self.playground.size().height() - self.height:
                    self.my_y += 5 
                self.Me.setGeometry(QtCore.QRect(self.my_x, self.my_y, self.height, self.width))
        elif key == self.left:
            if self.my_direction != "left":
                self.Me.setPixmap(QtGui.QPixmap(":/icons/me_left.png").scaled(self.height, self.width))
                self.my_direction = "left"
            elif self.my_direction == "left":
                if self.my_x > 0:
                    self.my_x -= 5
                self.Me.setGeometry(QtCore.QRect(self.my_x, self.my_y, self.height, self.width))
        
        elif key == self.fire:
            if not self.bullet.is_alive():
                if self.my_direction == "right":
                    self.my_bullet_height = 25
                    self.my_bullet_width = 40
                    self.my_bullet.setPixmap(QtGui.QPixmap(":/icons/my_right_bullet.png").scaled(self.my_bullet_width, self.my_bullet_height))
                    self.my_bullet.setGeometry(QtCore.QRect(self.my_x + self.width - 5, self.my_y + 30, self.my_bullet_width, self.my_bullet_height))
                elif self.my_direction == "down":
                    self.my_bullet_height = 40
                    self.my_bullet_width = 25
                    self.my_bullet.setPixmap(QtGui.QPixmap(":/icons/my_down_bullet.png").scaled(self.my_bullet_width, self.my_bullet_height))
                    self.my_bullet.setGeometry(QtCore.QRect(self.my_x + 26, self.my_y + self.height - 5, self.my_bullet_width, self.my_bullet_height))
                elif self.my_direction == "up":
                    self.my_bullet_height = 40
                    self.my_bullet_width = 25
                    self.my_bullet.setPixmap(QtGui.QPixmap(":/icons/my_up_bullet.png").scaled(self.my_bullet_width, self.my_bullet_height))
                    self.my_bullet.setGeometry(QtCore.QRect(self.my_x + 30, self.my_y - 35, self.my_bullet_width, self.my_bullet_height))
                elif self.my_direction == "left":
                    self.my_bullet_height = 25
                    self.my_bullet_width = 40
                    self.my_bullet.setPixmap(QtGui.QPixmap(":/icons/my_left_bullet.png").scaled(self.my_bullet_width, self.my_bullet_height))
                    self.my_bullet.setGeometry(QtCore.QRect(self.my_x - self.my_bullet_width + 5, self.my_y + 25, self.my_bullet_width, self.my_bullet_height))
                self.my_bullet.show()
                del self.bullet
                self.bullet = threading.Thread(target=self.fire_func, args=(self.my_direction,))
                self.bullet.start()