from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd
import os
    
def augmentation_show(image_id, path, samples, datagen, count):
    global label
    
    path = '/'.join(path) + "/" + str(image_id) + "_"
    
    # prepare iterator
    it = datagen.flow(samples, batch_size=1)
    
    # generate samples and plot
    for i in range(count):   
        #generate batch of image
        batch = it.next()
        
        # convert to unsigned integers for viewing
        image = batch[0].astype('uint8')
        
        # plot raw pixel data
        print(label)
        print(path + str(label) + ".png")
        plt.figure(figsize=(0.68, 0.68), frameon=False)
        plt.axis("off"), plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
        plt.imshow(image)
        # show the figure
        plt.savefig(path+str(label)+".png", format="png")
        # plt.show()
        label += 1

def image_augmentation(image_id, image_path):    
    # load the image
    img = load_img(image_path)
    path = image_path.split('/')[:-1]
    
    global label
    label = 1
    
    # convert to numpy array
    data = img_to_array(img)
    
    #
    print(data.shape)
    #

    # expand dimension to one sample
    samples = np.expand_dims(data, 0)
    
    # create image data augmentation generator
    datagen = ImageDataGenerator(zoom_range=[0.5, 1.3],
                                 rotation_range=360,
                                 height_shift_range=0.1,
                                 width_shift_range=0.1
                                 )
    augmentation_show(image_id, path, samples, datagen, 9)

if __name__=="__main__":
    data_list = pd.read_csv("./5country.csv")

    for i in range(len(data_list)):
        image_id = int(data_list.iloc[i][0])
        image_nation = data_list.iloc[i][3]
        image_path = "./valid_pictures/" + image_nation + "/{}.png".format(image_id)

        if (os.path.isfile(image_path)):
            image_augmentation(image_id, image_path)

        
