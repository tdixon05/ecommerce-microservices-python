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
                withCredentials([file(credentialsId: 'docker-config-id', variable: 'DOCKER_CONFIG_FILE')]) {
                    script {
                        echo "Building Docker Images..."
                        // Set DOCKER_CONFIG explicitly
                        sh 'export DOCKER_CONFIG=$(dirname "$DOCKER_CONFIG_FILE") && /usr/local/bin/docker-compose -f docker-compose.staging.yml build'
                    }
                }
            }
        }

        stage('Start Services for Testing') {
            steps {
                script {
                    echo "Starting Services for Testing..."
                    sh '/usr/local/bin/docker-compose -f docker-compose.staging.yml up -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running Tests..."
                    sh 'sleep 10'
                    sh 'python test-app.py'
                }
            }
        }

        stage('Stop Services') {
            steps {
                script {
                    echo "Stopping Services..."
                    sh '/usr/local/bin/docker-compose -f docker-compose.staging.yml down'
                }
            }
        }

        stage('Promote to Production') {
            input {
                message "Approve deployment to production?"
            }
            steps {
                script {
                    echo "Deploying to Production..."
                    sh '/usr/local/bin/docker-compose -f docker-compose.prod.yml up -d'
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
    }
}
