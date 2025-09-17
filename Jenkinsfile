pipeline{
    agent any

    stages{
        stage('GIT Check')
        {
            steps{
                echo 'Reading from GIT'
            }
        }
        stage('Run Code')
        {
            agent{
                docker{
                    image 'python:3.12'
                }
            }
            steps{
                sh '''
                    pip install -m requirements.txt
                    python app/main.py
                '''
            }
        }
    }
}
