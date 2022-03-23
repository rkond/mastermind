# MAstermind

A simple implementation fof Mastermind game, written as a tech evaluation assignment for a job application.

## Running
```
./mastermind.py [-h] [--letters N_LETTERS] [--length CODE_LENGTH] [--guesses MAX_GUESSES]

optional arguments:
  -h, --help            show this help message and exit
  --letters N_LETTERS   How many letters to choose from (default 6)
  --length CODE_LENGTH  Code length (default 4)
  --guesses MAX_GUESSES
                        Maximum number of guesses (default 12)

```

## Testing
```console
$ python3 -m unittest
```