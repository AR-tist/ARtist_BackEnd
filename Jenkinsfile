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
                    sh 'sudo -u ubuntu pip install -r requirements.txt'
                }
            }
        }
        stage('PM2 start'){
            steps {
                dir('python/source'){
                    script{
                        def pm2ListOutput = sh(script:'sudo -u ubuntu pm2 list', returnStdout: true).trim()

                        if(!pm2ListOutput.contains("main") && !pm2ListOutput.contains("online")){
                            echo 'Starting PM2 as "main" is not found in the list.'
                            sh 'sudo -u ubuntu pm2 start main.py --watch --interpreter python3'
                        }
                        else{
                            // sh 'sudo -u ubuntu pm2 restart main'
                            echo 'PM2 process with "main" is already running.'
                        }

                    }
                }
            }
        }
    }
}