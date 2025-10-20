# 🎯 Playwright Robot Driver (Python)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![Playwright](https://img.shields.io/badge/Playwright-1.40.0-green)](https://playwright.dev/python/)

This project is a **Python-based browser automation script using Playwright**.  
It automates a fixed workflow:

1. Opens a browser  
2. Navigates to a website  
3. Types into login fields  
4. Clicks the login button  
5. Searches for a product  
6. Prints the final result

---

## 🚀 Features

- ✅ Navigate to URL  
- ✅ Type into input fields  
- ✅ Click buttons  
- ✅ Handles slow or missing elements  
- ✅ Prints clear console output  

---

## 🛠️ Prerequisites

Make sure you have **Python 3.9+** installed:

```bash
python3 --version

If not installed:

brew install python

📁 Project Setup

    Create a project folder:

mkdir playwright_project
cd playwright_project

    (Optional) Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

    Install Playwright:

pip install playwright

    Install browser binaries:

playwright install

📂 File Structure

playwright_project/
│
├── venv/              # Virtual environment (optional)
├── robot_driver.py    # Main automation script
└── README.md          # Documentation

▶️ How to Run

Activate your virtual environment (if using one):

source venv/bin/activate

Run the script:

python3 robot_driver.py

✅ Expected Output

On success, the terminal prints:

✅ Page loaded successfully
✅ Login attempt completed
✅ Logged in successfully
✅ Success! Product 'Sauce Labs Backpack' found with price: $29.99

On failure, it prints relevant error messages.
