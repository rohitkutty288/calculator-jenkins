pipeline{
    agent any
    parameters{
        choice(name: 'ENVIRONMENT',choices: ['docker-run-prod','Testing'],description: 'ENVIRONMENT_NAME')
    }
    stages{
        stage('Git clone calculator project'){
            steps{
                git branch: 'main', credentialsId: 'calculator in jenkins', url: 'https://github.com/rohitkutty288/calculator-jenkins.git'
            }
        }
        stage('Listing calculator project'){
            steps{
                sh 'ls'
            }
        }
        stage('Docker build and run'){
            when{
                expression{
                    params.ENVIRONMENT == 'docker-run-prod'
                }
            }
            steps{
                sh '''
                docker build -t calculator-container-pipeline .
                docker rm -f calculator-container-pipeline || true
                docker run -d -p 5003:5000 --name=calculator-container-pipeline calculator-container-pipeline
                '''
            }
        }
    }
}
