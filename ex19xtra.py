def ocr(document_count, pages, document_type, no_of_lines, document_size):
    print "Your document file contains %d documents with %d pages." % (document_count, pages)
    print "The average number of lines per page is %d." % (no_of_lines/pages)
    print "Your document size has been calculated to be %d bytes" % document_size
    print "Your document type is %r." % document_type

ocr(300, 14356, "pdf", 200000, 100567)
