PROJECT: Flask Application CI/CD using Ansible, Docker, Kubernetes & Jenkins
AUTHOR: Team Project
PLATFORM: Ubuntu / Linux

---

PROJECT OVERVIEW

This project demonstrates a complete DevOps workflow:

1. Ansible provisions the system (Docker, Jenkins, Kubernetes tools)
2. Docker containerizes a Flask application
3. Kubernetes (Minikube) runs the container
4. Jenkins automates the CI/CD pipeline
5. Flask app is accessed via browser

---

SYSTEM REQUIREMENTS

Operating System:

* Ubuntu 20.04 / 22.04 / 24.04

Minimum Requirements:

* 8 GB RAM
* Virtualization enabled
* Internet access

---

PROJECT DIRECTORY STRUCTURE

Run this command to verify structure:

tree -L 2

Expected structure:

.
├── ansible
│   ├── provision_flaskapp.yml
│   └── provision_jenkins.yaml
├── docker
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── web.py
│   ├── lorenz.py
│   ├── templates
│   └── static
├── flaskapp_deployment.yaml
├── flaskapp_service.yaml
├── Jenkinsfile
├── README.md

---

STEP 1: INSTALL ANSIBLE

Run the following commands:

sudo apt update
sudo apt install -y ansible
ansible --version

---

STEP 2: PROVISION SYSTEM USING ANSIBLE

This installs:

* Docker
* Jenkins
* kubectl
* Minikube

Run Jenkins provisioning:

ansible-playbook ansible/provision_jenkins.yaml

Run Docker & Kubernetes provisioning:

ansible-playbook ansible/provision_flaskapp.yml

---

STEP 3: START AND VERIFY JENKINS

Start Jenkins:

sudo systemctl start jenkins
sudo systemctl enable jenkins

Get Jenkins admin password:

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

Open Jenkins in browser:

[http://localhost:8080](http://localhost:8080)

---

STEP 4: START MINIKUBE

Start Minikube using Docker driver:

minikube start --driver=docker

Verify cluster:

kubectl get nodes

---

STEP 5: CONFIGURE DOCKER TO USE MINIKUBE

This step is mandatory:

eval $(minikube docker-env)

Verify Docker is pointing to Minikube:

docker info | grep minikube

---

STEP 6: BUILD DOCKER IMAGE

Go to docker directory:

cd docker

Build the Flask image:

docker build -t flaskapp:latest .

Verify image:

docker images | grep flaskapp

---

STEP 7: DEPLOY APPLICATION TO KUBERNETES

Go back to project root:

cd ..

Apply deployment:

kubectl apply -f flaskapp_deployment.yaml

Apply service:

kubectl apply -f flaskapp_service.yaml

Check pod status:

kubectl get pods

Check service:

kubectl get svc

---

STEP 8: ACCESS FLASK APPLICATION

Expose service:

minikube service flaskapp-service

OR manually:

minikube ip
kubectl get svc flaskapp-service

Open in browser:

http://<MINIKUBE-IP>:<NODE-PORT>

---

FLASK APPLICATION ROUTES

/           → Home Page
/lorenz     → Lorenz System Visualization

---

STEP 9: JENKINS CI/CD PIPELINE SETUP

1. Open Jenkins UI
2. Click "New Item"
3. Select "Pipeline"
4. Choose "Pipeline from SCM"
5. Select Git
6. Enter GitHub repository URL
7. Branch: main
8. Jenkinsfile path: Jenkinsfile
9. Save

Run pipeline using "Build Now"

---

JENKINS PIPELINE STAGES

1. Git Checkout
2. Docker Build
3. Kubernetes Deployment
4. Verification

Green pipeline indicates success.

---

COMMON TROUBLESHOOTING COMMANDS

Check pod logs:

kubectl logs <pod-name>

Restart deployment:

kubectl rollout restart deployment flaskapp

Delete all Kubernetes resources:

kubectl delete deployment flaskapp
kubectl delete service flaskapp-service

Clean Docker:

docker system prune -af

Reset Minikube:

minikube delete

---

TEAM RESPONSIBILITY DISTRIBUTION

Member 1: Ansible provisioning
Member 2: Flask application development
Member 3: Docker & Kubernetes deployment
Member 4: Jenkins CI/CD pipeline


