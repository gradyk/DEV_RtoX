#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""
Format and compress the working_xml_file. This is the last step before the
file is moved to the folder designated by the user for the output file,
and the file is renamed to the output file name designated by the user.
[Based on xmlformatter by P. Andreas Moeller.]
"""

__author__ = "Kenneth A. Grady/P. Andreas Moeller"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-26"
__name__ = "Contents.Library.xmlformatter"

import re
import os
import sys
import xml.parsers.expat
from xml.parsers.expat import ExpatError
from xml.parsers.expat import ParserCreate as Pc
import xml.parsers.expat.model


DEFAULT_COMPRESS = False
DEFAULT_CORRECT = True
DEFAULT_INDENT = 2
DEFAULT_INDENT_CHAR = " "
DEFAULT_INLINE = True
DEFAULT_ENCODING_INPUT = None
DEFAULT_ENCODING_OUTPUT = None
DEFAULT_PRESERVE = ""


class Formatter:
    # Use internal encoding:
    encoding_internal = None

    def __init__(self,
                 indent=DEFAULT_INDENT,
                 compress=DEFAULT_COMPRESS,
                 indent_char=DEFAULT_INDENT_CHAR,
                 encoding_input=DEFAULT_ENCODING_INPUT,
                 encoding_output=DEFAULT_ENCODING_OUTPUT,
                 inline=DEFAULT_INLINE,
                 correct=DEFAULT_CORRECT,
                 preserve=DEFAULT_PRESERVE) -> None:
        # Minify the XML document: TODO Does this do anything?
        self.compress = compress
        # Correct text nodes
        self.correct = correct
        # Decode the XML document:
        self.encoding_input = self.enc_normalize(encoding_input)
        # Encode ouput by:
        self.encoding_output = self.enc_normalize(encoding_output)
        # Insert indent = indent*level*indent_char:
        self.indent = int(indent)
        # Indent by char:
        self.indent_char = indent_char
        # Format inline objects:
        self.inline = inline
        # Don't compress these elements and their descendants:
        self.preserve = preserve

    @property
    def encoding_effective(self):
        if self.encoding_output:
            return self.encoding_output
        elif self.encoding_internal:
            return self.encoding_internal
        elif self.encoding_input:
            return self.encoding_input
        else:
            return 'UTF-8'

    @staticmethod
    def enc_normalize(string):
        """ Format an Encoding identifier to upper case. """
        if isinstance(string, str):
            return string.upper()
        return None

    @staticmethod
    def enc_output(path, strg):
        """ Output according to encoding """
        fh = sys.stdout
        if strg is not None:
            if path is not None:
                return strg
            elif sys.version_info > (3, 0):
                with open(os.path.join("/Users/gradyke/Documents/DEV_RtoX/, "
                                       "working_xml_file.xml"), "w") as \
                        new_file_pre:
                    new_file_pre.write(strg)
                # fh.buffer.write(strg)
            else:
                fh.write(strg)

    # First step: format the infile (working_xml_file.xml).
    def format_file(self, file):
        """ Format the XML document. """
        fh = open(file, 'rb')
        # Use Formatter.TokenList to create a list (in order) of tokens in
        # the file.
        token_list = Formatter.TokenList(self)
        token_list.parser.ParseFile(fh)
        fh.close()
        return str(token_list)

    class TokenList:
        # Being in a cdata section:
        cdata_section = False
        # Lock deletion of leading whitespace:
        desc_mixed_level = None
        # Lock indenting:
        indent_level = None
        # Reference the Formatter:
        formatter = None
        # Count levels:
        level_counter = 0
        # Lock deletion of whitespaces:
        preserve_level = None

        def __init__(self, formatter):
            # Keep tokens in a list:
            self._list = []
            self.formatter = formatter
            self.parser = Pc(encoding=self.formatter.encoding_input)
            self.parser.specified_attributes = 1
            self.parser.buffer_text = True
            # Push tokens to buffer:
            for pattern in ['XmlDecl%s', 'ElementDecl%s', 'AttlistDecl%s',
                            'EntityDecl%s', 'StartElement%s', 'EndElement%s',
                            'ProcessingInstruction%s', 'CharacterData%s',
                            'Comment%s', 'Default%s', 'StartDoctypeDecl%s',
                            'EndDoctypeDecl%s', 'StartCdataSection%s',
                            'EndCdataSection%s', 'NotationDecl%s']:
                setattr(self.parser, pattern %'Handler',
                        self.xml_handler(pattern %''))

        def __iter__(self):
            return iter(self._list)

        def __len__(self):
            return len(self._list)

        def __getitem__(self, pos):
            if 0 <= pos < len(self._list):
                return self._list[pos]
            else:
                raise IndexError

        def __setitem__(self, pos, value):
            if 0 <= pos < len(self._list):
                self._list[pos] = value
            else:
                raise IndexError

        # TODO For __str__ see: https://lucumr.pocoo.org/2011/1/22/
        #  forwards-compatible-python/ specifically Recursion Error with str
        def __str__(self):
            """ Returns the formatted XML document in UTF-8. """
            for step in ["configure", "pre_operate", "post_operate"]:
                for tk in iter(self):
                    getattr(tk, step)()
            result = ""
            for tk in iter(self):
                result += str(tk)
            return result

        def append(self, tk):
            """ Add token to tokenlist. """
            tk.pos = len(self._list)
            self._list.append(tk)

        def level_increment(self):
            """ Increment level counter. """
            self.level_counter += 1

        def level_decrement(self):
            """ Decrement level counter. """
            self.level_counter -= 1

        def token_descendant_mixed(self, tk):
            """ Mark descendants of mixed content. """
            if tk.name == "StartElement":
                # Mark every descendant:
                if tk.content_model in [2, 3] and self.desc_mixed_level is None:
                    self.desc_mixed_level = tk.level
                    return False
                return self.desc_mixed_level is not None
            elif tk.name == "EndElement":
                # Stop marking every descendant:
                if tk.level is self.desc_mixed_level:
                    self.desc_mixed_level = None
                elif self.desc_mixed_level is not None:
                    return True
                return False
            elif self.desc_mixed_level is None:
                return False
            return self.desc_mixed_level >= tk.level-1

        def sequence(self, tk, scheme=None):
            """
            Returns sublist of token list.
            None: next to last
            EndElement: first to previous
            """
            if scheme == "EndElement" or (scheme is None and tk.end):
                return reversed(self._list[:tk.pos])
            return self._list[(tk.pos + 1):]

        def token_indent(self, tk):
            if self.formatter.inline:
                return self.token_indent_inline(tk)
            """ Indent outside of text of mixed content. """
            if tk.name == "StartElement":
                # Block indenting for descendants of text and mixed content:
                if tk.content_model in [2, 3] and self.indent_level is None:
                    self.indent_level = tk.level
                elif self.indent_level is not None:
                    return False
                return True
            elif tk.name == "EndElement":
                # Unblock indenting for descendants of text and mixed content:
                if tk.level == self.indent_level:
                    self.indent_level = None
                elif self.indent_level is None:
                    return True
                return False
            return self.indent_level is None

        def token_indent_inline(self, tk):
            """
            Indent every element content - no matter if enclosed by text or
            mixed content.
            """
            for itk in iter(self.sequence(tk, "EndElement")):
                if itk.level < tk.level and itk.name == "StartElement":
                    if itk.content_model == 1:
                        return True
                    return False
                if itk.level == tk.level and tk.name == "EndElement" \
                        and itk.name == "StartElement":
                    if itk.content_model == 1:
                        return True
                    return False
            return True

        def token_model(self, tk):
            """ Returns code for content model.
                0: empty
                1: element
                2: text
                3: mixed """
            eflag = tflag = 0
            for itk in iter(self.sequence(tk)):
                # Element boundary found:
                if itk.level <= tk.level:
                    break
                # Direct child found:
                elif (itk.level - 1) == tk.level:
                    if itk.start:
                        eflag = 1
                    elif itk.not_empty:
                        tflag = 2
            return eflag + tflag

        def token_preserve(self, tk):
            """ Preserve every descendant of a preserved element.
                0: not locked
                1: just (un)locked
                2: locked
            """
            # Lock preserving for StartElements:
            if tk.name == "StartElement":
                if self.preserve_level is not None:
                    return 2
                if tk.arg[0] in self.formatter.preserve:
                    self.preserve_level = tk.level
                    return 1
                return 0
            # Unlock preserving for EndElements:
            elif tk.name == "EndElement":
                if tk.arg[0] in self.formatter.preserve and \
                        tk.level == self.preserve_level:
                    self.preserve_level = None
                    return 1
                elif self.preserve_level is None:
                    return 0
                return 2
            return self.preserve_level is not None

        def whitespace_append_trailing(self, tk):
            """ Add a trailing whitespace to previous character data. """
            if self.formatter.correct and tk.leading and tk.not_empty:
                self.whitespace_append(tk, "EndElement", "StartElement", True)

        def whitespace_append_leading(self, tk):
            """ Add a leading whitespace to previous character data. """
            if self.formatter.correct and tk.trailing and tk.not_empty:
                self.whitespace_append(tk)

        def whitespace_append(self, tk, start="StartElement", stop="EndElement",
                              direct=False):
            """ Add a whitespace to token list. """
            for itk in self.sequence(tk, start):
                if itk.empty or (itk.name == stop and itk.descendant_mixed is
                                 False) or (itk.name == start and
                                            abs(tk - itk) == 1):
                    break
                elif itk.not_empty or (itk.name == start and
                                       itk.descendant_mixed):
                    self.insert_empty(itk, direct)
                    break

        def whitespace_delete_leading(self, tk):
            """
            Returns True, if no next token or all empty (up to next end element)
            """
            if self.formatter.correct and tk.leading and not tk.preserve \
                    and not tk.cdata_section:
                for itk in self.sequence(tk, "EndElement"):
                    if itk.trailing:
                        return True
                    elif itk.name in ["EndElement", "CharacterData",
                                      "EndCdataSection"]:
                        return False
                return True
            return False

        def whitespace_delete_trailing(self, tk):
            """
            Returns True, if no next token or all empty (up to next
            end element)
            """
            if self.formatter.correct and tk.trailing and not tk.preserve and \
                    not tk.cdata_section:
                for itk in self.sequence(tk, "StartElement"):
                    if itk.end:
                        return True
                    elif itk.name in ["StartElement", "StartCdataSection"] \
                            or itk.not_empty:
                        return False
                return True
            return False

        def insert_empty(self, tk, before=True):
            """ Insert an Empty Token into token list - before or after tk. """
            if not (0 < tk.pos < (len(self) - 1)):
                return False
            ptk = self[tk.pos-1]
            ntk = self.formatter.CharacterData(self, [" "])
            ntk.level = max(ptk.level, tk.level)
            ntk.descendant_mixed = tk.descendant_mixed
            ntk.preserve = ptk.preserve*tk.preserve
            ntk.cdata_section = (ptk.cdata_section or tk.cdata_section)
            if before:
                self._list.insert(tk.pos+1, ntk)
            else:
                self._list.insert(tk.pos, ntk)
            for i in range((tk.pos - 1), len(self._list)):
                self._list[i].pos = i

        def xml_handler(self, key):
            """ Returns lambda function which adds token to token list"""
            return lambda *arg: self.append(
                getattr(self.formatter, key)(self, arg))

    class Token(object):
        def __init__(self, tklist, arg):
            # Reference Token List:
            self.list = tklist
            # Token data:
            self.arg = list(arg)
            # Token is placed in an CDATA section:
            self.cdata_section = False
            # Token has content model:
            self.content_model = None
            # Remove trailing whitespaces:
            self.delete_trailing = False
            # Remove leading whitespaces:
            self.delete_leading = False
            # Token is descendant of text or mixed content element:
            self.descendant_mixed = False
            # Reference to formatter:
            self.formatter = tklist.formatter
            # Insert indenting white spaces:
            self.indent = True
            # N-th generation of roots descendants:
            self.level = self.list.level_counter
            # Token class:
            self.name = self.__class__.__name__
            # Preserve white spaces within enclosed tokens:
            self.preserve = False
            # Position in token list:
            self.pos = None

        def __sub__(self, other):
            return self.pos - other.pos

        def __str__(self):
            return ""

        @property
        def end(self):
            return self.name == "EndElement"

        @property
        def empty(self):
            return self.name == "CharacterData" and re.match(r'^[\t\s\n]*$',
                                                             self.arg[0])

        @property
        def leading(self):
            return self.name == "CharacterData" and re.search(r'^[\t\s\n]+',
                                                              self.arg[0])

        @property
        def not_empty(self):
            return self.name == "CharacterData" and not self.cdata_section \
                   and not re.match(r'^[\t\s\n]+$', self.arg[0])

        @property
        def trailing(self):
            return self.name == "CharacterData" and re.search(r'[\t\s\n]+$',
                                                              self.arg[0])

        @property
        def start(self):
            return self.name == "StartElement"

        @property
        def correct(self):
            return self.formatter.correct

        @staticmethod
        def attribute(key, value):
            if key and value:
                return f" {key}=\"{value}\""
            return ""

        def indent_insert(self):
            """ Indent token. """
            # Child of root and no empty node
            if (self.level > 0 and not (self.end and
                                        self.list[self.pos-1].start)
                # not empty node:
                    or self.end and not self.list[self.pos-1].start):
                return self.indent_create(self.level)
            return ""

        def indent_create(self, times=1):
            """ Returns indent string. """
            if not self.formatter.compress and self.formatter.indent:
                indent = f"\n{(times * self.formatter.indent) * self.formatter.indent_char}"
                return indent
            return ""

        @staticmethod
        def identifier(systemid, publicid):
            # TODO add base parameter:
            if publicid and systemid:
                return f' PUBLIC {publicid} {systemid}'
            elif publicid:
                return f' PUBLIC {publicid}'
            elif systemid:
                return f' SYSTEM {systemid}'
            return ""

        def configure(self):
            """ Set token properties. """
            self.descendant_mixed = self.list.token_descendant_mixed(self)
            self.preserve = self.list.token_preserve(self)
            self.cdata_section = self.list.cdata_section

        def pre_operate(self):
            pass

        def post_operate(self):
            pass

    class AttlistDecl(Token):
        def __str__(self):
            strg = self.indent_create()
            strg += f"<!ATTLIST {self.arg[0]} {self.arg[1]}"
            if self.arg[2] is not None:
                strg += f" {self.arg[2]}"
            if self.arg[4] and not self.arg[3]:
                strg += " #REQUIRED"
            elif self.arg[3] and self.arg[4]:
                strg += " #FIXED"
            elif not self.arg[4] and not self.arg[3]:
                strg += " #IMPLIED"
            if self.arg[3]:
                strg += f' {self.arg[3]}'
            strg += ">"
            return strg

    class CharacterData(Token):
        def __str__(self):
            strg = self.arg[0]
            if not self.preserve and not self.cdata_section:
                # Remove empty tokens always in element content!
                if self.empty and not self.descendant_mixed:
                    strg = ""
                else:
                    if self.correct:
                        strg = re.sub(r'\r\n', '\n', strg)
                        strg = re.sub(r'\\[rnt]', ' ', strg)
                        strg = re.sub(r'\s+', ' ', strg)
                    if self.delete_leading:
                        strg = re.sub(r'^\s', '', strg)
                    if self.delete_trailing:
                        strg = re.sub(r'\s$', '', strg)
            if not self.cdata_section:
                strg = re.sub(r'&', '&amp;', strg)
                strg = re.sub(r'<', '&lt;', strg)
            return strg

        def pre_operate(self):
            self.list.whitespace_append_trailing(self)
            self.list.whitespace_append_leading(self)

        def post_operate(self):
            self.delete_leading = self.list.whitespace_delete_leading(self)
            self.delete_trailing = self.list.whitespace_delete_trailing(self)

    class Comment(Token):
        def __str__(self):
            strg = ""
            if self.preserve in [0, 1] and self.indent:
                strg += self.indent_insert()
            strg += "<!--%s-->" % re.sub(r'^[\r\n]+$', '\n',
                                         re.sub(r'^[\r\n]+', '\n', self.arg[0]))
            return strg

        def configure(self):
            super(Formatter.Comment, self).configure()
            self.indent = self.list.token_indent(self)

    class Default(Token):
        pass

    class EndCdataSection(Token):
        def __str__(self):
            return "]]>"

        def configure(self):
            self.list.cdata_section = False

    class ElementDecl(Token):
        def __str__(self):
            strg = self.indent_create()
            strg += f"<!ELEMENT {self.arg[0]}" \
                    f"{self.evaluate_model(self.arg[1])}>"
            return strg

        def evaluate_model(self, model, modelstr="", concatstr=""):
            childseq = []
            mixed = (model[0] == xml.parsers.expat.model.XML_CTYPE_MIXED)
            haschilds = (len(model[3]) or mixed)
            if model[0] == xml.parsers.expat.model.XML_CTYPE_EMPTY:  # 1
                modelstr += " EMPTY"
            elif model[0] == xml.parsers.expat.model.XML_CTYPE_ANY:  # 2
                modelstr += " ANY"
            elif model[0] == xml.parsers.expat.model.XML_CTYPE_NAME:  # 4
                modelstr = f"{model[2]}"  # new start
            elif model[0] in (xml.parsers.expat.model.XML_CTYPE_CHOICE,
                              xml.parsers.expat.model.XML_CTYPE_MIXED):  # 5
                concatstr = "|"
            elif model[0] == xml.parsers.expat.model.XML_CTYPE_SEQ:  # 6
                concatstr = ","
            if haschilds:
                modelstr += " ("
            if mixed:
                childseq.append("#PCDATA")
            for child in model[3]:
                childseq.append(self.evaluate_model(child))
            modelstr += concatstr.join(childseq)
            if haschilds:
                modelstr += ")"
            modelstr += {xml.parsers.expat.model.XML_CQUANT_NONE: "",
                         xml.parsers.expat.model.XML_CQUANT_OPT: "?",
                         xml.parsers.expat.model.XML_CQUANT_PLUS: "+",
                         xml.parsers.expat.model.XML_CQUANT_REP: "*"
                         }[model[1]]
            return modelstr

    class EndDoctypeDecl(Token):
        def __str__(self):
            strg = ""
            if self.list[self.pos - 1].name != "StartDoctypeDecl":
                strg += self.indent_create(0)
                strg += "]"
            strg += ">"
            strg += self.indent_create(0)
            return strg

    class EndElement(Token):
        def __init__(self, listvar, arg):
            listvar.level_decrement()
            super(Formatter.EndElement, self).__init__(listvar, arg)

        def __str__(self):
            strg = ""
            # Don't close empty nodes on compression mode:
            if not self.formatter.compress or self.list[self.pos-1].name \
                    != "StartElement":
                if self.preserve in [0] and self.indent:
                    strg += self.indent_insert()
                strg += f"</{self.arg[0]}>"
            return strg

        def configure(self):
            self.descendant_mixed = self.list.token_descendant_mixed(self)
            self.preserve = self.list.token_preserve(self)
            self.indent = self.list.token_indent(self)

    class EntityDecl(Token):
        def __str__(self):
            strg = self.indent_create()
            strg += "<!ENTITY "
            if self.arg[1]:
                strg += "% "
            strg += f"{self.arg[0]} "
            if self.arg[2]:
                strg += f'{self.arg[2]}'
            else:
                strg += f"{self.identifier(self.arg[4], self.arg[5])} "
                if self.arg[6]:
                    strg += f"NDATA {self.arg[6]}"
            strg += ">"
            return strg

    class NotationDecl(Token):
        def __str__(self):
            strg = self.indent_create()
            strg += f"<!NOTATION {self.arg[0]}" \
                    f"{self.identifier(self.arg[2], self.arg[3])}>"
            return strg

    class ProcessingInstruction(Token):
        def __str__(self):
            strg = ""
            if self.preserve in [0, 1] and self.indent:
                strg += self.indent_insert()
            strg += f"<?{self.arg[0]} {self.arg[1]}?>"
            return strg

        def configure(self):
            super(Formatter.ProcessingInstruction, self).configure()
            self.indent = self.list.token_indent(self)

    class StartCdataSection(Token):
        def __str__(self):
            return "<![CDATA["

        def configure(self):
            self.list.cdata_section = True

    class StartDoctypeDecl(Token):
        def __str__(self):
            strg = f"<!DOCTYPE {self.arg[0]}"
            if self.arg[1]:
                strg += self.identifier(self.arg[1], self.arg[2])
            if self.arg[3]:
                strg += " ["
            return strg

    class StartElement(Token):
        def __init__(self, listvar, arg):
            super(Formatter.StartElement, self).__init__(listvar, arg)
            self.list.level_increment()

        def __str__(self):
            strg = ""
            if self.preserve in [0, 1] and self.indent:
                strg += self.indent_insert()
            strg += f"<{self.arg[0]}"
            for attr in sorted(self.arg[1].keys()):
                strg += self.attribute(attr, self.arg[1][attr])
            if self.list[self.pos+1].end and self.formatter.compress:
                strg += "/>"
            else:
                strg += ">"
            return strg

        def configure(self):
            self.content_model = self.list.token_model(self)
            self.descendant_mixed = self.list.token_descendant_mixed(self)
            self.preserve = self.list.token_preserve(self)
            self.indent = self.list.token_indent(self)

    class XmlDecl(Token):
        def __init__(self, listvar, arg):
            super(Formatter.XmlDecl, self).__init__(listvar, arg)
            if len(self.arg) > 1:
                self.formatter.encoding_internal = self.arg[1]

        def __str__(self):
            strg = f"<?xml{self.attribute('version', self.arg[0])}"
            f"{self.attribute('encoding', self.formatter.encoding_effective)}"

            if self.arg[2] > -1:
                strg += self.attribute("standalone", "yes")
            strg += "?>\n"
            return strg


def xmlformatter_start(infile, outfile):
    """ xmlformatter is run as the last step before returning the XML named
    according to the user's preference. The goal is to have a properly
    indented XML file. """
    res = ()
    formatter = ()
    indent = DEFAULT_INDENT
    indent_char = DEFAULT_INDENT_CHAR
    outfile = outfile
    preserve = DEFAULT_PRESERVE
    compress = DEFAULT_COMPRESS
    encoding = DEFAULT_ENCODING_INPUT
    outencoding = DEFAULT_ENCODING_OUTPUT
    inline = DEFAULT_INLINE
    correct = DEFAULT_CORRECT

    try:
        formatter = Formatter(indent=indent,
                              preserve=preserve,
                              compress=compress,
                              encoding_input=encoding,
                              encoding_output=outencoding,
                              indent_char=indent_char,
                              inline=inline,
                              correct=correct)
        res = formatter.format_file(infile)

    except ExpatError as err:
        print(f"XML error: {err}")
    except IOError as err:
        print(f"IO error: {err}")
    xml_formatted_text = formatter.enc_output(outfile, res)
    return xml_formatted_text
