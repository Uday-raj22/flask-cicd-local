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
                  echo "Switching Docker context to Minikube"
                  eval $(minikube docker-env)

                  echo "Building Flask Docker image inside Minikube"
                  docker build -t flaskapp:latest docker/
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                  echo "Deploying Flask app to Kubernetes"
                  kubectl apply -f flaskapp_deployment.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                  echo "Checking Pods"
                  kubectl get pods

                  echo "Checking Services"
                  kubectl get svc
                '''
            }
        }
    }
}

