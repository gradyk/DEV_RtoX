# RtoX File Conversion Package

The primary purpose of this software is to convert an RTF file into a basic XML
 tagged file. By converting an RTF file rather than a TXT file, the user
  retains certain features (e.g., italics, bold) that may be useful have
   available when analyzing the XML file.
   
This README paper gives a brief overview of the RtoX package. For more
 information, including details of how the package performs the conversion
 , please go to _________________.

## Motivation
For the most part, legal documents used in tribunal proceedings or produced
 by a tribunal are accessible to the public only in pdf format. This makes
  sense. Parties submitting briefs to the tribunal do not want those
   documents accidentally or intentionally altered. The tribunal needs to
    insure integrity in what it produces, and an "unalterable" pdf document
     suffices. (PDF documents can be altered, but the security level of the
      pdf format is sufficient for the tribunal and participants.) This means
       the researcher must convert pdf documents into other formats if they
        want to perform computer manipulation of the text.
        
The question of which format to use raises several questions. How does the
 researcher want to manipulate the text? What features are important to
  retain from the pdf to the new format? What software options are available
   to the researcher? Cost? Time? Difficulty?
   
For various reasons explained elsewhere, the TPRES system uses the XML
 language to tag documents. Thus, an XML document is the destination for
  converted pdf documents. We are fortunate at this time to have available
   software that will convert from almost any format to almost any other
    format. So, conversion from pdf directly to XML is possible. The
     researcher, however, is left with an XML coded document which uses tags
      that probably do not fit their needs. The tagging system may be verbose
      . The tags will not be part of a well-defined system. In most cases
      , the tags will not provide the detail the researcher requires. 
      
Another approach is to convert from the pdf to an XML document using a
 stepped approach. The pdf document is converted to one or more intermediate
  formats and from there to the desired XML document. The last step of the
   conversion--from an intermediate format to the desired XML document
   --presents the greatest challenge. Technically it can be done, but the
    researcher still is left with a document bearing unwanted XML tags.
    
Those challenges demonstrated a need for the RtoX software. Converting from a
 pdf to an rtf document is easy. The rtf document retains the features a
  researcher might want in the final XML document. And, if the final step in
   the conversion--from rtf to XML--is configurable, the researcher is left
    with an XML document using the XML tags they prefer. 
    
There was an existing software package that offered the possibility of being
 the last step conversion software: rtf2xml by Paul H. Tremblay
 . Unfortunately, that package was written in 2004 using Python 2.x. Python 2
 .x has reached its end of life. The package could be ported to Python 3.x
 , but that still left several issues with the software. The better path was
  to build a software package from scratch in Python 3.x (Python 3.6, to be
   exact) which would fit the need more precisely. RtoX is that package.

## Workflow Design
The user runs a pdf format file through OCR software, saving the
         output as an RTF file. Some OCR software will permit you to do this
          directly, while other software requires an intermediate step (e.g
          ., OCR --> Word --> RTF). The RtoX package converts the rtf
           formatted document to an XML document. The user chooses whether
            the final document will use plain XML, tags from the Text
             Encoding Initiative, of tags from the TPRES system. See
              [REFERENCE TO SPHINX PAGE]

The RtoX software is designed to convert legal
 documents used in or resulting from tribunal proceedings. This focus made
  it easier to code the RtoX software. But this design constraint limits the
   software's usefulness outside the legal setting. For example, RtoX will
    not convert Wingdings or other unusual characters, as those seldom (if
     ever) appear in legal documents.
          
## What the software does.
An RTF document is a confusing mixture of destination codes, keyword codes
, other codes, and plain text. Those codes, when read by an RTF reader, tell
 the software how to format the RTF document so that it matches the PDF
  document (more or less) form which it was generated. The RtoX
   software picks out those codes that provide information which may be
    useful in content analysis, and converts them to XML tags. The resulting
     XML document does not have sufficient information to format it to look
      like the PDF document. But it does have relevant information.
      
For example, a researcher may want to know what text was emphasized in the
 original document and how it was emphasized. Was it in italics? Bold
 ? Underlined? The RTF document and the XML document retain that information
 . The researcher, however, probably is not interested in the text margins of
  the original document and that information (though in the RTF file) is not
   captured in the XML document.

## What the software does not do.

Because the intended end result is an XML file, the software (Version 0.1
.0a) omits certain
 information coded into the RTF file. Future versions may pick up some or all
  of this coding. For example, legal documents seldom use a text color
   other than black. While text color information is coded into the RTF file
   , that information is not captured in the XML file. The
    following sections give a bit more information about the coding which is
     not passed from the RTF file to the XML file.
  
### Color Table

An RTF file includes a color table (\colortbl) in the header
. Documents used in and produced by tribunals seldom use colors other
 than black and white. Therefore, the RtoX software
  omits information from the RTF color table.
  
### Stylesheets

RTF stylesheet information provides detailed instructions to RTF readers on
 how to format text throughout the document. Given the many possible
  combinations of font, margins, highlighting, etc., an RTF document can
   contain several dozen lines of stylesheet codes.
   
An XML document used for content analysis does not benefit from
 most of the information contained in the RTF stylesheets. Margins (with a
  few exceptions), changes in font size, and other formatting details may be
   omitted from an RTF to XML conversion without losing significant data. As
    a result, RtoX focuses on the formatting information relevant
     to content analysis. This information includes: bold, italic, underline
     , small caps, footnotes, headers, titles, and similar
      information.
     
### Style and Formatting Restrictions


### Revision Information

RTF files generated from PDF files run through OCR software will not include
 revision information. But, a document that is converted directly from Word
  to RTF may contain that information. If so, the RTF captures it in a
   specific table.
   
The RtoX software can convert both the PDF to RTF and Word to RTF files to
 XML. However, the primary purpose of the software is to handle the
  PDF to RTF situation in which case no revision information is available
  . Even when it is available (e.g., Word to RTF) its value is questionable
  . Therefore, RtoX does not attempt to capture and XML tag revision
   information. 

### File Security Information

File security information is similar to revision information. It will not be
 present in PDF to RTF conversions. It may be present in Word to RTF
  conversions. But, it has questionable value. RtoX does not attempt to
   capture and XML tag file security information.

## PDF to OCR Limitations

Software that converts PDF documents through optical character recognition
 (OCR) to other formats has certain limitations that affect the RTF to XML
  conversion process. In a nutshell, OCR software takes a page of a PDF
   document and breaks the page into blocks that seem to share
    characteristics. For example, a page of text with a header and a footer
     could become three blocks: 1) the header, 2) the body of the page, and 3
     ) the footer. The software then attempts to match the formatting of each
      block and to perform character recognition on the text in the block.
      
Many factors affect the accuracy of the software. They include the clarity of
 the PDF document, the complexity of the formatting, and complexity of the
  document. The OCR software is not "reading" the document, so it does not
   understand logical connections among blocks. 
   
One aspect of legal documents that the OCR process does not handel well is
 footnotes. A human reading a legal document with footnotes understands that
  the smaller print at the bootom of the page, preceded by a superscript
   number or symbol, is a footnote. That human also recognizes when a
    footnote from one page runs over onto the next page. 
    
OCR software does not understand "footnote". To the software, it is a block
 of text formatted in a different style from the preceding block of text. It
  does not understand that a footnote split between two pages is part of one
   block of text. 
   
When you look at the result of an OCR conversion, the page looks fine. Each
 block of text resembles the original PDF. But when that document is opened
  in a text editing software package (such as Word) or converted to a format
   such as RTF, the blocks are not connected. In text processing language
   , the text from one block does not flow into another block. 
   
In practical terms, this means that a footnote split between two pages
 becomes two isolated blocks of text in an RTF document. Each block is placed
  following a text block (or another footnote block, if there was more than
   one footnote on the page). But the partial footnote from one page is not
    connected in any way to the remainder of the footnote on the next page
    . To rebuild the footnote, a person must manually move the text.
    
 The same type of challenge exists with headers and footers. To the OCR, they
  were blocks formatted in different styles than other blocks on the page
  . But the OCR software does not understand a "header" or a "footer". A human
   must place the appropriate text and XML tags in tags indicating a header or
    footer.
    
 If there are other unusual blocks of text, the OCR software will have
  similar problems. 

## RtoX User Preferences

The RtoX package gives the user some configuration options. 

The software gives you three options for XML tags: 1) plain XML
  tags, 2) tags from the Text Encoding Initiative (TEI), and 3) tags from the
   Tribunal Proceedings and Resolutions Encoding System (TPRES). 

## Plans for the RtoX Software Package

The RtoX software package is one part of a larger suite of tools under the
 name Oliver™. Oliver recognizes that content creation, data, and content
  analysis should not be three separate things in the law. Oliver's
   components connect the three areas so that the author can, in real time
   , connect their work to the body of law.
   