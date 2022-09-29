import math, csv, matplotlib, random
import time

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

M = 0
SW = 0
Genauigkeit = 0.05
Q_Fehler = []
SUM_Q_Fehler = 0
SUM_Q_Fehler_alt = 0
DIFF = []


def init():
	global M, SW
	M = random.uniform(-3, 3)
	SW = 5


def main():
	global SUM_Q_Fehler, SUM_Q_Fehler_alt, DIFF, M, SW
	init()
	coords = []
	ai_coords = []
	counter = 0
	data = open('data.csv', newline='')
	reader = csv.reader(data)
	for row in reader:
		row = row[0].split(';')
		if row[0] == 'x':
			continue
		coords.append((float(row[0]), float(row[1])))
	data.close()
	while True:
		for x, y in coords:
			ai_coord = (x, x * M)
			ai_coords.append(ai_coord)
			fehler = (x * M) - y
			Q_Fehler.append(fehler**2)
		SUM_Q_Fehler = sum(Q_Fehler)
		Q_Fehler.clear()
		if counter == 0:
			print('M: ', M, 'SW: ', SW, 'SUM_Q_Fehler: ', SUM_Q_Fehler)
			counter += 1
		else:
			diff = SUM_Q_Fehler_alt - SUM_Q_Fehler
			if diff < 0:
				SW *= -0.5
			elif diff <= Genauigkeit:
				print("Fertig\n")
				print('M: ', M, 'SW: ', SW, 'SUM_Q_Fehler: ', SUM_Q_Fehler)
				break
			print('M: ', M, 'SW: ', SW, 'SUM_Q_Fehler: ', SUM_Q_Fehler, 'DIFF: ', diff)
		SUM_Q_Fehler_alt = SUM_Q_Fehler
		M += SW
				
		
	
		# plot the data
		plt.plot([x for x, y in coords], [y for x, y in coords], 'b-')
		plt.plot([x for x, y in coords], [y for x, y in coords], 'bo')
		plt.plot([x for x, y in ai_coords], [y for x, y in ai_coords], 'g-')
		plt.plot([x for x, y in ai_coords], [y for x, y in ai_coords], 'go')
		
		ai_coords.clear()
	
		# create legend
		blue_line = matplotlib.lines.Line2D([0], [0], color='blue', marker='o', linestyle='')
		green_line = matplotlib.lines.Line2D([0], [0], color='green', marker='o', linestyle='')
		plt.legend((blue_line, green_line), ('Data', 'AI'), loc='upper left')
	
		# show plot for 1 second
		plt.show(block=False)
		plt.pause(1)
		plt.clf()


if __name__ == '__main__':
	main()
