pipeline {
    agent any

    environment {
        TEST_EMAIL    = credentials('TEST_EMAIL')
        TEST_PASSWORD = credentials('TEST_PASSWORD')
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
            archiveArtifacts artifacts: 'report.html, report.xml', allowEmptyArchive: true
        }
    }
}
