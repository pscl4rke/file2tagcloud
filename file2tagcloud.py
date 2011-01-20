#!/usr/bin/env python


"""
"""


import sys


def parse_line(line):
    name, wrapped = line.rsplit(None, 1)
    url = wrapped[1:-1]
    return (name, url)


def load_tags(filehandle):
    for line in filehandle:
        tag = parse_line(line)
        yield tag


def display_tag(tag):
    name, url = tag
    output = '<a href="%s">%s</a>' % (url, name)
    return output


def main():
    if len(sys.argv) == 1:
        filehandle = sys.stdin
    else:
        filehandle = open(sys.argv[1])
    tags = list(load_tags(filehandle))
    for tag in tags:
        print display_tag(tag)


if __name__ == '__main__':
    main()


