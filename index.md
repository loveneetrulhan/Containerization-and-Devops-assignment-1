# 📦 Containerized Web Application with PostgreSQL (Assignment 1)

## 👤 Name: Loveneet Rulhan
## Sap -id :500123392
## batch : 3


## 📚 Subject: Containerization and DevOps

## 📅 Semester: 6

---
# 📘 Introduction

Containerization is a modern approach to software deployment that packages an application along with all its dependencies into a standardized unit called a container. This ensures that the application runs consistently across different environments such as development, testing, and production.

In this project, we have implemented a containerized web application using Docker and Docker Compose. The system includes a backend API built with FastAPI and a PostgreSQL database. The application demonstrates key DevOps concepts such as container orchestration, networking, and persistent storage.

This approach improves portability, scalability, and deployment efficiency compared to traditional methods. :contentReference[oaicite:0]{index=0}

---

# 🎯 Objectives

The main objectives of this assignment are:

- To understand the concept of containerization
- To build and deploy a multi-container application
- To use Docker Compose for orchestration
- To implement networking using macvlan and bridge
- To demonstrate data persistence using volumes
- To test REST APIs using curl
- To understand isolation in container networking

This project provides hands-on experience with real-world DevOps practices.

---

# 🏗️ System Architecture

The system consists of the following components:

- **Backend Service (FastAPI)**  
  Handles API requests and interacts with the database.

- **Database Service (PostgreSQL)**  
  Stores application data persistently.

- **Docker Compose**  
  Manages multiple containers and their configurations.

- **Networks**  
  - Macvlan network for static IP assignment  
  - Bridge network for host access

- **Volumes**  
  Used to persist database data even after container restart.

The architecture follows a microservices-based approach where each component runs in its own container.

---

# 📁 Project Structure

```
assignment-1/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── db/
│   ├── Dockerfile
│   └── init.sql
│
└── docker-compose.yml
```

📸 Screenshot:
![Project Structure](images_assignment/1_project_structure.png.png)

---

# ⚙️ Backend Implementation

* FastAPI used to build REST APIs
* Endpoints:

  * `/` → Health check
  * `/insert` → Insert data
  * `/data` → Fetch data

📸
![Backend Code](images_assignment/2_backend_app_code.png.png)

📸
![Backend Dockerfile](images_assignment/3_backend_dockerfile.png.png)

📸
![Requirements](images_assignment/4_requirements.png.png)

---

# 🗄️ Database Setup

* PostgreSQL container with custom Dockerfile
* Initialization script creates table

📸
![DB Dockerfile](images_assignment/5_db_dockerfile.png.png)

📸
![Init SQL](images_assignment/6_init_sql.png.png)

---

# 🔗 Docker Compose Configuration

* Two services: backend & db
* Static IP assigned using macvlan
* Volume used for persistence
* Bridge network added for host access

📸
![Docker Compose](images_assignment/7_docker_compose.png.png)

---

# 🌐 Networking

Two types of networks are used in this project:

### 🔹 Macvlan Network
- Assigns static IP addresses to containers
- Allows containers to appear as separate devices on the network
- Provides better isolation

### 🔹 Bridge Network
- Enables communication between containers and host
- Used for accessing services via localhost

This combination ensures both isolation and accessibility.

📸
![Network Creation](images_assignment/8_network_creation.png.png)

---

# 🚀 Build & Run

```bash
docker compose up --build -d
```

📸
![Build Process](images_assignment/9_docker_build.png.png)

---

# 🐳 Running Containers

```bash
docker ps
```

📸
![Running Containers](images_assignment/10_running_containers.png.png)

---

# 🔍 Network Inspection

```bash
docker network inspect my_macvlan
```

📸
![Network Inspect](images_assignment/11_network_inspect.png.png)

---

# 🧪 API Testing

The backend API provides the following endpoints:

- `/` → Health check
- `/insert` → Insert data into database
- `/data` → Retrieve stored data

Testing was done using curl commands from the terminal. This confirms that the backend and database are correctly connected.

## Root API

```bash
curl http://localhost:8000/
```

📸
![API Root](images_assignment/12_api_root.png.png)

---

## Insert Data

```bash
curl -X POST http://localhost:8000/insert
```

📸
![Insert](images_assignment/13_api_insert.png.png)

---

## Fetch Data

```bash
curl http://localhost:8000/data
```

📸
![Data](images_assignment/14_api_data.png.png)

---

# 💾 Volume Persistence

Docker volumes are used to store database data outside the container.

Benefits:
- Data is not lost when containers are stopped
- Enables backup and recovery
- Improves reliability of the application

This was verified by restarting containers and checking that data remained unchanged.

## Before Restart

📸
![Before Restart](images_assignment/15_data_before_restart.png.png)

---

## Stop Containers

```bash
docker compose down
```

📸
![Stopped](images_assignment/16_containers_stopped.png.png)

---

## Restart Containers

```bash
docker compose up -d
```

📸
![Restart](images_assignment/17_containers_restart.png.png)

---

## After Restart

📸
![After Restart](images_assignment/18_data_after_restart.png.png)

---

# 📊 Logs & Inspection

```bash
docker logs backend_app
```

📸
![Logs](images_assignment/19_backend_logs.png.png)

---

```bash
docker inspect backend_app
```

📸
![Inspect](images_assignment/20_container_inspect.png.png)

---

```bash
docker volume ls
```

📸
![Volumes](images_assignment/21_volume_list.png.png)


---

# ⚠️ Macvlan Limitation

```bash
curl http://192.168.1.20:8000   ❌
curl http://localhost:8000      ✅
```

📸
![Macvlan Limitation](images_assignment/23_macvlan_limitation.png.png)

---

# 🧠 Explanation

Macvlan network isolates containers from the host system.
Therefore:

* Direct access using container IP fails
* Port mapping with bridge network allows access

---
# ⚠️ Challenges Faced

During the project, the following challenges were encountered:

- Docker Compose not working in WSL initially
- Macvlan network not accessible from host
- GitHub authentication using token
- Image path issues in Markdown
- Port mapping configuration errors

All issues were resolved through debugging and proper configuration.

---

# 📌 Key Features Implemented

✔ Docker multi-stage builds
✔ PostgreSQL container with custom config
✔ Static IP assignment (macvlan)
✔ Docker Compose orchestration
✔ Volume persistence
✔ API endpoints
✔ Network isolation demonstration

---

# 🏁 Conclusion

This project successfully demonstrates the implementation of containerization using Docker and Docker Compose. It highlights key DevOps concepts such as service orchestration, networking, and data persistence.

Containerization provides significant advantages including portability, scalability, and efficient deployment. It is widely used in modern software development and cloud environments.

Overall, this assignment provided practical exposure to real-world DevOps tools and techniques.
---

# 🚀 END

