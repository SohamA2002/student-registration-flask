
# 🎓 Flask-Based Student Registration Web Application deployed using Jenkins

A complete full-stack deployment of a Flask-based Student Registration Web Application using Jenkins CI/CD, hosted on **AWS EC2**, and connected to **AWS RDS MySQL** in a custom VPC.

---

# 🚀 Project Overview

This project demonstrates:

- Flask-based web application (Student Registration)
- CI/CD pipeline using Jenkins
- Deployment on EC2
- MySQL database hosted on AWS RDS
- Secure infrastructure inside custom VPC
- Gunicorn for production server

---

# ☁️ Architecture

            +----------------------+
            |   End User (Browser) |
            +----------+-----------+
                       |
                       v
           +-----------+------------+
           |       Flask App        |
           |     (Running on EC2)   |
           +-----------+------------+
                       |
                       v
         +-------------+--------------+
         |    Amazon RDS (MySQL)      |
         +----------------------------+

        +----------------------------+
        |       Jenkins Server       |
        |     (Also on EC2 or local) |
        +----------------------------+
---
