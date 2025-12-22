How is this system deployed and operated in production?

The system follows cloud-native principles: stateless services, observability-first design, and automated deployments.



Internet
   |
[ DNS ]
   |
[ Load Balancer ]
   |
[ Ingress Controller ]
   |
[ FastAPI Pods ]
   |
[ Agent Services ]
   |
[ Databases ]

Expand Databases:
PostgreSQL (pgvector)
MongoDB
Object Storage (S3)


Monitoring Sidecar:
Pods
 ├── App Container
 └── Prometheus Exporter


CI/CD Flow (Bottom of Diagram):
GitHub
  |
GitHub Actions
  |
Docker Build
  |
Container Registry
  |
Kubernetes Deploy




Infra narration:

1) DNS - 
Routes traffic to the platform

2) Load Balancer - 
Distributes traffic across instances

3) Ingress Controller - 
Routes requests inside Kubernetes

4) FastAPI Pods -
Horizontally scalable
Stateless

5) Agent Services -
Separate services or modules
Independently scalable

6) Databases -
PostgreSQL with pgvector
MongoDB for unstructured data

7) Monitoring Stack -
Prometheus collects metrics
Grafana visualizes health

8) CI/CD Pipeline -
GitHub Actions
Docker builds
Automated deployment
