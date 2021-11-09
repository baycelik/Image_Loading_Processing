%matplotlib inline
import matplotlib.pyplot as plt
from IPython.display import display
import pandas as pd
import numpy as np
from PIL import Image
test_data=np.random.beta(1,1,size=(100,100,3))
img = Image.open('')
img_size = img.size
print("The image size is: {}".format(img_size))
img

img_cropped = img.crop([25,25,75,75])
display(img_cropped)
img_rotated = img.rotate(45,expand=25)
display(img_rotated)
img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
display(img_flipped)


img_data = np.array(img)
img_data_shape = img_data.shape
plt.imshow(img_data)
plt.show()
plt.imshow(img_data[:,:,0], cmap=plt.cm.Reds_r)
plt.show()
plt.imshow(img_data[:,:,1], cmap=plt.cm.Greens_r)
plt.show()
plt.imshow(img_data[:,:,2], cmap=plt.cm.Blues_r)
plt.show()
img_data[:,:,1]

def plot_kde(channel, color):
    data = channel.flatten()
    return pd.Series(data).plot.density(c=color)
channels = ['r','g','b']
    
def plot_rgb(image_data):
    for ix, color in enumerate(channels):
        plot_kde(image_data[:,:,ix],color)
    plt.show()    
plot_rgb(img_data)
honey=Image.open('')
display(honey)
honey_data=np.array(honey)
plot_rgb(honey_data)
bumble=Image.open('')
display(bumble)
bumble_data=np.array(bumble)
plot_rgb(bumble_data)
honey_bw = honey.convert("L")
display(honey_bw)
honey_bw_arr = np.array(honey_bw)
honey_bw_arr_shape = honey_bw_arr.shape
print("Our NumPy array has the shape: {}".format(honey_bw_arr_shape))
plt.imshow(honey_bw_arr, cmap=plt.cm.gray)
plt.show()
plot_kde(honey_bw_arr, 'k')
honey_bw_flip = honey_bw.transpose(Image.FLIP_LEFT_RIGHT)
display(honey_bw_flip)
honey_bw_flip.save("")
honey_hc_arr = np.maximum(honey_bw_arr, 100)
plt.imshow(honey_hc_arr, cmap=plt.cm.gray)
honey_bw_hc = Image.fromarray(honey_hc_arr)
honey_bw_hc.save("")
image_paths = ['', '', '', '']

def process_image(path):
    img = Image.open(path)
    bw_path = "".format(path.stem)
    rcz_path = "".format(path.stem)
    print("Creating grayscale version of {} and saving to {}.".format(path, bw_path))
    bw = img.convert("L")
    bw.save(bw_path)
    print("Creating rotated, cropped, and zoomed version of {} and saving to {}.".format(path, rcz_path))
    rcz = bw.rotate(45).crop([25,25,75,75]).resize((100,100))
    rcz.save(rcz_path)
for img_path in image_paths:
    process_image(Path(img_path))
    
    