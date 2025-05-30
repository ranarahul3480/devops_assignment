# DevOps Take-Home Assignment

## Overview

This project demonstrates a secure, observable, and automated CI/CD pipeline for a containerized Flask application deployed on Kubernetes.

---

## Tech Stack

- *App*: Python Flask
- *Container*: Docker (multistage, non-root)
- *CI/CD*: GitHub Actions
- *Security*: Trivy scan
- *Registry*: Docker Hub
- *K8s Deployment*: Helm + Minikube
- *Secrets*: Kubernetes Secrets
- *Observability*: Prometheus metrics + stdout logging

---

# Architecture and Design Decisions

### 🗂 Project Structure

devops_assignment/
├── app/ # Flask web app
│ ├── app.py # Main application
│ ├── Dockerfile # Container definition
│ └── requirements.txt # Python dependencies
├── charts/ # Helm chart for deployment
│ └── flask-app/
│ ├── Chart.yaml
│ ├── values.yaml
│ └── templates/ # Kubernetes manifests
│ ├── deployment.yaml
│ ├── service.yaml
│ └── ingress.yaml

## Key Features

- ✅ Secure Docker build (no root, no secrets in image)
- ✅ CI pipeline: build → scan → push → deploy
- ✅ K8s setup: resource limits, probes, Ingress
- ✅ Secrets injected via K8s Secret manifests
- ✅ Metrics exposed on /metrics

---

## How to Run

### Prerequisites

- Docker
- Kubernetes cluster (Minikube)
- [Helm](https://helm.sh/)
- (Optional) NGINX Ingress Controller

# The pipeline will automatically triggered when there will be a push in main branch.

# Areas for Improvement

- Scalability: Add HPA (Horizontal Pod Autoscaler).
- Implement alerting (Slack/email/Webhook)
- Use ArgoCD or Flux for GitOps-style deployment