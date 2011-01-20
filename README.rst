

``file2tagcloud``
=================

Generate the HTML for a tag cloud from a file of tag data.


Usage
-----

Prepare a tag file consisting of lines that match one of the two
following forms::

    Name of tag [http://url.to.tag]
    A different tag [weight] [http://the.tags.url]

The tag's name can be anything you like and appears as the
link text in the cloud.  The url is the address that the link
will point to.

The optional weight tells the program how significant the tag
is (where significance is usually indicated with size).
1 is the least significant; 5 the most.  If omitted the weight
defaults to 3.

The file ``example.tag`` contains an example of a tag file.
A basic stylesheet for the tag cloud can be found in
``tagcloud.css``.

The script is run by passing the path to the tag file as the
first argument.  If omitted, stdin is used instead.


Roadmap
-------

Things still left to do:

  - Support blank lines and comments.

  - Lots of error trapping to cope with poor user input.


  - Add ``--help`` options.

  - Add ``--a2z`` and ``--z2a`` options to sort alphabetically.
    Otherwise leave in file order.  Consider adding options for
    sorting by weight as well.

  - Support for a base url, which is prepended to all the tag
    URLs.  Then the full address will not need to be typed out
    each time when the file is maintained by hand.

  - Write a script that can undo the process, to create a tag
    file.  Maybe.


