pipeline {
  agent { docker { image 'python:3.7.5-slim-buster' } }
  environment {
    FLASK_ENV=development
    FLASK_APP=./src/api/__init__.py
    DATASET_DIR=./src/files
    CURRENT_MODEL_DIR=./src/current_model
    TRAINED_MODELS_DIR=./src/trained_models
    FEATURE_DEFINITION_PATH=./src/api/features-definition.json
    LOGS_DIRECTORY=./src/api_logs
  }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r src/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python -m unittest discover -s src'
      }   
    }
  }
}