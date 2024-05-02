from IPython.display import HTML, Audio, clear_output, Image
from google.colab.output import eval_js
from base64 import b64decode, b64encode
import numpy as np
from scipy.io.wavfile import read as wav_read
import io
import ffmpeg
from google.colab import files
import os
import cv2

import shutil
from google.colab import drive

import moviepy.editor as mp

from IPython.core.display import display

from ghc.l_ghc_cf import l_ghc_cf

# Copyright

copyright = '<div style="background-color: #dff2bf; border: 1px solid rgb(79, 138, 16); color: #4f8a10; padding: 10px;"><div class="separator" style="clear: both; direction: rtl; text-align: left;">&nbsp; &nbsp; Coach Rajat Sharma</div><div style="direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;">✅ JAI HIND JAI BHARAT ✅</span></div></div>'
display(HTML(copyright))