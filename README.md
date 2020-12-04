# sample_app for CI
## Sample app using Github, Github Action, Github Packages and Azure Kubernetes Service

# Steps

1. [Develop and Test App](#develop-and-test-app)
2. [Build and run docker images](#build-and-run-docker-images)
3. [Build CI pipeline](#build-ci-pipeline)
4. [Deploy on Azure Kubernetes Service](#deploy-on-azure-kubernetes-service)

## Develop and Test App

Build app.py, test_app.py and wsgi.py

## Build and run docker images
To build and run the docker image, which automatically starts the model serving API, run:
```
$ docker build -t docker.pkg.github/matthiasfalk/sample_app/sample_app:1 .
```

```
$ docker run -it -p 8000:8000 docker.pkg.github/matthiasfalk/sample_app/sample_app:1
```

## Build CI pipeline 

Write workflow.yaml for Github Actions.


## Deploy on Azure Kubernetes Service:


On your Kubernetes cluster, run the following commands:

```
$ kubectl apply -f deployment.yaml
```


