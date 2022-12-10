import cv2
import seam_carving

"""
1) Crie um programa para redimensionamento de vídeo utilizando o Seam Carving.
"""
def retarget_frames(frame, new_size, e_mode='forward', carving_order='height-first') :
    print("Retargeting...")
    return seam_carving.resize(
        frame, new_size,
        energy_mode=e_mode,   
        order=carving_order)


def retarget_video(filename: str) -> None:
    cap = cv2.VideoCapture(filename)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

    while True:
        ret, frame = cap.read()
        print("Reading Frames")

        if not ret: 
            print("error on reading the file")
            break

        x_scale, y_scale = 0.70, 0.70
        img_h, img_w, _ = frame.shape
        new_size = (int(img_w*x_scale), int(img_h*y_scale))
        
        frame = retarget_frames(frame, new_size)
        
        cv2.imshow("Retarget Frame",frame)

        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def show_video():
    cap = cv2.VideoCapture('output.avi')
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error on reading the file")
            break

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    filename = '../data/videos/v1.avi'
    #retarget_video(filename)
    show_video()

    