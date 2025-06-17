from PySide6.QtWidgets import (
    QWidget, QLabel, QFormLayout, QVBoxLayout, QScrollArea, QTextEdit,
    QSpinBox, QComboBox, QLineEdit, QDoubleSpinBox,
    QGraphicsBlurEffect, QPushButton, QHBoxLayout, QMessageBox
)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFileDialog
from . import database as dtbase


class goods_receiving_form(QWidget):
    def __init__(self):
        super().__init__()

        # Scroll area setup
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.NoFrame)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                border-radius: 20px;
                background-color: transparent;
            }
        """)

        # Scroll widget that holds the form
        scroll_widget = QWidget()
        scroll_widget.setAutoFillBackground(True)
        scroll_widget.setGraphicsEffect(self.get_blur_effect())
        scroll_widget.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 20px;
        """)

        layout = QFormLayout()
        layout.setSpacing(14)

        # List of field tuples (label, field)
        add_layout_list = []

        self.p_info = QLabel("Product info:")
        self.p_info_input = QTextEdit()
        self.p_info_input.setFixedHeight(60)
        add_layout_list.append((self.p_info, self.p_info_input))

        self.cs_info = QLabel("Supplier info:")
        self.cs_info_ip = QTextEdit()
        self.cs_info_ip.setFixedHeight(60)
        add_layout_list.append((self.cs_info, self.cs_info_ip))

        self.Quantity = QLabel("self.Quantity:")
        self.Quantity_ip = QSpinBox()
        self.Quantity_ip.setSpecialValueText(" ")
        self.Quantity_ip.setRange(0, 1000000)
        add_layout_list.append((self.Quantity, self.Quantity_ip))

        self.Rate_per_unit = QLabel("Rate per unit:")
        self.rate_input = self.blank_double_spinbox()
        add_layout_list.append((self.Rate_per_unit, self.rate_input))

        self.total_rate = QLabel("Total rate:")
        self.total_rate_input = self.blank_double_spinbox()
        add_layout_list.append((self.total_rate, self.total_rate_input))

        self.Tax = QLabel("self.Tax:")
        self.Tax_ip = self.blank_double_spinbox(max_val=100.0)
        add_layout_list.append((self.Tax, self.Tax_ip))

        # Add form fields with consistent styling
        for label, field in add_layout_list:
            label.setFont(QFont("Segoe UI", 12))
            label.setStyleSheet(""" color : #ffffff """)
            field.setStyleSheet("""
                background-color: rgba(255, 255, 255, 0.15);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.3);
                padding: 12px;
                border-radius: 12px;
            """)
            layout.addRow(label, field)

        # Unit of measurement combo
        Unit_of_measurement = QLabel("Unit of measurement:")
        Unit_of_measurement.setStyleSheet(""" color : #ffffff """)
        self.unit_mes_input = QComboBox()
        self.unit_mes_input.addItem("Select mesurement unit ...")
        self.unit_mes_input.addItems(["kg", "g", "L", "mL", "meters", "cm", "Other..."])
        self.unit_mes_input.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 10px;
            border-radius: 12px;
        """)
        self.unit_mes_input.currentIndexChanged.connect(self.on_unit_selected)

        self.custom_unit_input = QLineEdit()
        self.custom_unit_input.setPlaceholderText("Enter custom unit")
        self.custom_unit_input.setVisible(False)
        self.custom_unit_input.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)

        layout.addRow(Unit_of_measurement, self.unit_mes_input)
        layout.addRow("", self.custom_unit_input)

        submit_button = QPushButton(" Submit ")
        submit_button.clicked.connect(self.submit_goods)
        submit_button.setMaximumWidth(200)
        
        submit_button.setStyleSheet("""
            background-color: #14532d;  
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)

        button_container = QWidget()
        button_layout = QHBoxLayout()
        
        button_layout.addWidget(submit_button)
        
        button_container.setLayout(button_layout)
        button_container.setMaximumHeight(60)
        button_container.setStyleSheet("""  background-color: rgba(0, 0, 0, 0); border : rgba(0, 0, 0, 0);  """)
        
        layout.addWidget(button_container)

      
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

        
        self.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(33, 33, 33, 255),
                    stop:1 rgba(64, 64, 64, 255)
                );
            }
        """)

    def submit_goods(self):
        print("done")
        m = self.unit_mes_input.currentText()
        m_unit = m if m != "Other..." else self.custom_unit_input.text()           # QLineEdit    else  # QComboBox
        form = (
            self.p_info_input.toPlainText(),        # QTextEdit
            self.cs_info_ip.toPlainText(),          # QTextEdit
            self.Quantity_ip.value(),               # QSpinBox
            m_unit,
            self.rate_input.value(),                # QDoubleSpinBox
            self.total_rate_input.value(),           # QDoubleSpinBox
            self.Tax_ip.value(),                    # QDoubleSpinBox
        )
        dtbase.store_goods(form)
        QMessageBox.information(self, "Updated Database", "Successfully stored form !")
        fields = [ self.unit_mes_input, self.p_info_input,  self.cs_info_ip, self.Quantity_ip, self.rate_input, self.total_rate_input , self.Tax_ip ]
        for field in fields :
            field.clear()


    def get_blur_effect(self):
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(15)
        return blur_effect

    def on_unit_selected(self, index=None):
        if self.unit_mes_input.currentText() == "Other...":
            self.custom_unit_input.setVisible(True)
        else:
            self.custom_unit_input.setVisible(False)

    def blank_double_spinbox(self, max_val=1000000.0):
        spinbox = QDoubleSpinBox()
        spinbox.setRange(0.0, max_val)
        spinbox.setDecimals(2)
        spinbox.setSpecialValueText(" ")  # visually looks blank
        spinbox.setValue(spinbox.minimum())  # still 0 internally
        spinbox.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: gray;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)
        return spinbox



class sales_form(QWidget):
    def __init__(self):
        super().__init__()

        # Scroll area setup
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.NoFrame)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                border-radius: 20px;
                background-color: transparent;
            }
        """)

        # Scroll widget that holds the form
        scroll_widget = QWidget()
        scroll_widget.setAutoFillBackground(True)
        scroll_widget.setGraphicsEffect(self.get_blur_effect())
        scroll_widget.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 20px;
        """)

        layout = QFormLayout()
        layout.setSpacing(14)

        # List of field tuples (label, field)
        add_layout_list = []

        self.p_info = QLabel("Product info:")
        self.p_info_input = QTextEdit()
        self.p_info_input.setFixedHeight(60)
        add_layout_list.append((self.p_info, self.p_info_input))

        self.cs_info = QLabel("Customer info:")
        self.cs_info_ip = QTextEdit()
        self.cs_info_ip.setFixedHeight(60)
        add_layout_list.append((self.cs_info, self.cs_info_ip))

        self.Quantity = QLabel("self.Quantity:")
        self.Quantity_ip = QSpinBox()
        self.Quantity_ip.setSpecialValueText(" ")
        self.Quantity_ip.setRange(0, 1000000)
        add_layout_list.append((self.Quantity, self.Quantity_ip))

        self.Rate_per_unit = QLabel("Rate per unit:")
        self.rate_input = self.blank_double_spinbox()
        add_layout_list.append((self.Rate_per_unit, self.rate_input))

        self.total_rate = QLabel("Total rate:")
        self.total_rate_input = self.blank_double_spinbox()
        add_layout_list.append((self.total_rate, self.total_rate_input))

        self.Tax = QLabel("self.Tax:")
        self.Tax_ip = self.blank_double_spinbox(max_val=100.0)
        add_layout_list.append((self.Tax, self.Tax_ip))

        # Add form fields with consistent styling
        for label, field in add_layout_list:
            label.setFont(QFont("Segoe UI", 12))
            label.setStyleSheet(""" color : #ffffff """)
            field.setStyleSheet("""
                background-color: rgba(255, 255, 255, 0.15);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.3);
                padding: 12px;
                border-radius: 12px;
            """)
            layout.addRow(label, field)

        # Unit of measurement combo
        Unit_of_measurement = QLabel("Unit of measurement:")
        Unit_of_measurement.setStyleSheet(""" color : #ffffff """)
        self.unit_mes_input = QComboBox()
        self.unit_mes_input.addItem("Select mesurement unit ...")
        
        self.unit_mes_input.addItems(["kg", "g", "L", "mL", "meters", "cm", "Other..."])
        self.unit_mes_input.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 10px;
            border-radius: 12px;
        """)
        self.unit_mes_input.currentIndexChanged.connect(self.on_unit_selected)

        self.custom_unit_input = QLineEdit()
        self.custom_unit_input.setPlaceholderText("Enter custom unit")
        self.custom_unit_input.setVisible(False)
        self.custom_unit_input.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)

        layout.addRow(Unit_of_measurement, self.unit_mes_input)
        layout.addRow("", self.custom_unit_input)

        submit_button = QPushButton(" Submit ")
        submit_button.clicked.connect(self.submit_sales)
        submit_button.setMaximumWidth(200)
        
        submit_button.setStyleSheet("""
            background-color: #14532d;  
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)

        button_container = QWidget()
        button_layout = QHBoxLayout()
        
        button_layout.addWidget(submit_button)
        
        button_container.setLayout(button_layout)
        button_container.setMaximumHeight(60)
        button_container.setStyleSheet("""  background-color: rgba(0, 0, 0, 0); border : rgba(0, 0, 0, 0);  """)
        
        layout.addWidget(button_container)

        # Final layout setup
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

        # background gradient for the full widget
        self.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(33, 33, 33, 255),
                    stop:1 rgba(64, 64, 64, 255)
                );
            }
        """)

    def submit_sales(self):
        print("done")
        m = self.unit_mes_input.currentText()
        m_unit = m if m != "Other..." else self.custom_unit_input.text()
        form = (
            self.p_info_input.toPlainText(),        # QTextEdit
            self.cs_info_ip.toPlainText(),          # QTextEdit
            self.Quantity_ip.value(),               # QSpinBox
            m_unit,
            self.rate_input.value(),                # QDoubleSpinBox
            self.total_rate_input.value(),               # QDoubleSpinBox
            self.Tax_ip.value(),                    # QDoubleSpinBox
        )
        dtbase.store_sales(form)
        QMessageBox.information(self, "Updated Database", "Successfully stored form !")
        fields = [ self.unit_mes_input, self.p_info_input,  self.cs_info_ip, self.Quantity_ip, self.rate_input, self.total_rate_input , self.Tax_ip ]
        for field in fields :
            field.clear()

    def get_blur_effect(self):
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(15)
        return blur_effect

    def on_unit_selected(self, index=None):
        if self.unit_mes_input.currentText() == "Other...":
            self.custom_unit_input.setVisible(True)
        else:
            self.custom_unit_input.setVisible(False)

    def blank_double_spinbox(self, max_val=1000000.0):
        spinbox = QDoubleSpinBox()
        spinbox.setRange(0.0, max_val)
        spinbox.setDecimals(2)
        spinbox.setSpecialValueText(" ")  # visually looks blank
        spinbox.setValue(spinbox.minimum())  # still 0 internally
        spinbox.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: gray;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)
        return spinbox



class productmaster_form(QWidget):
    def __init__(self):
        super().__init__()

        # Scroll area setup
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.NoFrame)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                border-radius: 20px;
                background-color: transparent;
            }
        """)

        # Scroll widget that holds the form
        scroll_widget = QWidget()
        scroll_widget.setAutoFillBackground(True)
        scroll_widget.setGraphicsEffect(self.get_blur_effect())
        scroll_widget.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 20px;
        """)

        layout = QFormLayout()
        layout.setSpacing(14)

        # List of field tuples (label, field) to add in layout 1 shot
        add_layout_list = []

        self.Barcode = QLabel("self.Barcode")
        self.Barcode_input = QLineEdit()
        #self.Barcode_input.setFixedHeight(60)
        add_layout_list.append((self.Barcode, self.Barcode_input))

        self.SKU_Id = QLabel("SKU ID")
        self.SKU_Id_ip = QLineEdit()
        #self.SKU_Id_ip.setFixedHeight(60)
        add_layout_list.append((self.SKU_Id, self.SKU_Id_ip))

        self.Product_name = QLabel("Product Name")
        self.Product_name_input = QLineEdit()
        #self.Product_name_input.setFixedHeight(60)
        add_layout_list.append((self.Product_name, self.Product_name_input))

        self.Product_desc = QLabel("Product Description : ")
        self.Product_desc_input = QTextEdit()
        self.Product_desc_input.setFixedHeight(80)
        add_layout_list.append((self.Product_desc, self.Product_desc_input))


        self.img = QLabel("Product Image :")
        self.img_btn = QPushButton(" Select ")
        self.img_btn.clicked.connect(self.fdialog)
        add_layout_list.append((self.img, self.img_btn))
        

        self.Price = QLabel("self.Price : ")
        self.price_input = self.blank_double_spinbox()
        add_layout_list.append((self.Price, self.price_input))

        self.Tax = QLabel("self.Tax:")
        self.Tax_ip = self.blank_double_spinbox(max_val=100.0)
        add_layout_list.append((self.Tax, self.Tax_ip))

        # Add form fields with consistent styling
        for label, field in add_layout_list:
            label.setFont(QFont("Segoe UI", 12))
            label.setStyleSheet(""" color : #ffffff """)
            field.setStyleSheet("""
                background-color: rgba(255, 255, 255, 0.15);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.3);
                padding: 12px;
                border-radius: 10px;
            """)
            layout.addRow(label, field)


        category = QLabel("Category : ")
        category.setFont(QFont("Segoe UI", 12))
        category.setStyleSheet(""" color : #ffffff """)
        self.category_ip = QComboBox()
        self.category_ip.addItem("Select sub category ...")
        self.category_ip.addItems(["category 1", "category 2", "category 3", "category 4", "Other..."])
        self.category_ip.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 10px;
            border-radius: 12px;
        """)
        self.category_ip.currentIndexChanged.connect(self.on_cat_selected)

        self.custom_category_ip = QLineEdit()
        self.custom_category_ip.setPlaceholderText("Enter custom unit")
        self.custom_category_ip.setVisible(False)
        self.custom_category_ip.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)

        

        sub_category = QLabel("sub_Category : ")
        sub_category.setFont(QFont("Segoe UI", 12))
        sub_category.setStyleSheet(""" color : #ffffff """)
        self.sub_category_ip = QComboBox()
        self.sub_category_ip.addItem("Select sub category ...")
        self.sub_category_ip.addItems(["sub category 1", "sub category 2", "sub category 3", "sub category 4", "Other..."])
        self.sub_category_ip.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 10px;
            border-radius: 12px;
        """)
        self.sub_category_ip.currentIndexChanged.connect(self.on_subcat_selected)

        self.custom_sub_category_ip = QLineEdit()
        self.custom_sub_category_ip.setPlaceholderText("Enter custom unit")
        self.custom_sub_category_ip.setVisible(False)
        self.custom_sub_category_ip.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)
        

        # Unit of measurement combo
        Unit_of_measurement = QLabel("Unit of measurement:")
        Unit_of_measurement.setFont(QFont("Segoe UI", 12))
        Unit_of_measurement.setStyleSheet(""" color : #ffffff """)
        self.unit_mes_input = QComboBox()
        self.unit_mes_input.addItem("Select unit...")  # fake placeholder
        #self.unit_mes_input.setItemData(0, 0, role=0x0100)
        self.unit_mes_input.addItems(["kg", "g", "L", "mL", "meters", "cm", "Other..."])
        self.unit_mes_input.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 10px;
            border-radius: 12px;
        """)
        self.unit_mes_input.currentIndexChanged.connect(self.on_unit_selected)

        self.custom_unit_input = QLineEdit()
        self.custom_unit_input.setPlaceholderText("Enter custom unit")
        self.custom_unit_input.setVisible(False)
        self.custom_unit_input.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)

        layout.addRow(Unit_of_measurement, self.unit_mes_input)
        layout.addRow("", self.custom_unit_input)
        layout.addRow(sub_category, self.sub_category_ip)
        layout.addWidget(self.custom_sub_category_ip)
        layout.addRow(category, self.category_ip)
        layout.addWidget(self.custom_category_ip)

        submit_button = QPushButton(" Submit ")
        submit_button.clicked.connect(self.submit_pmaster)
        submit_button.setMaximumWidth(200)
        
        submit_button.setStyleSheet("""
            background-color: #14532d;  
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)

        button_container = QWidget()
        button_layout = QHBoxLayout()
        
        button_layout.addWidget(submit_button)
        
        button_container.setLayout(button_layout)
        button_container.setMaximumHeight(60)
        button_container.setStyleSheet("""  background-color: rgba(0, 0, 0, 0); border : rgba(0, 0, 0, 0);  """)
        
        layout.addWidget(button_container)

        # Final layout setup
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

        # background gradient for the full widget
        self.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(33, 33, 33, 255),
                    stop:1 rgba(64, 64, 64, 255)
                );
            }
        """)

    def submit_pmaster(self):
        
        if self.category_ip.currentText() == "Other..." :
            main_cat = self.custom_category_ip.text()
        else :
            main_cat = self.category_ip.currentText()

        s = self.sub_category_ip.currentText()
        sub_cat = s if s!= "Other..." else self.custom_sub_category_ip.text()

        u =  self.unit_mes_input.currentText()
        m_unit = u if u != "Other..." else self.custom_unit_input.text()

        form = (
            self.Barcode_input.text(),                    # QLineEdit
            self.SKU_Id_ip.text(),                        # QLineEdit
            main_cat,
            sub_cat,
            self.Product_name_input.text(),               # QLineEdit
            self.Product_desc_input.toPlainText(),        # QTextEdit
            self.Tax_ip.value(),                          # QDoubleSpinBox
            self.price_input.value(),                     # QDoubleSpinBox
            m_unit
        )
        image = self.img_file or None
        
        dtbase.store_productmaster(form)
        dtbase.store_product_images(image, self.SKU_Id_ip.text() )
        QMessageBox.information(self, "Updated Database", "Successfully stored form !")

        fields = [self.category_ip, self.sub_category_ip, self.unit_mes_input,self.Barcode_input , self.SKU_Id_ip, self.Product_name_input,
                  self.Product_desc_input,  self.Tax_ip , self.price_input ]
        for field in fields :
            field.clear()

    def fdialog(self) :
        file_path, _ = QFileDialog.getOpenFileName(
                self, 
                "Select an image", 
                "", 
                "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
            )
        self.img_file = file_path or None

    def get_blur_effect(self):
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(15)
        return blur_effect

    def on_unit_selected(self, index=None):
        if self.unit_mes_input.currentText() == "Other...":
            self.custom_unit_input.setVisible(True)
        else:
            self.custom_unit_input.setVisible(False)
    def on_subcat_selected(self, index=None):
        if self.sub_category_ip.currentText() == "Other...":
            self.custom_sub_category_ip.setVisible(True)
        else:
            self.custom_sub_category_ip.setVisible(False)
    def on_cat_selected(self, index=None):
        if self.category_ip.currentText() == "Other...":
            self.custom_category_ip.setVisible(True)
        else:
            self.custom_category_ip.setVisible(False)

    def blank_double_spinbox(self, max_val=1000000.0):
        spinbox = QDoubleSpinBox()
        spinbox.setRange(0.0, max_val)
        spinbox.setDecimals(2)
        spinbox.setSpecialValueText(" ")  # visually blank
        spinbox.setValue(spinbox.minimum())  #  0 internally
        spinbox.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.15);
            color: gray;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px;
            border-radius: 12px;
        """)
        return spinbox
