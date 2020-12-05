import os
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("--input","-i", type=str, default="data/custom/images", help="path to image dir")
parser.add_argument("--output","-o", type=str, default="data/custom/", help="path to output")
opt = parser.parse_args()

train = open(os.path.join(opt.output,'train.txt'),'w')
valid = open(os.path.join(opt.output,'valid.txt'),'w')


filenames = os.listdir(opt.input)
num = len(filenames)
random.shuffle(filenames)

for filename in filenames[:int(num * 0.8)+1]:
    train.write(os.path.join(opt.input,filename)+'\n')

for filename in filenames[int(num * 0.8):]:
    valid.write(os.path.join(opt.input,filename)+'\n')

train.close()
valid.close()

