"""
Skelletex, simple latex skelleton script.
"""
import sys, os

class Document(object):
    """A document."""

    def __init__(self, abs_path, layout):
        """Init"""
        self.abs_path = abs_path
        self.layout = layout
        self.layout_body = {}
        # Basic layout.
        self.layout_body['basic'] = '' + \
                '\\documentclass[a4paper, 11pt]{article}\n' + \
                '\\usepackage[utf8]{inputenc}\n' + \
                '\\usepackage{fancyhdr}\n' + \
                '\\usepackage[centering, margin={2.54cm, 2.54cm},' + \
                'includeheadfoot]{geometry}\n' + \
                '\\pagestyle{fancy}\n' + \
                '\\fancyhead[L]{Name...}\n' + \
                '\\linespread{1}\n' + \
                '\\textwidth=15cm\n' + \
                '\\begin{document}\n' + \
                '\\section*{Section}\n' + \
                'Content...\n' + \
                '\\end{document}\n'

    def write_document(self):
        """Write document"""
        # Open file.
        f = open(self.abs_path, 'w')
        print "Writing to %r with %r layout..." % (self.abs_path, self.layout)
        # Write and close.
        f.write(self.layout_body[self.layout])
        f.close()
        print "Done!"

if __name__ == '__main__':
    # Allowed layouts.
    ALLOWED_LAYOUTS = ['basic']
    # Arguments?
    if len(sys.argv) > 2 and sys.argv[2] in ALLOWED_LAYOUTS:
        FILENAME = sys.argv[1]
        if FILENAME[-4:] != '.tex':
            FILENAME += '.tex'
        ABS_PATH = os.getcwd() + '/' + FILENAME
        # Layout.
        LAYOUT = sys.argv[2]
        # Create doc object.
        DOC = Document(ABS_PATH, LAYOUT)
        # Write document.
        DOC.write_document()
    else:
        # Print usage.
        print 'Usage: skelletex.py FILENAME LAYOUT\n' + \
        'Allowed layouts: %r' % ALLOWED_LAYOUTS
