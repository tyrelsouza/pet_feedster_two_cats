import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def render_stl(stl_file, output_image, elev=20, azim=45):
    mesh = trimesh.load(stl_file)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    vertices = mesh.vertices
    faces = mesh.faces

    # Plot the mesh
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2],
                     triangles=faces, alpha=0.7, edgecolor='none', shade=True)

    # Set equal aspect ratio
    max_range = np.array([vertices[:, 0].max() - vertices[:, 0].min(),
                         vertices[:, 1].max() - vertices[:, 1].min(),
                         vertices[:, 2].max() - vertices[:, 2].min()]).max() / 2.0

    mid_x = (vertices[:, 0].max() + vertices[:, 0].min()) * 0.5
    mid_y = (vertices[:, 1].max() + vertices[:, 1].min()) * 0.5
    mid_z = (vertices[:, 2].max() + vertices[:, 2].min()) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(stl_file.split('/')[-1])

    # Set view angle
    ax.view_init(elev=elev, azim=azim)

    plt.savefig(output_image, dpi=150, bbox_inches='tight')
    print(f"Saved {output_image}")
    plt.close()

if __name__ == '__main__':
    # Dish rotated 200 degrees
    render_stl('dish.STL', 'dish.png', elev=20, azim=200)
    # Diverter with standard view
    render_stl('Diverter.STL', 'diverter.png', elev=20, azim=45)
