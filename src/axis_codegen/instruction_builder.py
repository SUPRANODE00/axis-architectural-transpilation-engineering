def build_instructions_from_ast(node):
    instructions = []

    # MOV_3D if node has resource coordinates
    if node.resource:
        instructions.append({
            "op": "MOV_3D",
            "x": node.resource.x,
            "y": node.resource.y,
            "z": node.resource.z
        })

    # PUSH node name for debugging / tracing
    if node.name:
        instructions.append({
            "op": "PUSH",
            "value": node.name
        })

    # Recurse into children
    for child in node.children:
        instructions.extend(build_instructions_from_ast(child))

    return instructions
