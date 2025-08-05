from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.drop_privileges = False # Prevent matrix from switching to less privileged user

matrix = RGBMatrix(options = options)
