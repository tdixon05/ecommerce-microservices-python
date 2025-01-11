pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/tdixon05/ecommerce-microservices-python.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '/usr/local/bin/docker-compose -f docker-compose.staging.yml build'
            }
        }

        stage('Start Services for Testing') {
            steps {
                sh '/usr/local/bin/docker-compose -f docker-compose.staging.yml up -d'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'sleep 10' // Wait for services to initialize
                sh 'python test-app.py'
            }
        }

        stage('Stop Services') {
            steps {
                sh '/usr/local/bin/docker-compose -f docker-compose.staging.yml down'
            }
        }

        stage('Promote to Production') {
            input {
                message "Approve deployment to production?"
            }
            steps {
                sh '/usr/local/bin/docker-compose -f docker-compose.prod.yml up -d'
            }
        }
    }

    post {
        always {
            cleanWs() // Clean up workspace after build
        }
    }
}
