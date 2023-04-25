import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def create_labeled_rectangles(coords, labels):
    fig, ax = plt.subplots()
    for i, (x1, y1, x2, y2) in enumerate(coords):
        width = x2 - x1
        height = y2 - y1
        rect = Rectangle((x1, y1), width, height, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        # Add label to the center of the rectangle
        x_center = x1 + width / 2
        y_center = y1 + height / 2
        ax.text(x_center, y_center, labels[i], ha='center', va='center')

    # Set the plot limits based on the coordinates of all the rectangles
    x_min = min(coords, key=lambda c: c[0])[0]
    y_min = min(coords, key=lambda c: c[1])[1]
    x_max = max(coords, key=lambda c: c[2])[2]
    y_max = max(coords, key=lambda c: c[3])[3]
    plt.xlim(x_min - 1, x_max + 1)
    plt.ylim(y_min - 1, y_max + 1)

    plt.show()

def adjacency(rect):
    for i in range(len(rect)): # Plotting the current rectangles
        ans = []
        ans.append(i+1)
        count = 0
        for j in range(len(rect)):
            if rect[i][2] == rect[j][0] and rect[i][1] <= rect[j][3] and rect[i][3] >= rect[j][1]:
                count += 1
                ans.append(j+1)
                ans.append(max(rect[i][0], rect[j][0]))  
                ans.append(max(rect[i][1], rect[j][1]))  
                ans.append(min(rect[i][3], rect[j][3]))  
        ans.insert(1, count)
        print(ans)



# Example usage with labeled rectangles
coords = [[0 , 0 , 20 , 30],[8 , 40 , 20 , 55],[20 , 0 , 28 , 8],[20 , 12 , 50 , 16],[20 , 22 , 40 , 45],[40 , 22 , 47 , 30],[40 , 35 , 42 , 45],[42 , 42 , 48 , 52],[50 , 13 , 60 , 24],[60 , 14 , 70 , 25],[70 , 15 , 80 , 29]]
labels = []

for i in range(len(coords)):
    labels.append(i+1)

create_labeled_rectangles(coords, labels)

adjacency(coords)