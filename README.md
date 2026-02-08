# Django REST Framework Mastery

A comprehensive Django REST Framework (DRF) project covering core DRF concepts **except authentication**. This repository serves as a practical guide for understanding DRF through hands-on examples, focusing on class-based views, serializers, pagination, nested serializers, and more.

---

## Project Overview

This project demonstrates how to build RESTful APIs using Django REST Framework. It is designed as a learning resource for anyone who wants to understand DRF in-depth, with examples for:

- Class-Based Views (`APIView`, `GenericAPIView`, Mixins)  
- Function-Based Views  
- Serializers & Nested Serializers  
- Pagination (PageNumber, LimitOffset, Cursor)  
- Querysets and filtering  
- Handling CRUD operations efficiently  

> **Note:** Authentication, permissions, and token-based access are intentionally **not covered** in this repository.

---

## Features Covered

- **Class-Based Views**
  - `APIView`
  - `GenericAPIView` with Mixins (`ListModelMixin`, `CreateModelMixin`, `RetrieveModelMixin`, etc.)
  - Fully customized CRUD operations

- **Serializers**
  - Model Serializers
  - Custom validation
  - Nested Serializers for handling relational data

- **Pagination**
  - PageNumber Pagination
  - LimitOffset Pagination
  - Cursor Pagination

- **Filtering & Search**
  - Basic queryset filtering
  - Search filters

- **Error Handling**
  - Proper API response messages
  - Status codes handling

---

## Getting Started

These instructions will help you set up the project locally for learning and experimentation.

### Prerequisites

- Python 3.10+
- Django 4.x
- Django REST Framework 3.x
- Pip or Poetry

---

