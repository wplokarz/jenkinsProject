pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/wplokarz/jenkinsProject.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
