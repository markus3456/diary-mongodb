**Diary App with MongoDB Database**


This is a simple app for CRUD-operations with MongoDB written in python


**Overview**

This app facilitaes CRUD-operations to interact with a MongodB Database.
You can create new entries about tasks you have done today and specify the time you have spent on it.
Each task is stored as a document on the MongoDB Database.
Each entry can be read, updated and deleted in a table on the mainpage.


**Architecture**

The app consists of two Docker containers of which one containes the app data and the other one contains the Database. 
Both Containers are connected via a docker network. 

**Deployment**

The folder contains one Dockerfile for each container and a docker-compose.yaml file and Jenkinsfile. 
Hence, the app can be deployed using docker-compose or Jenkins.

**Requirements for Deployment with CI/CD pipline using Jenkins:**

For Linux CentOS Machine:
- Java 17
- Jenkins
- Configuration of Firewall:
    - add port 8080/tcp
- Docker
- docker-compose
- git

**Configure Pipeline**

1. Open Jenkins and go to the Jenkins dashboard.
2. Click on "New Item" to create a new Jenkins job.
3. Enter a name for your job (e.g., "diary-mongodb-pipeline") and select the "Pipeline" type.
4. Scroll down to the "Pipeline" section, and in the "Definition" dropdown, choose "Pipeline script from SCM."
5. In the "SCM" dropdown, select "Git."
6. In the "Repository URL" field, enter the URL of your Git repository: https://github.com/markus3456/diary-mongodb.
7. If your repository is private, you might need to provide Jenkins with credentials to access the repository. Click on the "Add" button next to the "Credentials" field to add your GitHub credentials.
8. Optionally, you can specify a branch to build in the "Branches to build" field. If left blank, Jenkins will build the default branch (usually master).
9. You can configure additional options based on your project needs, such as polling for changes or setting up webhooks.
10. Click on "Save" to save your Jenkins job configuration.

