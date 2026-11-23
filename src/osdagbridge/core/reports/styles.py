
"""Centralized LaTeX report formatting settings for OsdagBridge."""

# Table formatting
TABLE_COLUMN_PADDING = "6pt"
TABLE_ROW_STRETCH = "1.12"
TABLE_RULE_WIDTH = "0.5pt"
TABLE_EXTRA_ROW_HEIGHT = "0.6pt"

# Longtable spacing
LONGTABLE_PRE_SKIP = "0pt"
LONGTABLE_POST_SKIP = "6pt"

# Page layout
TABLE_MINIMUM_PAGE_SPACE = r"5\baselineskip"

# Report theme
REPORT_GREEN = "91B014"

# Header and footer
HEADER_RULE_WIDTH = "1pt"
FOOTER_TEXT = r"Osdag $|$ FOSSEE $|$ Indian Institute of Technology Bombay"

# Common LaTeX packages
REPORT_PACKAGES = [
    "graphicx",
    "amsmath",
    "amssymb",
    "booktabs",
    "array",
    "tabularx",
    "float",
    "fancyhdr",
    "xcolor",
    "setspace",
    "enumitem",
    "caption",
    "subcaption",
    "multirow",
    "colortbl",
    "longtable",
    "titlesec",
    "titletoc",
    "lastpage",
    "makecell",
    "etoolbox",
    "needspace",
]