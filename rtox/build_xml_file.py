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

"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-24"
__name__ = "build_xml"

# From standard libraries
import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def table_union():
    from debugdir.config_dict import config_dictionary

    host = config_dictionary.get("host")
    database = config_dictionary.get("database")
    user = config_dictionary.get("user")
    password = config_dictionary.get("password")

    con = psycopg2.connect(host=host, database=database, user=user,
                           password=password)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    try:

        build_doc = """(DELETE FROM rtox_db.final.table_name);
        CREATE TABLE rtox_db.final.table_name AS (SELECT * FROM 
        rtox_db.doccodes.cslinecodes UNION ALL 
        SELECT lineno, lineend, null as Col3, null as Col4, null as Col5, null 
        as Col6, null as Col7, null as Col8 FROM rtox_db.doccodes.footnotes X
        ORDER BY lineno);"""

        cur.execute(build_doc)
        con.commit()

    except psycopg2.DatabaseError as err:
        pg_err = str(err.pgcode)
        sys.stdout.write("Problem entering style codes in database.\n"
                         f"Error number {pg_err}; {err}\n")

    if con is not None:
        cur.close()
        con.close()


if __name__ == "build_xml":
    table_union()
