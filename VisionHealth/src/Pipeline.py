from generate_csv import generate_csv
from utils import convertToWAV

class audio_package:
    def __init__(self):
        self.mp4_audio_path = '../audio_files/train-horn-challenge.mp4'
        self.wav_audio_path = '../audio_files/train-horn-challenge.wav'
        self.wav_path = '../audio_files/'
        self.output_csv_path = "../output_files/output.csv"
        self.save_csv = True
        self.top_db = 15
        self.min_chunk_size = 10000

    def main(self):
        # Task 3
        # convertToWAV(self.mp4_audio_path, self.wav_path)
        generate_csv(self.wav_audio_path, self.output_csv_path, self.save_csv, self.top_db, self.min_chunk_size)


ob = audio_package()
ob.main()
