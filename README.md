# Ticktick

Handy little Python timer that starts playing music (at a low volume) some time before it rings, and gradually increases the volume after it rings. You can use `p` (pause) and `q` (quit) to interact with the timer.

All values are adjustable either using commandline or directly in the code (first few lines of `main`).

---

## Installation

Install pygame using `pip install pygame`, or do `pip install -r requirements.txt`

Alternatively, create a `pyvenv` using `python -m venv /pyvenv`, then `source /pyvenv/bin/activate`, and `pip install -r requirements.txt`.

## Usage

- `-f`: Required, string, file name to music
- `-t`: Required, integer, total countdown time in seconds
- `-i`: Required, integer, time in seconds (before countdown ends) when music starts playing. *i.e.* time of "prelude" in music
- `-d`: Required, float, time in seconds of volume increasing 1% after timer ends. *e.g.* a value of `0.1` would mean the volume increases by 10% each second

During timer, use `p` to pause or unpause the timer, and use `q` to quit the timer (either before or after the timer rings). The timer will automatically quit once the music playthrough completes, but you may swap in 1h versions or combine multiple music files to extend the length.

## Examples

Examples of counting down 300s with the alarm sound files in the repo:

```
python app.py -f alarm_sound_intro.mp3 -t 300 -i 38 -d 0.1 
```

```
python app.py -f alarm_sound_monody.mp3 -t 300 -i 50 -d 0.1 
```

```
python app.py -f alarm_sound_hopesanddreams.mp3 -t 300 -i 22 -d 0.1 
```

Have fun!
