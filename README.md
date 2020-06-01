# Chimera

`// TODO: Finish this readme`

The intent of Chimera is to streamline the operationalization of a Kubernetes cluster. Other solutions exist, but they are either complicated to deploy or don't encompass some crucial aspects of Kubernetes operationalization.

In order to productivly leverage Kubernetes in an enterprise the following needs to happen: 
1. Infrastructure must exist. This means that the infrastructure, wether physical or cloud based, needs to have been built, secured, and operationalized. (what does does it mean to build, secure, and operationalize?)
2. The Kubernetes cluster will need to have been deployed and operationalized. While this requirement may seem obvious, it actually encompases more than one might realize.
    - The cluster has to have been installed and configured.
    - The running cluster may need cluster state backups.
    - Metrics will need to be collected and stored for the cluster, node, and network.
    - Dashboards will need to be built to display the stored metrics and troubleshoot the inevitable performance issues end users will report.
    - Alarms will need to be configured to alert on events that might impact cluster stability.
    - A security solution will need to be installed and configured to ensure the cluster isn't a giant attack vector.
    - An identity solution will need to be in place
    - The cluster will require a deployment pipeline

    And as a bonus:
    - We'll need some way of managing all this.


Chimeras tagline will be: "Make easy Kubernetes useful".

