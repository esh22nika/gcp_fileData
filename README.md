# Cloud Computing Project on GCP

 This is a system where uploading a file to a Cloud Storage bucket triggers a Cloud Run function. This function should extract the file's name, size, and format, and publish the information to a Pub/Sub topic.

## Architecture:
- **Platform**: Cloud Run Functions (2nd gen)
- **Trigger**: Cloud Storage file upload via Eventarc
- **Processing**: Extract file name, size, and format
- **Output**: Publish information to Pub/Sub topic

## Function Details:
The function uses CloudEvents format and logs detailed information about each uploaded file, then sends structured data to Pub/Sub for further processing.

## Deployment:
This function is deployed as a Cloud Run service with Cloud Storage trigger via Eventarc, connected directly to this GitHub repository.