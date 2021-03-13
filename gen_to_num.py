#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:45:53 2021

@author: atiyab
"""
import numpy as np
text='ttaccaactagatttttctaaacctacaatatttccatatccgcctatttttcttattaa'


'''
genomic sequence for Insulin
'''
text1='AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC'
#text1='ATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAG'
#text1='ATGGAATAAAGCCCT'
text1=text1.lower()
text1.replace(" ", "")
print(text1)
def convert_base4(text):
    base4=[]
    for i in text:
        if(i=='a'):
            base4.append(0)
        elif(i=='t'):
            base4.append(1)
        elif(i=='g'):
            base4.append(2)
        else:
            base4.append(3)
    return base4


def convert_tuples_to_decimal(text):
    if (len(text)%2) == 0:
        a=np.arange(1,len(text)+1,2)
    else:
        a=np.arange(1,len(text),2)
    
    tuples=[]
    for i in a:
        #print(i)
        tuples.append(text[i-1]+text[i])
    #print(tuples)
    
    change={
            'genome':['aa','at','ag','ac',
                      'ta','tt','tg','tc',
                      'ga','gt','gg','gc',
                      'ca','ct','cg','cc'],
            'converted':[0,1,2,3,
                         4,5,6,7,
                         8,9,10,11,
                         12,13,14,15]
            }
    base10frompair=[]
    base10text=''
    count=0
    for pair in tuples:
        i=np.where(np.array(change['genome'])==pair)
        #print(i,tuples[count])
        conv=change['converted'][i[0][0]]
        base10frompair.append(conv)
        base10text=base10text+str(conv)
        count=count+1
    return(base10frompair,base10text)

def convert_codons_to_decimal(text1):
    codons = [(text1[i:i+3]) for i in range(0, len(text1), 3)] 
    change={
            'genome':['aaa','aat','aag','aac',
                      'ata','att','atg','atc',
                      'aga','agt','agg','agc',
                      'aca','act','acg','acc',
                      'taa','tat','tag','tac',
                      'tta','ttt','ttg','ttc',
                      'tga','tgt','tgg','tgc',
                      'tca','tct','tcg','tcc',
                      'gaa','gat','gag','gac',
                      'gta','gtt','gtg','gtc',
                      'gga','ggt','ggg','ggc',
                      'gca','gct','gcg','gcc',
                      'caa','cat','cag','cac',
                      'cta','ctt','ctg','ctc',
                      'cga','cgt','cgg','cgc',
                      'cca','cct','ccg','ccc'],
            'converted':np.arange(64),
            }
    base10frompair=[]
    base10text=''
    count=0
    for pair in codons:
        i=np.where(np.array(change['genome'])==pair)
        #print(i,codons[count])
        conv=change['converted'][i[0][0]]
        base10frompair.append(conv)
        base10text=base10text+str(conv)
        count=count+1
    return(codons,base10frompair,base10text)


base10frompair,base10text=convert_tuples_to_decimal(text1)
#print(base10frompair)
print(base10text)
print(text1)

base4=convert_base4(text1)
#print(base4)


codons,base10frompair,base10text=convert_codons_to_decimal(text1)
#print(base10frompair)
print(base10text)
print(codons)