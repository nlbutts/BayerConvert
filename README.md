# BayerConvert

## Setup

You can install the the requirements directly or setup a python virtualenv.
I recommend a virtualenv:

```
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

## Run

You can get the help info:

`python BayerConvert.py -h`

To convert a Bayer raw image you need to know the width and height and the
bayer pattern.

For example:

`python BayerConvert.py -f GB --width 1572 --height 1212 -i input.raw -o output.png`