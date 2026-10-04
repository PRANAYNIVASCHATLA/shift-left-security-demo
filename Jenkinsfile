
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                bat 'if not exist reports mkdir reports'
                bat '"C:\\Users\\prana\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install bandit'
            }
        }

        stage('Scan Vulnerable Code') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                    bat 'venv\\Scripts\\bandit -r vulnerable -f txt -o reports\\vulnerable_report.txt'
                }
            }
        }

        stage('Scan Fixed Code') {
            steps {
                bat 'venv\\Scripts\\bandit -r fixed -f txt -o reports\\fixed_report.txt'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.txt', allowEmptyArchive: true
        }
    }
}
