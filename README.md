FLASK DEVOPS PROJECT
Ansible | Jenkins | Docker | Kubernetes (Minikube)

PROJECT OVERVIEW
This project demonstrates a complete DevOps pipeline for deploying a Flask web application using:
- Ansible for provisioning
- Docker for containerization
- Jenkins for CI/CD
- Kubernetes (Minikube) for orchestration
The project runs fully on a local machine.

--------------------------------------------------

PROJECT STRUCTURE
.
├── ansible/
│   ├── provision_flaskapp.yml
│   └── provision_jenkins.yaml
├── docker/
│   ├── Dockerfile
│   ├── web.py
│   ├── lorenz.py
│   ├── requirements.txt
│   ├── templates/
│   └── static/
├── flaskapp_deployment.yaml
├── flaskapp_service.yaml
├── Jenkinsfile
└── README.txt

--------------------------------------------------

PREREQUISITES
- Linux (Ubuntu recommended)
- Git
- Python 3
- Internet connection

Install basics:
sudo apt update
sudo apt install -y git curl python3 python3-pip

--------------------------------------------------

STEP 1: CLONE REPOSITORY
git clone https://github.com/Uday-raj22/flask-cicd-local.git
cd flask-cicd-local

--------------------------------------------------

STEP 2: INSTALL ANSIBLE
sudo apt install -y ansible
ansible --version

--------------------------------------------------

STEP 3: PROVISION SYSTEM USING ANSIBLE
Installs Docker, Jenkins, Kubectl, Minikube

Run Jenkins setup:
ansible-playbook ansible/provision_jenkins.yaml

Run Docker + Kubernetes setup:
ansible-playbook ansible/provision_flaskapp.yml

--------------------------------------------------

STEP 4: START MINIKUBE
minikube start --driver=docker
kubectl get nodes

--------------------------------------------------

STEP 5: CONFIGURE DOCKER FOR MINIKUBE
IMPORTANT:
eval $(minikube docker-env)
docker info | grep minikube

--------------------------------------------------

STEP 6: BUILD DOCKER IMAGE
cd docker
docker build -t flaskapp:latest .
cd ..

Verify:
docker images | grep flaskapp

--------------------------------------------------

STEP 7: DEPLOY TO KUBERNETES
kubectl apply -f flaskapp_deployment.yaml
kubectl apply -f flaskapp_service.yaml

Check:
kubectl get pods

--------------------------------------------------

STEP 8: ACCESS APPLICATION
minikube service flaskapp-service

OR manually:
kubectl get svc
minikube ip

Open in browser:
http://<minikube-ip>:<node-port>

--------------------------------------------------

APPLICATION ROUTES
/        -> Home page
/lorenz  -> Lorenz visualization

--------------------------------------------------

STEP 9: JENKINS PIPELINE (OPTIONAL)
Open Jenkins:
http://localhost:8080

Create Pipeline job and link GitHub repository.
Pipeline automatically builds and deploys app.

--------------------------------------------------

TROUBLESHOOTING
View pod logs:
kubectl logs <pod-name>

If image pull fails:
eval $(minikube docker-env)
docker build -t flaskapp:latest .

--------------------------------------------------

SCREENSHOTS REQUIRED
- Ansible execution
- Jenkins pipeline success
- Docker image build
- kubectl get pods
- kubectl get svc
- Browser output

--------------------------------------------------

TEAM RESPONSIBILITIES
Member 1: Ansible
Member 2: Docker & Flask
Member 3: Kubernetes
Member 4: Jenkins CI/CD

--------------------------------------------------

IMPORTANT NOTE
Always run:
eval $(minikube docker-env)
before building Docker images.

