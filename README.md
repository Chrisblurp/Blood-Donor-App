# 🩸 Blood Donor App — Cloud-Native DevOps Platform

A production-style **cloud-native Blood Donor Management System** designed to demonstrate real-world DevOps practices, including Kubernetes orchestration, GitOps, CI/CD automation, observability, and infrastructure provisioning.

---

## 🚀 Project Overview

This project goes beyond application development and focuses on **end-to-end DevOps engineering**.

It simulates a real-world healthcare system where users can register and manage blood donations, while showcasing how modern infrastructure is built, deployed, and maintained in production environments.

---

🧰 Prerequisites / Required Tools

Before running this project locally or deploying it, ensure the following tools are installed:

🖥️ Core Tools
Docker
Used for containerizing all services
https://docs.docker.com/get-docker/
Docker Compose
Used for local multi-service orchestration
https://docs.docker.com/compose/install/
Kubernetes (kubectl)
CLI tool to interact with the cluster
https://kubernetes.io/docs/tasks/tools/
Helm
Kubernetes package manager used for deployments
https://helm.sh/docs/intro/install/
☸️ Local Kubernetes (Recommended)
Minikube or Kind
Used for local cluster simulation

Minikube:
https://minikube.sigs.k8s.io/docs/start/

Kind:
https://kind.sigs.k8s.io/docs/user/quick-start/

☁️ Cloud / IaC (Optional but used in project)
Terraform
Infrastructure provisioning (Azure setup)
https://developer.hashicorp.com/terraform/downloads
Azure CLI
Used for Azure resource management
https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
🔁 CI/CD Tools
Git
GitHub Actions (built-in, no install required)
📊 Monitoring Stack
Prometheus & Grafana are deployed via Kubernetes manifests/Helm charts
(no local install required if using cluster deployment)
🐍 Python Automation Tool
Python 3.9+
kubectl configured and accessible in PATH
Helm installed (for deployment automation features)

⚠️ Important Notes
Ensure kubectl cluster-info works before deploying
Ensure Docker is running before using Compose
Ensure Helm is initialized (helm version)
Configure kubeconfig correctly if using remote cluster
💡 Optional Setup Verification

Run:

docker --version
kubectl version --client
helm version
terraform version
python3 --version

## 🧱 Architecture

```
[ React Frontend ]
        ↓
[ Nginx Reverse Proxy ]
        ↓
[ Django REST API Backend ]
        ↓
[ PostgreSQL Database ]

Observability:
- Prometheus (metrics scraping)
- Grafana (visual dashboards)

GitOps:
- ArgoCD (declarative deployment)

Infrastructure:
- Terraform (Azure provisioning)

CI/CD:
- GitHub Actions (build → push → deploy)
```

---

## ⚙️ Tech Stack

### Application Layer

* **Frontend:** React + Nginx
* **Backend:** Python (Django REST Framework)
* **Database:** PostgreSQL

### DevOps & Cloud

* Docker (containerization)
* Kubernetes (orchestration)
* Helm (package management)
* ArgoCD (GitOps deployment)
* Prometheus + Grafana (monitoring & observability)
* Terraform (Infrastructure as Code – Azure)
* GitHub Actions (CI/CD pipeline)

---

## ☸️ Kubernetes Deployment

The entire system is deployed using **Helm charts**, enabling reusable and configurable deployments.

### Components:

* Backend Deployment + Service
* Frontend Deployment + Service (NodePort)
* PostgreSQL Deployment + Persistent Volume
* ConfigMaps & Secrets for environment management
* Kubernetes Job for database migrations

### Key Features:

* Helm templating with dynamic values
* Environment-driven configuration
* Service discovery via Kubernetes DNS
* Scalable microservices architecture

---

## 🔄 Database Migration Strategy

Database migrations are handled automatically using a **Kubernetes Job**:

* Triggered during deployment
* Waits for PostgreSQL readiness (initContainer)
* Executes:

  ```
  python manage.py migrate
  ```
* Ensures schema consistency across deployments

---

## 📊 Monitoring & Observability

### Prometheus

* Scrapes backend metrics endpoint `/metrics`

### Grafana

* Visual dashboards for:

  * API performance
  * Resource usage
  * System health

This enables real-time monitoring and debugging of the system.

---

## 🔁 GitOps with ArgoCD

Deployment is managed using GitOps principles:

* Git repository is the **single source of truth**
* ArgoCD automatically syncs changes to Kubernetes
* Enables declarative and auditable deployments

---

## ☁️ Infrastructure as Code (Terraform)

Infrastructure is provisioned using Terraform:

* Azure resource setup
* Container registry support
* Scalable cloud-ready architecture

---

## 🔄 CI/CD Pipeline (GitHub Actions)

Automated pipeline that:

1. Builds Docker images (backend & frontend)
2. Tags images using commit SHA (immutable builds)
3. Pushes images to DockerHub
4. Deploys to Kubernetes using Helm

This ensures consistent and automated delivery of new features.

---

## 🐍 DevOps Automation Script

A custom Python script was built to simplify operations and cluster management.

### Features:

* Cluster health checks
* Pod and service monitoring
* Helm release inspection
* Deployment trigger
* Frontend restart automation

### Usage:

```bash
python3 devops_tool.py
python3 devops_tool.py --restart-frontend
python3 devops_tool.py --deploy
```

---

## 🧠 Key DevOps Concepts Demonstrated

* Microservices architecture
* Containerization with Docker
* Kubernetes orchestration
* Helm templating & lifecycle management
* GitOps workflows (ArgoCD)
* CI/CD automation (GitHub Actions)
* Infrastructure as Code (Terraform)
* Observability (Prometheus + Grafana)
* Automated database migrations
* Service discovery and networking
* DevOps automation scripting (Python)

---

## 📌 Challenges Solved

* Kubernetes DNS/service resolution issues
* Helm hook timing and lifecycle problems
* PostgreSQL authentication mismatches
* Container image caching and rollout issues
* Init container dependency handling
* Nginx reverse proxy misconfiguration
* Multi-service orchestration debugging

---

## 🧪 Local Deployment

```bash
# Clone repository
git clone https://github.com/your-username/blood-donor-app.git

# Deploy with Helm
helm install blood-app ./Helm

# Check system
kubectl get pods
```

---


## 💼 Project Highlights

This project demonstrates the ability to:

* Design and deploy cloud-native applications
* Implement full DevOps lifecycle (build → deploy → monitor)
* Work with Kubernetes and Helm in real scenarios
* Apply GitOps and CI/CD best practices
* Automate infrastructure and operations

---




