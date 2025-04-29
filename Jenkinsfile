pipeline {
    agent any
    stages {
        stage("Clone") {
            steps {
                git branch: 'main', url: 'https://github.com/SAILATHA-284/Devops_prac_1.git'
            }
        }
        stage("Deploy") {
            steps {
                script {
                    bat "copy index2.html C:\\xampp\\htdocs\\index2.html"
                }
            }
        }
    }
}
