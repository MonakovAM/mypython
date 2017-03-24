#!/usr/bin/env python3

"""
Created on Thu Mar 23 21:44:22 2017

@author: Student
"""

import argparse
import json

def Generate(inputTemplate, content, outputHtml):
    with open(inputTemplate) as finpt:
        template = finpt.read()
        renderedHtml = template.format(**content)

    with open(outputHtml, 'w') as fout:
        fout.write(renderedHtml)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Meme generator',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-i', '--input', default='source-1.txt', help='Input template')
    parser.add_argument('-c', '--content', default='source-1.json', help='Content for template')
    parser.add_argument('-o', '--output', default='htmlGen-1.html', help='Output template')

    args = parser.parse_args()

    with open(args.content) as fin:
        content = json.load(fin)

    Generate(args.input, content, args.output)

