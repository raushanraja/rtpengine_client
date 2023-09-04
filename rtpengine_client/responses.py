from dataclasses import dataclass
from collections import OrderedDict
from typing import List

@dataclass
class RTPEngineResult:
    cookie: str
    result: str
    raw_data: bytes
    decoded_data: OrderedDict


class PingResult(RTPEngineResult):
    pass


@dataclass
class CallListResult(RTPEngineResult):
    calls: List[str]
