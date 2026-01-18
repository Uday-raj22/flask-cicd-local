pipeline {

    agent any

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flaskapp:latest docker/'
            }
        }

        stage('Deploy Using Ansible') {
            steps {
                sh 'ansible-playbook ansible/provision_flaskapp.yml'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl get pods'
                sh 'kubectl get svc'
            }
        }
    }
}

