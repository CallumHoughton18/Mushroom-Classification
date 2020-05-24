pipeline {
  agent none

  environment {
    FLASK_ENV='development'
    FLASK_APP='./src/api/__init__.py'
    DATASET_DIR='./src/files'
    CURRENT_MODEL_DIR='./src/current_model'
    TRAINED_MODELS_DIR='./src/trained_models'
    FEATURE_DEFINITION_PATH='./src/api/features-definition.json'
    LOGS_DIRECTORY='./src/api_logs'
  }
  
  stages {

    stage('build and test') {
      agent { docker { image 'python:3.7.5-slim-buster' } }
      stages {
        stage('build') {
          steps {
            sh 'pip install -r src/requirements.txt'
          }
        }
        stage('test') {
          steps {
            sh 'nosetests --with-xunit'
            sh 'pylint --rcfile src/.pylintrc --exit-zero --output-format=parseable --reports=no src/api src/mushroom_classifier src/test_api src/test_mushroom_classifier > pylint.log'
          }   
        }
      }
      post {
        always {
          junit '**/nosetests.xml'
          recordIssues(
            enabledForFailure: false, 
            tool: java(pattern: 'pylint.log'))
        }
      }
    }

    stage('push') {
      agent{ label 'master' }
      when {
        branch 'master'
      }
      steps {
        echo 'Building and Pushing API Image to DockerHub'
        script {
          withCredentials([string(credentialsId: 'dockerhub-repo', variable: 'REPO')]) {
            def apiImage = docker.build("${REPO}", "./src")
            docker.withRegistry('https://registry.hub.docker.com', 'DockerHub') {
              apiImage.push("${env.BUILD_NUMBER}")
              apiImage.push("latest")
            }
          }
        }
      }
    }
  }

  post {
    always {
      node('master') {
        withCredentials([string(credentialsId: 'sendto-email', variable: 'EMAIL')]) {
          emailext( to: "${EMAIL}", body: "${env.BUILD_URL}", 
                    subject: "[${currentBuild.currentResult}] ${env.JOB_NAME} - Build # ${env.BUILD_NUMBER}",
                    attachLog: true)
        }
      }
    }
  }
}