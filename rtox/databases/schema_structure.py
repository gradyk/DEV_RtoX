#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2019. Kenneth A. Grady
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright
#  notice, this list of conditions and the following disclaimer in the
#  documentation and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#  contributors may be used to endorse or promote products derived
#  from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Set up schemas in rtox_db.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-08"
__name__ = "schema_structure"

import psycopg2
import psycopg2.errorcodes
import sys
from psycopg2 import sql


class SchemaStructure:

    def __init__(self,
                 con,
                 cur) -> None:
        self.con = con
        self.cur = cur

    def schema_setup(self):

        sys.stdout.write("Starting schema creation... \n")

        # List of schemas to set up, if they don't already exist.
        schema_family = ["fontcodes", "stylecodes", "docinfocodes",
                         "doccodes", "filecodes"]

        for schema in schema_family:
            try:
                sys.stdout.write(f"Creating {schema} schema... \n")
                self.cur.execute(sql.SQL(
                    f"CREATE SCHEMA IF NOT EXISTS {schema}").
                    format(sql.Identifier(f"{schema}")))

            except psycopg2.DatabaseError as err:
                SchemaStructure.error_code(err=err)

    @staticmethod
    def error_code(err) -> None:

        if str(err.pgcode) == "3F000":
            # Schema already exists.
            sys.stdout.write(f"{err}.\n")
        else:
            # There is a different problem.
            pg_err = str(err.pgcode)
            print(f"Error number {pg_err}; {err}.\n")
            sys.exit(1)
