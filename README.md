# Image Processing Pipeline

Capstone project for CPSC 436C - Cloud Computing at The University of British Columbia (2024WT1 Group 3)

## Project Description

Our project aims to implement an image processing pipeline thaat takes in images of license plates, analyzes the images, and returns relevant information, such as the license plate number, region, timestamp, etc. The application will be hosted on the cloud using Amazon Web Services.

[Click here for a link to the project proposal.](https://docs.google.com/document/d/192WeYQOffhKELanuQ4ml_5SlDGZchOfY/edit?usp=sharing&ouid=114845963421172762607&rtpof=true&sd=true)

## Citations

### OpenALPR

This project utilizes OpenALPR, a free open source library for license plate recognition. [Link](https://github.com/openalpr/openalpr)

To use OpenALPR, we created a Docker image. In order to integrate with AWS, the image includes the AWS CLI installation and a script that generates our results.
