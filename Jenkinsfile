#!groovy

def tryStep(String message, Closure block, Closure tearDown = null) {
    try {
        block();
    }
    catch (Throwable t) {
        slackSend message: "${env.JOB_NAME}: ${message} failure ${env.BUILD_URL}", channel: '#ci-channel', color: 'danger'

        throw t;
    }
    finally {
        if (tearDown) {
            tearDown();
        }
    }
}

node {
    stage("Checkout") {
        checkout scm
    }


    stage('Test') {
        tryStep "Test", {
            sh "app/deploy/test/jenkins-script.sh"
        }
    }


    stage("Build develop image") {
        tryStep "build", {
            def image = docker.build("repo.secure.amsterdam.nl/fixxx/looplijsten:${env.BUILD_NUMBER}", "./app")
            image.push()
        }
    }
}

String BRANCH = "${env.BRANCH_NAME}"

if (BRANCH == "master") {
    node {
        stage('Push acceptance image') {
            tryStep "image tagging", {
                def image = docker.image("repo.secure.amsterdam.nl/fixxx/looplijsten:${env.BUILD_NUMBER}")
                image.pull()
                image.push("acceptance")
            }
        }
    }

    node {
        stage("Deploy to ACC") {
            tryStep "deployment", {
                build job: 'Subtask_Openstack_Playbook',
                        parameters: [
                                [$class: 'StringParameterValue', name: 'INFRASTRUCTURE', value: 'secure'],
                                [$class: 'StringParameterValue', name: 'INVENTORY', value: 'acceptance'],
                                [$class: 'StringParameterValue', name: 'PLAYBOOK', value: 'deploy-looplijsten-backend.yml'],
                        ]
            }
        }
    }

    stage('Waiting for approval') {
        slackSend channel: '#ci-channel', color: 'warning', message: 'Looplijsten backend is waiting for Production Release - please confirm'
        input "Deploy to Production?"
    }

    node {
        stage('Push production image') {
            tryStep "image tagging", {
                def image = docker.image("repo.secure.amsterdam.nl/fixxx/looplijsten:${env.BUILD_NUMBER}")
                image.pull()
                image.push("production")
                image.push("latest")
            }
        }
    }

    node {
        stage("Deploy") {
            tryStep "deployment", {
                build job: 'Subtask_Openstack_Playbook',
                        parameters: [
                                [$class: 'StringParameterValue', name: 'INFRASTRUCTURE', value: 'secure'],
                                [$class: 'StringParameterValue', name: 'INVENTORY', value: 'production'],
                                [$class: 'StringParameterValue', name: 'PLAYBOOK', value: 'deploy-looplijsten-backend.yml'],
                        ]
            }
        }
    }
}