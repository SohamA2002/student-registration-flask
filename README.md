
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

# ⚙️ Technologies Used

| Category            | Technology                   | Purpose                                          |
| ------------------- | ---------------------------- | ------------------------------------------------ |
| **Frontend**        | `HTML`, `CSS`                | UI for student registration form                 |
| **Backend**         | `Python`, `Flask`            | Web framework and app logic                      |
| **Database**        | `MySQL (Amazon RDS)`         | Persistent storage for student records           |
| **Version Control** | `Git`, `GitHub`              | Source code management                           |
| **CI/CD**           | `Jenkins`, `Jenkinsfile`     | Continuous Integration and Deployment            |
| **Hosting**         | `AWS EC2`                    | Virtual server to run the Flask app              |
| **Networking**      | `AWS VPC`, `Security Groups` | Isolated network environment and traffic control |
| **Dependency Mgmt** | `pip`, `requirements.txt`    | Python package installation                      |
| **Virtual Env**     | `venv`                       | Isolate Python environment for app               |

---
