import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_resource_heatmap(ast, vm):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs, ys, zs = [], [], []
    for node in ast.children:
        xs.append(node.resource.x)
        ys.append(node.resource.y)
        zs.append(node.resource.z)
    ax.scatter(xs, ys, zs, c='cyan', s=80)

    if hasattr(vm, "path") and vm.path:
        px, py, pz, intensity = zip(*vm.path)
        colors = plt.cm.plasma(np.array(intensity))
        ax.scatter(px, py, pz, c=colors, s=120)

    ax.set_xlabel('Subsystem (x)')
    ax.set_ylabel('Lifecycle (y)')
    ax.set_zlabel('Resource Layer (z)')
    plt.show()
