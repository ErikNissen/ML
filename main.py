import math, csv, matplotlib, random

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

M = 0
SW = 0
Genauigkeit = 0.05
Q_Fehler = 0
DIFF = 0


def init():
	global M, SW
	M = random.random()
	SW = 1


def main():
	init()
	coords = []
	ai_coords = []
	data = open('data.csv', newline='')
	reader = csv.reader(data)
	for row in reader:
		row = row[0].split(';')
		if row[0] == 'x':
			continue
		coords.append((float(row[0]), float(row[1])))
	data.close()
	for coord in coords:
		ai_coords.append((coord[0], coord[0] * M))

	# plot the data
	plt.plot([x for x, y in coords], [y for x, y in coords], 'b-')
	plt.plot([x for x, y in coords], [y for x, y in coords], 'bo')
	plt.plot([x for x, y in ai_coords], [y for x, y in ai_coords], 'g-')
	plt.plot([x for x, y in ai_coords], [y for x, y in ai_coords], 'go')

	# create legend
	blue_line = matplotlib.lines.Line2D([0], [0], color='blue', marker='o', linestyle='')
	green_line = matplotlib.lines.Line2D([0], [0], color='green', marker='o', linestyle='')
	plt.legend((blue_line, green_line), ('Data', 'AI'), loc='upper left')

	plt.show()


if __name__ == '__main__':
	main()
