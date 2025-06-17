import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtCore import QEasingCurve 
import inventory.database as dtbase
import inventory.forms as forms


class LogIN_page(QWidget) :
    login_successful = Signal()
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        #layout.setAlignment()   caused missalignment of few widgets
        title_label = QLabel("Infoware Inventoey")
        title_label.setFont(QFont("Arial", 22, QFont.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_label.setStyleSheet("color: #4ec73c; margin-bottom: 20px; margin-top: 10px;")
        layout.addWidget(title_label)

        username_layout = QHBoxLayout()
        username_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        username_label = QLabel("username ")
        username_label.setFont(QFont("Arial", 12))
        username_label.setStyleSheet("""
                background-color: rgba(255, 255, 255, 0.13);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.3);
                
                border-radius: 12px;
            """)
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("""
                background-color: rgba(255, 255, 255, 0.13);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.3);
                padding: 12px;
                border-radius: 12px;
            """)
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setFont(QFont("Arial", 12))
        self.username_input.setFixedSize(250, 40)

        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        
        username_row = QWidget()
        username_row.setLayout(username_layout)
        username_row.setStyleSheet("""
                background-color: rgba(255, 255, 255, 0.08);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.3);
                
                border-radius: 12px;
            """)
        layout.addWidget(username_row, alignment=Qt.AlignCenter)
        layout.addSpacing(15)

        # Password Input
        password_layout = QHBoxLayout()
        password_label = QLabel("Password ")
        password_label.setFont(QFont("Arial", 12))
        password_label.setStyleSheet("""
                background-color: rgba(255, 255, 255, 0.13);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.3);
                
                border-radius: 12px;
            """)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setFont(QFont("Arial", 12))
        self.password_input.setEchoMode(QLineEdit.Password) # Hide password characters
        self.password_input.setFixedSize(250, 40)
        self.password_input.setStyleSheet("""
                background-color: rgba(255, 255, 255, 0.13);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.3);
                
                border-radius: 12px;
            """)
         # Center the input
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        
        password_row = QWidget()
        password_row.setLayout(password_layout)
        password_row.setStyleSheet("""
                background-color: rgba(255, 255, 255, 0.08);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.3);
                
                border-radius: 12px;
            """)
        layout.addWidget(password_row, alignment=Qt.AlignCenter)
        layout.addSpacing(15)

        # Login Button
        login_button = QPushButton("Log in")
        login_button.setFont(QFont("Arial", 16, QFont.Bold))
        login_button.setFixedSize(150, 45)
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Green */
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)
        layout.addWidget(login_button, alignment=Qt.AlignCenter)
        login_button.clicked.connect(self.check_login)

    def check_login(self) :
        username = self.username_input.text()
        password = self.password_input.text()
        is_correct = dtbase.validate_user((username, password))
        #self.login_successful.emit() ## For testing. to be removed later
        if is_correct :  
            self.password_input.clear()
            self.username_input.clear()      
            #QMessageBox.information(self, "Login Success", "Successfully logged in!") Not needed user enters in main page
            self.login_successful.emit() # Emit signal on success to go to main page
        else :    
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
            self.password_input.clear()
            self.username_input.clear()

class Sidebar(QFrame):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(20)
        self.setMaximumHeight(230)
        self.setStyleSheet("""
                background-color: rgba(205, 205, 205, 0.08);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.3);
                
                border-radius: 12px;
            """)

        self.layout = QVBoxLayout()
        

        self.back_btn = QPushButton("Back to Login")
        self.formA_btn = QPushButton("Goods Receiving")
        self.formB_btn = QPushButton("Sales Form")
        self.formC_btn = QPushButton("Product Master")

        self.back_btn.setStyleSheet("""
                color: #ffffff;
                background-color: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.3);
                text-align: left;
                padding-left: 10px;
                padding-right: 10px;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 12px;
            """)
        self.layout.addWidget(self.back_btn)
        self.layout.addSpacing(20)
        
        self.default_style = """
            color: #ffffff;
            background-color: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.3);
            text-align: left;
            padding: 10px;
            border-radius: 12px;
        """

        self.active_style = """
            color: #ffffff;
            background-color: rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(0, 0, 0, 0.3);
            text-align: left;
            padding: 10px;
            border-radius: 12px;
        """
        self.buttons = [self.formA_btn, self.formB_btn, self.formC_btn]   ## form B = Sales form  ## form C = Product master form

        for btn in self.buttons:
            btn.setStyleSheet(self.default_style)
            btn.clicked.connect(lambda checked, b=btn: self.set_active_button(b))
           
            self.layout.addWidget(btn)
            self.layout.addSpacing(10)

        self.formA_btn.setStyleSheet(self.active_style) ## becase form A (Goods form) is default page when entering in page.

        self.setLayout(self.layout)
    def set_active_button(self, clicked_btn):
        for btn in self.buttons:
            if btn == clicked_btn:
                btn.setStyleSheet(self.active_style)
            else:
                btn.setStyleSheet(self.default_style)

class MainContentPage(QWidget):
    back_to_login = Signal()

    def __init__(self):
        super().__init__()

        # Main layout
        main_layout = QHBoxLayout()
        
        self.setLayout(main_layout)

        # Sidebar
        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar, alignment=Qt.AlignmentFlag.AlignTop)

        # Stacked form pages
        self.form_stack = QStackedWidget()
        self.form_a = forms.goods_receiving_form()
        self.form_b = forms.sales_form()
        self.form_c = forms.productmaster_form()

        self.form_stack.addWidget(self.form_a)  # index 0
        self.form_stack.addWidget(self.form_b)  # index 1
        self.form_stack.addWidget(self.form_c)  # index 2

        main_layout.addWidget(self.form_stack)

        # Show Form A by default
        self.form_stack.setCurrentIndex(0)

        #Button functionality
        self.sidebar.formA_btn.clicked.connect(lambda: self.form_stack.setCurrentIndex(0))
        self.sidebar.formB_btn.clicked.connect(lambda: self.form_stack.setCurrentIndex(1))
        self.sidebar.formC_btn.clicked.connect(lambda: self.form_stack.setCurrentIndex(2))
        self.sidebar.back_btn.clicked.connect(self.back_to_login.emit)


class Infoware_App(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Infoware Inventory")
        self.stacked_main_pages = QStackedWidget()
        self.stacked_main_pages.setStyleSheet(("""
            QWidget {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(33, 33, 33, 255),
                    stop:1 rgba(64, 64, 64, 255)
                );
            }
        """))
        self.setCentralWidget(self.stacked_main_pages)
  
        self.main_content_page = MainContentPage()
        
        self.stacked_main_pages.addWidget(self.main_content_page)
        self.login_page = LogIN_page()
        self.stacked_main_pages.addWidget(self.login_page)

        
        self.stacked_main_pages.setCurrentWidget(self.login_page)

        self.login_page.login_successful.connect(self.show_main_content)
        self.main_content_page.back_to_login.connect(lambda : self.stacked_main_pages.setCurrentWidget(self.login_page))
    def show_main_content(self) :
        self.stacked_main_pages.setCurrentWidget(self.main_content_page)


if __name__ == "__main__":
    app = QApplication([])

    widget = Infoware_App()
    widget.resize(900, 800)
    widget.show()
    sys.exit(app.exec())