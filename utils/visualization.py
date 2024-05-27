import matplotlib.pyplot as plt

def create_visualization(data):
    # Example: Creating a bar chart of some data
    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values())
    plt.savefig('static/images/visualization.png')
    return 'static/images/visualization.png'
