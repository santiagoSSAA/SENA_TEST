# SENA_TEST Project

## Setup Instructions

Follow these steps to set up and run the project in a Python virtual environment.

### Prerequisites
- Python 3.12 or higher installed on your system.
- `pip` (Python package manager) installed.

### Steps to Execute

1. **Clone the Repository**
   ```powershell
   git clone <repository-url>
   cd SENA_TEST
   ```

2. **Create a Virtual Environment**
   ```powershell
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```powershell
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```powershell
   python src/main.py
   ```

6. **Deactivate the Virtual Environment** (when done)
   ```powershell
   deactivate
   ```

### Notes
- Ensure that you have the correct version of Python installed.
- If you encounter any issues, verify that all dependencies are installed correctly by re-running `pip install -r requirements.txt`.

---

For further details, refer to the documentation in the `docs/` folder.
