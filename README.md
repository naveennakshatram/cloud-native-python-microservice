# Steps to run the microservice in local machine.

## Prerequisites
1. Install python3.12 or above.
2. Install pip3.12 or above.
3. Install docker.
4. Install gcloud.
5. Install kubectl or minikube.

## Create a virtual environment.
1. Open a terminal and navigate to the directory where you want to create the virtual environment.
2. Run the following command to create a virtual environment:
    python3.12 -m venv myvenv
    Note : Replace myvenv with the name of the virtual environment you want to create.
3. Activate the virtual environment:
    source myvenv/bin/activate
    Note : Replace myvenv with the name of the virtual environment you created.
4. To install the required packages, run the following command:
    make update
5. To run the microservice, run the following command:
    make run


# Steps to deploy a python microservice to GCP.

## write a python microservice that will make some response to a request using fastapi.

## Create a docker file that will build a container from the python microservice.

    When you are using apple silicon mac, you need to use the following command to build the docker image.

    docker buildx build --platform linux/amd64 -t gcr.io/YOUR_PROJECT_ID/YOUR_IMAGE_NAME:TAG --push .
    
    Note : The above command will build the docker image and push it to the GCR.

## Need a GCP account to deploy.

## write the docker images into GCR. Google Container Registry.

    Steps to write docker images into GCR.
    1. command to check available images in your gcr account.
        
        gcloud container images list 

    2. command to Enable Container Registry API.

        gcloud services enable containerregistry.googleapis.com

    3. command to Configure Docker to use GCP credentials

        gcloud auth configure-docker

    4. command to Tag your local Docker image with your project’s registry name

        docker tag your-image gcr.io/project-id/your-image:Tag
    
    5. command to push the image to GCR

        docker push gcr.io/project-id/your-image:Tag

##  Create a Kubernetes cluster in GCP.

    1. Use UI GCP console to create a cluster.

    2. Command to check available clusters.

        gcloud container clusters list    

##  To deploy the docker image into the cluster.
    1. Command to check available clusters.
        gcloud container clusters list
    2. Command to get the credentials of the cluster.
        gcloud container clusters get-credentials cluster-name --zone us-central1-a --project project-id
    3. Command to deploy the docker image into the cluster.
        kubectl apply -f deployment.yaml
        Note: deployment.yaml is the file that contains the deployment configuration. Plese check the deployment.yaml file for more details.
    4. Command to check the status of the deployment.
        kubectl get deployment
    5. Command to check the status of the pods.
        kubectl get pods
    6. Command to check the status of the services.
        kubectl get services


