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
                    script{
                        try{
                            def pm2Output = sh(script:'sudo -u ubuntu pm2 start main.py --watch --interpreter python3', returnStdout: true).toString().trim()
                        } catch (Exception e){
                            echo pm2Output
                            if (pm2Output.contains('Script already launched')){
                                echo 'Script already launched'
                            } else{
                                throw e
                            }
                        }
                    }
                }
            }
        }
    }
}