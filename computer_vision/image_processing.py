import numpy as np

def image_process(img, targetandtolleranceRGB):
    # print("Filtering numpy style")
    pix = np.array(img)
    RGB_ref = np.array(list(targetandtolleranceRGB[:-1]))
    a = np.transpose(np.abs(pix - RGB_ref), (2,0,1))
    b = (a[0] + a[1] + a[2]) < targetandtolleranceRGB[-1]
    y_plot, x_plot = np.where(b)
    points = np.transpose(np.array([x_plot, -y_plot]))
    return points, x_plot, -y_plot
