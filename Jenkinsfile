pipeline {
    agent {
            docker {
                image 'docker:dind'         // Use the official Docker-in-Docker image
                args '--privileged'         // Required for Docker daemon to run inside the container
                // IMPORTANT: Do NOT mount /var/run/docker.sock from the host
                // You are running a Docker daemon INSIDE this container.
            }
        }


    stages {
        stage("commands") {
            steps{
                sh 'echo check docker'
                sh 'docker ps'
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/wplokarz/jenkinsProject.git'

            }
        }
         stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh 'echo "$DOCKERHUB_USER" login success'
                }
            }
        }

       stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Run Flask in Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }
    }
}
