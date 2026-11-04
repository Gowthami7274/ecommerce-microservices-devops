
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    for service in user_auth product_management order_processing
                    do
                        echo "Installing dependencies for $service"
                        python3 -m venv $service/venv
                        $service/venv/bin/pip install -r $service/requirements.txt
                    done
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    for service in user_auth product_management order_processing
                    do
                        echo "Running tests for $service"
                        $service/venv/bin/python -m pytest $service/test_app.py -v
                    done
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }
        failure {
            echo 'CI pipeline failed. Check the console output.'
        }
    }
}
