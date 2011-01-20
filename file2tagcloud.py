#!/usr/bin/env python


"""
"""

FILE = "example.tag"


def parse_line(line):
    name, wrapped = line.rsplit(None, 1)
    url = wrapped[1:-1]
    return (name, url)


def load_tags(filename):
    f = open(filename)
    for line in f:
        tag = parse_line(line)
        yield tag


def display_tag(tag):
    name, url = tag
    output = '<a href="%s">%s</a>' % (url, name)
    return output


def main():
    filename = FILE
    tags = list(load_tags(filename))
    for tag in tags:
        print display_tag(tag)


if __name__ == '__main__':
    main()


