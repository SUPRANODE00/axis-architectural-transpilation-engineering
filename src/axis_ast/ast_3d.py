from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Resource3D:
    """
    3D resource coordinate model for AST nodes.

    x = subsystem / domain
    y = time / lifecycle phase
    z = resource layer (compute, storage, network, signal)
    """
    x: float
    y: float
    z: float
    layer: str


@dataclass
class Axis3DNode:
    """
    AST node with 3D resource mapping and troubleshooting metadata.
    """
    kind: str
    name: Optional[str] = None
    children: List["Axis3DNode"] = field(default_factory=list)
    resource: Optional[Resource3D] = None
    trace_id: Optional[str] = None
    severity: Optional[str] = None

    def add_child(self, node: "Axis3DNode") -> None:
        self.children.append(node)


def attach_3d_resource(node: Axis3DNode,
                       x: float,
                       y: float,
                       z: float,
                       layer: str,
                       severity: str = "info",
                       trace_id: Optional[str] = None) -> Axis3DNode:
    node.resource = Resource3D(x=x, y=y, z=z, layer=layer)
    node.severity = severity
    node.trace_id = trace_id
    return node
