# SENA_TEST Project

## Project Overview
SENA_TEST is a backend system designed to automate the management and commercialization of agricultural products for SENA regional Risaralda. The backend provides inventory, sales, user, invoice, notification, and analytics management via a RESTful API. The project is built with FastAPI and PostgreSQL, following a modular monolithic architecture.

**Current Status:**
- **Backend:** Fully functional (API endpoints for inventory, sales, users, invoices, notifications, analytics, and multi-warehouse management).
- **Frontend:** _Not implemented yet._
- **Unit/Integration Tests:** _Not implemented yet._
- **Docker/Containerization:** _Docker and Docker Compose files are present, but not fully tested or documented. Use at your own risk._
- **Only the backend is currently supported and tested._

## Features
- Inventory and multi-warehouse management
- Product and sales management
- User authentication and role-based access (JWT)
- Invoice and notification system
- Reports and analytics (export to PDF/Excel)
- Transaction history
- (Planned) Offline sync and mobile app support

## Setup Instructions

Follow these steps to set up and run the backend in a Python virtual environment.

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

5. **Create the Database**
   The project uses a local SQLite database for development and testing (neither MongoDB nor PostgreSQL was used due to time constraints).
   Run the following command to initialize the database:
   ```powershell
   python init_db.py
   ```

6. **Run the Application**
   ```powershell
   python -m uvicorn src.main:app --reload
   ```

7. **Deactivate the Virtual Environment** (when done)
   ```powershell
   deactivate
   ```

## Documentation
- See the `docs/` folder for architecture, requirements, coding rules, and workflow test steps.
- Manuals for deployment, development, and user instructions are in `docs/manuals/`.
- UML diagrams are in the `uml/` folder.

## Limitations & Roadmap
- **Frontend:** Not implemented yet.
- **Unit/Integration Tests:** Not implemented yet. See `docs/manuals/test_coverage_and_instructions.md` for future test plans.
- **Docker:** Docker and Docker Compose files are present but not fully tested. Use with caution.
- **Offline sync, mobile app, and advanced permission management:** Planned for future releases.
- **Database:** Uses SQLite for now; migration to PostgreSQL or MongoDB is planned for future versions.

## Contact & Contribution
- For technical questions, see the developer manual or contact the project lead.
- Contributions are welcome! Please follow the coding rules and document your changes.

---

For further details, refer to the documentation in the `docs/` folder.
