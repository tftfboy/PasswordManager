# Password Manager (Day 29)

A simple Tkinter password manager app built in Python.

## Features
- Generate a random password
- Save website, email, and password entries
- Search saved credentials by website
- Copy generated password to clipboard

## Requirements
- Python 3.9+
- `pyperclip`

## Setup
1. Open a terminal in this folder.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run
```bash
python main.py
```

## Notes
- The app writes credentials to `password.json`.
- `password.json` is ignored by git in `.gitignore` so local credentials are not pushed.
- `logo.png` must remain in the same folder as `main.py`.
