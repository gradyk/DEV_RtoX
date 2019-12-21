#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
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
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:

"""
Part of the setup process for RtoX. This module should run only once when
the user installs RtoX.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-03"
__name__ = "Setup_db"

# TODO Remove this hint when satisfied with Setup_db.
# See https://kb.objectrocket.com/postgresql/
# python-error-handling-with-the-psycopg2-postgresql-adapter-645

import os
import psycopg2
import psycopg2.errorcodes
import rtox.databases.database_config
import rtox.databases.schema_structure
import rtox.databases.table_structure
import sys
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class SetupDatabase:

    @staticmethod
    def base_script_dir():
        base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        return base_script_dir

    @staticmethod
    def db_prep(base_script_dir):
        """
        Creates a database that RtoX will use to store document information
        relevant to producing the final XML file.
        """

        config_vars = rtox.databases.database_config.DatabasePrep.config(
            self=rtox.databases.database_config.DatabasePrep(
                base_script_dir=base_script_dir))

        host = config_vars[0]
        database = config_vars[1]
        user = config_vars[2]
        password = config_vars[3]

        return host, database, user, password

    @staticmethod
    def db_create(host, database, user, password):

        sys.stdout.write("Starting database creation...\n")
        con = psycopg2.connect(host=host, database=database, user=user,
                               password=password)

        sys.stdout.write('Connecting to host...\n')
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = con.cursor()

        try:
            sys.stdout.write('Creating database...\n')
            # Use the psycopg2.sql module instead of string concatenation
            # in order to avoid sql injection attacks.
            cur.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier("rtox_db")))

        except psycopg2.DatabaseError as err:

            if str(err.pgcode) == "42P04":
                # rtox_db exists
                sys.stdout.write("rtox_db database already exists.\n")

            else:
                # There is a different problem.
                pg_err = str(err.pgcode)
                print(f"Error number {pg_err}; {err}\n")
                sys.exit(1)

        return con, cur


if __name__ == "Setup_db":
    base_script_dir_pass = SetupDatabase.base_script_dir()

    db_prep_vars = SetupDatabase.db_prep(
        base_script_dir=base_script_dir_pass)

    host_pass = db_prep_vars[0]
    database_pass = db_prep_vars[1]
    user_pass = db_prep_vars[2]
    password_pass = db_prep_vars[3]

    db_create_vars = SetupDatabase.db_create(host=host_pass,
                                             database=database_pass,
                                             user=user_pass,
                                             password=password_pass)
    con_pass = db_create_vars[0]
    cur_pass = db_create_vars[1]

    rtox.databases.schema_structure.SchemaStructure.schema_setup(
        self=rtox.databases.
        schema_structure.SchemaStructure(con=con_pass, cur=cur_pass))

    rtox.databases.table_structure.TableStructure.style_table(
        self=rtox.databases.table_structure.TableStructure(con=con_pass,
                                                           cur=cur_pass))

    rtox.databases.table_structure.TableStructure.font_table(
        self=rtox.databases.table_structure.TableStructure(con=con_pass,
                                                           cur=cur_pass))

    rtox.databases.table_structure.TableStructure.docinfo_table(
        self=rtox.databases.table_structure.TableStructure(con=con_pass,
                                                           cur=cur_pass))

    rtox.databases.table_structure.TableStructure.doc_table(
        self=rtox.databases.table_structure.TableStructure(con=con_pass,
                                                           cur=cur_pass))

    rtox.databases.table_structure.TableStructure.file_table(
        self=rtox.databases.table_structure.TableStructure(con=con_pass,
                                                           cur=cur_pass))

    rtox.databases.table_structure.TableStructure.tables_finished(
        self=rtox.databases.table_structure.TableStructure(con=con_pass,
                                                           cur=cur_pass))
