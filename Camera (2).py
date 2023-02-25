import cv2, os

def Capture():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        cv2.waitKey(1)
        if not ret:
            print("failed to grab frame for camera")
            break

        cv2.imshow("Camera", frame)
        k = cv2.waitKey(1)

        if k%256 == 27:
            print("Esc Key Pressed, Closing")
            break
        elif k%256 == 32:
            person_name1 = str(input("Enter Name of the Person: "))
            path = "Authorized_Persons_Data/Captured_Images/" +person_name1+ ".png"
            isExist = os.path.exists(path)
            # print(isExist)

            if isExist:
                print("Person is already present in the Database, Enter Name of the Person that is Not Registered!")
                continue
                # person_name = str(input("Enter Name of the Person that is Not Registered: "))
            else:
                person_name = person_name1


            cv2.imwrite("Authorized_Persons_Data/Captured_Images/" + person_name +".png", frame)
            print("Image Captured and Saved!")


    cam.release()
    cv2.destroyAllWindows()

Capture()
