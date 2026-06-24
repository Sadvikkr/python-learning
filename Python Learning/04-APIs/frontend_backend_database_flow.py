# =========================================
# FRONTEND - BACKEND - DATABASE ARCHITECTURE
# =========================================

# Every modern application follows:

# Frontend
#    ↓
# Backend
#    ↓
# Database


# =========================================
# FRONTEND
# =========================================

# Frontend is what the user sees and interacts with.

# Examples:
# Buttons
# Forms
# Images
# Dashboard
# Login Page

# Technologies:
# HTML
# CSS
# JavaScript
# React
# Flutter

# Think:
# Frontend = User Interface (UI)


# =========================================
# BACKEND
# =========================================

# Backend is the brain of the application.

# Responsibilities:
# Business Logic
# Authentication
# API Handling
# Validation
# Calculations

# Technologies:
# Python
# FastAPI
# Node.js
# Java

# Think:
# Backend = Brain


# =========================================
# DATABASE
# =========================================

# Database stores data permanently.

# Examples:
# Users
# Products
# Orders
# Reports
# Messages

# Databases:
# PostgreSQL
# MySQL
# MongoDB

# Think:
# Database = Memory


# =========================================
# DATA FLOW
# =========================================

# Frontend
#    ↓
# Sends Request
#    ↓
# Backend
#    ↓
# Processes Logic
#    ↓
# Database
#    ↓
# Returns Data
#    ↓
# Backend
#    ↓
# Frontend


# =========================================
# EXAMPLE: LOGIN SYSTEM
# =========================================

# User enters:
# Email
# Password

# Frontend
#    ↓
# POST Request
#    ↓
# Backend
#    ↓
# Checks Credentials
#    ↓
# Database
#    ↓
# Returns User Data
#    ↓
# Backend
#    ↓
# Login Success
#    ↓
# Frontend


# =========================================
# EXAMPLE: UPDATE STUDENT MARKS
# =========================================

# User clicks "Update Marks"

# Frontend
#    ↓
# PUT Request
#    ↓
# Backend
#    ↓
# Validate Request
#    ↓
# Database
#    ↓
# Update Marks
#    ↓
# Backend
#    ↓
# Success Message
#    ↓
# Frontend


# =========================================
# CRUD OPERATIONS
# =========================================

# CREATE -> POST
# READ   -> GET
# UPDATE -> PUT
# DELETE -> DELETE


# Student API Example

# POST   /students
# GET    /students
# PUT    /students
# DELETE /students


# =========================================
# IMPORTANT RULE
# =========================================

# Frontend should NOT directly access Database.

# Wrong:
# Frontend -> Database

# Correct:
# Frontend -> Backend -> Database

# Reason:
# Backend validates data,
# handles business logic,
# manages security,
# and protects the database.


# =========================================
# QUICK REVISION
# =========================================

# Frontend = UI
# Backend = Brain
# Database = Memory

# Flow:
# Frontend -> Backend -> Database
# Database -> Backend -> Frontend