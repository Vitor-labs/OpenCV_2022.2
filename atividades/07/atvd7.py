import cv2
import time
"""
1) Usando o classificador HaarCascade, crie um programa que realize a detecção de rosto 
utilizando vídeo. Teste com imagens de diferentes resoluções e crie uma tabela com os 
tempos de execução em cada caso

2) Repita a questão anterior mas detecte também a boca e os olhos, diferenciando entre 
olho direito e olho esquerdo.
    – Em ambas as questões inclua imagens de rostos com as seguintes características:
        a) Vistos frontal e lateralmente;
        b) Utilizando acessórios (chapéu, óculos, máscaras, etc);
        c) Com e Sem barba, cabelos curtos/compridos/sem cabelo;
        d) De pessoas de diferentes etnias.
"""
def rescale_frames(frame, scale_factor=0.5):
    width = int(frame.shape[1] * scale_factor)
    height = int(frame.shape[0] * scale_factor)
    # resize image
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


def detect_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('haar_face.xml')
    eye_cascade = cv2.CascadeClassifier('haar_eye.xml')

    faces_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    num_faces = len(faces_rect)

    for x, y, w, h in faces_rect: 
        cv2.putText(img, "Face Detected", (x,y), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)
        
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    return img, num_faces


def main():    
    # Face detection, using Haar cascade classifier
    files = ['face1.avi',
            'face2.avi',
            'face3.avi']
    
    for file in files:
        start = time.time()
        cap = cv2.VideoCapture(f'../data/videos/{file}')
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame, num_faces = detect_faces(frame)

            cv2.imshow(f'Detected Faces', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        end = time.time()
        
        print("File: ",file," | Time: ",int(end-start)," s.")

if __name__ == '__main__':
    main()