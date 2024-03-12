import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser(
                    prog='BayerConverter',
                    description='Converts a bayer image into a 16-bit PNG')

parser.add_argument('-i', '--input', type=str, required=True, help='Input bayer image to convert')
parser.add_argument('-o', '--output', type=str, required=True, help='Output png file name')
parser.add_argument('--width', type=int, required=True, help='Width of the image')
parser.add_argument('--height', type=int, required=True, help='Height of the image')
parser.add_argument('-f', '--format', type=str, required=True, help='Bayer format BG, BR, RG, BG')

args = parser.parse_args()

buf = np.fromfile(args.input, 'uint16')
img = np.reshape(buf, (args.width, args.height)).T

if args.format == 'BG':
    format = cv.COLOR_BAYER_BG2BGR
elif args.format == 'RG':
    format = cv.COLOR_BAYER_RG2BGR
elif args.format == 'GB':
    format = cv.COLOR_BAYER_GB2BGR
elif args.format == 'GR':
    format = cv.COLOR_BAYER_GR2BGR
else:
    print("Error: invalid bayer format")
    exit(-1)

bgr = cv.cvtColor(img, format)
bgr8 = bgr.astype('float32') / (np.max(bgr) / 255)
bgr8 = bgr8.astype('uint8')
cv.imwrite(args.output, bgr8)