import argparse
import cv2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Stitch given images.')
    parser.add_argument("inputs", metavar='input', type=str, nargs='+', help='input file')
    parser.add_argument("--output", type=str, default='a.jpg', help='output file (default=a.jpg)')
    args = parser.parse_args()

    input_images = []
    for i in args.inputs:
        image = cv2.imread(i)
        if image is None:
            print(f'Error: Unable to open file "{i}".')
            exit()
        input_images.append(image)

    if len(input_images) == 1:
        cv2.imwrite(args.output, input_images[0])
    else:
        stitcher = cv2.Stitcher.create(cv2.STITCHER_SCANS)
        result = stitcher.stitch(input_images)
        print('STATUS CODE: ' + str(result[0]))
        if result[0] == cv2.STITCHER_OK:
            cv2.imwrite(args.output, result[1])