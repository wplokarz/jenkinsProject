pipeline {
    agent any


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
