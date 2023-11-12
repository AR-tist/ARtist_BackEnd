pipeline {
    agent any

    stages {
        stage('Clone Git Repository') { 
            steps {
                git branch: 'main', credentialsId: 'Jaezic', url:'https://github.com/AR-tist/ARtist_BackEnd.git'
                echo 'Clone Git Repository'
            }
        }
        stage('Install Dependencies') {
            steps {
                dir('python'){
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('PM2 start'){
            steps {
                dir('python/source'){
                    sh 'pm2 start main.py --watch --interpreter python3 --user ubuntu'
                }
            }
        }
    }
}