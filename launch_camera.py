import cv2
import importlib


num_of_faceup = 0
num_of_facedown = 0

def generatePatternMetrics():
    return (num_of_faceup, num_of_facedown)

def camera():
    sample_snapped = False
    # import detect sample module
    detect_module = importlib.import_module("detect_sample")
    capture_module = importlib.import_module("snap_and_save")
    
    # define a video capture object
    vid = cv2.VideoCapture(0)
    
    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        img = frame

        # flip the fram
        # frame = cv2.flip(frame, 90)?
    
        # Display the resulting frame
        (num_of_faceup, num_of_facedown) = detect_module.detect_sample(frame)
        # cv2.imshow('frame', frame)
        
        # if key "c" is pressed, capture the samples and store in the sample5 directory
        if cv2.waitKey(1) & 0xFF == ord('c'):
            capture_module.snap_and_save(frame, num_of_faceup, num_of_facedown)
            sample_snapped = True
            print("Sample Captured")
            break
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    if(sample_snapped):
        img = cv2.imread("./sample.png")
        img = cv2.resize(img,(416,416), interpolation=cv2.INTER_AREA)
        cv2.imshow("Sample captured", img)
        cv2.waitKey(0)
        print("Is the sample correct? If no, re-capture the sample")
        
    else:
        print("Camera Closed")