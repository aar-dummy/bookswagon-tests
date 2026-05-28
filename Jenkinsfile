pipeline {
    agent any

    environment {
        TEST_EMAIL    = credentials('aarconn23@gmail.com')
        TEST_PASSWORD = credentials('Password@12')
        HEADLESS      = 'true'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install selenium pytest pytest-html webdriver-manager setuptools'
                bat 'venv\\Scripts\\pip install -e .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python -m pytest --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportName : 'E2E Test Report',
                reportDir  : '.',
                reportFiles: 'report.html',
                keepAll    : true
            ])
        }
    }
}
