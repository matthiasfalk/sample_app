# sample_app for CI
## Sample app using Github, Github Action, Github Packages and Azure Kubernetes Service CI

# Steps

1. [Develop App](#develop-app-locally)
2. [Test App](#deploy-on-kubernetes)
3. [Build docker images](#deploy-on-red-hat-openshift)
4. [Run](#run-locally)

## Develop and Test App

Build app.py, test_app.py and wsgi.py
To run the docker image, which automatically starts the model serving API, run:

```
$ docker run -it -p 8000:8000 falkmatt/u8_sample_app:1
```


## Build CI pipeline 

Write workflow.yaml for Github Acttions.


## Deploy on Azure Kubernetes Service:


On your Kubernetes cluster, run the following commands:

```
$ kubectl apply -f https://github.com/IBM/MAX-Recommender/raw/master/max-recommender.yaml
```


