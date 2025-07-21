# PerceptiFlow

A scalable ML model inference backend designed for perception research workflows.

## Features

- FastAPI REST API for serving ML models
- Dockerized for easy local development and deployment
- Kubernetes manifests included for scalable cloud deployment
- Prometheus metrics endpoint for monitoring and observability

## Setup

### Prerequisites

- Python 3.10+
- Docker (optional, for containerized deployment)
- Kubernetes cluster (optional, for production deployment)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/jay-munjapara/PerceptiFlow.git
   cd PerceptiFlow
   ```
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI server locally:
   ```
   uvicorn app.main:app --reload
   ```
4. Access the API docs at:
   ```
   http://localhost:8000/docs
   ```

### Docker

1. Build the Docker image:
   ```
   docker build -t perceptiflow .
   ```
2. Run the container:
   ```
   docker run -p 8000:8000 perceptiflow
   ```

### Kubernetes Deployment

1. Apply the deployment and service manifests:
   ```
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```

### API Endpoints

- POST /predict/ — Upload an image file to get ML model predictions

- GET /metrics — Prometheus metrics for monitoring
