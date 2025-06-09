
1. write a python microservice that will make some response to a request using fastapi.

2. Create a docker file that will build a container from the python microservice.

    When you are using apple silicon mac, you need to use the following command to build the docker image.

    docker buildx build --platform linux/amd64 -t gcr.io/YOUR_PROJECT_ID/YOUR_IMAGE_NAME:TAG --push .
    
    Note : The above command will build the docker image and push it to the GCR.

3. Need a GCP account to deploy.

4. write the docker images into GCR. Google Container Registry.

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

5.  Create a Kubernetes cluster in GCP.

    1. Use UI GCP console to create a cluster.

    2. Command to check available clusters.

        gcloud container clusters list    

6.  Deploy the docker image into the cluster.
