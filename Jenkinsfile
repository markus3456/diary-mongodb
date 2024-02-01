pipeline {
    agent any
    
    stages {
        stage('Build and Deploy') {
            steps {
                script {
                    // Pull the code from Git
                    checkout scm

                    // Build and start the Docker containers
                    sh 'docker-compose up -d --build'

                    // You can add additional steps like running tests here
                }
            }
        }
    }

    post {
        always {
            // Cleanup: Stop and remove Docker containers
            sh 'docker-compose down'
        }
    }
}
