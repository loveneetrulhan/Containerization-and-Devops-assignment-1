# 📦 Containerized Web Application with PostgreSQL (Assignment 1)

## 👤 Name: Loveneet Rulhan
## Sap -id :500123392
## batch : 3


## 📚 Subject: Containerization and DevOps

## 📅 Semester: 6

---

# 🎯 Objective

To design, containerize, and deploy a web application using:

* PostgreSQL (Database)
* FastAPI (Backend)
* Docker & Docker Compose
* Macvlan networking with static IP

---

# 🏗️ Project Architecture

Client → Backend (FastAPI) → PostgreSQL Database

* Backend communicates with DB using environment variables
* Macvlan network used for static IP
* Bridge network used for host access

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

# 🌐 Network Configuration

* Macvlan network created with subnet
* Static IP assigned:

  * DB → 192.168.1.10
  * Backend → 192.168.1.20

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

# 🌐 API Testing

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

The project successfully demonstrates containerization of a web application using Docker.
It also highlights networking concepts such as macvlan isolation and bridge network communication.

---

# 🚀 END
