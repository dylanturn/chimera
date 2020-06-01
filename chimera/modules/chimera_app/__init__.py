from constructs import Construct
from cdk8s import Chart
from chimera.modules.chimera_app import ProbeResponse


class ChimeraApp(Chart):
    #def __init__(self, scope: Construct, name: str, ):
    #    super().__init__(scope, name)

    def __init__(self, name: str = None, ports: list = []):
        self.name = name
        self.ports = ports

    def on_start(self) -> int:
        pass

    def on_stop(self) -> int:
        pass

    def on_liveness_probe(self) -> ProbeResponse:
        pass

    def on_readiness_probe(self) -> ProbeResponse:
        pass


class ProbeResponse(object):
    def __init__(self, response_status: int, response_message: str = None):
        self.response_status = response_status
        self.response_message = response_message
