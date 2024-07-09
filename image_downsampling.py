import numpy as np
import cv2

def image_downsampling( f, sampling_rate ):
	nr, nc = f.shape[:2]
	nr_s, nc_s = nr // sampling_rate, nc // sampling_rate
	g = np.zeros( [ nr_s, nc_s ], dtype = 'uint8' )
	for x in range( nr_s ):
		for y in range( nc_s ):
			g[x,y] = f[x * sampling_rate, y * sampling_rate]
	return g
	
def main( ):
	img1 = cv2.imread( "Barbara.bmp", -1 )
	img2 = image_downsampling( img1, 2 )		
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Downsampling by 2", img2 )					
	cv2.waitKey( 0 )

main( )