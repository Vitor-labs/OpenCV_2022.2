import cv2

"""
1) Usando o classificador HaarCascade, crie um programa que realize a detecção de rosto 
utilizando vídeo. Teste com imagens de diferentes resoluções e crie uma tabela com os 
tempos de execução em cada caso

2) Repita a questão anterior mas detecte também a boca e os olhos, diferenciando entre 
olho direito e olho esquerdo.
    – Em ambas as questões inclua imagens de rostos com as seguintes características:
        a) Vistos frontal e lateralmente;
        b) Utilizando acessórios (chapéu, óculos, máscaras, etc);
        c) Com e Sem barba,  cabelos curtos/compridos/sem cabelo;
    d) De pessoas de diferentes etnias.
"""
def rescale_frames(frame, scale_factor=0.5):
    width = int(frame.shape[1] * scale_factor)
    height = int(frame.shape[0] * scale_factor)
    # resize image
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


def detect_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier('haar_face.xml')
    faces_rect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
    
    num_faces = len(faces_rect)

    for x, y, w, h in faces_rect:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), thickness=2)

    return img, num_faces


def main():    
    # Face detection, using Haar cascade classifier
    filename = '../data/images/oscar.jpg'
    img = cv2.imread(filename)

    faces_img, faces = detect_faces(img)
    resized = rescale_frames(faces_img)

    cv2.imshow(f'Detected {faces} faces', resized)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()