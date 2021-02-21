# TEST

python3 example.py

# Usage

## plain text
```
from main import detect_from_text

DATA = """
okok
On 2/18/21 8:46 AM, Tungnt wrote:
> ok thaasy r nhe
> 
> On 2/18/21 8:46 AM, Tungnt24 wrote:
>> đây là test plain text
"""

result = detect_from_text(DATA)

#result == ['> ok thaasy r nhe', '> ', '> On 2/18/21 8:46 AM, Tungnt24 wrote:', '>> đây là test plain text']
```

## html
```
from main import detect_from_html

DATA = """
<p>second message</p>\n<p>&nbsp;</p>\n<p>V&agrave;o 15:03, 28/01/2021,<strong>B</strong> &lt;<a href=\"mailto:nameB@gmail.com\" target=\"_blank\"rel=\"noopener\">nameB@gmail.com</a>&gt; đ&atilde; viết:</p>\n<blockquote>\n<div     
dir=\"ltr\">first message</div></blockquote>
"""

result = detect_from_html(DATA)

#result == ['> first message']
```
