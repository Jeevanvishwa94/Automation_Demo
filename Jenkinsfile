pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Jeevanvishwa94/Automation_Demo.git'
            }
        }
        stage('Test') {
            steps {
                'pytest -v testcase\play_childrens_lesson.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
