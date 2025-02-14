# Spotify Trendz - DevOps Project

**Spotify Trendz** is a Flask-based REST API application that integrates with the **Spotify API** to provide music recommendations based on user preferences. This project demonstrates **DevOps best practices** by utilizing **Terraform for infrastructure provisioning, Docker Swarm for container orchestration, Kubernetes for fault tolerance, and monitoring with Prometheus and Grafana**.

---

## **Project Overview**

The goal of this project is to deploy a scalable and reliable microservices-based application using various DevOps tools and methodologies. The architecture includes:

- **AWS Infrastructure** provisioned using Terraform.
- **Containerization** using Docker and Docker Swarm.
- **Kubernetes Cluster (EKS)** deployment for fault tolerance.
- **Monitoring and Logging** with Prometheus and Grafana.
- **CI/CD Pipeline** for automated deployments.

---

## **Features**

✅ **Terraform-managed AWS infrastructure** (EC2, Security Groups, and EKS Cluster).  
✅ **Spotify API Integration** for fetching trending songs.  
✅ **Kubernetes Deployment** for high availability and fault tolerance.  
✅ **Docker Swarm Stack Deployment** for quick service management.  
✅ **Prometheus and Grafana Monitoring** using Helm Charts.  
✅ **CI/CD Pipeline** for automated testing and deployments.  

---

## **Repository**

Clone the project repository:

```bash
git clone https://github.com/Pshar10/Spotify_trendz_Rest_API.git
cd Spotify_trendz_Rest_API
```

---

## **Infrastructure as Code (Terraform)**

Terraform is used to provision the AWS infrastructure:

- **EC2 Instance** for hosting Docker Swarm.
- **Security Groups** to manage access control.
- **EKS Cluster** for Kubernetes deployments.

### **Run Terraform**

1. Initialize Terraform:

    ```bash
    terraform init
    ```

2. Apply Terraform configuration:

    ```bash
    terraform apply -auto-approve
    ```

3. After deployment, get the **EC2 Public IP**:

    ```bash
    terraform output public_ip
    ```

---

## **Kubernetes Deployment**

To deploy the application on **AWS EKS**, follow these steps:

### **Create EKS Cluster**

```bash
eksctl create cluster --name trendz-cluster --region us-east-1 --nodegroup-name standard-workers --node-type t3.medium --nodes 3 --nodes-min 1 --nodes-max 4 --managed
```

### **Apply Kubernetes Configurations**

```bash
kubectl apply -f secrets.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### **Verify Pods & Services**

```bash
kubectl get pods
kubectl get services
```

---

## **Docker Swarm Deployment**

If you prefer **Docker Swarm** instead of Kubernetes:

1. **Initialize Swarm**:

    ```bash
    docker swarm init
    ```

2. **Create Docker Secrets**:

    ```bash
    echo "your-spotify-client-id" | docker secret create SPOTIPY_CLIENT_ID -
    echo "your-spotify-client-secret" | docker secret create SPOTIPY_CLIENT_SECRET -
    ```

3. **Deploy Stack**:

    ```bash
    docker stack deploy -c docker-compose.yml my_flask_stack
    ```

---

## **Monitoring with Prometheus & Grafana**

We use **Helm Charts** to install Prometheus and Grafana on our Kubernetes cluster.

### **Install Helm**

```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```

### **Add Prometheus & Grafana Helm Repo**

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

### **Deploy Monitoring Stack**

```bash
helm install prometheus prometheus-community/kube-prometheus-stack
```

### **Access Grafana Dashboard**

1. **Get Grafana Admin Password**:

    ```bash
    kubectl get secret prometheus-grafana -o jsonpath="{.data.admin-password}" | base64 --decode
    ```

2. **Forward Grafana Port**:

    ```bash
    kubectl port-forward svc/prometheus-grafana 3000:80
    ```

3. **Open Grafana UI**:

    Access **Grafana Dashboard** at:

    ```
    http://localhost:3000
    ```

    Default Login:
    - Username: `admin`
    - Password: (Retrieved from step 1)

---

## **CI/CD Pipeline (Optional)**

For **automated deployments**, configure a **GitHub Actions CI/CD pipeline**:

1. **Set up AWS Credentials in GitHub Secrets**.
2. **Create a `.github/workflows/deploy.yml`** file.
3. **Trigger deployments on push events**.

---

## **Conclusion**

This project showcases **modern DevOps practices** by leveraging:
- **Terraform for AWS provisioning** 🚀
- **Docker & Kubernetes for container orchestration** 🛠️
- **Prometheus & Grafana for monitoring** 📊
- **GitHub Actions for CI/CD automation** 🔄

### **Next Steps**
- Implement logging with **ELK Stack**.
- Enhance security with **IAM roles & policies**.
- Optimize **auto-scaling** for dynamic workloads.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Contributors**

👤 **Pranav Sharma**  
📧 [pshar416@gmail.com](mailto:pshar416@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/pranav-sharma)  

For any queries, feel free to **raise an issue** in the repository! 🚀

