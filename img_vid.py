import cv2



num = input("Enter: "
            "\n 1: to script Image"
            "\n 2: to script video"
            "\n your number:"
            )

print("====================================================")


####################   script Imaga     #####################

if num == "1":

        num = input("Enter: "
                    "\n 1: to show the image with color(color)"
                    "\n 2: to show the image without color(Grayscale) "
                    "\n 3: to change '.jpg' file to '.png' file"
                    "\n 4: to change resize image"
                    "\n 5: to Blurred image "
                    "\n your number:"

                    )

        if num == "1":
            read_img = cv2.imread('img_car.jpg',1)
            cv2.imshow("Title_Image",read_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif num == "2":
            read_img = cv2.imread('img_car.jpg', 0)
            cv2.imshow("Title_Image", read_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif num == "3":
            read_img = cv2.imread('img_car.jpg', 1)
            cv2.imwrite("img_car.png", read_img)
            cv2.imshow("Title_Image", read_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif num == "4":
            read_img = cv2.imread('img_car.jpg', 1)
            width = 400
            height = 200
            resize = cv2.resize(read_img,(width,height))
            cv2.imshow("Title_Image", resize)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif num == "5":
            read_img = cv2.imread('img_car.jpg', 1)
            blurred = cv2.GaussianBlur(read_img , (31,31) , 0)
            cv2.imshow("Title_Image", blurred)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


####################   script video     #####################
elif num == "2":

    num = input("Enter: "
                "\n 1: to show Video"
                "\n 2: to Blurred Video "
                "\n 3: to Background Subtraction"
                "\n your number:"

                )

    if num == "1":

        read_vid = cv2.VideoCapture("VIDEO_car.mp4")
        if(read_vid.isOpened() == False):
            print("Error for read video")

        while (read_vid.isOpened()):
            ret,frame = read_vid.read()

            if ret == True:
                cv2.imshow('frame',frame)
                if cv2.waitKey(50)  == ord('q'):
                    break
            else:
                cv2.waitKey(0)


        read_vid.release()
        cv2.destroyAllWindows()



    if num == "2":

        read_vid = cv2.VideoCapture("VIDEO_car.mp4")

        if(read_vid.isOpened() == False):
            print("Error for read video")
        while (read_vid.isOpened()):
            ret,frame = read_vid.read()
            frame_bluer = cv2.GaussianBlur(frame,(11,11),0)

            if ret == True:
                cv2.imshow('frame',frame)
                cv2.imshow('frame Bluer', frame_bluer)
                if cv2.waitKey(50)  == ord('q'):
                    break
            else:
                cv2.waitKey(0)


        read_vid.release()
        cv2.destroyAllWindows()


    if num == "3":

        read_vid = cv2.VideoCapture("VIDEO_car.mp4")
        subtractor = cv2.createBackgroundSubtractorMOG2()

        if(read_vid.isOpened() == False):
            print("Error for read video")
        while (read_vid.isOpened()):
            ret,frame = read_vid.read()
            subtractor_frame = subtractor.apply(frame)

            if ret == True:
                cv2.imshow('frame',frame)
                cv2.imshow('subtraction frame', subtractor_frame)
                if cv2.waitKey(50)  == ord('q'):
                    break
            else:
                cv2.waitKey(0)


        read_vid.release()
        cv2.destroyAllWindows()






