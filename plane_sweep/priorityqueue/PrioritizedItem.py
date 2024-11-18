from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: tuple[float, float]
    item: Any=field(compare=False)
    
    
