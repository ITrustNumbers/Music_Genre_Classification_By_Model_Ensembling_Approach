import librosa
from pydub import AudioSegment
import os

def Splitter(path_to_orgnl, path_to_new):

  #Create New directory
  os.mkdir(path_to_new)
  processed_count = 0
  count = 0
  
  #Looping through the orignal dataset
  for dirname, dirs, files in os.walk(path_to_orgnl):

    if len(files) == 0:
      continue

    #Creating genre folder for processed dataset
    dir_to_cr = dirname.split('\\')[-1]
    dir_genre = os.path.join(path_to_new, dir_to_cr)
    os.mkdir(dir_genre) #Directory for each genre
    
    #Looping through audio file
    for fl in files:

      #Skip unwanted tracks
      if fl in audio_fl_to_skip:
        continue

      audio_path = os.path.join(dirname, fl) #Path to each audio file
      try:
        audio_pd = AudioSegment.from_wav(audio_path)
      except:
        error_audio_fl.append(fl)
        continue
      
      #Splitting into n sec clips
      count += 1
      n = 3
      dur_secs = audio_pd.duration_seconds
      n_splits = int(dur_secs//n)
      start = 0
      for i in range(n_splits):
        end = start + (n * 1000)
        split_fn = fl[0:-3] + str(i) + '.wav'
        split_audio = audio_pd[start:end]
        split_audio.export(os.path.join(dir_genre,split_fn), format='wav') #Exporting
        start = end
        processed_count +=1

  print('Found a total of {} audio files without error'.format(count))
  print('Splited Dataset contains {} audio files of {} second each'.format(processed_count,n))
  print('Found error in {} file(s)'.format(len(error_audio_fl)))
  print('File(s) with error:')
  for i,fl in enumerate(error_audio_fl):
    print('{}. {}'.format(i+1,fl))

if __name__ == '__main__':

  audio_fl_to_skip = ['reggae.00086.wav'] #Potentially distorted audio
  error_audio_fl = [] #Error catcher

  #Path to Dataset
  path_to_orgnl = 'GTZAN_Dataset

  #New directory
  path_to_new = 'Dataset_Splitted'

  #Run the Splitter
  Splitter(path_to_orgnl, path_to_new)

  exit_pause = input('\n')