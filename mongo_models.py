from dataclasses import dataclass
from datetime import datetime
import enum
import json

@dataclass
class LogLevels(enum.Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

@dataclass
class EvaluationStatusEnum(enum.Enum):
    QUEUED = "QUEUED"
    DISPATCHED = "DISPATCHED"
    BUILDING = "BUILDING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"

@dataclass
class EvaluationStatus:
    id: int
    time: int
    status: EvaluationStatusEnum
    meta: str
    evaluation_id: int

@dataclass
class Agent:
    id: int
    name: str
    type: str
    evaluation_id: int
    #evaluation:
    #logs:
    #order_by:
    #metrics:
    #order_by:

@dataclass
class AgentLog:
    id: int
    time: datetime.now
    level: LogLevels
    message: str
    agent_id: int
    #agent:

@dataclass
class Metic:
    id: int
    time: datetime.now
    type: str
    data: json
    agent_id: int
    evaluation_id: int
    #evaluation:

@dataclass
class Network:
    id: int
    name: str
    specification: json
    #evaluations:

@dataclass
class Experiment:
    id: int
    name: str
    meta: json
    network_id: int
    #network:
    experiment_id: int
    #experiment:
    #agents:
    #metrics:
    #statuses:

def to_json(self):
        return json.dumps(self.__dict__, default=lambda x: x.__dict__, indent=4)