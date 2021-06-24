# Grammar Checker

This is a simple implementation of a grammar checker that uses context-free grammars rules to check if a sentence is grammatically correct. By parsing a sentence the checker looks for basic structures that are provided and evaluates if the sentence is valid or not.

## Data

The assignment's train data can be found in [data/train.tsv](data/train.tsv).

## 1. Members

- Scott Kavalinas
- Fraser Redford

## 2. Listed Resources

- Chapter 12 https://web.stanford.edu/~jurafsky/slp3/12.pdf
- Chapter 13 https://web.stanford.edu/~jurafsky/slp3/13.pdf
- Exporting to TSV https://datatofish.com/export-dataframe-to-csv/

## 3. Installation

### Requirements

- Python3
- Pandas
- NLTK

The program can be run directly from the project directory if the user has Pandas and NLTK installed using:

```
$ python3 code/main.py
```

If the user does not have `pandas` or `nltk`, then they can run the program by first installing:

```
$ pip install pandas
$ pip install nltk
```

The program will effectively operate within the confines of the `main.py` and the provided inputs. A TSV file `output.tsv` will be generated when `main.py` is run inside of the `output` folder.
