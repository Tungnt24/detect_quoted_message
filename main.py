import html2text
import filter


def mark_message_lines(lines):
    """Mark message lines with markers to distinguish quotation lines.

    Markers:

    * e - empty line
    * m - line that starts with quotation marker '>'
    """
    markers = ["e" for _ in lines]
    for i in range(len(lines)):
        if not lines[i].strip():
            markers[i] = "e"  # empty line
        elif filter.QUOT_PATTERN.match(lines[i]):
            markers[i] = "m"  # line with quotation marker
    return "".join(markers)


def process_marked_lines(lines, markers):
    markers = "".join(markers)
    quotation = filter.QUOTATION.search(
        markers
    ) or filter.EMPTY_QUOTATION.search(markers)

    if quotation:
        return lines[quotation.start(1) : quotation.end(1) + 1]
    return lines


def detect_from_text(text):
    lines = text.strip().splitlines()
    markers = mark_message_lines(lines)
    lines = process_marked_lines(lines, markers)
    return lines


def detect_from_html(html):
    text = html2text.html2text(html).strip()
    return detect_from_text(text)
