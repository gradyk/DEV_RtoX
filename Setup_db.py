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
Part of the setup process for RtoX. This module should run only once when
the user installs RtoX.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-03"
__name__ = "Setup_db"

# See https://kb.objectrocket.com/postgresql/
# python-error-handling-with-the-psycopg2-postgresql-adapter-645

import os
import psycopg2
import psycopg2.errorcodes
import rtox.database_config
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
        # TODO database_config should be moved to a folder with other setup
        #  modules (under main folder, not in rtox).
        config_vars = rtox.database_config.DatabasePrep.config(
            self=rtox.database_config.DatabasePrep(
                base_script_dir=base_script_dir))
        host = config_vars[0]
        database = config_vars[1]
        user = config_vars[2]
        password = config_vars[3]

        return host, database, user, password

    @staticmethod
    def handle_psycopg2_exception(host, database, user, password):
        # TODO Should start with create database. Then, if error (database
        #  exists) should exit saying db exists. If db doesn't exist, should
        #  continue with creating db and then exit saying db is set up.
        sys.stdout.write('Starting database removal...')
        con = psycopg2.connect(host=host,
                               database=database,
                               user=user,
                               password=password)

        sys.stdout.write('Connecting to host...')
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        try:
            sys.stdout.write('Dropping database...')
            cur = con.cursor()
            cur.execute(sql.SQL("DROP DATABASE {}").format(
                sql.Identifier("rtox_db")))

        except psycopg2.DatabaseError as err:

            if str(err.pgcode) == "3D000":  # rtox_db does not exist

                sys.stdout.write("Starting database creation ...")
                con = psycopg2.connect(host=host_pass,
                                       database=database_pass,
                                       user=user_pass,
                                       password=password_pass)

                sys.stdout.write('Connecting to host...')
                con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

                cur = con.cursor()

                # Use the psycopg2.sql module instead of string concatenation
                # in order to avoid sql injection attacks.
                sys.stdout.write('Creating database...')
                cur.execute(sql.SQL("CREATE DATABASE {}").format(
                    sql.Identifier("rtox_db")))

                cur.close()
                con.close()
                sys.stdout.write('All done!')

            else:
                # There is a different problem.
                pg_err = str(err.pgcode)
                print(f"Error number {pg_err}; {err}\n")
                print("a different database problem exists.")
                sys.exit(1)


if __name__ == "Setup_db":
    base_script_dir_pass = SetupDatabase.base_script_dir()

    db_prep_vars = SetupDatabase.db_prep(
        base_script_dir=base_script_dir_pass)
    host_pass = db_prep_vars[0]
    database_pass = db_prep_vars[1]
    user_pass = db_prep_vars[2]
    password_pass = db_prep_vars[3]

    SetupDatabase.handle_psycopg2_exception(
        host=host_pass,
        database=database_pass,
        user=user_pass,
        password=password_pass)
