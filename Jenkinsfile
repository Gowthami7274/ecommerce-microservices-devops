pipeline {
    agent any

    environment {
        UV_NO_CONFIG = '1'
        UV_CACHE_DIR = '/var/lib/jenkins/.cache/uv'
        UV = '/var/lib/jenkins/.local/bin/uv'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Python Version') {
            steps {
                sh '$UV run --python 3.12 python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    for service in user_auth product_management order_processing
                    do
                        echo "Installing dependencies for $service"

                        $UV venv --clear --python 3.12 $service/venv

                        $UV pip install --python $service/venv/bin/python -r $service/requirements.txt

                        $UV pip install --python $service/venv/bin/python pytest
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
