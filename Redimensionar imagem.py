import cv2 as cv

imagem = cv.imread("Endereço da imagem aqui")

tamanho = cv.resize(imagem,(720, 1080))

cv.imshow("IMAGEM EDITADA", tamanho)

cv.imshow("IMAGEM ORIGINAL", imagem)

cv.waitKey()
