from dataclasses import dataclass
import uuid
from datetime import datetime
import enum

@dataclass
class EvaluationStatusEnum:
    QUEUED = "QUEUED"
    DISPATCHED = "DISPATCHED"
    BUILDING = "BUILDING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"

@dataclass
class Evaluation:
    time = datetime.now
    status = enum(EvaluationStatusEnum)
    
