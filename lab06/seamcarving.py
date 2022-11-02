#pip install seam-carving
#https://pypi.org/project/seam-carving/

import cv2
import argparse
import seam_carving


def waitKey(window_name, key):
    while cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(1000) & 0xFF
        if (keyCode == key):
            cv2.destroyAllWindows()
            break

# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="Arquivo de imagem a ser redimensionada")
ap.add_argument("-fe","--forward", action='store_true', help="Calcular a energia adicionada")
ap.add_argument("-hf","--height_first", action='store_true', help="Remover primeiro as linhas")
ap.add_argument("-x", "--x_scale", type=int,default="100", help="Percentual de redimensionamento em x (0 a 100)")
ap.add_argument("-y", "--y_scale", type=int,default="100", help="Percentual de redimensionamento em y (0 a 100)")
args = vars(ap.parse_args())


#Imagem
img = cv2.imread(args["image"])
img_h, img_w, _ = img.shape


#Escala
x_scale = args["x_scale"]/100
y_scale = args["y_scale"]/100

new_size = (img_w*x_scale, img_h*y_scale)

#Cálculo da energia
if(args["forward"]):
    e_mode = 'forward'
else:
    e_mode = 'backward'
    
#Ordem de remoção dos seams
if(args["height_first"]):
    carving_order = 'height-first'
else:
    carving_order = 'width-first'

#Seam Carving
img_seam = seam_carving.resize(
    img, new_size,
    energy_mode=e_mode,   
    order=carving_order)

# Show
cv2.imshow("Original", img)
cv2.imshow("Seam Carving", img_seam)


waitKey("Original",27)
waitKey("Seam Carving",27)


