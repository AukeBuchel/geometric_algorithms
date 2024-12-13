from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: tuple[float, float, int]
    item: Any=field(compare=False)
    
    
