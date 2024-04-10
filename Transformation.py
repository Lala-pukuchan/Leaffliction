import argparse


def options():
    parser = argparse.ArgumentParser(description="Imaging processing")
    parser.add_argument("-src", help="Source directory", required=False)
    parser.add_argument("-dst", help="Destination directory", required=False)
    parser.add_argument(
        "-gau", help="Apply Gaussian blur to pictures", action="store_true"
    )
    parser.add_argument("-msk", help="Apply mask to pictures", action="store_true")
    parser.add_argument("-roi", help="Apply ROI to pictures", action="store_true")
    parser.add_argument("-anz", help="Analyze pictures", action="store_true")
    parser.add_argument("-psd", help="Generate Pseudolandmarks", action="store_true")
    parser.add_argument("file_path", help="Path to the image file", nargs="?")
    args = parser.parse_args()
    return args


def main():
    args = options()
    if args.file_path:
        print(f"Processing file at {args.file_path}")
    else:
        print("No file path provided.")


if __name__ == "__main__":
    main()
