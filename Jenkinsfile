
pipeline { 
agent any
    stages {
        stage('Clone Git Repository') {
            steps {
                git 'https://github.com/shrey27tri01/jenkins_demo.git'
            }
        }
        stage('Run Code') {
            steps {
                sh "/usr/bin/python3 main.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "/usr/bin/python3 unit_test.py"
            }
        }
    } 
