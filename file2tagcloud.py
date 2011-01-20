#!/usr/bin/env python
#======================================================================#
                                                         #$  <BEGIN>  $#


"""
//  TAG CLOUD GENERATOR

(c)  2011  P. S. Clarke

See the README distributed with this script or visit
https://github.com/pscl4rke/file2tagcloud
for more information.
"""


import sys


def is_wrapped(word):
    return word.startswith('[') and word.endswith(']')


def parse_line(line):
    words = line.split()
    url = words[-1][1:-1]
    if is_wrapped(words[-2]):
        level = int(words[-2][1:-1])
        name = " ".join(words[:-2])
    else:
        level = 3
        name = " ".join(words[:-1])
    return (name, level, url)


def load_tags(filehandle):
    for line in filehandle:
        tag = parse_line(line)
        yield tag


def display_tag(tag):
    name, level, url = tag
    output = '<a class="tag-level-%i" href="%s">%s</a>' % (level, url, name)
    return output


def main():
    if len(sys.argv) == 1:
        filehandle = sys.stdin
    else:
        filehandle = open(sys.argv[1])
    tags = list(load_tags(filehandle))
    print '<div class="tag-cloud">'
    for tag in tags:
        print display_tag(tag)
    print '</div>'


if __name__ == '__main__':
    main()


#======================================================================#
                                                           #$  <END>  $#
