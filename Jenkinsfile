pipeline {
    agent { docker 'python:3.6' }
    stages {
        stage('setup') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('build') {
            steps {
                sh 'python manage.py test'
                junit 'TEST-*.xml'
            }
        }
    }
}
