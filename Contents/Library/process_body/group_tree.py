#  !/usr/bin/env python3
#   -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  This file is part of RtoX.
#
#  RtoX is free software: you can redistribute it and / or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see <https://www.gnu.org/licenses/>.

from anytree import RenderTree, AnyNode, LevelOrderIter
from anytree.exporter import JsonExporter


def make_tree():
    group0 = AnyNode(id="group0", parent=None, type="group")
    cw1 = AnyNode(id="\\intro", parent=group0, type="ctrl_wrd")
    cw2 = AnyNode(id="\\word", parent=group0, type="ctrl_wrd")
    group1 = AnyNode(id="{\\*\\thing {\\nothing\\else}}", parent=group0, type="group")
    cw3 = AnyNode(id="\\*\\thing", parent=group1, type="ctrl_wrd")
    group2 = AnyNode(id="{\\nothing\\else}", parent=group1, type="group")
    cw4 = AnyNode(id="\\nothing", parent=group2, type="ctrl_wrd")
    cw5 = AnyNode(id="\\else", parent=group2, type="ctrl_wrd")
    cw6 = AnyNode(id="\\given", parent=group0, type="ctrl_wrd")
    cw7 = AnyNode(id="\\together", parent=group0, type="ctrl_wrd")
    group3 = AnyNode(id="{\\speaking\\fast}", parent=group0, type="group")
    cw8 = AnyNode(id="\\speaking", parent=group3, type="ctrl_wrd")
    cw9 = AnyNode(id="\\fast", parent=group3, type="ctrl_wrd")
    cw10 = AnyNode(id="\\hyper", parent=group0, type="ctrl_wrd")
    cw11 = AnyNode(id="\\charged", parent=group0, type="ctrl_wrd")
    group4 = AnyNode(id="{\\terrible{\\*\\awful\\lawyer}}", parent=group0,
                     type="group")
    cw12 = AnyNode(id="\\terrible", parent=group4, type="ctrl_wrd")
    group5 = AnyNode(id="{\\*\\awful\\lawyer}", parent=group4, type="group")
    cw13 = AnyNode(id="\\*\\awful", parent=group5, type="ctrl_wrd")
    cw14 = AnyNode(id="\\lawyer", parent=group5, type="ctrl_wrd")
    cw15 = AnyNode(id="\\game", parent=group0, type="ctrl_wrd")
    txt = AnyNode(id="changer", parent=group0, type="txt")
    # name = AnyAnyNode(id=f"{element_name}", parent=f"{parent_name}",
    #                type=f'{type_name}')
    for pre, _, node in RenderTree(group0):
        print("%s%s" % (pre, node.id))

    exporter = JsonExporter(indent=2, sort_keys=False)
    print(exporter.export(group0))

    node_list = [node.id for node in LevelOrderIter(group0, maxlevel=2)]
    print(node_list)


if __name__ == "__main__":
    make_tree()
