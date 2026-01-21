pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'your-dockerhub-username/flask-portfolio:latest'
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials' // Replace with your Jenkins credentials ID
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Application') {
            steps {
                sh 'python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: "$DOCKER_CREDENTIALS_ID", usernameVariable: "DOCKER_USER", passwordVariable: "DOCKER_PASS")]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
