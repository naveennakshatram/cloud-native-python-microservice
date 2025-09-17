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
                    python -m venv myvenv
                    . myvenv/bin/activate
                    pip install -r requirements.txt
                    myvenv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
                '''
            }
        }
    }
}
