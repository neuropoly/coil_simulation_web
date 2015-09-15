
import scipyo
from scipyo import math as m
from scipyo 

global N = 100, PI = m.pi

class Coil: #Define class Coil for rotate, translate, define_coil, gen_coil and gen_array

	def __init__(self, posinx, posiny, posinz, rada, radb, radc):  #Écrire bobine = Coil(10, 20) voudra dire que bobine.xpos = 10 et bobine.ypos = 20
																   #S'il est nécéssaire d'initialiser à 0, on peut le faire directement dans les () e.g. (self, xpos=0, ypos...)
		self.posinx = posinx
		self.posiny = posiny
		self.posinz = posinz
		self.rada = rada
		self.radb = radb
		self.radc = radc
		
	def gen_coil(self, posinx, posiny, posinz, rada, radb, coil_init):
		coil_init = [[0 for j in range(N)] for j in range(3)]
		t=-PI/2  #used to describe the circle 		*** DIVISION PAR 0? *** *** "N-i" ou "i-1"? dans gen_coil la fomule originale est N-1) ***
		for i in N-1	
			xcoor = posinx+rada*m.cos(t)    	 		 #x coordinates of the coil			*** VÉRIFIER LA CRÉATION DU VECTEUR AVEC LE "t" ***
			ycoor = posiny+radb*m.sin(t)   				 #y coordinates of the coil
			zcoor = posinz*numpy.ones(size(t)) 			 #z coordinates of the coil
			
			#Matrice 100X3 lignes 0 à 99, colones x, y, z cotenant chacun un vecteur de 3 valeurs (fournies par "t")
			coil_init[i][0] = xcoor 
			coil_init[i][1] = ycoor
			coil_init[i][2] = zcoor
			t+=2*PI/(N-1)
		#for end
		return coil_init
	
	def rotation(self, posinx, radc)
		theta=-(m.asin(posinx(en)/radc)
		#generate rotation matrix for Y axis
		Ry = [[m.cos(theta), 0, m.sin(theta)], [0, 1, 0], [-m.sin(theta), 0, m.cos(theta)]]
		self.coil_rotated = dot(Ry, self.coil_init)
		return self.coil_rotated
	
	def translation(self, Tx, Ty, Tz, Tr):
		Tx=self.posinx(en)
		Ty=0
		Tz=self.radc-m.cos(m.asin(self.posinx(en)/self.radc))*self.radc
		Tr=[[1, 0, 0, Tx], [0, 1, 0, Ty], [0, 0, 1, Tz], [0, 0, 0, 1]]
		
		temp = np.vstack((self.coil_rotated),(np.ones(100,1))
		
		self.coil_translated = dot(Tr, temp)
		
		return self.coil_translated
#class Coil end
	
# ***EST-CE QUE JAJOUTE UNE METHODE "SET" (ET PEUT-ÊTRE "GET" OU "DELETE")?***


			
		
		