# Google-ASR Metric
Use Google-ASR system as a metric to evalute the quality of wav files.
Google-ASR system is not free, the fee of Google-ASR system is [here](https://cloud.google.com/speech-to-text/pricing).

## Packages
- google.cloud
- librosa
- editdistance
- inflect
- pinyin
- cn2an
- zhon

## Client keys
- Get client keys. [example](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
- export GOOGLE_APPLICATION_CREDENTIALS={path of json file}.

## Directory Format
- Put wav file and groundtruth in same directory.
- The name of wav file and groundtruth must be same. e.g. test.wav & test.txt

## Details
- Compute with lower characters and no punctuations.
- Convert digit numbers to language numbers.

## Compute WER and CER
<pre><code>python evalute.py -r {directory of data} -s {sample rate} -l {language} -n {number of thread}
</code></pre>
