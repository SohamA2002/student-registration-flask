
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

# ⚙️ How It Works

1. User visits the app and submits the registration form.
2. Flask handles the request and stores the form data in MySQL RDS.
3. GitHub holds the project code.
4. Jenkins monitors the GitHub repo and triggers a deployment pipeline on code changes.
5. The updated Flask app is deployed to the EC2 server.

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

# 📦 Setup Guide (Step-by-Step)

# 🔹 Step 1: RDS MySQL Setup

- Launch RDS:
  - Engine: MySQL
  - DB Name: `studentdb`
  - Username: `admin`
  - Password: `*****123`
  - Public Access: Yes (for testing)
- Create RDS Security Group:
  - Type: MySQL/Aurora
  - Port: 3306
  - Source: EC2 Security Group

📌 Save your:
Endpoint: student-db.****.rds.amazonaws.com
Username/password

# 🔹 Step 2: EC2 + Flask Setup
- Launch EC2 (Ubuntu) in Public Subnet with:
  - Port 22 (SSH)
  - Port 5000 (Flask)
  - Port 8080 (Jenkins)
- SSH & install dependencies
  
- Clone project & setup Flask:
  
```bash
git clone https://github.com/SohamA2002/student-registration-flask.git
cd student-registration-flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Edit `app.py`, `config.py`, `register.html`, for public access:

```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

- Set correct `db_config` using RDS credentials.

- Check your terminal. After running 'python app.py' , you should see:

```
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

- Open the correct URL:
  - In EC2: [http://<your-ec2-public-ip>:5000] in your browser.
  - Form will be Visible

---

# 🔹 Step 3: Jenkins Installation 

- Create Jenkinsfile (in root of repo)
```
  - student-registration-flask/
    ├── app.py
    ├── config.py        
    ├── requirements.txt 
    ├── templates/
    │   └── register.html
    └── Jenkinsfile ✅ CI/CD pipeline
```
  ✅ Replace the GitHub URL with your actual repo URL.

- Install Jenkins on EC2
```bash
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update -y
sudo apt install openjdk-17-jdk jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

- Visit `http://<EC2-Public-IP>:8080`  
- Unlock Jenkins using:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

---

# 🔹 Step 4: Jenkins CI/CD Pipeline

 - Click New Item → Freestyle or Pipeline → Give it a name
 - Choose Pipeline, click OK
 - Scroll to Pipeline > Definition: Pipeline script from SCM
   - Set:
   - SCM: Git
   - Repository URL: your GitHub repo
   - Script Path: Jenkinsfile (default)
   - Save and click Build Now

---
     
# 🔹 Step 5: Test the Application

- Jenkins Console: ✅ Build should show SUCCESS  
- Verify `gunicorn` process is running:

```bash
ps aux | grep gunicorn
```

- Visit the app in browser:

```
http://<your-ec2-ip>:5000
```

- Fill the registration form and test RDS insert

---

# 🙋‍♀📬 Author

**Soham Arekar**  
📧 sohamarekar2002@gmail.com




















