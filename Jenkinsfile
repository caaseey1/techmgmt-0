pipeline {
  environment {
    registry = "kc12345/automation_testing"
    registryCredential = 'dockerhub'
    dockerImage = 'python:3-apline'
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps{
          git 'https://github.com/caaseey1/techmgmt-0'
      }
  }
    stage('Building image') {
      steps{
        script {
          docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
        steps {
            script {
                docker.withRegistry( '', registryCredential ){
                    dockerImage.push
                }
        }
    }
  }
  }
}
