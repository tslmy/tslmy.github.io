"""
Take a screenshot for the given URL, saving as the given output file.

Usage:
  screenshot.py [--size=<s>] [URL] [FILENAME]
  screenshot.py -h | --help

Options:
  -h --help     Show this screen.
  --size=<s>    Size of image [default: 800].

Arguments:
  URL        URL to take a screenshot for [default: https://myli.page].
  FILENAME  Output filename [default: screenshot.png].
"""

import io

from docopt import docopt
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    # Read options.
    args = docopt(__doc__)
    if args["URL"] is None:
        args["URL"] = "https://myli.page"
    if args["FILENAME"] is None:
        args["FILENAME"] = "screenshot.png"
    args["SIZE"] = int(args["--size"])
    # Take screenshot.
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(args["URL"])
    driver.set_window_size(args["SIZE"] * 2, args["SIZE"] * 2)
    image = driver.get_screenshot_as_png()
    driver.quit()
    # Resize the screenshot.
    image = Image.open(io.BytesIO(image))
    image.thumbnail((args["SIZE"], args["SIZE"]))
    image.save(args["FILENAME"])
