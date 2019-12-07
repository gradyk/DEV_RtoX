# RtoX File Conversion Package

The primary purpose of this software is to convert an RTF file into a basic XML
 tagged file. The software gives you three options for XML tags: 1) plain XML
  tags, 2) tags from the Text Encoding Initiative (TEI), and 3) tags from the
   Tribunal Proceedings and Resolutions Encoding System (TPRES). By
    converting an RTF file rather than a TXT file, the user retains certain
     features (e.g., italics, bold) that may be useful to tag and have
      available when analyzing the XML file, but which are lost in plain text
       files.

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
             Encoding Initiative, of tags from the TPRES system.

The RtoX software is intended for the conversion of legal
 documents used in or resulting from tribunal proceedings. This focus made
  it easier to code the RtoX software. But this design criteria limits the
   software's usefulness outside the legal setting.
          
## What the software does.
An rtf document is a confusing mixture of destination codes, keyword codes
, other codes, and plain text. Those codes, when read by an rtf reader, tell
 the software how to format the rtf document to that it matches the pdf
  document (or other format document) form which it was generated. The RtoX
   software picks out those codes that provide information which may be
    useful in content analysis, and converts them to XML tags. The resulting
     XML document does not have sufficient information to format it to look
      like the pdf document. But it does have relevant information.
      
For example, a researcher may want to know what text was emphasized in the
 original document and how it was emphasized. Was it in italics? Bold
 ? Underlined? The rtf document and the XML document retain that information
 . The researcher, however, is probably not interested in the text margins of
  the original document, and that information (though in the rtf file) is not
   captured in the XML document.

## What the software does not do.

Because the intended end result is an XML file, the software (Version 0.1
.0a) omits certain
 information coded into the rtf file. Future versions may pick up some or all
  of this coding. For example, legal documents very rarely use a text color
   other than black. While text color information is coded into the rtf file
   , that information currently is not captured in the XML file. The
    following sections give a bit more information about the coding which is
     not passed from the rtf file to the XML file.
  
### Color Table

An RTF file usually includes a color table (\colortbl) in the header
. Documents used in and produced by tribunals very rarely use colors other
 than black and white. Therefore, this version (0.1.0a) for the RtoX software
  omits information from the RTF color table.
  
### Stylesheets

RTF stylesheet information provides detailed instructions to RTF readers on
 how to format text throughout the document. Given the many possible
  combinations of font, margins, highlighting, etc., an RTF document can
   contain several dozen lines of stylesheet codes.
   
An XML document, particularly one used for content analysis, does not need
 most of the information contained in the RTF stylesheets. Margins (with a
  few exceptions)
 , changes
  in font size, and other formatting details can be left out of an RTF to XML
   conversion without losing any significant data. As a result, RtoX focuses
    on the formatting information that provide information potentially relevant
     to content analysis. This information includes: bold, italic, underline
     , footnote, ______________.
     
### Style and Formatting Restrictions


### Revision Information


### File Security Information


## RtoX User Preferences


