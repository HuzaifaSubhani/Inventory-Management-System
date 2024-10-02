# Inventory Management System

This is a Django-based Inventory Management System that manages inventory with the following features:
- **User Authentication and Authorization** (Role-based access control)
- **CRUD Operations** for products and orders
- **Forgot Password Functionality**
- **Django Signals** for notifications
- **Graphical Dashboard** for visualizing inventory data

## Features
- **User Roles**: Separate views for staff and admin.
- **CRUD Functionality**: Ability to create, read, update, and delete inventory products.
- **Graphs**: Graphs showing the trends in inventory data.
- **Forgot Password**: Allows users to reset their password via email.
- **Authentication**: User login, logout, and registration functionality.
- **Profile Management**: Users can update their profile and upload profile pictures.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (for development)
- **Graphs**: Chart.js
- **Other**: Django Signals for profile creation

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/inventory-management-system.git
    cd inventory-management-system
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application** in your browser:
    ```
    http://127.0.0.1:8000/
    ```

## Screenshots
(Add screenshots here if you'd like to showcase parts of your system, like the dashboard or product listing.)

## Usage
1. **Admin Access**: Admin users can add, update, or delete products.
2. **Staff Access**: Staff can view their assigned tasks and products.
3. **Forgot Password**: Users can recover their account password via email.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
