from constructs import Construct
from cdk8s import Chart
from chimera.kube.kubeasy import Deployment, Service


class RedisChart(Chart):
    def __init__(self, scope: Construct, name: str):
        super().__init__(scope, name)

        name = "redis-db"
        image = "redis"
        release = "6.0.4"
        environment = "lab"
        replicas = 1

        self.__read_defaults__()

        deployment = Deployment(name=name, image=image, tag=release, environment=environment) \
            .set_replicas(replicas) \
            .render(self)

        Service("redis", deployment, release, environment) \
            .set_port(6379)   \
            .set_target(6379) \
            .render(self)

    def __read_defaults__(self):
        # This is an example how how we could read in and override some values.
        pass