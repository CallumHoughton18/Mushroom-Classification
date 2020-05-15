pipeline {
  agent { docker { image 'python:3.7.5-slim-buster' } }
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