import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_ast_3d(ast):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs, ys, zs, labels = [], [], [], []

    for node in getattr(ast, 'children', []):
        if node.resource:
            xs.append(node.resource.x)
            ys.append(node.resource.y)
            zs.append(node.resource.z)
            labels.append(node.name)

    if xs:
        ax.scatter(xs, ys, zs, c='cyan', s=80)
        for i, label in enumerate(labels):
            ax.text(xs[i], ys[i], zs[i], label)

    ax.set_xlabel('Subsystem (x)')
    ax.set_ylabel('Lifecycle (y)')
    ax.set_zlabel('Resource Layer (z)')
    plt.show()
