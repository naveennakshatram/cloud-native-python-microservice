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
                    args '-p 8000:8000' // map container port 8000 to host
                }
            }
            steps{
                sh '''
                    docker build -t cloud-native-python-microservice .
                    docker run -p 8000:8000 cloud-native-python-microservice
                '''
            }
        }
    }
}
