# bla

pdf_file_type_string = f"All Files (*);;PDF Files (*pdf)"
pdf_file_name_string = "*.pdf"

# Supported Formats
Bitmap = [".bmp", ".dib"]

EPS = [".epsf", ".epsi"]  # out: .eps,  problems: .epsi

GIF = [".gif"]

ICONS = [".ico"]  # out: .icns

JPEG = [".jpeg", ".jpg", ".jpeg", ".jpx"]  # out: .j2p

PCX = [".pcx"]

PNG = [".png"]

PPM = [".pbm", ".pgm", ".ppm", ".pnm"]

TIFF = [".tiff", ".tif"]

TGA = [".tga"]  # out: .tpic

other = [".sgi", ".webp"]  # .spi,.xbm out

supportedImageFormats = {"Bitmap": Bitmap, "EPS": EPS, "GIF": GIF, "ICONS": ICONS, "JPEG": JPEG, "PCX": PCX, "PNG": PNG,
                         "PPM": PPM, "TIFF": TIFF, "TGA": TGA, "other": other}
PDF = {"PDF": [".pdf"]}

modes = {"Merge": PDF, "Split": PDF, "Convert": supportedImageFormats}

conversion = ["1",  # (1-bit pixels, black and white, stored with one pixel per byte)

              "L",  # (8-bit pixels, black and white)

              "P",  # (8-bit pixels, mapped to any other mode using a color palette)

              "RGB",  # (3x8-bit pixels, true color)

              "RGBA",  # (4x8-bit pixels, true color with transparency mask)

              "CMYK",  # (4x8-bit pixels, color separation)

              "YCbCr",  # (3x8-bit pixels, color video format)

              # Note that this refers to the JPEG, and not the ITU-R BT.2020, standard

              # "LAB",  # (3x8-bit pixels, the L*a*b color space) RGB to Lab

              "HSV",  # (3x8-bit pixels, Hue, Saturation, Value color space)

              "I",  # (32-bit signed integer pixels)

              "F"]  # (32-bit floating point pixels)
