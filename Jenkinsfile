pipeline {
    agent any

    environment {
        PYTHON = "/home/joshnareddy202/MyAutomationProject/venv/bin/python"
        PIP = "/home/joshnareddy202/MyAutomationProject/venv/bin/pip"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/YOUR_USERNAME/RealProject.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                ${PIP} install --upgrade pip
                ${PIP} install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                ${PYTHON} -m pytest -v
                '''
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            }
        }
    }

    post {
        always { echo 'Build Finished' }
        success { echo 'Tests Passed ✅' }
        failure { echo 'Tests Failed ❌' }
    }
}
