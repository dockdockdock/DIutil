import os
import re
from datetime import datetime

class seqClip:
    def __init__(self, clip_name: str, start_frame: int, end_frame: int,
                extension: str, first_frame: str, directory: str):
        self.clip_name = clip_name
        self.start_frame = start_frame
        self.end_frame = end_frame
        self.extension = extension
        self.first_frame = first_frame
        self.directory = directory
        self.creation_time = self.get_creation_time()

    def get_creation_time(self):
        first_frame_path = os.path.join(self.directory, self.first_frame) 
        creation_time = datetime.fromtimestamp(os.path.getctime(first_frame_path))
        return creation_time
    
    def duration(self):
        return self.end_frame - self.start_frame + 1
    

class seqMGR:
    def __init__(self, directory):
        self.directory = directory
        self.sequences = self.analyze_directory()

    def analyze_directory(self):
        files = os.listdir(self.directory)
        pattern = r"(.*?)(\d+)(\.\w+)$"


directory = "sequence/tst"
seq = seqClip("seq_tst", 0, 360, "jpeg", "seq_tst_0000.jpg", directory)
print(seq.duration())