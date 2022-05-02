![](https://img.shields.io/badge/Problem-Music%20Genre%20Classification-red) ![](https://img.shields.io/badge/Technique%20Used-Ensembling-yellow) ![](https://img.shields.io/badge/Validation%20Acc.-97.8%25-informational)

# Music Genre Classification by Utilizing Model Ensembling Approach

<img src="https://images.unsplash.com/photo-1623018035231-ebe361a64c76?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80 " width=100% height=500 />

## The Problem:

Audio processing is one of the most complex tasks in artificial intelligence as compared to image processing and other classification techniques. One such application is Music Genre Classification or MGR which aims to classify the audio files in certain categories of sound to which they belong ([Read More](https://en.wikipedia.org/wiki/Music_genre)). This application is very important and requires automation to reduce the manual error and time because if we have to classify the music manually then one has to listen out each file for the complete duration. So to automate the process we use Machine Learning techniques and this project is my attempt at solving this particular problem.

## Summary of my solution (The TL;DR Version):


 - I Utilized the open access dataset called GTZAN. It consists of 1000 clips of songs, 10 for each of the ten genres it contains.  
 
 - Each clip is a 30 second recording of the song, which I further cropped to 3 secs that gave me 10 parts of one clip effectively increasing the size of the dataset to 10000 clips of 3sec, 100 for each of its 10 genres

- Then I extracted various features from both time and frequency domain using librosa library ([Read Here](https://librosa.org/doc/latest/index.html)), took the mean and standard deviation of the features in a csv.

- Some of the features i utilized:

    -  20 Mel-frequency cepstral coefficients(MFCC) - [Read Here](https://medium.com/prathena/the-dummys-guide-to-mfcc-aceab2450fd)
    -  Zero Crossing Rate - [Read Here](https://www.sciencedirect.com/topics/engineering/zero-crossing-rate)
    -  Spectral Bandwidth, Spectral Centroid, and Rolloff -[Read Here](https://analyticsindiamag.com/a-tutorial-on-spectral-feature-extraction-for-audio-analytics/#:~:text=Spectral%20Bandwidth,-Bandwidth%20is%20the&text=As%20we%20know%20the%20signals,signal%20at%20that%20time%20frame.)
    -  Root Mean Squared Energy - [Read Here](https://musicinformationretrieval.com/energy.html)
    -  Chromagrams (Short Term Fourier Transformation) - [Read Here](https://towardsdatascience.com/learning-from-audio-pitch-and-chromagrams-5158028a505?gi=2428dc10ad47)

- Trained and Tuned three classification algorithm on the dataset namely:
  - XGBoost - 90% Val. Accuracy
  - CatBoost - 90% Val. Accuracy
  - Random Forest Classifier - 85% Val. Accuracy

- Created an Ensembled model using all three of the trained model using a custom bagging approach with user defined weights
  - Ensembled Model (XGB, CatBoost, Random Forest) - 97.8% Valdiation Accuracy

## The Solution (Long Version)

## 1. The Data:

The Data used in this project can be accessed via kaggle [here](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification/discussion/226726?sort=published)

It consist of 1000 audio clips that are 30 seconds in duration. The data is subdivided into 10 classes or genres with a balanced distribution of samples, 100 clips for each genre.  
The Genres included in the Dataset are:

<table>
  <tr>
    <td> Blues </td>
    <td> Country </td>
    <td> Classic</td>
    <td> Metal </td>
    <td> Jazz </td>
  </tr>
  <tr>
    <td> Pop </td>
    <td> HipHop </td>
    <td> Rock </td>
    <td> Reggae </td>
    <td> Disco </td>
  </tr>
</table>

As per the documentation, each clip is taken from a different song and a 30 second window was sampled from anywhere in the song randomly.

**Additional Information:**  If like me, you are taking the data from kaggle, the jazz.00054.wav file is broken and the replacement for the same can be downloaded from the disscussion section of the dataset on kaggle itself ([Here](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification/discussion/158649?sort=published))

## 2. Preprocessing:

Two Inital checks were done on the data before any feature were extracted.

### 1. Initial Librosa compatibility check  

Since, all features will be extracted using the librosa library, it was required that every file in dataset should be compatible with librosa. For this test all the files were dump loaded and only one file named jazz.00054.wav was found incamptible or broken, the replacement for which was found and therefore 100% of the dataset became librosa compatible

### 2. Distorsion Check

Potential Distorsion in audio files can adversly affect the learning phase, Therefore using Spectral Flatness as a measure of Flatness every file was checked.

Top 30 most distorted song were plotted in a histogram coloured by their repective genres to pin-point the genre that should be focuesd:

<img src="https://github.com/ITrustNumbers/Music_Genre_Classification_By_Model_Ensembling_Approach/blob/master/Visualization/Distorsion.png" />
