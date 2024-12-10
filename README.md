# Image Processing Pipeline

Capstone project for CPSC 436C - Cloud Computing at The University of British Columbia (2024WT1 Group 3)


## Project Description

Our project aims to implement an image processing pipeline thaat takes in images of license plates, analyzes the images, and returns relevant information, such as the license plate number, region, timestamp, etc. The application will be hosted on the cloud using Amazon Web Services.

[Click here for a link to the project proposal.](https://docs.google.com/document/d/192WeYQOffhKELanuQ4ml_5SlDGZchOfY/edit?usp=sharing&ouid=114845963421172762607&rtpof=true&sd=true)

## List of Services Used

### Frontend
- Vue.js and Nuxt.js
- AWS Load balancer
- AWS ECR
- AWS ECS
- AWS API Gateway

### Image Processing
- Docker
- AWS ECR
- AWS ECS
- AWS Lambda

### Data Storage and Querying
- MySQL Database
- AWS S3
- AWS RDS
- AWS Athena


## Testing the Project

[Click here for a link to the project frontend.](http://internet-loadbalancer-nuxt-1931143557.ca-central-1.elb.amazonaws.com)

In order to test the application, upload an image of a vehicle with a license plate.

- The character recognition may not recognize your image, in which case you can use the test images found in this repository (openalpr/images). 

Once the image is uploaded, the program will take about a minute to return its results.

Note: We will remove services on December 16th to avoid incurring additional costs.

## Set up the container

### Frontend

To set up the container for the frontend, navigate to the client directory.
A dockerfile exists in the directory, so we need to build the docker image in the command line:
```
docker buildx build --platform linux/amd64 --no-cache --provenance=false -t frontend-image-processing .
```
Once the docker image is made, we can run the docker image on port 3000:

```
docker run -p 3000:3000 frontend-image-processing
```

The web app should then be available on localhost.

## Citations

### OpenALPR

This project utilizes OpenALPR, a free open source library for license plate recognition. [Link](https://github.com/openalpr/openalpr)

To use OpenALPR, we created a Docker image. In order to integrate with AWS, the image includes the AWS CLI installation and a script that generates our results.
