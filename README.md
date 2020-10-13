# Google-ASR Metric
## Packages
- google.cloud
- librosa
- editdistance
- inflect
- pinyin
- cn2an
- zhon

## Propare
- Get client keys. [example](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
- Put wav file and groundtruth in same directory.
- The name of wav file and groundtruth must be same. e.g. test.wav & test.txt

## Details
- Compute with lower characters and no punctuations.
- Convert digit numbers to language numbers

## Compute WER and CER
<pre><code>python evalute.py -r {directory of data} -s {sample rate} -l {language} -n {number of thread}
</code></pre>
