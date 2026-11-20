import cv2
from sys import argv

RECTANGLES = [
	("0_quest", 86, 325, 909, 510),
	("1_top_l", 59, 1286, 454, 342),
	("2_top_r", 568, 1286, 454, 342),
	("3_mid_l", 59, 1481, 454, 342),
	("4_mid_r", 568, 1481, 454, 342),
	("5_bot_l", 59, 1675, 454, 342),
	("6_bot_r", 568, 1675, 454, 342),
]

def main():
	try:
		n = int(argv[1])
	except:
		print("Usage: python3 crop.py <n>")
		return
	img = cv2.imread("dest/out%d.png" % n)
	for name, x, y, w, h in RECTANGLES:
		crop = img[y:y+h, x:x+w]
		cv2.imwrite("cropped/img_%d_%s.jpg" % (n, name), crop)

main()