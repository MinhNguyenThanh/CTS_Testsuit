pipeline {
    agent any
      environment {
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
    }
    stages {
        stage('CTS') {
            steps {
                echo 'Running CTS..' 
                sh """
                 #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    python run_cts_suite.py
                """
            }
            
        }
        stage('VTS') {
            steps {
                echo 'Running VTS..'
            }
        }
        stage('WTS') {
            steps {
                echo 'Running WTS....'
            }
        }
    }
 /* post {
        always {
	     Use slackNotifier.groovy from shared library and provide current build result as parameter  
            slackNotifier(currentBuild.currentResult)
        }
    }
*/
}