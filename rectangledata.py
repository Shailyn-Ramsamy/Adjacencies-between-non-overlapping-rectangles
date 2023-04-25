import matplotlib.pyplot as plt
import numpy as np
import timeit
import random
import pandas as pd

def adjacency(rect):
    for i in range(len(rect)): # Plotting the current rectangles
        ans = []
        ans.append(i)
        count = 0
        for j in range(len(rect)):
            if rect[i][2] == rect[j][0] and rect[i][1] <= rect[j][3] and rect[i][3] >= rect[j][1]:
                count += 1
                ans.append(j)
                ans.append(max(rect[i][0], rect[j][0]))  
                ans.append(max(rect[i][1], rect[j][1]))  
                ans.append(min(rect[i][3], rect[j][3]))  
        ans.insert(1, count)
        # print(ans)

random.seed(90)
#Define outer rectangle
xb = 1
yb = 1
xt = 100000
yt = 100000

x = np.array([xb,xt,xt,xb,xb])
y = np.array([yb,yb,yt,yt,yb])

plt.plot(x, y)
plt.show()

rect = []

rect.append([xb,yb,xt,yt])

print(rect)


# Split the first 4 rectangles into 4 rectangles each
for k in range(5):
    print("k is ", k)
    new = rect.pop(0)

    xb = new[0]
    yb = new[1]
    xt = new[2]
    yt = new[3]

    if ((xt-xb) > 1000) and ((yt -yb) > 1000):
        print("which rectangle", new)

        midx = int((xt - xb)/2) + xb
        midy = int((yt - yb)/2) + yb
        rx = random.randint(midx-400,midx+400)
        ry = random.randint(midy-400,midy+400)

        print(rx,ry)

        rect.append([xb,yb,rx,ry])
        rect.append([xb,ry,rx,yt])
        rect.append([rx,yb,xt,ry])
        rect.append([rx,ry,xt,yt])

        print(rect)

        for i in range(len(rect)):
            xb = rect[i][0]
            yb = rect[i][1]
            xt = rect[i][2]
            yt = rect[i][3]
            print(i, xb, yb, xt, yt)
            x1 = np.array([xb,xt,xt,xb,xb])
            y1 = np.array([yb,yb,yt,yt,yb])

            plt.plot(x1, y1)

    plt.show()

# Choose a random rectange and split it into 4 rectangles
for i in range(40000):
    # print("length of list ", len(rect))

    thisRect = random.randint(0,len(rect)-1)

    # print("which rectangle has been chosen ", thisRect)

    new = rect.pop(thisRect)

    #print("list", rect)

    xb = new[0]
    yb = new[1]
    xt = new[2]
    yt = new[3]

    if ((xt - xb) > 1000) and ((yt - yb) > 1000):
        # print("which rectangle", new)

        midx = int((xt - xb)/2) + xb
        midy = int((yt - yb)/2) + yb
        rx = random.randint(midx-200,midx+200)
        ry = random.randint(midy-200,midy+200)

        # print(rx,ry)

        rect.append([xb,yb,rx,ry])
        rect.append([xb,ry,rx,yt])
        rect.append([rx,yb,xt,ry])
        rect.append([rx,ry,xt,yt])
    else:
        rect.append(new)

##        print(rect) # Printing the current list of rectangles
##
##        for i in range(len(rect)): # Plotting the current rectangles
##            xb = rect[i][0]
##            yb = rect[i][1]
##            xt = rect[i][2]
##            yt = rect[i][3]
##            print(i, xb, yb, xt, yt)
##            x1 = np.array([xb,xt,xt,xb,xb])
##            y1 = np.array([yb,yb,yt,yt,yb])
##
##            plt.plot(x1, y1)
##
##    plt.show()

# the final rectangles
# print("the final list of rectangles")
# print("------------------------------")
for i in range(len(rect)): # Plotting the current rectangles
    xb = rect[i][0]
    yb = rect[i][1]
    xt = rect[i][2]
    yt = rect[i][3]
    # print(i, xb, yb, xt, yt)
    x1 = np.array([xb,xt,xt,xb,xb])
    y1 = np.array([yb,yb,yt,yt,yb])

    plt.plot(x1, y1)

adjacency(rect)
plt.show()

input_arr_1 = []
times_1 = []

for n in range(1, 20001, 100):
    mylist_1 = rect[:n]
    t1 = timeit.timeit(lambda: adjacency(mylist_1), number=1)
    input_arr_1.append(n)
    times_1.append(f"{t1*1000}")

data_1 = {"input": input_arr_1, "time": times_1}
df_1 = pd.DataFrame(data_1)
df_1.to_csv("adjacency.csv", index = False, sep=',')