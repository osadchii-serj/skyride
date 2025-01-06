from icecream import ic
from dataclasses import dataclass
from .client_meta import ClientMeta


@dataclass
class SkyRiderClient(metaclass=ClientMeta):
    
    def get_info(self):
        ic(SkyRiderClient.__dict__)
