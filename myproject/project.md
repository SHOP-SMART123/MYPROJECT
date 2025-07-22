# 🛍 Shop Smart

*Shop Smart* is an e-commerce platform built with *Python* and *PostgreSQL*, providing core functionalities like user registration, product listing, cart management, and order processing. It is designed as part of a Final Year Project (FYP).

---

## 🚀 Features

- 👤 User and Admin management
- 📦 Product listing and stock control
- 🛒 Shopping cart with quantity tracking
- 🧾 Order placement and history
- 🔐 Secure password hashing and login system
- 🗃 PostgreSQL database integration via psycopg2
- 📡 REST API support using *FastAPI*

---

## 🧩 Technologies Used

- *Backend*: Python 3, FastAPI
- *Database*: PostgreSQL
- *Libraries*: psycopg2, passlib (for password hashing)
- *Tools*: VS Code, pgAdmin, Git & GitHub

---

## 🛠 Project Structure

SHOP SMART/ └── myproject/ ├── main.py          # App entry point (FastAPI or CLI) ├── db.py            # Database connection handler ├── user.py          # User CRUD functions ├── product.py       # Product CRUD functions ├── order.py         # Order management ├── cart.py          # Cart operations ├── ...

---

## 🔌 Database Schema

The PostgreSQL database includes the following tables:

- users
- admins
- products
- cart
- orders

All tables are linked via foreign keys where appropriate.

---

## 📦 Installation & Usage

### 1. Clone the Repository

bash
git clone https://github.com/SHOP-SMART123/MYPROJECT.git
cd MYPROJECT/myproject

