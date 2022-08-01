# -*- coding: utf-8 -*-
"""
    pygments.styles.custom
    ~~~~~~~~~~~~~~~~~~~~~
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Generic, Whitespace, Punctuation


class CustomStyle(Style):
    """
    my custom pygments style -- ukim - 01 aug 2022.
    """

    background_color = "#000000"
    highlight_color = "#444444"

    default_style = "#ff0000"

    styles = {
        Whitespace:                "#bbbbbb",
        Comment:                   "italic #ff7000",  # orange.

        Comment.Preproc:           "noitalic",
        Comment.Special:           "noitalic bold",

        Keyword:                   "bold #00ff00",  # ex. filler, pic
        Keyword.Pseudo:            "nobold",
        Operator:                  "bold #ff0000",  # no-op?
        Operator.Word:             "bold #ff0000",  # no-op?

        Punctuation:                  "#ff0000",

        Name.Variable:             "#00ffff",  # paragraph/procedure names, etc.

        String:                    "italic #faff00",  # yellow
        String.Doc:                "bold italic",
        Number:                    "#005dff",  # light blue

        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FFff00"
    }
