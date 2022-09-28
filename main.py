import math, csv
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

M = 0
SW = 0
Genauigkeit = 0.05
Q_Fehler = []
DIFF = []


	

def main():
	coords = []
	data = open('data.csv', newline='')
	reader = csv.reader(data)
	for row in reader:
		row = row[0].split(';')
		if row[0] == 'x':
			continue
		coords.append((float(row[0]), float(row[1])))
	data.close()

	# plot the data
	plt.plot([x for x, y in coords], [y for x, y in coords], 'b-')
	plt.plot([x for x, y in coords], [y for x, y in coords], 'ro')
	plt.show()


if __name__ == '__main__':
	main()
