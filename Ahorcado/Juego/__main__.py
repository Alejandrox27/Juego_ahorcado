import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QStackedLayout, QMessageBox, QPushButton,
                             QGridLayout)
from PyQt6.QtGui import QPixmap, QFont, QIcon, QFontDatabase
from PyQt6.QtCore import Qt, QSize
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        icon_path = "images/icon.png"
        self.setWindowIcon(QIcon(icon_path))
        
        with open("styles/estilos.css", 'r') as file:
            style = file.read()
        self.setStyleSheet(style)
        
        self.palabra_frase = []
        self.palabra = ''
        self.permitido = False
        self.ahorcado = 1
        font_path = os.path.abspath(os.path.join("styles", "TeachersStudent-Regular.ttf"))
        font_id = QFontDatabase.addApplicationFont(font_path)
        self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        self.initializeGui()
    
    def initializeGui(self):
        self.setGeometry(390,200,700,300)
        self.setWindowTitle('Ahorcado')
        self.generateWindow()
        self.show()
    
    def generateWindow(self):
        #pagina 1:
        lay_v_page1 = QVBoxLayout()
        
        lbl_ahorcado = QLabel('Ahorcado')
        lbl_ahorcado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_ahorcado.setObjectName('lbl_ahorcado')
        lbl_ahorcado.setFont(QFont(self.font_family, 85))
        
        btn_iniciar = QPushButton('Iniciar')
        btn_iniciar.clicked.connect(self.change_window)
        btn_iniciar.setObjectName('btn_iniciar')
        btn_iniciar.setFont(QFont(self.font_family, 25))
        
        lbl_creador = QLabel('Alejandro Mejía')
        lbl_creador.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_creador.setObjectName('lbl_creador')
        lbl_creador.setFont(QFont(self.font_family, 25))
        
        lay_v_page1.addWidget(lbl_ahorcado)
        lay_v_page1.addWidget(btn_iniciar)
        lay_v_page1.addWidget(lbl_creador)
        
        container_1 = QWidget()
        container_1.setLayout(lay_v_page1)
        
        #pagina 2:
        lay_v_page2 = QVBoxLayout()
        
        lbl_inserte_palabra = QLabel('Inserte una palabra o frase de maximo 22 letras\n(incluyendo espacios)')
        lbl_inserte_palabra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_inserte_palabra.setObjectName('lbl_inserte_palabra')
        lbl_inserte_palabra.setFont(QFont(self.font_family, 25))
        
        self.txt_palabra_frase = QLineEdit()
        self.txt_palabra_frase.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_palabra_frase.setFont(QFont(self.font_family, 20))
        self.txt_palabra_frase.setMaxLength(22)
        self.txt_palabra_frase.setObjectName('txt_palabra_frase')
        
        btn_siguiente = QPushButton('Siguiente')
        btn_siguiente.clicked.connect(self.change_window)
        btn_siguiente.setObjectName('btn_siguiente')
        btn_siguiente.setFont(QFont(self.font_family, 25))
        
        lay_v_page2.addWidget(lbl_inserte_palabra)
        lay_v_page2.addWidget(self.txt_palabra_frase)
        lay_v_page2.addWidget(btn_siguiente)
        
        container_2 = QWidget()
        container_2.setLayout(lay_v_page2)
        
        #pagina 3:
        lay_h_page3 = QHBoxLayout()
        
        self.lbl_ahorcado_imagen = QLabel('')
        self.lbl_ahorcado_imagen.setFixedSize(400,400)
        self.lbl_ahorcado_imagen.setScaledContents(True)
        
        self.lay_grid_palabra_frase = QGridLayout()
        
        palabra_frase = QWidget()
        palabra_frase.setLayout(self.lay_grid_palabra_frase)
        
        lay_h_page3.addWidget(self.lbl_ahorcado_imagen)
        lay_h_page3.addWidget(palabra_frase)
        
        container_3 = QWidget()
        container_3.setLayout(lay_h_page3)
        
        #pagina 4:
        lay_v_page4 = QVBoxLayout()
        
        self.lbl_end = QLabel('')
        self.lbl_end.setFont(QFont(self.font_family, 35))
        
        self.btn_reintentar = QPushButton('Reintentar?')
        self.btn_reintentar.setIcon(QIcon("images/reintentar.png"))
        self.btn_reintentar.setIconSize(QSize(50,50))
        self.btn_reintentar.clicked.connect(self.change_window)
        self.btn_reintentar.setObjectName('btn_reintentar')
        self.btn_reintentar.setFont(QFont(self.font_family, 25))
        
        lay_v_page4.addWidget(self.lbl_end)
        lay_v_page4.addWidget(self.btn_reintentar)
        
        container_4 = QWidget()
        container_4.setLayout(lay_v_page4)
        
        
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container_1)
        self.stacked_layout.addWidget(container_2)
        self.stacked_layout.addWidget(container_3)
        self.stacked_layout.addWidget(container_4)
        
        stacked_container = QWidget()
        stacked_container.setLayout(self.stacked_layout)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(stacked_container)
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)
        
    def change_window(self):
        self.button = self.sender()
        
        if self.button.text().lower() == 'iniciar' or self.button.text().lower()=='reintentar?':
            self.stacked_layout.setCurrentIndex(1)
        elif self.button.text().lower() == 'siguiente':
            frase = self.txt_palabra_frase.text().replace(' ', 'espace')
            if frase.isalpha():
                self.palabra = self.txt_palabra_frase.text().lower()
                if len(self.txt_palabra_frase.text()) > 5:
                    self.labels = self.crear_frase(self.lay_grid_palabra_frase)
                    self.txt_letra = QLineEdit()
                    self.txt_letra.setMaxLength(1)
                    self.txt_letra.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                    self.txt_letra.setObjectName('txt_letra')
                    self.txt_letra.textChanged.connect(self.verifyInput)
                    self.txt_letra.setFont(QFont(self.font_family, 25))
                    
                    self.btn_insertar = QPushButton('Insertar')
                    self.btn_insertar.clicked.connect(self.insertar_letra)
                    self.btn_insertar.setObjectName('btn_insertar')
                    self.btn_insertar.setFont(QFont(self.font_family, 25))
                    
                    mid = (self.column_number // 2)
                    if mid >= 4:
                        self.lay_grid_palabra_frase.addWidget(self.txt_letra, 2, mid -1, 1, mid - 2)
                        self.lay_grid_palabra_frase.addWidget(self.btn_insertar, 3, mid -1, 1, mid - 2)
                    else:
                        self.lay_grid_palabra_frase.addWidget(self.txt_letra, 2, mid -1, 1, mid - 1)
                        self.lay_grid_palabra_frase.addWidget(self.btn_insertar, 3, mid -1, 1 , mid - 1)
                    
                    self.setMinimumSize(1200,600)
                    self.move(50,30)
                    self.showMaximized()
                    
                    self.txt_palabra_frase.setText('')
                    self.stacked_layout.setCurrentIndex(2)
                else:
                    QMessageBox.warning(self, 
                                        'mensaje', 
                                        'Debe agregar minimo 6 letras.',
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok
                                        )
                
            else:
                QMessageBox.warning(self, 
                                    'mensaje', 
                                    'Solo debe contener letras.',
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok
                                    )
            
        else:
            self.stacked_layout.setCurrentIndex(3)
            self.setMinimumSize(700,300)
            self.setGeometry(470,200,700,300)
            self.clearAll()
            
            
            
    def crear_frase(self, lay_grid):
        self.column_number = 0
        iteration = 0
        labels = []
        self.palabra_frase = []
        for l in range(len(self.txt_palabra_frase.text())):
            if self.txt_palabra_frase.text()[l] == ' ':
                self.palabra_frase.append('_')
            else:
                self.palabra_frase.append(self.txt_palabra_frase.text()[l].lower())
            if self.txt_palabra_frase.text()[l] == ' ':
                if l <= 10:
                    label = QLabel('/')
                    label.setFont(QFont(self.font_family, 25))
                    lay_grid.addWidget(label, 0, iteration, 1,1)
                    iteration += 1
                    labels.append(label)
                    continue
                elif l == 11:
                    self.column_number = iteration
                    iteration = 0
                    label = QLabel('/')
                    label.setFont(QFont(self.font_family, 25))
                    lay_grid.addWidget(label, 1, iteration, 1,1)
                    iteration += 1
                    labels.append(label)
                    continue
                else:
                    label = QLabel('/')
                    label.setFont(QFont(self.font_family, 25))
                    lay_grid.addWidget(label, 1, iteration, 1,1)
                    iteration += 1
                    labels.append(label)
                    continue
                    
            if l <= 10:
                label = QLabel('―')
                label.setFont(QFont(self.font_family, 25))
                lay_grid.addWidget(label, 0, iteration, 1,1)
                iteration += 1
                labels.append(label)
                continue
            elif l == 11:
                self.column_number = iteration
                iteration = 0
                label = QLabel('―')
                label.setFont(QFont(self.font_family, 25))
                lay_grid.addWidget(label, 1, iteration, 1,1)
                iteration += 1
                labels.append(label)
                continue
            else:
                label = QLabel('―')
                label.setFont(QFont(self.font_family, 25))
                lay_grid.addWidget(label, 1, iteration, 1,1)
                iteration += 1
                labels.append(label)
                continue
        
        if self.column_number == 0:
            self.column_number = iteration
        
        return labels

    def insertar_letra(self):
        self.txt_letra.setFocus()
        letra = self.txt_letra.text().lower()
        encuentra_letra = False
        
        if self.permitido == True:
            for l in range(len(self.palabra_frase)):
                if self.palabra_frase[l] == letra:
                    self.palabra_frase[l] = '_'
                    encuentra_letra = True
                    self.changeText(l, letra)
                    self.txt_letra.setText('')
                    self.txt_letra.setStyleSheet('background-color:rgba(0,0,0,0);')
            
            if encuentra_letra == False:
                self.txt_letra.setText('')
                self.txt_letra.setStyleSheet('background-color:#F78181;')
                image_url = 'images/ahorcado' + str(self.ahorcado) + '.png'
                pixmap = QPixmap(image_url)
                self.lbl_ahorcado_imagen.setPixmap(pixmap)
                self.ahorcado += 1
            
            if self.ahorcado > 8:
                self.change_window()
                self.lbl_end.setText('Has perdido :(\nla palabra/frase era:\n{}'.format(self.palabra))
                self.lbl_end.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                return
            
            if self.verifyWord(self.palabra_frase) != True:
                self.change_window()
                self.lbl_end.setText('Has Ganado! :D\nla palabra/frase era:\n{}\nbien hecho!!'.format(self.palabra))
                self.lbl_end.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                return
            
            encuentra_letra = False
        
    def verifyWord(self, word):
        for l in word:
            if l != '_':
                return True
        
        return False
                
        
    def verifyInput(self):
        if not self.txt_letra.text().isalpha():
            if self.txt_letra.text() != '':
                self.txt_letra.setStyleSheet('background-color:#F78181;')
                self.permitido = False
                return
            
            self.txt_letra.setStyleSheet('background-color:rgba(0,0,0,0);')
            self.permitido = True
            
        else:
            self.txt_letra.setStyleSheet('background-color:rgba(0,0,0,0);')
            self.permitido = True
            
            
    def changeText(self, index, nuevo_texto):
        if 0 <= index < len(self.labels):
            self.labels[index].setText(nuevo_texto)
    
    def clearLayout(self):
        while self.lay_grid_palabra_frase.count():
            item = self.lay_grid_palabra_frase.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
    
    def clearAll(self):
        self.lbl_ahorcado_imagen.clear()
        self.labels = []
        self.permitido = False
        self.ahorcado = 1
        self.txt_letra.deleteLater()
        self.btn_insertar.deleteLater()
        self.clearLayout()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
    