# Little Lemon

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Little Lemon is a landing page for a restaurant.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

1. **User-Friendly Landing Page:**
   - A visually appealing and user-friendly landing page that showcases the purpose and functionality of the application.

2. **Reservation Management:**
   - An intuitive admin panel for managing reservations easily.
   - View, create, edit, and delete reservations with ease.

3. **Database Integration:**
   - Integration with a database to persistently store reservation data.
   - Use of Django's ORM for efficient and organized data management.

4. **Backend Functionality:**
   - Implementation of backend functionality to handle reservation logic.
   - Customized backend code to ensure smooth communication between the frontend and database.

5. **Deployment-Ready:**
   - Configured for easy deployment, whether on a local development environment or a production server.

6. **Version Control:**
    - Utilization of Git for version control, enabling efficient collaboration and tracking changes over time.

7. **Security Measures:**
    - Implementation of security best practices to protect against common web vulnerabilities.


## Getting Started

### Prerequisites

- python
- pipfile includes all dependencies needed for this project

### Installation

1. Clone the repository:

```bash
git clone https://github.com/mkellner43/littlelemon.git
cd littlelemon
```

2. (optional) Use a python virtual env:

```bash
#recommended to use a virtual environment
pipenv shell

```

3. Install dependencies:
```bash
pipenv install
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser account:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the Application:
- Open your web browser and go to http://localhost:8000 to view the landing page. The admin panel is accessible at http://localhost:8000/admin.

## Usage
- Visit the landing page to explore your restaurant's offerings and ambiance.
- Customers can make reservations using the integrated reservation system.
- Admins can log in to the admin panel to manage reservations, view customer details, and update restaurant information.

**Happy coding from LittleLemon! 🍋**