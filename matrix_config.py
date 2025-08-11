from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.drop_privileges = False # Prevent matrix from switching to less privileged user
options.brightness = 35
options.disable_hardware_pulsing = True
options.gpio_slowdown = 1 # Helps a bit with flickering
options.pwm_bits = 11
options.pwm_lsb_nanoseconds = 130

matrix = RGBMatrix(options = options)
