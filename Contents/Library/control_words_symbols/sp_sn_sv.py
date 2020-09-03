#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# sp, sn, and sv are part of the Shapes destination in RTF.
# See Word2007RTFSpec9 Pictures, p.162. They also form part of the Pictures
# destination.

# The control words appear in a group {\shp ... {\sp{\sn XXX}{\sv N}}
# The entire group {\shp ...} can be ignored.
# However, another group may follow within the {\shp ...} group:
# {\shptxt ... XXX} where "..." will be some combination of control words,
# and XXX is the text. This group should be processed and included in the
# output file.
