import re


QUOT_PATTERN = re.compile("^>+ ?")
NO_QUOT_LINE = re.compile("^[^>].*[\S].*")


QUOTATION = re.compile(
    r"""
    (
        # quotation border: splitter line or a number of quotation marker lines
        (?:
            s
            |
            (?:me*){1,}
        )

        # quotation lines could be marked as splitter or text, etc.
        .*

        # but we expect it to end with a quotation marker line
        me*
    )

    # after quotations should be text only or nothing at all
    [te]*$
    """,
    re.VERBOSE,
)

EMPTY_QUOTATION = re.compile(
    r"""
    (
        # quotation border: splitter line or a number of quotation marker lines
        (?:
            (?:se*)+
            |
            (?:me*){1,}
        )
    )
    e*
    """,
    re.VERBOSE,
)
