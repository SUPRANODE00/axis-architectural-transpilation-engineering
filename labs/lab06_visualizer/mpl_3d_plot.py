import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_ast_3d(ast, vm=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs, ys, zs, labels = [], [], [], []

    for node in ast.children:
        if hasattr(node, 'resource') and node.resource:
            xs.append(node.resource.x)
            ys.append(node.resource.y)
            zs.append(node.resource.z)
            labels.append(node.name)

    if xs:
        ax.scatter(xs, ys, zs, c='cyan', s=80)

    for i, label in enumerate(labels):
        ax.text(xs[i], ys[i], zs[i], label)

    # VM trajectory line
    if vm and hasattr(vm, 'path') and vm.path:
        px = [p[0] for p in vm.path]
        py = [p[1] for p in vm.path]
        pz = [p[2] for p in vm.path]
        ax.plot(px, py, pz, color='red', linewidth=2)
        if px:
            ax.scatter(px[-1], py[-1], pz[-1], c='red', s=120)
            ax.text(px[-1], py[-1], pz[-1], "VM")

    ax.set_xlabel('Subsystem (x)')
    ax.set_ylabel('Lifecycle (y)')
    ax.set_zlabel('Resource Layer (z)')
    plt.show()
