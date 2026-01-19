pipeline {

    agent any

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image (Minikube)') {
            steps {
                sh '''
                  echo "Configuring Minikube Docker environment"

                  eval $(minikube -p minikube docker-env --shell bash)

                  echo "Building Docker image inside Minikube"
                  docker build -t flaskapp:latest docker/
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                  echo "Deploying application to Kubernetes"
                  kubectl apply -f flaskapp_deployment.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                  echo "Pods status:"
                  kubectl get pods

                  echo "Services status:"
                  kubectl get svc
                '''
            }
        }
    }
}

