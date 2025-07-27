# FastAPI Quick‑Start Guide

> **Goal:** Get a simple FastAPI project running locally in an isolated Python environment.

---

## 1 . Prerequisites

| Tool   | Minimum Version | Check Command      |
| ------ | --------------- | ------------------ |
| Python | 3.8+            | `python --version` |
| pip    | 20.0+           | `pip --version`    |

> **Tip (Windows):** If multiple Python versions are installed, use `py -3.11` instead of `python`.

---

## 2 . Create a Virtual Environment

```bash
# Replace <env_name> with any name you like\python -m venv <env_name>
```

This creates an isolated directory containing its own Python interpreter and libraries.

---

## 3 . Activate the Environment

| OS                       | Command                            |
| ------------------------ | ---------------------------------- |
| **Windows (PowerShell)** | `.<env_name>\Scripts\Activate.ps1` |
| **Windows (CMD)**        | `.<env_name>\Scripts\activate.bat` |
| **macOS / Linux**        | `source <env_name>/bin/activate`   |

You should see the env name prefixed in your shell prompt, e.g. `(<env_name>) C:\>`.

---

## 4 . Install FastAPI & Uvicorn

```bash
pip install fastapi uvicorn[standard]
```

> **Why Uvicorn?** It’s a high‑performance ASGI server that runs your FastAPI app.

---

## 5 . Create a Minimal App

`main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}
```

---

## 6 . Run the App (Hot‑Reload)

```bash
uvicorn main:app --reload
```

- Navigate to [**http://127.0.0.1:8000**](http://127.0.0.1:8000) to see JSON output.
- Interactive docs available at **/docs** (Swagger UI) and **/redoc**.

---

## 7 . Deactivate the Environment

```bash
deactivate
```

---

## 8 . Common Troubleshooting

| Issue                                                                             | Fix                                                                                                                 |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| *“Scripts cannot be loaded because running scripts is disabled”* (Win PowerShell) | Run PowerShell as Administrator and execute: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Old packages lingering                                                            | Delete the env folder and create a new one with the steps above.                                                    |

---

[Open PDF](fastapi.pdf)

---

© 2025 Gaurav — Feel free to copy, adapt, and share.

