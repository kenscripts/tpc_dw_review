#! /usr/bin/env python

# This script extracts sequences from a fasta file using input identifiers.


import argparse
import sys


parser = argparse.ArgumentParser(
                                 description = "Extract specified sequences."
                                 )


parser.add_argument(
                    "-i",
                    "--fasta",
                    action = "store",
                    dest = "IN_FASTA",
                    help = "Fasta with sequences."
                    )
parser.add_argument(
                    "-d",
                    "--id",
                    action = "store",
                    dest = "ID",
                    help = "ID of sequence to extract."
                    )
parser.add_argument(
                    "-l",
                    "--id_list",
                    action = "store",
                    dest = "ID_LIST",
                    help = "IDs of sequences to extract."
                    )
parser.add_argument(
                    "-f",
                    "--id_file",
                    action = "store",
                    dest = "ID_FILE",
                    help = "File with ids of sequences to extract."
                    )
parser.add_argument(
                    "-z",
                    "--fuzzy_search",
                    action = "store_true",
                    dest = "FUZZY",
                    default = False
                    )
ARGS = parser.parse_args()


def parse_seq_ids():
   if ARGS.ID:
      return [ARGS.ID]
   elif ARGS.ID_LIST:
      return ARGS.ID_LIST.split(",")
   elif ARGS.ID_FILE:
      with open(ARGS.ID_FILE,"r") as ID_FILE:
         return ID_FILE.read().strip("\n").split("\n")
   else :
      print("ERROR: Need to specify sequences to extract.")


def parse_fasta(FASTA_FILE):
   with open(FASTA_FILE,"r") as FASTA_HANLDE:
      FASTA = FASTA_HANLDE.read().strip("\n")
      SEQ_DICT = {}
      if "\n\n>" in FASTA:
         SEQ_L = FASTA.split("\n\n") 
      else: 
         NEW_FASTA = FASTA.replace("\n>","\n\n>")
         SEQ_L = NEW_FASTA.split("\n\n") 
      for SEQ_INFO in SEQ_L:
         ID,SEQ = SEQ_INFO.split("\n",1)
         SEQ_DICT[ID.strip(">")] = SEQ.replace("\n","")

      return SEQ_DICT


def extract_seqs(SEQ_DICT,IDS):
   if ARGS.FUZZY:
      for ID in IDS:
         [
         print(
               ">%s\n%s\n" % (
                              KEY,
                              SEQ.replace("\n","")
                              )
               )
         for KEY,SEQ in SEQ_DICT.items()
         if ID in KEY
         ]
   else:
      for ID in IDS:
         try:
             print(
                   ">%s\n%s\n" % (
                                  ID,
                                  SEQ_DICT[ID].replace("\n","")
                                  )
                   )
         except:
             print("ERROR: Double check sequence id or put script in fuzzy mode")
       

IDS = parse_seq_ids()
sys.stderr.write(
                 "Number of sequences: %s\n" % len(IDS)
                 )
SEQ_DICT = parse_fasta(ARGS.IN_FASTA)
extract_seqs(SEQ_DICT,IDS)
         

"""
import sys
sys.path.append("~/Tools/biopython-1.70")
from Bio import SeqIO

Script, File, ID = sys.argv

for Seq_Record in SeqIO.parse(File,"fasta"):
   if ID in Seq_Record.id:
      SEQ_INFO = ">%s\n%s\n" %(
                               Seq_Record.id,
                               Seq_Record.seq
                               )
      print(SEQ_INFO)
   else:
      pass
"""
