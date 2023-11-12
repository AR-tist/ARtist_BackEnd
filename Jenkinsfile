pipeline {
    agent any

    environment {
        GIT_CREDENTIALS = credentials('Jaezic')
        PROJECT_PATH = '/home/ubuntu/ARtist_BackEnd'
    }

    stages {
        // stage('Clone Git Repository') {
        //     steps {
        //         git branch: 'main', credentialsId: 'Jaezic', url:'https://github.com/AR-tist/ARtist_BackEnd.git'
        //         echo 'Clone Git Repository'
        //     }
        // }
        
        // stage('Source Zip File') {
        //     steps {
        //         dir('python/source'){
        //             sh "zip -r source.zip ."
        //             sh "mv source.zip ../../"
        //         }
        //         echo 'Zip File'
        //     }
        // }
        stage('Github Pull'){
            steps {
                script {
                    // Move to the repository directory
                    dir(PROJECT_PATH) {
                        // Execute git pull command with credentials
                        sh "git pull --credentials=${GIT_CREDENTIALS}"
                    }
                }
            }
        }
        stage('PIP install'){
            steps {
                dir(PROJECT_PATH+'/python'){
                    sh 'pip install -r requirements.txt'
                }
            }
        }
    }
}