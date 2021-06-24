"""
CMPUT 497 - Assignment 2
Fall 2020

Fraser Redford
Scott Kavalinas
"""

from nltk.parse import ChartParser
from nltk.grammar import CFG
import nltk
import pandas as pd
import re

def main():

    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    # Read in training data to dataframe
    df_dataset = pd.read_csv("data/train.tsv", sep="\t")

    # Initialize output dataframe
    df_output = pd.DataFrame(columns=["id", "ground_truth", "prediction"])

    # From the forums on solving NLTK rules input error
    nltk.grammar._STANDARD_NONTERM_RE = re.compile(r'( [:\w$`\'.,/-][\w$`\'/^<>-]* ) \s*', re.VERBOSE)

    # Load config file to NLTK
    cfg = nltk.data.load("grammars/toy.cfg", format='cfg')

    # Initialize Chart Parser
    parser = ChartParser(cfg)

    # Iterate through each sentence in the dataset
    for index, row in df_dataset.iterrows():
        tags = row.pos.split()

        # Try parsing the tags giving the rules provided to the CFG object
        try:
            p = list(parser.parse(tags))

            # If there are valid rules to form this sentence
            if len(p) == 0:
                df_output.loc[index] = [row.id, row.label, 1]

                if row.label == 1:
                    true_positive += 1
                else:
                    false_positive += 1
            # If no valid rules exist to form this sentence
            else:
                df_output.loc[index] = [row.id, row.label, 0]

                if row.label == 0:
                    true_negative += 1
                else:
                    false_negative += 1
        # If there exists invalid inputs to the parser
        except ValueError as e:
            print(e)

    # Generate an output TSV file
    df_output.to_csv("output/output.tsv", sep="\t", index=False)

    # Calculate the precision and recall
    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)

    print("Precision: " + str(precision*100) + "%")
    print("Recall: " + str(recall*100) + "%")

main()

