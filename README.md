# 🧳 AI Travel Planner

An **AI-powered travel planning assistant** that generates smart itineraries and trip recommendations using **LangChain** and **Groq LLMs**.
The app runs with **Streamlit** and is fully containerized for deployment on **Docker + Kubernetes**, with monitoring/logging via the **ELK stack**.

---

## 🚀 Features

* ✅ AI-driven **itinerary generation**
* ✅ **Context-aware planning** with LangChain
* ✅ Interactive **Streamlit frontend**
* ✅ Cloud-ready: **Docker + Kubernetes** deployment
* ✅ **ELK stack** (Elasticsearch, Logstash, Kibana, Filebeat) for logs

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-%F0%9F%A4%96-orange)
![Groq](https://img.shields.io/badge/LLM-Groq-green)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-326CE5)
![ELK](https://img.shields.io/badge/Logs-ELK_Stack-yellow)

---

## 📂 Project Structure

```bash
AI-TRAVEL-AGENT/
│── logs/                          # Application logs
│── src/
│   ├── chains/
│   │   └── itinerary_chain.py      # Core itinerary generation
│   ├── config/
│   │   └── config.py               # App configuration
│   ├── core/
│   │   └── planner.py              # Travel planning logic
│   └── utils/
│       ├── custom_exception.py     # Error handling
│       └── logger.py               # Logging
│
│── app.py                          # Streamlit entrypoint
│── Dockerfile                      # Containerization
│── k8s-deployment.yaml             # Kubernetes deployment
│── elasticsearch.yaml              # Elasticsearch config
│── kibana.yaml                     # Kibana config
│── logstash.yaml                   # Logstash config
│── filebeat.yaml                   # Filebeat config
│── requirements.txt                # Dependencies
│── setup.py                        # Package installation
│── script.sh                       # Helper script
│── LICENSE                         # License file
│── README.md                       # Documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sushant097/AI-Travel-Planner.git
cd AI-Travel-Planner
```

### 2️⃣ Install Package

```bash
pip install -e .
```

### 3️⃣ Setup `.env`

Create `.env` file with:

```ini
GROQ_API_KEY=""
```

### 4️⃣ Run Locally

```bash
streamlit run app.py
```

---

## ☁️ Deploy on Google Cloud VM

### Step 1: Create VM Instance

* Machine: **E2 Standard (16 GB RAM)**
* Boot Disk: **Ubuntu 24.04 LTS (256 GB)**
* Networking: Enable **HTTP/HTTPS**

### Step 2: Install Docker

```bash
sudo apt update && sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
docker run hello-world
```

Allow running without sudo:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

### Step 3: Install Minikube & kubectl

```bash
# Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start

# kubectl
sudo snap install kubectl --classic
kubectl version --client
```

### Step 4: Build & Deploy App

```bash
eval $(minikube docker-env)

docker build -t streamlit-app:latest .

kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY=""

kubectl apply -f k8s-deployment.yaml
kubectl get pods
```

Forward service:

```bash
kubectl port-forward svc/streamlit-service 8501:80 --address 0.0.0.0
```

App available at: `http://<VM_IP>:8501`

---

## 📊 ELK Stack Setup on Kubernetes (for Logs)

### Step 1: Namespace

```bash
kubectl create namespace logging
```

### Step 2: Deploy Elasticsearch

```bash
kubectl apply -f elasticsearch.yaml -n logging
kubectl get pods -n logging
```

### Step 3: Deploy Kibana

```bash
kubectl apply -f kibana.yaml -n logging
kubectl port-forward -n logging svc/kibana 5601:5601 --address 0.0.0.0
```

Access Kibana at: `http://<VM_IP>:5601`

### Step 4: Deploy Logstash

```bash
kubectl apply -f logstash.yaml -n logging
kubectl get pods -n logging
```

### Step 5: Deploy Filebeat

```bash
kubectl apply -f filebeat.yaml -n logging
kubectl get pods -n logging
```

### Step 6: Configure Kibana Index

1. Open Kibana → `Stack Management → Index Patterns`
2. Create pattern: `filebeat-*`
3. Set timestamp field: `@timestamp`

### Step 7: Explore Logs

In **Analytics → Discover**, filter logs by:

* `kubernetes.container.name`
* `kubernetes.pod.name`

✅ **Now you can monitor and analyze app logs in real-time.**

---

## 📦 Requirements

`requirements.txt`:

```
langchain
langchain-core
langchain-groq
langchain-community
python-dotenv
streamlit
```

---

## 🔮 Roadmap

* [ ] Add multi-day itinerary planner
* [ ] Add user preference memory (e.g., budget, destination type)
* [ ] Integrate external APIs (flights, hotels)
* [ ] Expand observability with Grafana

---

## 📜 License

MIT License