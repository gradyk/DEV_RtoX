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
Clean out the tables in the rtox_db in preparation for new data.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-03"
__name__ = "rtox_db_clean"

import psycopg2
import psycopg2.errorcodes
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DBClean:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def db_clean(self):
        con = psycopg2.connect(host=self.host, database=self.database,
                               user=self.user, password=self.password)

        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()

        try:
            cur.execute(f"DELETE FROM fontcodes.fontinfo")
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write(f"Error {pg_err}, {err}.\n")

        try:
            cur.execute(f"DELETE FROM stylecodes.emphasis")
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write(f"Error {pg_err}, {err}.\n")

        try:
            cur.execute(f"DELETE FROM stylecodes.misc")
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write(f"Error {pg_err}, {err}.\n")

        try:
            cur.execute(f"DELETE FROM stylecodes.style_type")
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write(f"Error {pg_err}, {err}.\n")

        try:
            cur.execute(f"DELETE FROM docinfocodes.create")
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write(f"Error {pg_err}, {err}.\n")

        try:
            cur.execute(f"DELETE FROM docinfocodes.revise")
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write(f"Error {pg_err}, {err}.\n")

        try:
            cur.execute(f"DELETE FROM docinfocodes.print")
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write(f"Error {pg_err}, {err}.\n")

        try:
            cur.execute(f"DELETE FROM docinfocodes.backup")
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write(f"Error {pg_err}, {err}.\n")

        try:
            cur.execute(f"DELETE FROM docinfocodes.general")
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write(f"Error {pg_err}, {err}.\n")

        try:
            cur.execute(f"DELETE FROM doccodes.doccodes")
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write(f"Error {pg_err}, {err}.\n")

        if con is not None:
            cur.close()
            con.close()
