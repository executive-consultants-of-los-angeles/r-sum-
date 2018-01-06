pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh 'pip install django;'
        dir(path: 'files/rsum/rsum') {
          sh './manage.py test'
        }
        
      }
    }
  }
}