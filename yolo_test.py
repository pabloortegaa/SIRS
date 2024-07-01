import cv2
from ultralytics import YOLO

from inference_sdk import InferenceHTTPClient
trash_dicc = {'battery': "yellow",
    'can': "grey",
    'cardboard': "blue",
    'drink carton': "yellow",
    'glass bottle': "blue",
    'paper': "blue",
    'plastic bag': "yellow",
    'plastic bottle': "yellow",
    'plastic bottle cap': "yellow",
    'pop tab': "yellow"
}
# apply yolo with my camera
cap = cv2.VideoCapture(0)
#model = YOLO('best.pt')
#classes = model.names
acc = 0



CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="edaGCjsVTBNpdktOlNxH"
)


while True:
    ret, frame = cap.read()
    acc +=1
    print(acc)

    #cv2.imshow('frame', frame)
    if acc == 60: 
        acc = 0
        '''
        results = model(frame)
        rectangle_thickness = 2
        text_thickness = 2
        highest_probability = 0
        highest_probability_class = ""
        highest_result = None
        box = None
        
        for result in results:
            for box in result.boxes:
                # get the one with the highest probability
                if box.conf[0] > highest_probability:
                    highest_probability = box.conf[0]
                    highest_probability_class = result.names[int(box.cls[0])]
                    highest_result = result
        
        if box:
            print(highest_probability_class)
            print(highest_probability)
            bin = trash_dicc[highest_probability_class]
            # Calculate the middle coordinates of the image
            image_height, image_width, _ = frame.shape
            middle_x = int(image_width / 2)
            middle_y = int(image_height / 2)
            
            # Draw rectangle and put text in the middle of the image
            #cv2.rectangle(frame, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),(int(box.xyxy[0][2]), int(box.xyxy[0][3])), (255, 0, 0), rectangle_thickness)
            cv2.putText(frame, f"{bin}",
                        (middle_x, middle_y),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), text_thickness)
            print(bin)
            '''
        
        result = CLIENT.infer(frame, model_id="garbage-classification-3/2")

        print(result)
            
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break