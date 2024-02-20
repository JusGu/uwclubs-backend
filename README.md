# UWClubs Backend

The UWClubs Backend is a Django-based application designed to manage club information for the University of Waterloo. It provides endpoints for health checks, CSRF token retrieval, and a search functionality for querying club data.

## Quick Start Guide

To get the UWClubs Backend running locally, follow these steps:

### Prerequisites

- Python 3.11
- pip

### Setup

1. Clone the repository to your local machine.

2. Navigate to the project directory and create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. Apply the migrations to create the database schema:
   ```
   python manage.py migrate
   ```

2. Start the Django development server:
   ```
   python manage.py runserver
   ```

The server will start on `http://127.0.0.1:8000/`. You can access the provided endpoints (`/health/`, `/search/`, `/csrf/`) to interact with the application.
