import nltk
import os
import sys


# Chunks a given sentence
def chunk_it(sent):
    return nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)))


# Code based on Marti's slides
# Extracts person names, which might include club names, manager names in addition to player names
def get_persons(text):
    players = []
    sent_tok = nltk.data.load('tokenizers/punkt/english.pickle')
    for sent in sent_tok.tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'node') and (chunk.node == "PERSON" or chunk.node == "ORGANIZATION"):
                player = ' '.join(c[0] for c in chunk.leaves())
                players.append(player)
    return players


# Replace names that appear in shorter forms into their longer forms.
# For example, Arsene Wenger can appear as Wenger; this function will replace Wenger with Arsene Wenger.
def normalize_names(lst):
    ret = []
    for i in lst:
        to_add = i
        for j in lst:
            if to_add in j:
                to_add = j
        ret.append(to_add)
    return ret

ALL_TEXT = ""


def process_report_dir(args, dirname, filenames):
    global ALL_TEXT

    for report_file in filenames:
        with open(dirname + "/" + report_file, 'r') as file:
            text = file.read()
            ALL_TEXT += text
            print report_file, len(text)


def main():
    if len(sys.argv) >= 2:
        report_dir = sys.argv[1]
    else:
        print "Usage: ", sys.argv[0], "<report_dir>"
        sys.exit(1)

    os.path.walk(report_dir, process_report_dir, None)

    print len(ALL_TEXT)
    nltk.FreqDist(normalize_names(get_persons(ALL_TEXT))).tabulate()



if __name__ == "__main__":
    main()
