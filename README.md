# Image Processing Pipeline
Capstone project for CPSC 436C - Cloud Computing at The University of British Columbia

## Project Description
Our project aims to implement an image processing pipeline thaat takes in images of license plates, analyzes the images, and returns relevant information, such as the license plate number, region, timestamp, etc. The application will be hosted on the cloud using Amazon Web Services.

[Click here for a link to the project proposal.](https://docs.google.com/document/d/192WeYQOffhKELanuQ4ml_5SlDGZchOfY/edit?usp=sharing&ouid=114845963421172762607&rtpof=true&sd=true)

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
### Code
