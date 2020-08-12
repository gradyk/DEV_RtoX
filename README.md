# RtoX

## Context

The RtoX package will constitute one part of a larger project (the "Oliver
 Project").

## Timeline

RtoX should go into alpha testing in Fall 2020.

## Status

THIS IS A PACKAGE UNDER DEVELOPMENT. WHEN COMPLETED, IT WILL BE RELEASED AS
 AN OPEN SOURCE PACKAGE. AT THIS TIME, IT IS NOT YET IN THE ALPHA STAGE. IT
  IS PUBLIC SO 1) VARIOUS ASPECTS CAN BE TESTED IN ADVANCE OF TESTING THE
   FULL PACKAGE, AND 2) THOSE WHO CHOOSE CAN WATCH THE DEVELOPMENT.
   
THIS README FILE EXPLAINS, IN ABBREVIATED FORM, THE RtoX SOFTWARE AND THE
 MAIN REASON FOR DEVELOPING IT. MORE DETAILED INFORMATION WILL BE INCLUDED
  WITH THE SOFTWARE AS IT REACHES THE PUBLIC TESTING PHASE. 

## What is it?
The RtoX package converts files from Microsoft's RTF format to XML tagged
 text. The user selects the XML tag families from which RtoX will draw specific
  tags. At the outset, the user may choose the Text Encoding Initiative
   Guidelines (TEI) tag family or the Tribunal Proceedings and Resolutions 
   Encoding Scheme (TPRES) tag family. These tag set choices reflect RtoX's
    initial focus on tribunal materials.
   
The TEI Guidelines tag family was created in the 1980s and has become the
 leading XML tag format used in the digital humanities. Projects ranging
  across the humanities use TEI tags or variations of the TEI tag set created
   specifically for projects or areas. For example, the [Women Writers
    Project](http://www.wwp.northeastern.edu/) focuses on early modern women 
    writers, while the [CELT](http://celt.ucc.ie/publishd.html) project focuses
     on Ancient and Medieval Irish Manuscripts.
     
TEI Guidelines, an open source project, were designed so that users could
 select subsets; modify, add to, or delete tags, and otherwise amend the tag
  family to realize a new tag family specific to the user's purpose. TPRES
   represents one such new tag family.
   
The TPRES tag family focuses on documents created or used in tribunal
 proceedings. The tag set was designed to cover briefs, orders, decisions
 , transcripts, and related documents. Although the tag set was built using
  materials from tribunals in the United States, future versions will extend
   the tag set (as necessary) to jurisdictions outside the United States. 
   
Although the focus for RtoX has been on tribunal materials, nothing in the
 coding limits its use to those materials. A user may supply the program with
  any RTF file and get an XML tagged file as the output. 
  
## Why focus on converting RTF files?

Tribunal materials often exist, at least publicly, in PDF formatted files
. A user may find some files formatted as Microsoft Word, New Corel
 WordPerfect, Google Docs, or other formatted documents. Formats other than
  PDF tend to exist among documents submitted to, rather than created by
  , tribunals. The predominance of PDF documents raises various problems for
   the researcher interested in accessing and analyzing the text of the
    documents.
    
The challenge becomes defining the "best" workflow to convert the
 PDF file into another format more amenable to the researcher's interests
 . Modern optical character recognition (OCR) software becomes an important
  if not essential part of the workflow. The PDF document becomes the input
  and the user must select an output format. Of the typical options, RTF
   often becomes the "lesser of evils" choice. 
   
RtoX will bridge the gap between an RTF file and a useable XML file. Other
 conversion software had failings eliminating them from consideration. For
  example, they had no or limited capacity for custom tag sets (i.e., TPRES
  ), the provided limited tagging, the software was out of date, or the
   software did not fit future goals of the Oliver Project.