pipeline {
    agent any

    environment{
    }

    stages {
        stage('Clone Git Repository') {
            steps {
                git branch: 'main', credentialsId: 'Jaezic', url:'https://github.com/'
                echo 'Clone Git Repository'
            }
        }
        stage('Source Zip File') {
            steps {
                dir('python/source'){
                    sh "zip -r source.zip ."
                    sh "mv source.zip ../../"
                }
                echo 'Zip File'
            }
        }
        stage('PIP install'){
            steps {
                dir('python'){
                    sh 'pip3 install --platform manylinux2014_x86_64 --target ./python --implementation cp --python-version 3.10 --only-binary=:all: --upgrade -r requirements.txt'
                    // sh "pip3 install -r requirements.txt -t ./python"
                    sh "zip -r python.zip ./python"
                    sh "mv python.zip ../"
                }
            }
        }
    }
}