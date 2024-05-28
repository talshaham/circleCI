pipeline {
    agent any 
    environment {     
      DOCKERHUB_CREDENTIALS = credentials('dockerhub_username_password') 
      REPLICA= "4"
    }

    stages {
        stage('clone') {
            steps {
                git branch: 'main', credentialsId: 'gitlab_user_password', url: 'http://172.31.19.174/tal_user/app'
                echo 'Hello world!' 
            }
        }
        
        stage('build') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
        
        
        stage('login to dockerhub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'                 
	            echo 'Login Completed'
            }
        }

        stage('Tag and Push APP Image to Docker Hub') {
            steps{
                sh 'docker tag app-app:latest talshaham/app-weather:latest'
                sh 'docker tag app-app:latest talshaham/app-weather:$BUILD_NUMBER'
                //sh 'docker tag app-nginx talshaham/nginx:latest'

                sh 'docker push talshaham/app-weather:latest'
                sh 'docker push talshaham/app-weather:$BUILD_NUMBER'
                //sh 'docker push talshaham/nginx:latest'

                echo 'APP Push Image Completed'
            }
        }
        
        stage('second clone') {
            steps {
                git branch: 'main', credentialsId: 'second_pipeline_gitlab_username_password', url: 'http://172.31.19.174/tal_user/deployment'
                echo 'Hello world!' 
            }
        }
        
        

        stage('kubernetes cluster chagne context') {
            steps {
                sh 'aws eks update-kubeconfig --name pc-eks --region eu-north-1'
            }
        }



        stage('change version of value.yaml file ') {
            steps {
                sh "yq e '.spec.template.spec.containers[0].image = \"talshaham/app-weather:${BUILD_NUMBER}\"' -i /home/ec2-user/agent1/workspace/app/mychart/templates/deployment.yaml"
                sh 'helm upgrade weather-app mychart'
            }
        }        
    }
  
    post {
        success {
            sh 'echo pipeline succeed'
        }
        failure {
            sh 'echo pipeline failed'
        }
        always {
            sh 'docker rm -v -f $(docker ps -qa)'
            sh 'docker rmi -f $(docker images -a -q)'
           //sh 'rm -rf /home/ec2-user/agent1/workspace'
        }
    }
}
