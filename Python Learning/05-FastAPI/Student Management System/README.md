# 🎓 Student Management System API

A RESTful backend application built using **FastAPI** to practice backend development fundamentals and API design.

## 🚀 Features

* Create Student
* Get All Students
* Get Student by ID
* Update Student
* Delete Student
* Search Students
* Filter by Age
* Filter by Marks
* Sort Students
* Pagination
* Request Validation using Pydantic
* Response Models
* Dependency Injection
* Environment Variables
* Production-style Folder Structure

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn
* python-dotenv

---

## 📁 Project Structure

```text
app/
├── main.py
├── routes/
├── services/
├── schemas/
├── data/
├── dependencies.py
└── config.py
```

---

## ▶️ Run the Project

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Server

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

OpenAPI

```
http://127.0.0.1:8000/openapi.json
```

---

## 🎯 Learning Objectives

This project was built to learn:

* REST APIs
* FastAPI
* API Design
* Dependency Injection
* Request Validation
* Response Models
* Project Structure
* Backend Best Practices

---

## 🚧 Future Improvements

* PostgreSQL Integration
* SQLAlchemy ORM
* JWT Authentication
* Password Hashing
* Role-Based Authorization
* Docker
* Redis
* Deployment on AWS
* Unit Testing
* Logging
* CI/CD Pipeline
* Production Database

---

## 👨‍💻 Author

Sadvik Kumar

Backend Engineering Learning Project
