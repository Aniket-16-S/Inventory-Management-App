# InvenSync - Inventory Management Desktop Application

InvenSync is a lightweight inventory management desktop application built using **Python** and **PySide6**, with data persistence powered by **SQLite3**  designed to streamline goods receiving, sales entry, and product tracking for small to medium-scale businesses.

---

## 🔧 Features

- **Secure Operator Login :**
   Authenticates operator access via local credentials stored in database.

- **Goods Receiving Form :**
   Capture product delivery details including supplier info, quantity, rate, tax, etc.

- **Sales Entry Form :**
   Record product sales along with customer info, pricing, and applicable taxes.

- **Product Master Management :**
   Maintain a centralized list of products with barcode, SKU, category, pricing, tax %, and default unit.

- **Data Persistence :**
   Stores all input data locally using **SQLite3** (can be swapped with MySQL if needed).

- **Smart Form Design :**
   - Dropdowns and validations for a clean user experience
   - Glassy UI style for better UX

- **Executable Build :**
   App is packaged as a `.exe` for direct use on Windows without needing to install Python.

---

## UI Overview

<p align="left">
<img src ="https://github.com/Aniket-16-S/Inventory-Management-App/blob/08a64ca391d24533edca18a81f262af1bb6b2098/OUTPUT/Output-2.png?raw=true" width="45%" />
&nbsp; &nbsp; &nbsp;
<img src="https://github.com/Aniket-16-S/Inventory-Management-App/blob/08a64ca391d24533edca18a81f262af1bb6b2098/OUTPUT/Output-1.png" width="45%" / >
</p>



The app includes the following UI structure:

- **Login Page:** Simple login form with two pre-configured operator accounts
- **Main Window:** Tabbed interface with three modules:
  - *Goods Receiving*
  - *Sales Entry*
  - *Product Master*

---
## Run the App
[click here](https://github.com/Aniket-16-S/Inventory-Management-App/blob/08a64ca391d24533edca18a81f262af1bb6b2098/InfoVentry.exe) to download
the exe file directly. 



## Clone / Contribute 

### 1. Clone the Repository

```bash
git clone https://github.com/Aniket-16-S/Inventory-Management-App.git
```
```bash
cd inventory-management-app
```
```bash
pip install -r requirements.txt
```
```bash
python main.py
```
---

## Tech Stack
- Python 3.10+

- PySide6 

- SQLite3 
---
## Operator Login (Demo)
| username | password 
|----------|----------
| infoware1  | pass@1  
| infoware2  | pass@2

---

##  Future Goals
- add read , update, delete operations in GUI
- Swap sqlite with Mysql for wider connectivity between devices

## ⚠️  Legal Disclaimer
This project is intended solely for educational purposes. It is not affiliated with or endorsed by any organization or individual, and is not intended to criticize, harm, or humiliate any entity in any way.
