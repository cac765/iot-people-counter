import cv2


testImage = cv2.imread( 'input_images/T1.jpg' )

cv2.namedWindow( "test", cv2.WINDOW_NORMAL )
cv2.resizeWindow( "test", 800, 600 )
cv2.imshow( "test", testImage )

cv2.waitKey(0)
cv2.destroyAllWindows()
