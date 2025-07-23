# 🍽️ Django Food App - CRUD Operation Project

A simple yet effective web application built using **Django** that allows users to perform **CRUD operations** (Create, Read, Update, Delete) on food menu items. The project includes **user authentication**, **admin control**, and a clean **Bootstrap UI** for a smooth user experience.

---

## 🚀 Features

- ✅ User Registration & Login (Authentication)
- ✅ Add, View, Update, Delete food items (CRUD)
- ✅ Django Admin Panel for easy database control
- ✅ Responsive UI with Bootstrap and custom CSS
- ✅ Profile page to view user information
- ✅ Image support via URL for food items
- ✅ Logout page with custom message

---

## 📸 Screenshots

- Home Page:
  
  <img width="1889" height="877" alt="Screenshot (528)" src="https://github.com/user-attachments/assets/e444065b-5f09-4ede-809b-6945a343a40d" />

- Add Item:
  
  <img width="1920" height="871" alt="Screenshot (529)" src="https://github.com/user-attachments/assets/ad490c22-a2c3-45a5-b055-7a44d552e00d" />

- Profile Page:

  <img width="1920" height="867" alt="Screenshot (530)" src="https://github.com/user-attachments/assets/6b8d283d-c76a-4c73-bc10-2d22b9aec140" />

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Django (Python)
- **Database:** SQLite (default in Django)
- **Tools Used:** VS Code, Git, GitHub

---

## 🧪 How to Run the Project

1. **Clone the repository**

```
git clone https://github.com/yourusername/foodapp-django.git
cd FoodProject
```

2. **Create and activate a virtual environment**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```
pip install -r requirements.txt

```

4. **Run migrations**

```
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (admin)**

```
python manage.py createsuperuser

```

6. **Run the server**

```
python manage.py runserver

```

7. **Visit the app**

- Open your browser and go to: http://127.0.0.1:8000

---

## 🧩 CRUD Functionality Overview

| Action  | URL Path                | Description               |
|---------|--------------------------|---------------------------|
| Create  | `/additem/`              | Add a new food item       |
| Read    | `/`                      | View all menu items       |
| Update  | `/updateitem/<id>/`      | Update existing item      |
| Delete  | `/deleteitem/<id>/`      | Delete a food item        |

---

## 🔐 User Authentication

| Feature        | URL             |
|----------------|------------------|
| Register       | `/register/`     |
| Login          | `/login/`        |
| Logout         | `/logout/`       |
| Profile Page   | `/profile/`      |

---

## 📌 Requirements

- Python 3.8+

- Django 4.x

- SQLite (default)

---

##  License

- MIT License. Feel free to use and modify.





