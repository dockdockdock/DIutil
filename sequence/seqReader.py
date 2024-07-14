import os
import re
from datetime import datetime

class Sequence:
    def __init__(self, directory):
        self.directory = directory
        self.files = os.listdir(directory)


directory = "sequence/tst"
seq = Sequence(directory)
print("file_list:", seq.files)