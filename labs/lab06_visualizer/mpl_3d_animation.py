import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np

def animate_vm_path(ast, vm):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot AST nodes
    xs, ys, zs = [], [], []
    for node in ast.children:
        xs.append(node.resource.x)
        ys.append(node.resource.y)
        zs.append(node.resource.z)
    ax.scatter(xs, ys, zs, c='cyan', s=80)

    # VM path arrays
    px = [p[0] for p in vm.path]
    py = [p[1] for p in vm.path]
    pz = [p[2] for p in vm.path]
    intensity = [p[3] for p in vm.path]

    # Animated point
    point = ax.scatter([], [], [], c='red', s=120)

    # Animated trail
    trail, = ax.plot([], [], [], color='red', linewidth=2)

    def update(frame):
        # Update point position
        point._offsets3d = ([px[frame]], [py[frame]], [pz[frame]])

        # Update trail
        trail.set_data(px[:frame+1], py[:frame+1])
        trail.set_3d_properties(pz[:frame+1])

        return point, trail

    ani = FuncAnimation(fig, update, frames=len(px), interval=500, blit=False)

    ax.set_xlabel('Subsystem (x)')
    ax.set_ylabel('Lifecycle (y)')
    ax.set_zlabel('Resource Layer (z)')
    plt.show()
