import tensorflow as tf
from scipy.io import wavfile
import librosa
import pandas as pd


def remove_silence(waveform, top_db=15, min_chunk_size=10000, sample_rate=16000, merge_chunks=False):
    # Loads sample into chunks of non-silence
    splits = librosa.effects.split(waveform, top_db=top_db)

    waves = []
    start_list = []
    end_list = []
    for start, end in splits:
        if (end - start) < min_chunk_size:
            continue
        waves.append([waveform[start:end]])
        start_list.append(start / sample_rate)
        end_list.append(end / sample_rate)
    if merge_chunks:
        out = None
        for c in waves:
            if out is None:
                out = c.copy()
            else:
                out.append(c)
        waves = out

    return waves, start_list, end_list


def generate_csv():
    # Task -1
    wav_file_name = '../audio_files/train-horn-challenge.wav'
    sample_rate, wav_data = wavfile.read(wav_file_name, 'rb')
    wav_data = wav_data[:, 0]

    # Show some basic information about the audio.
    duration = len(wav_data) / sample_rate
    print(f'Sample rate: {sample_rate} Hz')
    print(f'Total duration: {duration:.2f}s')
    print(f'Size of the input: {len(wav_data)}')

    waveform = wav_data / tf.int16.max

    waves, start_list, end_list = remove_silence(waveform, sample_rate=sample_rate)

    print("Number of train sounds:", len(waves))
    df = pd.DataFrame(list(zip(start_list, end_list)),
                      columns=['Start', 'End'])
    df['Duration'] = df['End'] - df['Start']
    df['Rank'] = df['Duration'].rank(ascending=False)

    df.to_csv("../output_files/output.csv")
    temp_df = df.sort_values(by=['Duration']).iloc[-1]
    print("Details of the longest duration signal")
    print(f'Start: {temp_df.Start:.2f}s')
    print(f'End: {temp_df.End:.2f}s')
    print(f'Total Duration: {temp_df.Duration:.2f}s')