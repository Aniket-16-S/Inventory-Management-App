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

The app includes the following UI structure:

- **Login Page:** Simple login form with two pre-configured operator accounts
- **Main Window:** Tabbed interface with three modules:
  - *Goods Receiving*
  - *Sales Entry*
  - *Product Master*

---
## Clone / Contribute

### 1. Clone the Repository

```bash
git clone (not published yet)
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
