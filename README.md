# RtoX File Conversion Package

The primary purpose of this software is to convert an RTF file into a basic XML
 tagged file. The software gives you three options for XML tags: 1) plain XML
  tags, 2) tags from the Text Encoding Initiative (TEI), and 3) tags from the
   Tribunal Proceedings and Resolutions Encoding System (TPRES). By
    converting an RTF file rather than a TXT file, the user retains certain
     features (e.g., italics, bold) that may be useful to tag and have
      available when analyzing the XML file. 
      
The RtoX software is intended
       for use as part of a workflow where the source document is in PDF
        format. The user runs the PDF file through OCR software, saving the
         output as an RTF file. Some OCR software will permit you to do this
          directly, while other software requires and intermediate step (e.g
          ., OCR -> Word - RTF).

The RtoX software is further intended primarily for the conversion of legal
 documents used in or resulting from tribunal proceedings. This focus makes
  it easier to design the RtoX software, but limits its usefulness outside
   the legal setting.
          
## What the software does.


## What the software does not do.

Because the intended end result is an XML file, the software (Version 0.1
.0a) omits certain
 information coded into the RTF file. Future versions may pick up some or all
  of this coding.
  
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

