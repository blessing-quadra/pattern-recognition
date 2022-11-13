import cv2
import os

# path to save the image
directory = r'C:\Users\USER\Documents\newFinalProject\scripts\test-sample5'
def snap_and_save(img, num_of_faceup, num_of_facedown):
    os.chdir(directory)
    sample_name = "sample.png".format(0)
    cv2.imwrite(sample_name, img)
    result_filename = "result.txt"

    f = open(result_filename, "w")
    f.write(str(num_of_faceup)+str(num_of_facedown))
    f.close()
    
   