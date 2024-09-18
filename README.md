### DiscoVista Multi-Vendor App

#### Overview
DiscoVista is a multi-vendor marketplace application designed to allow multiple sellers to list and sell products under one platform. This app facilitates user registration for vendors and buyers, product listings, an intuitive dashboard for managing sales, orders, and vendor profiles. The app also integrates user authentication and basic e-commerce functionalities to provide a seamless buying and selling experience.

---

### Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

### Features

1. **Multi-vendor Marketplace**: Supports multiple vendors who can create their shops and list products for sale.
2. **User Authentication**: Includes a secure login, registration, and password reset system.
3. **Vendor Dashboard**: A detailed dashboard for vendors to manage their products, orders, and profile.
4. **Product Management**: Vendors can add, edit, and delete products with product descriptions, images, and pricing.
5. **Order Management**: Vendors can view and manage customer orders.
6. **Search & Filter**: Buyers can search for products and filter them based on categories and pricing.
7. **Shopping Cart & Checkout**: Buyers can add products to their cart and proceed to checkout with order summaries.
8. **Responsive Design**: The app is fully responsive and works seamlessly on mobile and desktop devices.
9. **Error Handling**: Proper error handling for invalid credentials and form submissions.

---

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/discovista-multi-vendor-app.git
cd discovista-multi-vendor-app
```

#### 2. Install Dependencies

Make sure you have Python installed, then set up the virtual environment and install the dependencies:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

#### 3. Set Up the Database

Run the following command to apply the initial migrations and set up the database:

```bash
python manage.py migrate
```

#### 4. Create a Superuser

To access the Django admin panel and manage the application, create a superuser:

```bash
python manage.py createsuperuser
```

#### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Now, you can access the application at `http://127.0.0.1:8000`.

---

### Configuration

#### 1. Environment Variables

Create a `.env` file in the root directory for storing your environment-specific configurations:

```bash
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=127.0.0.1, localhost
DATABASE_URL=your_database_url
```

#### 2. Database Setup

The app is configured to work with SQLite by default. To use another database (e.g., PostgreSQL), update your `DATABASE_URL` in the `.env` file accordingly.

#### 3. Static Files

To collect static files for production, run:

```bash
python manage.py collectstatic
```

---

### Usage

1. **Admin Panel**: Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage users, products, vendors, and orders.
2. **Vendor Registration**: Vendors can register their accounts and create a shop for listing products.
3. **Product Management**: Vendors can manage product listings through the dashboard, including uploading images and managing stock.
4. **Order Management**: Vendors can view customer orders and update order statuses (pending, shipped, completed).

---

### Project Structure

```bash
discovista/
│
├── discovista/               # Project-wide settings
│   ├── settings.py           # Django project settings
│   ├── urls.py               # URL routing for the application
│   ├── wsgi.py               # WSGI application setup
│
├── apps/
│   ├── accounts/             # User authentication and vendor registration
│   ├── marketplace/          # Core marketplace features (products, orders)
│   ├── orders/               # Order management logic
│   ├── dashboard/            # Vendor dashboard for managing listings
│
├── static/                   # Static assets (CSS, JS, images)
│
├── templates/                # HTML templates
│   ├── base.html             # Main base template
│   ├── login.html            # User login page
│   ├── register.html         # User registration page
│   ├── dashboard.html        # Vendor dashboard
│
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── .env                      # Environment configuration file
```

---

### Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript (Bootstrap for responsive design)
- **Database**: SQLite (Default), PostgreSQL (Optional)
- **Authentication**: Django Authentication with CSRF protection
- **Deployment**: Gunicorn, Nginx (for production setup)

---

### Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

Feel free to open issues for suggestions or bug reports.

---

### License

This project is licensed under the MIT License.

---

### Contact

For any inquiries or support, please contact us at: support@discovista.com

