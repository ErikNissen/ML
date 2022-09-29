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
	data = open('data.csv', newline='')
	reader = csv.reader(data)
	for row in reader:
		row = row[0].split(';')
		if row[0] == 'x':
			continue
		coords.append((float(row[0]), float(row[1])))
	data.close()
	while True:
		
		ai_coords = []
		for coord in coords:
			ai_coords.append((coord[0], coord[0] * M))
			DIFF.append(coord[1] - (coord[0] * M))
			Q_Fehler.append(DIFF[-1] ** 2)
			SUM_Q_Fehler += Q_Fehler[-1]
		print('M: ', M)
		print('SW: ', SW)
		print('Q_Fehler: ', SUM_Q_Fehler)
		if SUM_Q_Fehler_alt == 0:
			pass
		else:
			if SUM_Q_Fehler_alt - SUM_Q_Fehler < 0:
				SW *= -0.5
				SUM_Q_Fehler_alt = SUM_Q_Fehler
			elif SUM_Q_Fehler_alt - SUM_Q_Fehler <= Genauigkeit:
				print(f"""
				Ergebnis:
					M: {M}
					Q_Fehler: {SUM_Q_Fehler}
				""")
				break
			else:
				SUM_Q_Fehler_alt = SUM_Q_Fehler
		M += SW
				
		
	
		# plot the data
		plt.plot([x for x, y in coords], [y for x, y in coords], 'b-')
		plt.plot([x for x, y in coords], [y for x, y in coords], 'bo')
		plt.plot([x for x, y in ai_coords], [y for x, y in ai_coords], 'g-')
		plt.plot([x for x, y in ai_coords], [y for x, y in ai_coords], 'go')
	
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
