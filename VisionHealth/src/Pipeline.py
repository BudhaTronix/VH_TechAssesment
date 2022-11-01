from generate_csv import generate_csv


class audio_package:
    def __init__(self):
        self.audio_path = '../audio_files/train-horn-challenge.wav'
        self.save_csv = True

    def main(self):
        generate_csv()


ob = audio_package()
ob.main()
