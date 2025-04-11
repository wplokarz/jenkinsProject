pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/wplokarz/jenkinsProject.git'

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
