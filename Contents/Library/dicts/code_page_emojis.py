"""
Character identifiers for emojis.
"""

unicode_to_emoji_dict = {

}

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# emoji-test.txt
# Date: 2020-01-21, 13:40:25 GMT
# © 2020 Unicode®, Inc.
# Unicode and the Unicode Logo are registered trademarks of Unicode, Inc. in the U.S. and other countries.
# For terms of use, see http://www.unicode.org/terms_of_use.html
#
# Emoji Keyboard/Display Test Data for UTS #51
# Version: 13.0
#
# For documentation and usage, see http://www.unicode.org/reports/tr51
#
# This file provides data for testing which emoji forms should be in keyboards and which should also be displayed/processed.
# Format: code points; status # emoji name
#     Code points — list of one or more hex code points, separated by spaces
#     Status
#       component           — an Emoji_Component,
#                             excluding Regional_Indicators, ASCII, and non-Emoji.
#       fully-qualified     — a fully-qualified emoji (see ED-18 in UTS #51),
#                             excluding Emoji_Component
#       minimally-qualified — a minimally-qualified emoji (see ED-18a in UTS #51)
#       unqualified         — a unqualified emoji (See ED-19 in UTS #51)
# Notes:
#   • This includes the emoji components that need emoji presentation (skin tone and hair)
#     when isolated, but omits the components that need not have an emoji
#     presentation when isolated.
#   • The RGI set is covered by the listed fully-qualified emoji.
#   • The listed minimally-qualified and unqualified cover all cases where an
#     element of the RGI set is missing one or more emoji presentation selectors.
#   • The file is in CLDR order, not codepoint order. This is recommended (but not required!) for keyboard palettes.
#   • The groups and subgroups are illustrative. See the Emoji Order chart for more information.


# group: Smileys & Emotion

# subgroup: face-smiling
1F600                                      ; fully-qualified     # 😀 E1.0 grinning face
1F603                                      ; fully-qualified     # 😃 E0.6 grinning face with big eyes
1F604                                      ; fully-qualified     # 😄 E0.6 grinning face with smiling eyes
1F601                                      ; fully-qualified     # 😁 E0.6 beaming face with smiling eyes
1F606                                      ; fully-qualified     # 😆 E0.6 grinning squinting face
1F605                                      ; fully-qualified     # 😅 E0.6 grinning face with sweat
1F923                                      ; fully-qualified     # 🤣 E3.0 rolling on the floor laughing
1F602                                      ; fully-qualified     # 😂 E0.6 face with tears of joy
1F642                                      ; fully-qualified     # 🙂 E1.0 slightly smiling face
1F643                                      ; fully-qualified     # 🙃 E1.0 upside-down face
1F609                                      ; fully-qualified     # 😉 E0.6 winking face
1F60A                                      ; fully-qualified     # 😊 E0.6 smiling face with smiling eyes
1F607                                      ; fully-qualified     # 😇 E1.0 smiling face with halo

# subgroup: face-affection
1F970                                      ; fully-qualified     # 🥰 E11.0 smiling face with hearts
1F60D                                      ; fully-qualified     # 😍 E0.6 smiling face with heart-eyes
1F929                                      ; fully-qualified     # 🤩 E5.0 star-struck
1F618                                      ; fully-qualified     # 😘 E0.6 face blowing a kiss
1F617                                      ; fully-qualified     # 😗 E1.0 kissing face
263A FE0F                                  ; fully-qualified     # ☺️ E0.6 smiling face
263A                                       ; unqualified         # ☺ E0.6 smiling face
1F61A                                      ; fully-qualified     # 😚 E0.6 kissing face with closed eyes
1F619                                      ; fully-qualified     # 😙 E1.0 kissing face with smiling eyes
1F972                                      ; fully-qualified     # 🥲 E13.0 smiling face with tear

# subgroup: face-tongue
1F60B                                      ; fully-qualified     # 😋 E0.6 face savoring food
1F61B                                      ; fully-qualified     # 😛 E1.0 face with tongue
1F61C                                      ; fully-qualified     # 😜 E0.6 winking face with tongue
1F92A                                      ; fully-qualified     # 🤪 E5.0 zany face
1F61D                                      ; fully-qualified     # 😝 E0.6 squinting face with tongue
1F911                                      ; fully-qualified     # 🤑 E1.0 money-mouth face

# subgroup: face-hand
1F917                                      ; fully-qualified     # 🤗 E1.0 hugging face
1F92D                                      ; fully-qualified     # 🤭 E5.0 face with hand over mouth
1F92B                                      ; fully-qualified     # 🤫 E5.0 shushing face
1F914                                      ; fully-qualified     # 🤔 E1.0 thinking face

# subgroup: face-neutral-skeptical
1F910                                      ; fully-qualified     # 🤐 E1.0 zipper-mouth face
1F928                                      ; fully-qualified     # 🤨 E5.0 face with raised eyebrow
1F610                                      ; fully-qualified     # 😐 E0.7 neutral face
1F611                                      ; fully-qualified     # 😑 E1.0 expressionless face
1F636                                      ; fully-qualified     # 😶 E1.0 face without mouth
1F60F                                      ; fully-qualified     # 😏 E0.6 smirking face
1F612                                      ; fully-qualified     # 😒 E0.6 unamused face
1F644                                      ; fully-qualified     # 🙄 E1.0 face with rolling eyes
1F62C                                      ; fully-qualified     # 😬 E1.0 grimacing face
1F925                                      ; fully-qualified     # 🤥 E3.0 lying face

# subgroup: face-sleepy
1F60C                                      ; fully-qualified     # 😌 E0.6 relieved face
1F614                                      ; fully-qualified     # 😔 E0.6 pensive face
1F62A                                      ; fully-qualified     # 😪 E0.6 sleepy face
1F924                                      ; fully-qualified     # 🤤 E3.0 drooling face
1F634                                      ; fully-qualified     # 😴 E1.0 sleeping face

# subgroup: face-unwell
1F637                                      ; fully-qualified     # 😷 E0.6 face with medical mask
1F912                                      ; fully-qualified     # 🤒 E1.0 face with thermometer
1F915                                      ; fully-qualified     # 🤕 E1.0 face with head-bandage
1F922                                      ; fully-qualified     # 🤢 E3.0 nauseated face
1F92E                                      ; fully-qualified     # 🤮 E5.0 face vomiting
1F927                                      ; fully-qualified     # 🤧 E3.0 sneezing face
1F975                                      ; fully-qualified     # 🥵 E11.0 hot face
1F976                                      ; fully-qualified     # 🥶 E11.0 cold face
1F974                                      ; fully-qualified     # 🥴 E11.0 woozy face
1F635                                      ; fully-qualified     # 😵 E0.6 dizzy face
1F92F                                      ; fully-qualified     # 🤯 E5.0 exploding head

# subgroup: face-hat
1F920                                      ; fully-qualified     # 🤠 E3.0 cowboy hat face
1F973                                      ; fully-qualified     # 🥳 E11.0 partying face
1F978                                      ; fully-qualified     # 🥸 E13.0 disguised face

# subgroup: face-glasses
1F60E                                      ; fully-qualified     # 😎 E1.0 smiling face with sunglasses
1F913                                      ; fully-qualified     # 🤓 E1.0 nerd face
1F9D0                                      ; fully-qualified     # 🧐 E5.0 face with monocle

# subgroup: face-concerned
1F615                                      ; fully-qualified     # 😕 E1.0 confused face
1F61F                                      ; fully-qualified     # 😟 E1.0 worried face
1F641                                      ; fully-qualified     # 🙁 E1.0 slightly frowning face
2639 FE0F                                  ; fully-qualified     # ☹️ E0.7 frowning face
2639                                       ; unqualified         # ☹ E0.7 frowning face
1F62E                                      ; fully-qualified     # 😮 E1.0 face with open mouth
1F62F                                      ; fully-qualified     # 😯 E1.0 hushed face
1F632                                      ; fully-qualified     # 😲 E0.6 astonished face
1F633                                      ; fully-qualified     # 😳 E0.6 flushed face
1F97A                                      ; fully-qualified     # 🥺 E11.0 pleading face
1F626                                      ; fully-qualified     # 😦 E1.0 frowning face with open mouth
1F627                                      ; fully-qualified     # 😧 E1.0 anguished face
1F628                                      ; fully-qualified     # 😨 E0.6 fearful face
1F630                                      ; fully-qualified     # 😰 E0.6 anxious face with sweat
1F625                                      ; fully-qualified     # 😥 E0.6 sad but relieved face
1F622                                      ; fully-qualified     # 😢 E0.6 crying face
1F62D                                      ; fully-qualified     # 😭 E0.6 loudly crying face
1F631                                      ; fully-qualified     # 😱 E0.6 face screaming in fear
1F616                                      ; fully-qualified     # 😖 E0.6 confounded face
1F623                                      ; fully-qualified     # 😣 E0.6 persevering face
1F61E                                      ; fully-qualified     # 😞 E0.6 disappointed face
1F613                                      ; fully-qualified     # 😓 E0.6 downcast face with sweat
1F629                                      ; fully-qualified     # 😩 E0.6 weary face
1F62B                                      ; fully-qualified     # 😫 E0.6 tired face
1F971                                      ; fully-qualified     # 🥱 E12.0 yawning face

# subgroup: face-negative
1F624                                      ; fully-qualified     # 😤 E0.6 face with steam from nose
1F621                                      ; fully-qualified     # 😡 E0.6 pouting face
1F620                                      ; fully-qualified     # 😠 E0.6 angry face
1F92C                                      ; fully-qualified     # 🤬 E5.0 face with symbols on mouth
1F608                                      ; fully-qualified     # 😈 E1.0 smiling face with horns
1F47F                                      ; fully-qualified     # 👿 E0.6 angry face with horns
1F480                                      ; fully-qualified     # 💀 E0.6 skull
2620 FE0F                                  ; fully-qualified     # ☠️ E1.0 skull and crossbones
2620                                       ; unqualified         # ☠ E1.0 skull and crossbones

# subgroup: face-costume
1F4A9                                      ; fully-qualified     # 💩 E0.6 pile of poo
1F921                                      ; fully-qualified     # 🤡 E3.0 clown face
1F479                                      ; fully-qualified     # 👹 E0.6 ogre
1F47A                                      ; fully-qualified     # 👺 E0.6 goblin
1F47B                                      ; fully-qualified     # 👻 E0.6 ghost
1F47D                                      ; fully-qualified     # 👽 E0.6 alien
1F47E                                      ; fully-qualified     # 👾 E0.6 alien monster
1F916                                      ; fully-qualified     # 🤖 E1.0 robot

# subgroup: cat-face
1F63A                                      ; fully-qualified     # 😺 E0.6 grinning cat
1F638                                      ; fully-qualified     # 😸 E0.6 grinning cat with smiling eyes
1F639                                      ; fully-qualified     # 😹 E0.6 cat with tears of joy
1F63B                                      ; fully-qualified     # 😻 E0.6 smiling cat with heart-eyes
1F63C                                      ; fully-qualified     # 😼 E0.6 cat with wry smile
1F63D                                      ; fully-qualified     # 😽 E0.6 kissing cat
1F640                                      ; fully-qualified     # 🙀 E0.6 weary cat
1F63F                                      ; fully-qualified     # 😿 E0.6 crying cat
1F63E                                      ; fully-qualified     # 😾 E0.6 pouting cat

# subgroup: monkey-face
1F648                                      ; fully-qualified     # 🙈 E0.6 see-no-evil monkey
1F649                                      ; fully-qualified     # 🙉 E0.6 hear-no-evil monkey
1F64A                                      ; fully-qualified     # 🙊 E0.6 speak-no-evil monkey

# subgroup: emotion
1F48B                                      ; fully-qualified     # 💋 E0.6 kiss mark
1F48C                                      ; fully-qualified     # 💌 E0.6 love letter
1F498                                      ; fully-qualified     # 💘 E0.6 heart with arrow
1F49D                                      ; fully-qualified     # 💝 E0.6 heart with ribbon
1F496                                      ; fully-qualified     # 💖 E0.6 sparkling heart
1F497                                      ; fully-qualified     # 💗 E0.6 growing heart
1F493                                      ; fully-qualified     # 💓 E0.6 beating heart
1F49E                                      ; fully-qualified     # 💞 E0.6 revolving hearts
1F495                                      ; fully-qualified     # 💕 E0.6 two hearts
1F49F                                      ; fully-qualified     # 💟 E0.6 heart decoration
2763 FE0F                                  ; fully-qualified     # ❣️ E1.0 heart exclamation
2763                                       ; unqualified         # ❣ E1.0 heart exclamation
1F494                                      ; fully-qualified     # 💔 E0.6 broken heart
2764 FE0F                                  ; fully-qualified     # ❤️ E0.6 red heart
2764                                       ; unqualified         # ❤ E0.6 red heart
1F9E1                                      ; fully-qualified     # 🧡 E5.0 orange heart
1F49B                                      ; fully-qualified     # 💛 E0.6 yellow heart
1F49A                                      ; fully-qualified     # 💚 E0.6 green heart
1F499                                      ; fully-qualified     # 💙 E0.6 blue heart
1F49C                                      ; fully-qualified     # 💜 E0.6 purple heart
1F90E                                      ; fully-qualified     # 🤎 E12.0 brown heart
1F5A4                                      ; fully-qualified     # 🖤 E3.0 black heart
1F90D                                      ; fully-qualified     # 🤍 E12.0 white heart
1F4AF                                      ; fully-qualified     # 💯 E0.6 hundred points
1F4A2                                      ; fully-qualified     # 💢 E0.6 anger symbol
1F4A5                                      ; fully-qualified     # 💥 E0.6 collision
1F4AB                                      ; fully-qualified     # 💫 E0.6 dizzy
1F4A6                                      ; fully-qualified     # 💦 E0.6 sweat droplets
1F4A8                                      ; fully-qualified     # 💨 E0.6 dashing away
1F573 FE0F                                 ; fully-qualified     # 🕳️ E0.7 hole
1F573                                      ; unqualified         # 🕳 E0.7 hole
1F4A3                                      ; fully-qualified     # 💣 E0.6 bomb
1F4AC                                      ; fully-qualified     # 💬 E0.6 speech balloon
1F441 FE0F 200D 1F5E8 FE0F                 ; fully-qualified     # 👁️‍🗨️ E2.0 eye in speech bubble
1F441 200D 1F5E8 FE0F                      ; unqualified         # 👁‍🗨️ E2.0 eye in speech bubble
1F441 FE0F 200D 1F5E8                      ; unqualified         # 👁️‍🗨 E2.0 eye in speech bubble
1F441 200D 1F5E8                           ; unqualified         # 👁‍🗨 E2.0 eye in speech bubble
1F5E8 FE0F                                 ; fully-qualified     # 🗨️ E2.0 left speech bubble
1F5E8                                      ; unqualified         # 🗨 E2.0 left speech bubble
1F5EF FE0F                                 ; fully-qualified     # 🗯️ E0.7 right anger bubble
1F5EF                                      ; unqualified         # 🗯 E0.7 right anger bubble
1F4AD                                      ; fully-qualified     # 💭 E1.0 thought balloon
1F4A4                                      ; fully-qualified     # 💤 E0.6 zzz

# Smileys & Emotion subtotal:		162
# Smileys & Emotion subtotal:		162	w/o modifiers

# group: People & Body

# subgroup: hand-fingers-open
1F44B                                      ; fully-qualified     # 👋 E0.6 waving hand
1F44B 1F3FB                                ; fully-qualified     # 👋🏻 E1.0 waving hand: light skin tone
1F44B 1F3FC                                ; fully-qualified     # 👋🏼 E1.0 waving hand: medium-light skin tone
1F44B 1F3FD                                ; fully-qualified     # 👋🏽 E1.0 waving hand: medium skin tone
1F44B 1F3FE                                ; fully-qualified     # 👋🏾 E1.0 waving hand: medium-dark skin tone
1F44B 1F3FF                                ; fully-qualified     # 👋🏿 E1.0 waving hand: dark skin tone
1F91A                                      ; fully-qualified     # 🤚 E3.0 raised back of hand
1F91A 1F3FB                                ; fully-qualified     # 🤚🏻 E3.0 raised back of hand: light skin tone
1F91A 1F3FC                                ; fully-qualified     # 🤚🏼 E3.0 raised back of hand: medium-light skin tone
1F91A 1F3FD                                ; fully-qualified     # 🤚🏽 E3.0 raised back of hand: medium skin tone
1F91A 1F3FE                                ; fully-qualified     # 🤚🏾 E3.0 raised back of hand: medium-dark skin tone
1F91A 1F3FF                                ; fully-qualified     # 🤚🏿 E3.0 raised back of hand: dark skin tone
1F590 FE0F                                 ; fully-qualified     # 🖐️ E0.7 hand with fingers splayed
1F590                                      ; unqualified         # 🖐 E0.7 hand with fingers splayed
1F590 1F3FB                                ; fully-qualified     # 🖐🏻 E1.0 hand with fingers splayed: light skin tone
1F590 1F3FC                                ; fully-qualified     # 🖐🏼 E1.0 hand with fingers splayed: medium-light skin tone
1F590 1F3FD                                ; fully-qualified     # 🖐🏽 E1.0 hand with fingers splayed: medium skin tone
1F590 1F3FE                                ; fully-qualified     # 🖐🏾 E1.0 hand with fingers splayed: medium-dark skin tone
1F590 1F3FF                                ; fully-qualified     # 🖐🏿 E1.0 hand with fingers splayed: dark skin tone
270B                                       ; fully-qualified     # ✋ E0.6 raised hand
270B 1F3FB                                 ; fully-qualified     # ✋🏻 E1.0 raised hand: light skin tone
270B 1F3FC                                 ; fully-qualified     # ✋🏼 E1.0 raised hand: medium-light skin tone
270B 1F3FD                                 ; fully-qualified     # ✋🏽 E1.0 raised hand: medium skin tone
270B 1F3FE                                 ; fully-qualified     # ✋🏾 E1.0 raised hand: medium-dark skin tone
270B 1F3FF                                 ; fully-qualified     # ✋🏿 E1.0 raised hand: dark skin tone
1F596                                      ; fully-qualified     # 🖖 E1.0 vulcan salute
1F596 1F3FB                                ; fully-qualified     # 🖖🏻 E1.0 vulcan salute: light skin tone
1F596 1F3FC                                ; fully-qualified     # 🖖🏼 E1.0 vulcan salute: medium-light skin tone
1F596 1F3FD                                ; fully-qualified     # 🖖🏽 E1.0 vulcan salute: medium skin tone
1F596 1F3FE                                ; fully-qualified     # 🖖🏾 E1.0 vulcan salute: medium-dark skin tone
1F596 1F3FF                                ; fully-qualified     # 🖖🏿 E1.0 vulcan salute: dark skin tone

# subgroup: hand-fingers-partial
1F44C                                      ; fully-qualified     # 👌 E0.6 OK hand
1F44C 1F3FB                                ; fully-qualified     # 👌🏻 E1.0 OK hand: light skin tone
1F44C 1F3FC                                ; fully-qualified     # 👌🏼 E1.0 OK hand: medium-light skin tone
1F44C 1F3FD                                ; fully-qualified     # 👌🏽 E1.0 OK hand: medium skin tone
1F44C 1F3FE                                ; fully-qualified     # 👌🏾 E1.0 OK hand: medium-dark skin tone
1F44C 1F3FF                                ; fully-qualified     # 👌🏿 E1.0 OK hand: dark skin tone
1F90C                                      ; fully-qualified     # 🤌 E13.0 pinched fingers
1F90C 1F3FB                                ; fully-qualified     # 🤌🏻 E13.0 pinched fingers: light skin tone
1F90C 1F3FC                                ; fully-qualified     # 🤌🏼 E13.0 pinched fingers: medium-light skin tone
1F90C 1F3FD                                ; fully-qualified     # 🤌🏽 E13.0 pinched fingers: medium skin tone
1F90C 1F3FE                                ; fully-qualified     # 🤌🏾 E13.0 pinched fingers: medium-dark skin tone
1F90C 1F3FF                                ; fully-qualified     # 🤌🏿 E13.0 pinched fingers: dark skin tone
1F90F                                      ; fully-qualified     # 🤏 E12.0 pinching hand
1F90F 1F3FB                                ; fully-qualified     # 🤏🏻 E12.0 pinching hand: light skin tone
1F90F 1F3FC                                ; fully-qualified     # 🤏🏼 E12.0 pinching hand: medium-light skin tone
1F90F 1F3FD                                ; fully-qualified     # 🤏🏽 E12.0 pinching hand: medium skin tone
1F90F 1F3FE                                ; fully-qualified     # 🤏🏾 E12.0 pinching hand: medium-dark skin tone
1F90F 1F3FF                                ; fully-qualified     # 🤏🏿 E12.0 pinching hand: dark skin tone
270C FE0F                                  ; fully-qualified     # ✌️ E0.6 victory hand
270C                                       ; unqualified         # ✌ E0.6 victory hand
270C 1F3FB                                 ; fully-qualified     # ✌🏻 E1.0 victory hand: light skin tone
270C 1F3FC                                 ; fully-qualified     # ✌🏼 E1.0 victory hand: medium-light skin tone
270C 1F3FD                                 ; fully-qualified     # ✌🏽 E1.0 victory hand: medium skin tone
270C 1F3FE                                 ; fully-qualified     # ✌🏾 E1.0 victory hand: medium-dark skin tone
270C 1F3FF                                 ; fully-qualified     # ✌🏿 E1.0 victory hand: dark skin tone
1F91E                                      ; fully-qualified     # 🤞 E3.0 crossed fingers
1F91E 1F3FB                                ; fully-qualified     # 🤞🏻 E3.0 crossed fingers: light skin tone
1F91E 1F3FC                                ; fully-qualified     # 🤞🏼 E3.0 crossed fingers: medium-light skin tone
1F91E 1F3FD                                ; fully-qualified     # 🤞🏽 E3.0 crossed fingers: medium skin tone
1F91E 1F3FE                                ; fully-qualified     # 🤞🏾 E3.0 crossed fingers: medium-dark skin tone
1F91E 1F3FF                                ; fully-qualified     # 🤞🏿 E3.0 crossed fingers: dark skin tone
1F91F                                      ; fully-qualified     # 🤟 E5.0 love-you gesture
1F91F 1F3FB                                ; fully-qualified     # 🤟🏻 E5.0 love-you gesture: light skin tone
1F91F 1F3FC                                ; fully-qualified     # 🤟🏼 E5.0 love-you gesture: medium-light skin tone
1F91F 1F3FD                                ; fully-qualified     # 🤟🏽 E5.0 love-you gesture: medium skin tone
1F91F 1F3FE                                ; fully-qualified     # 🤟🏾 E5.0 love-you gesture: medium-dark skin tone
1F91F 1F3FF                                ; fully-qualified     # 🤟🏿 E5.0 love-you gesture: dark skin tone
1F918                                      ; fully-qualified     # 🤘 E1.0 sign of the horns
1F918 1F3FB                                ; fully-qualified     # 🤘🏻 E1.0 sign of the horns: light skin tone
1F918 1F3FC                                ; fully-qualified     # 🤘🏼 E1.0 sign of the horns: medium-light skin tone
1F918 1F3FD                                ; fully-qualified     # 🤘🏽 E1.0 sign of the horns: medium skin tone
1F918 1F3FE                                ; fully-qualified     # 🤘🏾 E1.0 sign of the horns: medium-dark skin tone
1F918 1F3FF                                ; fully-qualified     # 🤘🏿 E1.0 sign of the horns: dark skin tone
1F919                                      ; fully-qualified     # 🤙 E3.0 call me hand
1F919 1F3FB                                ; fully-qualified     # 🤙🏻 E3.0 call me hand: light skin tone
1F919 1F3FC                                ; fully-qualified     # 🤙🏼 E3.0 call me hand: medium-light skin tone
1F919 1F3FD                                ; fully-qualified     # 🤙🏽 E3.0 call me hand: medium skin tone
1F919 1F3FE                                ; fully-qualified     # 🤙🏾 E3.0 call me hand: medium-dark skin tone
1F919 1F3FF                                ; fully-qualified     # 🤙🏿 E3.0 call me hand: dark skin tone

# subgroup: hand-single-finger
1F448                                      ; fully-qualified     # 👈 E0.6 backhand index pointing left
1F448 1F3FB                                ; fully-qualified     # 👈🏻 E1.0 backhand index pointing left: light skin tone
1F448 1F3FC                                ; fully-qualified     # 👈🏼 E1.0 backhand index pointing left: medium-light skin tone
1F448 1F3FD                                ; fully-qualified     # 👈🏽 E1.0 backhand index pointing left: medium skin tone
1F448 1F3FE                                ; fully-qualified     # 👈🏾 E1.0 backhand index pointing left: medium-dark skin tone
1F448 1F3FF                                ; fully-qualified     # 👈🏿 E1.0 backhand index pointing left: dark skin tone
1F449                                      ; fully-qualified     # 👉 E0.6 backhand index pointing right
1F449 1F3FB                                ; fully-qualified     # 👉🏻 E1.0 backhand index pointing right: light skin tone
1F449 1F3FC                                ; fully-qualified     # 👉🏼 E1.0 backhand index pointing right: medium-light skin tone
1F449 1F3FD                                ; fully-qualified     # 👉🏽 E1.0 backhand index pointing right: medium skin tone
1F449 1F3FE                                ; fully-qualified     # 👉🏾 E1.0 backhand index pointing right: medium-dark skin tone
1F449 1F3FF                                ; fully-qualified     # 👉🏿 E1.0 backhand index pointing right: dark skin tone
1F446                                      ; fully-qualified     # 👆 E0.6 backhand index pointing up
1F446 1F3FB                                ; fully-qualified     # 👆🏻 E1.0 backhand index pointing up: light skin tone
1F446 1F3FC                                ; fully-qualified     # 👆🏼 E1.0 backhand index pointing up: medium-light skin tone
1F446 1F3FD                                ; fully-qualified     # 👆🏽 E1.0 backhand index pointing up: medium skin tone
1F446 1F3FE                                ; fully-qualified     # 👆🏾 E1.0 backhand index pointing up: medium-dark skin tone
1F446 1F3FF                                ; fully-qualified     # 👆🏿 E1.0 backhand index pointing up: dark skin tone
1F595                                      ; fully-qualified     # 🖕 E1.0 middle finger
1F595 1F3FB                                ; fully-qualified     # 🖕🏻 E1.0 middle finger: light skin tone
1F595 1F3FC                                ; fully-qualified     # 🖕🏼 E1.0 middle finger: medium-light skin tone
1F595 1F3FD                                ; fully-qualified     # 🖕🏽 E1.0 middle finger: medium skin tone
1F595 1F3FE                                ; fully-qualified     # 🖕🏾 E1.0 middle finger: medium-dark skin tone
1F595 1F3FF                                ; fully-qualified     # 🖕🏿 E1.0 middle finger: dark skin tone
1F447                                      ; fully-qualified     # 👇 E0.6 backhand index pointing down
1F447 1F3FB                                ; fully-qualified     # 👇🏻 E1.0 backhand index pointing down: light skin tone
1F447 1F3FC                                ; fully-qualified     # 👇🏼 E1.0 backhand index pointing down: medium-light skin tone
1F447 1F3FD                                ; fully-qualified     # 👇🏽 E1.0 backhand index pointing down: medium skin tone
1F447 1F3FE                                ; fully-qualified     # 👇🏾 E1.0 backhand index pointing down: medium-dark skin tone
1F447 1F3FF                                ; fully-qualified     # 👇🏿 E1.0 backhand index pointing down: dark skin tone
261D FE0F                                  ; fully-qualified     # ☝️ E0.6 index pointing up
261D                                       ; unqualified         # ☝ E0.6 index pointing up
261D 1F3FB                                 ; fully-qualified     # ☝🏻 E1.0 index pointing up: light skin tone
261D 1F3FC                                 ; fully-qualified     # ☝🏼 E1.0 index pointing up: medium-light skin tone
261D 1F3FD                                 ; fully-qualified     # ☝🏽 E1.0 index pointing up: medium skin tone
261D 1F3FE                                 ; fully-qualified     # ☝🏾 E1.0 index pointing up: medium-dark skin tone
261D 1F3FF                                 ; fully-qualified     # ☝🏿 E1.0 index pointing up: dark skin tone

# subgroup: hand-fingers-closed
1F44D                                      ; fully-qualified     # 👍 E0.6 thumbs up
1F44D 1F3FB                                ; fully-qualified     # 👍🏻 E1.0 thumbs up: light skin tone
1F44D 1F3FC                                ; fully-qualified     # 👍🏼 E1.0 thumbs up: medium-light skin tone
1F44D 1F3FD                                ; fully-qualified     # 👍🏽 E1.0 thumbs up: medium skin tone
1F44D 1F3FE                                ; fully-qualified     # 👍🏾 E1.0 thumbs up: medium-dark skin tone
1F44D 1F3FF                                ; fully-qualified     # 👍🏿 E1.0 thumbs up: dark skin tone
1F44E                                      ; fully-qualified     # 👎 E0.6 thumbs down
1F44E 1F3FB                                ; fully-qualified     # 👎🏻 E1.0 thumbs down: light skin tone
1F44E 1F3FC                                ; fully-qualified     # 👎🏼 E1.0 thumbs down: medium-light skin tone
1F44E 1F3FD                                ; fully-qualified     # 👎🏽 E1.0 thumbs down: medium skin tone
1F44E 1F3FE                                ; fully-qualified     # 👎🏾 E1.0 thumbs down: medium-dark skin tone
1F44E 1F3FF                                ; fully-qualified     # 👎🏿 E1.0 thumbs down: dark skin tone
270A                                       ; fully-qualified     # ✊ E0.6 raised fist
270A 1F3FB                                 ; fully-qualified     # ✊🏻 E1.0 raised fist: light skin tone
270A 1F3FC                                 ; fully-qualified     # ✊🏼 E1.0 raised fist: medium-light skin tone
270A 1F3FD                                 ; fully-qualified     # ✊🏽 E1.0 raised fist: medium skin tone
270A 1F3FE                                 ; fully-qualified     # ✊🏾 E1.0 raised fist: medium-dark skin tone
270A 1F3FF                                 ; fully-qualified     # ✊🏿 E1.0 raised fist: dark skin tone
1F44A                                      ; fully-qualified     # 👊 E0.6 oncoming fist
1F44A 1F3FB                                ; fully-qualified     # 👊🏻 E1.0 oncoming fist: light skin tone
1F44A 1F3FC                                ; fully-qualified     # 👊🏼 E1.0 oncoming fist: medium-light skin tone
1F44A 1F3FD                                ; fully-qualified     # 👊🏽 E1.0 oncoming fist: medium skin tone
1F44A 1F3FE                                ; fully-qualified     # 👊🏾 E1.0 oncoming fist: medium-dark skin tone
1F44A 1F3FF                                ; fully-qualified     # 👊🏿 E1.0 oncoming fist: dark skin tone
1F91B                                      ; fully-qualified     # 🤛 E3.0 left-facing fist
1F91B 1F3FB                                ; fully-qualified     # 🤛🏻 E3.0 left-facing fist: light skin tone
1F91B 1F3FC                                ; fully-qualified     # 🤛🏼 E3.0 left-facing fist: medium-light skin tone
1F91B 1F3FD                                ; fully-qualified     # 🤛🏽 E3.0 left-facing fist: medium skin tone
1F91B 1F3FE                                ; fully-qualified     # 🤛🏾 E3.0 left-facing fist: medium-dark skin tone
1F91B 1F3FF                                ; fully-qualified     # 🤛🏿 E3.0 left-facing fist: dark skin tone
1F91C                                      ; fully-qualified     # 🤜 E3.0 right-facing fist
1F91C 1F3FB                                ; fully-qualified     # 🤜🏻 E3.0 right-facing fist: light skin tone
1F91C 1F3FC                                ; fully-qualified     # 🤜🏼 E3.0 right-facing fist: medium-light skin tone
1F91C 1F3FD                                ; fully-qualified     # 🤜🏽 E3.0 right-facing fist: medium skin tone
1F91C 1F3FE                                ; fully-qualified     # 🤜🏾 E3.0 right-facing fist: medium-dark skin tone
1F91C 1F3FF                                ; fully-qualified     # 🤜🏿 E3.0 right-facing fist: dark skin tone

# subgroup: hands
1F44F                                      ; fully-qualified     # 👏 E0.6 clapping hands
1F44F 1F3FB                                ; fully-qualified     # 👏🏻 E1.0 clapping hands: light skin tone
1F44F 1F3FC                                ; fully-qualified     # 👏🏼 E1.0 clapping hands: medium-light skin tone
1F44F 1F3FD                                ; fully-qualified     # 👏🏽 E1.0 clapping hands: medium skin tone
1F44F 1F3FE                                ; fully-qualified     # 👏🏾 E1.0 clapping hands: medium-dark skin tone
1F44F 1F3FF                                ; fully-qualified     # 👏🏿 E1.0 clapping hands: dark skin tone
1F64C                                      ; fully-qualified     # 🙌 E0.6 raising hands
1F64C 1F3FB                                ; fully-qualified     # 🙌🏻 E1.0 raising hands: light skin tone
1F64C 1F3FC                                ; fully-qualified     # 🙌🏼 E1.0 raising hands: medium-light skin tone
1F64C 1F3FD                                ; fully-qualified     # 🙌🏽 E1.0 raising hands: medium skin tone
1F64C 1F3FE                                ; fully-qualified     # 🙌🏾 E1.0 raising hands: medium-dark skin tone
1F64C 1F3FF                                ; fully-qualified     # 🙌🏿 E1.0 raising hands: dark skin tone
1F450                                      ; fully-qualified     # 👐 E0.6 open hands
1F450 1F3FB                                ; fully-qualified     # 👐🏻 E1.0 open hands: light skin tone
1F450 1F3FC                                ; fully-qualified     # 👐🏼 E1.0 open hands: medium-light skin tone
1F450 1F3FD                                ; fully-qualified     # 👐🏽 E1.0 open hands: medium skin tone
1F450 1F3FE                                ; fully-qualified     # 👐🏾 E1.0 open hands: medium-dark skin tone
1F450 1F3FF                                ; fully-qualified     # 👐🏿 E1.0 open hands: dark skin tone
1F932                                      ; fully-qualified     # 🤲 E5.0 palms up together
1F932 1F3FB                                ; fully-qualified     # 🤲🏻 E5.0 palms up together: light skin tone
1F932 1F3FC                                ; fully-qualified     # 🤲🏼 E5.0 palms up together: medium-light skin tone
1F932 1F3FD                                ; fully-qualified     # 🤲🏽 E5.0 palms up together: medium skin tone
1F932 1F3FE                                ; fully-qualified     # 🤲🏾 E5.0 palms up together: medium-dark skin tone
1F932 1F3FF                                ; fully-qualified     # 🤲🏿 E5.0 palms up together: dark skin tone
1F91D                                      ; fully-qualified     # 🤝 E3.0 handshake
1F64F                                      ; fully-qualified     # 🙏 E0.6 folded hands
1F64F 1F3FB                                ; fully-qualified     # 🙏🏻 E1.0 folded hands: light skin tone
1F64F 1F3FC                                ; fully-qualified     # 🙏🏼 E1.0 folded hands: medium-light skin tone
1F64F 1F3FD                                ; fully-qualified     # 🙏🏽 E1.0 folded hands: medium skin tone
1F64F 1F3FE                                ; fully-qualified     # 🙏🏾 E1.0 folded hands: medium-dark skin tone
1F64F 1F3FF                                ; fully-qualified     # 🙏🏿 E1.0 folded hands: dark skin tone

# subgroup: hand-prop
270D FE0F                                  ; fully-qualified     # ✍️ E0.7 writing hand
270D                                       ; unqualified         # ✍ E0.7 writing hand
270D 1F3FB                                 ; fully-qualified     # ✍🏻 E1.0 writing hand: light skin tone
270D 1F3FC                                 ; fully-qualified     # ✍🏼 E1.0 writing hand: medium-light skin tone
270D 1F3FD                                 ; fully-qualified     # ✍🏽 E1.0 writing hand: medium skin tone
270D 1F3FE                                 ; fully-qualified     # ✍🏾 E1.0 writing hand: medium-dark skin tone
270D 1F3FF                                 ; fully-qualified     # ✍🏿 E1.0 writing hand: dark skin tone
1F485                                      ; fully-qualified     # 💅 E0.6 nail polish
1F485 1F3FB                                ; fully-qualified     # 💅🏻 E1.0 nail polish: light skin tone
1F485 1F3FC                                ; fully-qualified     # 💅🏼 E1.0 nail polish: medium-light skin tone
1F485 1F3FD                                ; fully-qualified     # 💅🏽 E1.0 nail polish: medium skin tone
1F485 1F3FE                                ; fully-qualified     # 💅🏾 E1.0 nail polish: medium-dark skin tone
1F485 1F3FF                                ; fully-qualified     # 💅🏿 E1.0 nail polish: dark skin tone
1F933                                      ; fully-qualified     # 🤳 E3.0 selfie
1F933 1F3FB                                ; fully-qualified     # 🤳🏻 E3.0 selfie: light skin tone
1F933 1F3FC                                ; fully-qualified     # 🤳🏼 E3.0 selfie: medium-light skin tone
1F933 1F3FD                                ; fully-qualified     # 🤳🏽 E3.0 selfie: medium skin tone
1F933 1F3FE                                ; fully-qualified     # 🤳🏾 E3.0 selfie: medium-dark skin tone
1F933 1F3FF                                ; fully-qualified     # 🤳🏿 E3.0 selfie: dark skin tone

# subgroup: body-parts
1F4AA                                      ; fully-qualified     # 💪 E0.6 flexed biceps
1F4AA 1F3FB                                ; fully-qualified     # 💪🏻 E1.0 flexed biceps: light skin tone
1F4AA 1F3FC                                ; fully-qualified     # 💪🏼 E1.0 flexed biceps: medium-light skin tone
1F4AA 1F3FD                                ; fully-qualified     # 💪🏽 E1.0 flexed biceps: medium skin tone
1F4AA 1F3FE                                ; fully-qualified     # 💪🏾 E1.0 flexed biceps: medium-dark skin tone
1F4AA 1F3FF                                ; fully-qualified     # 💪🏿 E1.0 flexed biceps: dark skin tone
1F9BE                                      ; fully-qualified     # 🦾 E12.0 mechanical arm
1F9BF                                      ; fully-qualified     # 🦿 E12.0 mechanical leg
1F9B5                                      ; fully-qualified     # 🦵 E11.0 leg
1F9B5 1F3FB                                ; fully-qualified     # 🦵🏻 E11.0 leg: light skin tone
1F9B5 1F3FC                                ; fully-qualified     # 🦵🏼 E11.0 leg: medium-light skin tone
1F9B5 1F3FD                                ; fully-qualified     # 🦵🏽 E11.0 leg: medium skin tone
1F9B5 1F3FE                                ; fully-qualified     # 🦵🏾 E11.0 leg: medium-dark skin tone
1F9B5 1F3FF                                ; fully-qualified     # 🦵🏿 E11.0 leg: dark skin tone
1F9B6                                      ; fully-qualified     # 🦶 E11.0 foot
1F9B6 1F3FB                                ; fully-qualified     # 🦶🏻 E11.0 foot: light skin tone
1F9B6 1F3FC                                ; fully-qualified     # 🦶🏼 E11.0 foot: medium-light skin tone
1F9B6 1F3FD                                ; fully-qualified     # 🦶🏽 E11.0 foot: medium skin tone
1F9B6 1F3FE                                ; fully-qualified     # 🦶🏾 E11.0 foot: medium-dark skin tone
1F9B6 1F3FF                                ; fully-qualified     # 🦶🏿 E11.0 foot: dark skin tone
1F442                                      ; fully-qualified     # 👂 E0.6 ear
1F442 1F3FB                                ; fully-qualified     # 👂🏻 E1.0 ear: light skin tone
1F442 1F3FC                                ; fully-qualified     # 👂🏼 E1.0 ear: medium-light skin tone
1F442 1F3FD                                ; fully-qualified     # 👂🏽 E1.0 ear: medium skin tone
1F442 1F3FE                                ; fully-qualified     # 👂🏾 E1.0 ear: medium-dark skin tone
1F442 1F3FF                                ; fully-qualified     # 👂🏿 E1.0 ear: dark skin tone
1F9BB                                      ; fully-qualified     # 🦻 E12.0 ear with hearing aid
1F9BB 1F3FB                                ; fully-qualified     # 🦻🏻 E12.0 ear with hearing aid: light skin tone
1F9BB 1F3FC                                ; fully-qualified     # 🦻🏼 E12.0 ear with hearing aid: medium-light skin tone
1F9BB 1F3FD                                ; fully-qualified     # 🦻🏽 E12.0 ear with hearing aid: medium skin tone
1F9BB 1F3FE                                ; fully-qualified     # 🦻🏾 E12.0 ear with hearing aid: medium-dark skin tone
1F9BB 1F3FF                                ; fully-qualified     # 🦻🏿 E12.0 ear with hearing aid: dark skin tone
1F443                                      ; fully-qualified     # 👃 E0.6 nose
1F443 1F3FB                                ; fully-qualified     # 👃🏻 E1.0 nose: light skin tone
1F443 1F3FC                                ; fully-qualified     # 👃🏼 E1.0 nose: medium-light skin tone
1F443 1F3FD                                ; fully-qualified     # 👃🏽 E1.0 nose: medium skin tone
1F443 1F3FE                                ; fully-qualified     # 👃🏾 E1.0 nose: medium-dark skin tone
1F443 1F3FF                                ; fully-qualified     # 👃🏿 E1.0 nose: dark skin tone
1F9E0                                      ; fully-qualified     # 🧠 E5.0 brain
1FAC0                                      ; fully-qualified     # 🫀 E13.0 anatomical heart
1FAC1                                      ; fully-qualified     # 🫁 E13.0 lungs
1F9B7                                      ; fully-qualified     # 🦷 E11.0 tooth
1F9B4                                      ; fully-qualified     # 🦴 E11.0 bone
1F440                                      ; fully-qualified     # 👀 E0.6 eyes
1F441 FE0F                                 ; fully-qualified     # 👁️ E0.7 eye
1F441                                      ; unqualified         # 👁 E0.7 eye
1F445                                      ; fully-qualified     # 👅 E0.6 tongue
1F444                                      ; fully-qualified     # 👄 E0.6 mouth

# subgroup: person
1F476                                      ; fully-qualified     # 👶 E0.6 baby
1F476 1F3FB                                ; fully-qualified     # 👶🏻 E1.0 baby: light skin tone
1F476 1F3FC                                ; fully-qualified     # 👶🏼 E1.0 baby: medium-light skin tone
1F476 1F3FD                                ; fully-qualified     # 👶🏽 E1.0 baby: medium skin tone
1F476 1F3FE                                ; fully-qualified     # 👶🏾 E1.0 baby: medium-dark skin tone
1F476 1F3FF                                ; fully-qualified     # 👶🏿 E1.0 baby: dark skin tone
1F9D2                                      ; fully-qualified     # 🧒 E5.0 child
1F9D2 1F3FB                                ; fully-qualified     # 🧒🏻 E5.0 child: light skin tone
1F9D2 1F3FC                                ; fully-qualified     # 🧒🏼 E5.0 child: medium-light skin tone
1F9D2 1F3FD                                ; fully-qualified     # 🧒🏽 E5.0 child: medium skin tone
1F9D2 1F3FE                                ; fully-qualified     # 🧒🏾 E5.0 child: medium-dark skin tone
1F9D2 1F3FF                                ; fully-qualified     # 🧒🏿 E5.0 child: dark skin tone
1F466                                      ; fully-qualified     # 👦 E0.6 boy
1F466 1F3FB                                ; fully-qualified     # 👦🏻 E1.0 boy: light skin tone
1F466 1F3FC                                ; fully-qualified     # 👦🏼 E1.0 boy: medium-light skin tone
1F466 1F3FD                                ; fully-qualified     # 👦🏽 E1.0 boy: medium skin tone
1F466 1F3FE                                ; fully-qualified     # 👦🏾 E1.0 boy: medium-dark skin tone
1F466 1F3FF                                ; fully-qualified     # 👦🏿 E1.0 boy: dark skin tone
1F467                                      ; fully-qualified     # 👧 E0.6 girl
1F467 1F3FB                                ; fully-qualified     # 👧🏻 E1.0 girl: light skin tone
1F467 1F3FC                                ; fully-qualified     # 👧🏼 E1.0 girl: medium-light skin tone
1F467 1F3FD                                ; fully-qualified     # 👧🏽 E1.0 girl: medium skin tone
1F467 1F3FE                                ; fully-qualified     # 👧🏾 E1.0 girl: medium-dark skin tone
1F467 1F3FF                                ; fully-qualified     # 👧🏿 E1.0 girl: dark skin tone
1F9D1                                      ; fully-qualified     # 🧑 E5.0 person
1F9D1 1F3FB                                ; fully-qualified     # 🧑🏻 E5.0 person: light skin tone
1F9D1 1F3FC                                ; fully-qualified     # 🧑🏼 E5.0 person: medium-light skin tone
1F9D1 1F3FD                                ; fully-qualified     # 🧑🏽 E5.0 person: medium skin tone
1F9D1 1F3FE                                ; fully-qualified     # 🧑🏾 E5.0 person: medium-dark skin tone
1F9D1 1F3FF                                ; fully-qualified     # 🧑🏿 E5.0 person: dark skin tone
1F471                                      ; fully-qualified     # 👱 E0.6 person: blond hair
1F471 1F3FB                                ; fully-qualified     # 👱🏻 E1.0 person: light skin tone, blond hair
1F471 1F3FC                                ; fully-qualified     # 👱🏼 E1.0 person: medium-light skin tone, blond hair
1F471 1F3FD                                ; fully-qualified     # 👱🏽 E1.0 person: medium skin tone, blond hair
1F471 1F3FE                                ; fully-qualified     # 👱🏾 E1.0 person: medium-dark skin tone, blond hair
1F471 1F3FF                                ; fully-qualified     # 👱🏿 E1.0 person: dark skin tone, blond hair
1F468                                      ; fully-qualified     # 👨 E0.6 man
1F468 1F3FB                                ; fully-qualified     # 👨🏻 E1.0 man: light skin tone
1F468 1F3FC                                ; fully-qualified     # 👨🏼 E1.0 man: medium-light skin tone
1F468 1F3FD                                ; fully-qualified     # 👨🏽 E1.0 man: medium skin tone
1F468 1F3FE                                ; fully-qualified     # 👨🏾 E1.0 man: medium-dark skin tone
1F468 1F3FF                                ; fully-qualified     # 👨🏿 E1.0 man: dark skin tone
1F9D4                                      ; fully-qualified     # 🧔 E5.0 man: beard
1F9D4 1F3FB                                ; fully-qualified     # 🧔🏻 E5.0 man: light skin tone, beard
1F9D4 1F3FC                                ; fully-qualified     # 🧔🏼 E5.0 man: medium-light skin tone, beard
1F9D4 1F3FD                                ; fully-qualified     # 🧔🏽 E5.0 man: medium skin tone, beard
1F9D4 1F3FE                                ; fully-qualified     # 🧔🏾 E5.0 man: medium-dark skin tone, beard
1F9D4 1F3FF                                ; fully-qualified     # 🧔🏿 E5.0 man: dark skin tone, beard
1F468 200D 1F9B0                           ; fully-qualified     # 👨‍🦰 E11.0 man: red hair
1F468 1F3FB 200D 1F9B0                     ; fully-qualified     # 👨🏻‍🦰 E11.0 man: light skin tone, red hair
1F468 1F3FC 200D 1F9B0                     ; fully-qualified     # 👨🏼‍🦰 E11.0 man: medium-light skin tone, red hair
1F468 1F3FD 200D 1F9B0                     ; fully-qualified     # 👨🏽‍🦰 E11.0 man: medium skin tone, red hair
1F468 1F3FE 200D 1F9B0                     ; fully-qualified     # 👨🏾‍🦰 E11.0 man: medium-dark skin tone, red hair
1F468 1F3FF 200D 1F9B0                     ; fully-qualified     # 👨🏿‍🦰 E11.0 man: dark skin tone, red hair
1F468 200D 1F9B1                           ; fully-qualified     # 👨‍🦱 E11.0 man: curly hair
1F468 1F3FB 200D 1F9B1                     ; fully-qualified     # 👨🏻‍🦱 E11.0 man: light skin tone, curly hair
1F468 1F3FC 200D 1F9B1                     ; fully-qualified     # 👨🏼‍🦱 E11.0 man: medium-light skin tone, curly hair
1F468 1F3FD 200D 1F9B1                     ; fully-qualified     # 👨🏽‍🦱 E11.0 man: medium skin tone, curly hair
1F468 1F3FE 200D 1F9B1                     ; fully-qualified     # 👨🏾‍🦱 E11.0 man: medium-dark skin tone, curly hair
1F468 1F3FF 200D 1F9B1                     ; fully-qualified     # 👨🏿‍🦱 E11.0 man: dark skin tone, curly hair
1F468 200D 1F9B3                           ; fully-qualified     # 👨‍🦳 E11.0 man: white hair
1F468 1F3FB 200D 1F9B3                     ; fully-qualified     # 👨🏻‍🦳 E11.0 man: light skin tone, white hair
1F468 1F3FC 200D 1F9B3                     ; fully-qualified     # 👨🏼‍🦳 E11.0 man: medium-light skin tone, white hair
1F468 1F3FD 200D 1F9B3                     ; fully-qualified     # 👨🏽‍🦳 E11.0 man: medium skin tone, white hair
1F468 1F3FE 200D 1F9B3                     ; fully-qualified     # 👨🏾‍🦳 E11.0 man: medium-dark skin tone, white hair
1F468 1F3FF 200D 1F9B3                     ; fully-qualified     # 👨🏿‍🦳 E11.0 man: dark skin tone, white hair
1F468 200D 1F9B2                           ; fully-qualified     # 👨‍🦲 E11.0 man: bald
1F468 1F3FB 200D 1F9B2                     ; fully-qualified     # 👨🏻‍🦲 E11.0 man: light skin tone, bald
1F468 1F3FC 200D 1F9B2                     ; fully-qualified     # 👨🏼‍🦲 E11.0 man: medium-light skin tone, bald
1F468 1F3FD 200D 1F9B2                     ; fully-qualified     # 👨🏽‍🦲 E11.0 man: medium skin tone, bald
1F468 1F3FE 200D 1F9B2                     ; fully-qualified     # 👨🏾‍🦲 E11.0 man: medium-dark skin tone, bald
1F468 1F3FF 200D 1F9B2                     ; fully-qualified     # 👨🏿‍🦲 E11.0 man: dark skin tone, bald
1F469                                      ; fully-qualified     # 👩 E0.6 woman
1F469 1F3FB                                ; fully-qualified     # 👩🏻 E1.0 woman: light skin tone
1F469 1F3FC                                ; fully-qualified     # 👩🏼 E1.0 woman: medium-light skin tone
1F469 1F3FD                                ; fully-qualified     # 👩🏽 E1.0 woman: medium skin tone
1F469 1F3FE                                ; fully-qualified     # 👩🏾 E1.0 woman: medium-dark skin tone
1F469 1F3FF                                ; fully-qualified     # 👩🏿 E1.0 woman: dark skin tone
1F469 200D 1F9B0                           ; fully-qualified     # 👩‍🦰 E11.0 woman: red hair
1F469 1F3FB 200D 1F9B0                     ; fully-qualified     # 👩🏻‍🦰 E11.0 woman: light skin tone, red hair
1F469 1F3FC 200D 1F9B0                     ; fully-qualified     # 👩🏼‍🦰 E11.0 woman: medium-light skin tone, red hair
1F469 1F3FD 200D 1F9B0                     ; fully-qualified     # 👩🏽‍🦰 E11.0 woman: medium skin tone, red hair
1F469 1F3FE 200D 1F9B0                     ; fully-qualified     # 👩🏾‍🦰 E11.0 woman: medium-dark skin tone, red hair
1F469 1F3FF 200D 1F9B0                     ; fully-qualified     # 👩🏿‍🦰 E11.0 woman: dark skin tone, red hair
1F9D1 200D 1F9B0                           ; fully-qualified     # 🧑‍🦰 E12.1 person: red hair
1F9D1 1F3FB 200D 1F9B0                     ; fully-qualified     # 🧑🏻‍🦰 E12.1 person: light skin tone, red hair
1F9D1 1F3FC 200D 1F9B0                     ; fully-qualified     # 🧑🏼‍🦰 E12.1 person: medium-light skin tone, red hair
1F9D1 1F3FD 200D 1F9B0                     ; fully-qualified     # 🧑🏽‍🦰 E12.1 person: medium skin tone, red hair
1F9D1 1F3FE 200D 1F9B0                     ; fully-qualified     # 🧑🏾‍🦰 E12.1 person: medium-dark skin tone, red hair
1F9D1 1F3FF 200D 1F9B0                     ; fully-qualified     # 🧑🏿‍🦰 E12.1 person: dark skin tone, red hair
1F469 200D 1F9B1                           ; fully-qualified     # 👩‍🦱 E11.0 woman: curly hair
1F469 1F3FB 200D 1F9B1                     ; fully-qualified     # 👩🏻‍🦱 E11.0 woman: light skin tone, curly hair
1F469 1F3FC 200D 1F9B1                     ; fully-qualified     # 👩🏼‍🦱 E11.0 woman: medium-light skin tone, curly hair
1F469 1F3FD 200D 1F9B1                     ; fully-qualified     # 👩🏽‍🦱 E11.0 woman: medium skin tone, curly hair
1F469 1F3FE 200D 1F9B1                     ; fully-qualified     # 👩🏾‍🦱 E11.0 woman: medium-dark skin tone, curly hair
1F469 1F3FF 200D 1F9B1                     ; fully-qualified     # 👩🏿‍🦱 E11.0 woman: dark skin tone, curly hair
1F9D1 200D 1F9B1                           ; fully-qualified     # 🧑‍🦱 E12.1 person: curly hair
1F9D1 1F3FB 200D 1F9B1                     ; fully-qualified     # 🧑🏻‍🦱 E12.1 person: light skin tone, curly hair
1F9D1 1F3FC 200D 1F9B1                     ; fully-qualified     # 🧑🏼‍🦱 E12.1 person: medium-light skin tone, curly hair
1F9D1 1F3FD 200D 1F9B1                     ; fully-qualified     # 🧑🏽‍🦱 E12.1 person: medium skin tone, curly hair
1F9D1 1F3FE 200D 1F9B1                     ; fully-qualified     # 🧑🏾‍🦱 E12.1 person: medium-dark skin tone, curly hair
1F9D1 1F3FF 200D 1F9B1                     ; fully-qualified     # 🧑🏿‍🦱 E12.1 person: dark skin tone, curly hair
1F469 200D 1F9B3                           ; fully-qualified     # 👩‍🦳 E11.0 woman: white hair
1F469 1F3FB 200D 1F9B3                     ; fully-qualified     # 👩🏻‍🦳 E11.0 woman: light skin tone, white hair
1F469 1F3FC 200D 1F9B3                     ; fully-qualified     # 👩🏼‍🦳 E11.0 woman: medium-light skin tone, white hair
1F469 1F3FD 200D 1F9B3                     ; fully-qualified     # 👩🏽‍🦳 E11.0 woman: medium skin tone, white hair
1F469 1F3FE 200D 1F9B3                     ; fully-qualified     # 👩🏾‍🦳 E11.0 woman: medium-dark skin tone, white hair
1F469 1F3FF 200D 1F9B3                     ; fully-qualified     # 👩🏿‍🦳 E11.0 woman: dark skin tone, white hair
1F9D1 200D 1F9B3                           ; fully-qualified     # 🧑‍🦳 E12.1 person: white hair
1F9D1 1F3FB 200D 1F9B3                     ; fully-qualified     # 🧑🏻‍🦳 E12.1 person: light skin tone, white hair
1F9D1 1F3FC 200D 1F9B3                     ; fully-qualified     # 🧑🏼‍🦳 E12.1 person: medium-light skin tone, white hair
1F9D1 1F3FD 200D 1F9B3                     ; fully-qualified     # 🧑🏽‍🦳 E12.1 person: medium skin tone, white hair
1F9D1 1F3FE 200D 1F9B3                     ; fully-qualified     # 🧑🏾‍🦳 E12.1 person: medium-dark skin tone, white hair
1F9D1 1F3FF 200D 1F9B3                     ; fully-qualified     # 🧑🏿‍🦳 E12.1 person: dark skin tone, white hair
1F469 200D 1F9B2                           ; fully-qualified     # 👩‍🦲 E11.0 woman: bald
1F469 1F3FB 200D 1F9B2                     ; fully-qualified     # 👩🏻‍🦲 E11.0 woman: light skin tone, bald
1F469 1F3FC 200D 1F9B2                     ; fully-qualified     # 👩🏼‍🦲 E11.0 woman: medium-light skin tone, bald
1F469 1F3FD 200D 1F9B2                     ; fully-qualified     # 👩🏽‍🦲 E11.0 woman: medium skin tone, bald
1F469 1F3FE 200D 1F9B2                     ; fully-qualified     # 👩🏾‍🦲 E11.0 woman: medium-dark skin tone, bald
1F469 1F3FF 200D 1F9B2                     ; fully-qualified     # 👩🏿‍🦲 E11.0 woman: dark skin tone, bald
1F9D1 200D 1F9B2                           ; fully-qualified     # 🧑‍🦲 E12.1 person: bald
1F9D1 1F3FB 200D 1F9B2                     ; fully-qualified     # 🧑🏻‍🦲 E12.1 person: light skin tone, bald
1F9D1 1F3FC 200D 1F9B2                     ; fully-qualified     # 🧑🏼‍🦲 E12.1 person: medium-light skin tone, bald
1F9D1 1F3FD 200D 1F9B2                     ; fully-qualified     # 🧑🏽‍🦲 E12.1 person: medium skin tone, bald
1F9D1 1F3FE 200D 1F9B2                     ; fully-qualified     # 🧑🏾‍🦲 E12.1 person: medium-dark skin tone, bald
1F9D1 1F3FF 200D 1F9B2                     ; fully-qualified     # 🧑🏿‍🦲 E12.1 person: dark skin tone, bald
1F471 200D 2640 FE0F                       ; fully-qualified     # 👱‍♀️ E4.0 woman: blond hair
1F471 200D 2640                            ; minimally-qualified # 👱‍♀ E4.0 woman: blond hair
1F471 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 👱🏻‍♀️ E4.0 woman: light skin tone, blond hair
1F471 1F3FB 200D 2640                      ; minimally-qualified # 👱🏻‍♀ E4.0 woman: light skin tone, blond hair
1F471 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 👱🏼‍♀️ E4.0 woman: medium-light skin tone, blond hair
1F471 1F3FC 200D 2640                      ; minimally-qualified # 👱🏼‍♀ E4.0 woman: medium-light skin tone, blond hair
1F471 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 👱🏽‍♀️ E4.0 woman: medium skin tone, blond hair
1F471 1F3FD 200D 2640                      ; minimally-qualified # 👱🏽‍♀ E4.0 woman: medium skin tone, blond hair
1F471 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 👱🏾‍♀️ E4.0 woman: medium-dark skin tone, blond hair
1F471 1F3FE 200D 2640                      ; minimally-qualified # 👱🏾‍♀ E4.0 woman: medium-dark skin tone, blond hair
1F471 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 👱🏿‍♀️ E4.0 woman: dark skin tone, blond hair
1F471 1F3FF 200D 2640                      ; minimally-qualified # 👱🏿‍♀ E4.0 woman: dark skin tone, blond hair
1F471 200D 2642 FE0F                       ; fully-qualified     # 👱‍♂️ E4.0 man: blond hair
1F471 200D 2642                            ; minimally-qualified # 👱‍♂ E4.0 man: blond hair
1F471 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 👱🏻‍♂️ E4.0 man: light skin tone, blond hair
1F471 1F3FB 200D 2642                      ; minimally-qualified # 👱🏻‍♂ E4.0 man: light skin tone, blond hair
1F471 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 👱🏼‍♂️ E4.0 man: medium-light skin tone, blond hair
1F471 1F3FC 200D 2642                      ; minimally-qualified # 👱🏼‍♂ E4.0 man: medium-light skin tone, blond hair
1F471 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 👱🏽‍♂️ E4.0 man: medium skin tone, blond hair
1F471 1F3FD 200D 2642                      ; minimally-qualified # 👱🏽‍♂ E4.0 man: medium skin tone, blond hair
1F471 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 👱🏾‍♂️ E4.0 man: medium-dark skin tone, blond hair
1F471 1F3FE 200D 2642                      ; minimally-qualified # 👱🏾‍♂ E4.0 man: medium-dark skin tone, blond hair
1F471 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 👱🏿‍♂️ E4.0 man: dark skin tone, blond hair
1F471 1F3FF 200D 2642                      ; minimally-qualified # 👱🏿‍♂ E4.0 man: dark skin tone, blond hair
1F9D3                                      ; fully-qualified     # 🧓 E5.0 older person
1F9D3 1F3FB                                ; fully-qualified     # 🧓🏻 E5.0 older person: light skin tone
1F9D3 1F3FC                                ; fully-qualified     # 🧓🏼 E5.0 older person: medium-light skin tone
1F9D3 1F3FD                                ; fully-qualified     # 🧓🏽 E5.0 older person: medium skin tone
1F9D3 1F3FE                                ; fully-qualified     # 🧓🏾 E5.0 older person: medium-dark skin tone
1F9D3 1F3FF                                ; fully-qualified     # 🧓🏿 E5.0 older person: dark skin tone
1F474                                      ; fully-qualified     # 👴 E0.6 old man
1F474 1F3FB                                ; fully-qualified     # 👴🏻 E1.0 old man: light skin tone
1F474 1F3FC                                ; fully-qualified     # 👴🏼 E1.0 old man: medium-light skin tone
1F474 1F3FD                                ; fully-qualified     # 👴🏽 E1.0 old man: medium skin tone
1F474 1F3FE                                ; fully-qualified     # 👴🏾 E1.0 old man: medium-dark skin tone
1F474 1F3FF                                ; fully-qualified     # 👴🏿 E1.0 old man: dark skin tone
1F475                                      ; fully-qualified     # 👵 E0.6 old woman
1F475 1F3FB                                ; fully-qualified     # 👵🏻 E1.0 old woman: light skin tone
1F475 1F3FC                                ; fully-qualified     # 👵🏼 E1.0 old woman: medium-light skin tone
1F475 1F3FD                                ; fully-qualified     # 👵🏽 E1.0 old woman: medium skin tone
1F475 1F3FE                                ; fully-qualified     # 👵🏾 E1.0 old woman: medium-dark skin tone
1F475 1F3FF                                ; fully-qualified     # 👵🏿 E1.0 old woman: dark skin tone

# subgroup: person-gesture
1F64D                                      ; fully-qualified     # 🙍 E0.6 person frowning
1F64D 1F3FB                                ; fully-qualified     # 🙍🏻 E1.0 person frowning: light skin tone
1F64D 1F3FC                                ; fully-qualified     # 🙍🏼 E1.0 person frowning: medium-light skin tone
1F64D 1F3FD                                ; fully-qualified     # 🙍🏽 E1.0 person frowning: medium skin tone
1F64D 1F3FE                                ; fully-qualified     # 🙍🏾 E1.0 person frowning: medium-dark skin tone
1F64D 1F3FF                                ; fully-qualified     # 🙍🏿 E1.0 person frowning: dark skin tone
1F64D 200D 2642 FE0F                       ; fully-qualified     # 🙍‍♂️ E4.0 man frowning
1F64D 200D 2642                            ; minimally-qualified # 🙍‍♂ E4.0 man frowning
1F64D 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🙍🏻‍♂️ E4.0 man frowning: light skin tone
1F64D 1F3FB 200D 2642                      ; minimally-qualified # 🙍🏻‍♂ E4.0 man frowning: light skin tone
1F64D 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🙍🏼‍♂️ E4.0 man frowning: medium-light skin tone
1F64D 1F3FC 200D 2642                      ; minimally-qualified # 🙍🏼‍♂ E4.0 man frowning: medium-light skin tone
1F64D 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🙍🏽‍♂️ E4.0 man frowning: medium skin tone
1F64D 1F3FD 200D 2642                      ; minimally-qualified # 🙍🏽‍♂ E4.0 man frowning: medium skin tone
1F64D 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🙍🏾‍♂️ E4.0 man frowning: medium-dark skin tone
1F64D 1F3FE 200D 2642                      ; minimally-qualified # 🙍🏾‍♂ E4.0 man frowning: medium-dark skin tone
1F64D 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🙍🏿‍♂️ E4.0 man frowning: dark skin tone
1F64D 1F3FF 200D 2642                      ; minimally-qualified # 🙍🏿‍♂ E4.0 man frowning: dark skin tone
1F64D 200D 2640 FE0F                       ; fully-qualified     # 🙍‍♀️ E4.0 woman frowning
1F64D 200D 2640                            ; minimally-qualified # 🙍‍♀ E4.0 woman frowning
1F64D 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🙍🏻‍♀️ E4.0 woman frowning: light skin tone
1F64D 1F3FB 200D 2640                      ; minimally-qualified # 🙍🏻‍♀ E4.0 woman frowning: light skin tone
1F64D 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🙍🏼‍♀️ E4.0 woman frowning: medium-light skin tone
1F64D 1F3FC 200D 2640                      ; minimally-qualified # 🙍🏼‍♀ E4.0 woman frowning: medium-light skin tone
1F64D 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🙍🏽‍♀️ E4.0 woman frowning: medium skin tone
1F64D 1F3FD 200D 2640                      ; minimally-qualified # 🙍🏽‍♀ E4.0 woman frowning: medium skin tone
1F64D 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🙍🏾‍♀️ E4.0 woman frowning: medium-dark skin tone
1F64D 1F3FE 200D 2640                      ; minimally-qualified # 🙍🏾‍♀ E4.0 woman frowning: medium-dark skin tone
1F64D 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🙍🏿‍♀️ E4.0 woman frowning: dark skin tone
1F64D 1F3FF 200D 2640                      ; minimally-qualified # 🙍🏿‍♀ E4.0 woman frowning: dark skin tone
1F64E                                      ; fully-qualified     # 🙎 E0.6 person pouting
1F64E 1F3FB                                ; fully-qualified     # 🙎🏻 E1.0 person pouting: light skin tone
1F64E 1F3FC                                ; fully-qualified     # 🙎🏼 E1.0 person pouting: medium-light skin tone
1F64E 1F3FD                                ; fully-qualified     # 🙎🏽 E1.0 person pouting: medium skin tone
1F64E 1F3FE                                ; fully-qualified     # 🙎🏾 E1.0 person pouting: medium-dark skin tone
1F64E 1F3FF                                ; fully-qualified     # 🙎🏿 E1.0 person pouting: dark skin tone
1F64E 200D 2642 FE0F                       ; fully-qualified     # 🙎‍♂️ E4.0 man pouting
1F64E 200D 2642                            ; minimally-qualified # 🙎‍♂ E4.0 man pouting
1F64E 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🙎🏻‍♂️ E4.0 man pouting: light skin tone
1F64E 1F3FB 200D 2642                      ; minimally-qualified # 🙎🏻‍♂ E4.0 man pouting: light skin tone
1F64E 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🙎🏼‍♂️ E4.0 man pouting: medium-light skin tone
1F64E 1F3FC 200D 2642                      ; minimally-qualified # 🙎🏼‍♂ E4.0 man pouting: medium-light skin tone
1F64E 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🙎🏽‍♂️ E4.0 man pouting: medium skin tone
1F64E 1F3FD 200D 2642                      ; minimally-qualified # 🙎🏽‍♂ E4.0 man pouting: medium skin tone
1F64E 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🙎🏾‍♂️ E4.0 man pouting: medium-dark skin tone
1F64E 1F3FE 200D 2642                      ; minimally-qualified # 🙎🏾‍♂ E4.0 man pouting: medium-dark skin tone
1F64E 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🙎🏿‍♂️ E4.0 man pouting: dark skin tone
1F64E 1F3FF 200D 2642                      ; minimally-qualified # 🙎🏿‍♂ E4.0 man pouting: dark skin tone
1F64E 200D 2640 FE0F                       ; fully-qualified     # 🙎‍♀️ E4.0 woman pouting
1F64E 200D 2640                            ; minimally-qualified # 🙎‍♀ E4.0 woman pouting
1F64E 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🙎🏻‍♀️ E4.0 woman pouting: light skin tone
1F64E 1F3FB 200D 2640                      ; minimally-qualified # 🙎🏻‍♀ E4.0 woman pouting: light skin tone
1F64E 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🙎🏼‍♀️ E4.0 woman pouting: medium-light skin tone
1F64E 1F3FC 200D 2640                      ; minimally-qualified # 🙎🏼‍♀ E4.0 woman pouting: medium-light skin tone
1F64E 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🙎🏽‍♀️ E4.0 woman pouting: medium skin tone
1F64E 1F3FD 200D 2640                      ; minimally-qualified # 🙎🏽‍♀ E4.0 woman pouting: medium skin tone
1F64E 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🙎🏾‍♀️ E4.0 woman pouting: medium-dark skin tone
1F64E 1F3FE 200D 2640                      ; minimally-qualified # 🙎🏾‍♀ E4.0 woman pouting: medium-dark skin tone
1F64E 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🙎🏿‍♀️ E4.0 woman pouting: dark skin tone
1F64E 1F3FF 200D 2640                      ; minimally-qualified # 🙎🏿‍♀ E4.0 woman pouting: dark skin tone
1F645                                      ; fully-qualified     # 🙅 E0.6 person gesturing NO
1F645 1F3FB                                ; fully-qualified     # 🙅🏻 E1.0 person gesturing NO: light skin tone
1F645 1F3FC                                ; fully-qualified     # 🙅🏼 E1.0 person gesturing NO: medium-light skin tone
1F645 1F3FD                                ; fully-qualified     # 🙅🏽 E1.0 person gesturing NO: medium skin tone
1F645 1F3FE                                ; fully-qualified     # 🙅🏾 E1.0 person gesturing NO: medium-dark skin tone
1F645 1F3FF                                ; fully-qualified     # 🙅🏿 E1.0 person gesturing NO: dark skin tone
1F645 200D 2642 FE0F                       ; fully-qualified     # 🙅‍♂️ E4.0 man gesturing NO
1F645 200D 2642                            ; minimally-qualified # 🙅‍♂ E4.0 man gesturing NO
1F645 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🙅🏻‍♂️ E4.0 man gesturing NO: light skin tone
1F645 1F3FB 200D 2642                      ; minimally-qualified # 🙅🏻‍♂ E4.0 man gesturing NO: light skin tone
1F645 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🙅🏼‍♂️ E4.0 man gesturing NO: medium-light skin tone
1F645 1F3FC 200D 2642                      ; minimally-qualified # 🙅🏼‍♂ E4.0 man gesturing NO: medium-light skin tone
1F645 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🙅🏽‍♂️ E4.0 man gesturing NO: medium skin tone
1F645 1F3FD 200D 2642                      ; minimally-qualified # 🙅🏽‍♂ E4.0 man gesturing NO: medium skin tone
1F645 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🙅🏾‍♂️ E4.0 man gesturing NO: medium-dark skin tone
1F645 1F3FE 200D 2642                      ; minimally-qualified # 🙅🏾‍♂ E4.0 man gesturing NO: medium-dark skin tone
1F645 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🙅🏿‍♂️ E4.0 man gesturing NO: dark skin tone
1F645 1F3FF 200D 2642                      ; minimally-qualified # 🙅🏿‍♂ E4.0 man gesturing NO: dark skin tone
1F645 200D 2640 FE0F                       ; fully-qualified     # 🙅‍♀️ E4.0 woman gesturing NO
1F645 200D 2640                            ; minimally-qualified # 🙅‍♀ E4.0 woman gesturing NO
1F645 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🙅🏻‍♀️ E4.0 woman gesturing NO: light skin tone
1F645 1F3FB 200D 2640                      ; minimally-qualified # 🙅🏻‍♀ E4.0 woman gesturing NO: light skin tone
1F645 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🙅🏼‍♀️ E4.0 woman gesturing NO: medium-light skin tone
1F645 1F3FC 200D 2640                      ; minimally-qualified # 🙅🏼‍♀ E4.0 woman gesturing NO: medium-light skin tone
1F645 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🙅🏽‍♀️ E4.0 woman gesturing NO: medium skin tone
1F645 1F3FD 200D 2640                      ; minimally-qualified # 🙅🏽‍♀ E4.0 woman gesturing NO: medium skin tone
1F645 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🙅🏾‍♀️ E4.0 woman gesturing NO: medium-dark skin tone
1F645 1F3FE 200D 2640                      ; minimally-qualified # 🙅🏾‍♀ E4.0 woman gesturing NO: medium-dark skin tone
1F645 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🙅🏿‍♀️ E4.0 woman gesturing NO: dark skin tone
1F645 1F3FF 200D 2640                      ; minimally-qualified # 🙅🏿‍♀ E4.0 woman gesturing NO: dark skin tone
1F646                                      ; fully-qualified     # 🙆 E0.6 person gesturing OK
1F646 1F3FB                                ; fully-qualified     # 🙆🏻 E1.0 person gesturing OK: light skin tone
1F646 1F3FC                                ; fully-qualified     # 🙆🏼 E1.0 person gesturing OK: medium-light skin tone
1F646 1F3FD                                ; fully-qualified     # 🙆🏽 E1.0 person gesturing OK: medium skin tone
1F646 1F3FE                                ; fully-qualified     # 🙆🏾 E1.0 person gesturing OK: medium-dark skin tone
1F646 1F3FF                                ; fully-qualified     # 🙆🏿 E1.0 person gesturing OK: dark skin tone
1F646 200D 2642 FE0F                       ; fully-qualified     # 🙆‍♂️ E4.0 man gesturing OK
1F646 200D 2642                            ; minimally-qualified # 🙆‍♂ E4.0 man gesturing OK
1F646 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🙆🏻‍♂️ E4.0 man gesturing OK: light skin tone
1F646 1F3FB 200D 2642                      ; minimally-qualified # 🙆🏻‍♂ E4.0 man gesturing OK: light skin tone
1F646 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🙆🏼‍♂️ E4.0 man gesturing OK: medium-light skin tone
1F646 1F3FC 200D 2642                      ; minimally-qualified # 🙆🏼‍♂ E4.0 man gesturing OK: medium-light skin tone
1F646 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🙆🏽‍♂️ E4.0 man gesturing OK: medium skin tone
1F646 1F3FD 200D 2642                      ; minimally-qualified # 🙆🏽‍♂ E4.0 man gesturing OK: medium skin tone
1F646 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🙆🏾‍♂️ E4.0 man gesturing OK: medium-dark skin tone
1F646 1F3FE 200D 2642                      ; minimally-qualified # 🙆🏾‍♂ E4.0 man gesturing OK: medium-dark skin tone
1F646 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🙆🏿‍♂️ E4.0 man gesturing OK: dark skin tone
1F646 1F3FF 200D 2642                      ; minimally-qualified # 🙆🏿‍♂ E4.0 man gesturing OK: dark skin tone
1F646 200D 2640 FE0F                       ; fully-qualified     # 🙆‍♀️ E4.0 woman gesturing OK
1F646 200D 2640                            ; minimally-qualified # 🙆‍♀ E4.0 woman gesturing OK
1F646 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🙆🏻‍♀️ E4.0 woman gesturing OK: light skin tone
1F646 1F3FB 200D 2640                      ; minimally-qualified # 🙆🏻‍♀ E4.0 woman gesturing OK: light skin tone
1F646 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🙆🏼‍♀️ E4.0 woman gesturing OK: medium-light skin tone
1F646 1F3FC 200D 2640                      ; minimally-qualified # 🙆🏼‍♀ E4.0 woman gesturing OK: medium-light skin tone
1F646 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🙆🏽‍♀️ E4.0 woman gesturing OK: medium skin tone
1F646 1F3FD 200D 2640                      ; minimally-qualified # 🙆🏽‍♀ E4.0 woman gesturing OK: medium skin tone
1F646 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🙆🏾‍♀️ E4.0 woman gesturing OK: medium-dark skin tone
1F646 1F3FE 200D 2640                      ; minimally-qualified # 🙆🏾‍♀ E4.0 woman gesturing OK: medium-dark skin tone
1F646 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🙆🏿‍♀️ E4.0 woman gesturing OK: dark skin tone
1F646 1F3FF 200D 2640                      ; minimally-qualified # 🙆🏿‍♀ E4.0 woman gesturing OK: dark skin tone
1F481                                      ; fully-qualified     # 💁 E0.6 person tipping hand
1F481 1F3FB                                ; fully-qualified     # 💁🏻 E1.0 person tipping hand: light skin tone
1F481 1F3FC                                ; fully-qualified     # 💁🏼 E1.0 person tipping hand: medium-light skin tone
1F481 1F3FD                                ; fully-qualified     # 💁🏽 E1.0 person tipping hand: medium skin tone
1F481 1F3FE                                ; fully-qualified     # 💁🏾 E1.0 person tipping hand: medium-dark skin tone
1F481 1F3FF                                ; fully-qualified     # 💁🏿 E1.0 person tipping hand: dark skin tone
1F481 200D 2642 FE0F                       ; fully-qualified     # 💁‍♂️ E4.0 man tipping hand
1F481 200D 2642                            ; minimally-qualified # 💁‍♂ E4.0 man tipping hand
1F481 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 💁🏻‍♂️ E4.0 man tipping hand: light skin tone
1F481 1F3FB 200D 2642                      ; minimally-qualified # 💁🏻‍♂ E4.0 man tipping hand: light skin tone
1F481 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 💁🏼‍♂️ E4.0 man tipping hand: medium-light skin tone
1F481 1F3FC 200D 2642                      ; minimally-qualified # 💁🏼‍♂ E4.0 man tipping hand: medium-light skin tone
1F481 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 💁🏽‍♂️ E4.0 man tipping hand: medium skin tone
1F481 1F3FD 200D 2642                      ; minimally-qualified # 💁🏽‍♂ E4.0 man tipping hand: medium skin tone
1F481 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 💁🏾‍♂️ E4.0 man tipping hand: medium-dark skin tone
1F481 1F3FE 200D 2642                      ; minimally-qualified # 💁🏾‍♂ E4.0 man tipping hand: medium-dark skin tone
1F481 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 💁🏿‍♂️ E4.0 man tipping hand: dark skin tone
1F481 1F3FF 200D 2642                      ; minimally-qualified # 💁🏿‍♂ E4.0 man tipping hand: dark skin tone
1F481 200D 2640 FE0F                       ; fully-qualified     # 💁‍♀️ E4.0 woman tipping hand
1F481 200D 2640                            ; minimally-qualified # 💁‍♀ E4.0 woman tipping hand
1F481 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 💁🏻‍♀️ E4.0 woman tipping hand: light skin tone
1F481 1F3FB 200D 2640                      ; minimally-qualified # 💁🏻‍♀ E4.0 woman tipping hand: light skin tone
1F481 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 💁🏼‍♀️ E4.0 woman tipping hand: medium-light skin tone
1F481 1F3FC 200D 2640                      ; minimally-qualified # 💁🏼‍♀ E4.0 woman tipping hand: medium-light skin tone
1F481 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 💁🏽‍♀️ E4.0 woman tipping hand: medium skin tone
1F481 1F3FD 200D 2640                      ; minimally-qualified # 💁🏽‍♀ E4.0 woman tipping hand: medium skin tone
1F481 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 💁🏾‍♀️ E4.0 woman tipping hand: medium-dark skin tone
1F481 1F3FE 200D 2640                      ; minimally-qualified # 💁🏾‍♀ E4.0 woman tipping hand: medium-dark skin tone
1F481 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 💁🏿‍♀️ E4.0 woman tipping hand: dark skin tone
1F481 1F3FF 200D 2640                      ; minimally-qualified # 💁🏿‍♀ E4.0 woman tipping hand: dark skin tone
1F64B                                      ; fully-qualified     # 🙋 E0.6 person raising hand
1F64B 1F3FB                                ; fully-qualified     # 🙋🏻 E1.0 person raising hand: light skin tone
1F64B 1F3FC                                ; fully-qualified     # 🙋🏼 E1.0 person raising hand: medium-light skin tone
1F64B 1F3FD                                ; fully-qualified     # 🙋🏽 E1.0 person raising hand: medium skin tone
1F64B 1F3FE                                ; fully-qualified     # 🙋🏾 E1.0 person raising hand: medium-dark skin tone
1F64B 1F3FF                                ; fully-qualified     # 🙋🏿 E1.0 person raising hand: dark skin tone
1F64B 200D 2642 FE0F                       ; fully-qualified     # 🙋‍♂️ E4.0 man raising hand
1F64B 200D 2642                            ; minimally-qualified # 🙋‍♂ E4.0 man raising hand
1F64B 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🙋🏻‍♂️ E4.0 man raising hand: light skin tone
1F64B 1F3FB 200D 2642                      ; minimally-qualified # 🙋🏻‍♂ E4.0 man raising hand: light skin tone
1F64B 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🙋🏼‍♂️ E4.0 man raising hand: medium-light skin tone
1F64B 1F3FC 200D 2642                      ; minimally-qualified # 🙋🏼‍♂ E4.0 man raising hand: medium-light skin tone
1F64B 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🙋🏽‍♂️ E4.0 man raising hand: medium skin tone
1F64B 1F3FD 200D 2642                      ; minimally-qualified # 🙋🏽‍♂ E4.0 man raising hand: medium skin tone
1F64B 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🙋🏾‍♂️ E4.0 man raising hand: medium-dark skin tone
1F64B 1F3FE 200D 2642                      ; minimally-qualified # 🙋🏾‍♂ E4.0 man raising hand: medium-dark skin tone
1F64B 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🙋🏿‍♂️ E4.0 man raising hand: dark skin tone
1F64B 1F3FF 200D 2642                      ; minimally-qualified # 🙋🏿‍♂ E4.0 man raising hand: dark skin tone
1F64B 200D 2640 FE0F                       ; fully-qualified     # 🙋‍♀️ E4.0 woman raising hand
1F64B 200D 2640                            ; minimally-qualified # 🙋‍♀ E4.0 woman raising hand
1F64B 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🙋🏻‍♀️ E4.0 woman raising hand: light skin tone
1F64B 1F3FB 200D 2640                      ; minimally-qualified # 🙋🏻‍♀ E4.0 woman raising hand: light skin tone
1F64B 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🙋🏼‍♀️ E4.0 woman raising hand: medium-light skin tone
1F64B 1F3FC 200D 2640                      ; minimally-qualified # 🙋🏼‍♀ E4.0 woman raising hand: medium-light skin tone
1F64B 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🙋🏽‍♀️ E4.0 woman raising hand: medium skin tone
1F64B 1F3FD 200D 2640                      ; minimally-qualified # 🙋🏽‍♀ E4.0 woman raising hand: medium skin tone
1F64B 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🙋🏾‍♀️ E4.0 woman raising hand: medium-dark skin tone
1F64B 1F3FE 200D 2640                      ; minimally-qualified # 🙋🏾‍♀ E4.0 woman raising hand: medium-dark skin tone
1F64B 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🙋🏿‍♀️ E4.0 woman raising hand: dark skin tone
1F64B 1F3FF 200D 2640                      ; minimally-qualified # 🙋🏿‍♀ E4.0 woman raising hand: dark skin tone
1F9CF                                      ; fully-qualified     # 🧏 E12.0 deaf person
1F9CF 1F3FB                                ; fully-qualified     # 🧏🏻 E12.0 deaf person: light skin tone
1F9CF 1F3FC                                ; fully-qualified     # 🧏🏼 E12.0 deaf person: medium-light skin tone
1F9CF 1F3FD                                ; fully-qualified     # 🧏🏽 E12.0 deaf person: medium skin tone
1F9CF 1F3FE                                ; fully-qualified     # 🧏🏾 E12.0 deaf person: medium-dark skin tone
1F9CF 1F3FF                                ; fully-qualified     # 🧏🏿 E12.0 deaf person: dark skin tone
1F9CF 200D 2642 FE0F                       ; fully-qualified     # 🧏‍♂️ E12.0 deaf man
1F9CF 200D 2642                            ; minimally-qualified # 🧏‍♂ E12.0 deaf man
1F9CF 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧏🏻‍♂️ E12.0 deaf man: light skin tone
1F9CF 1F3FB 200D 2642                      ; minimally-qualified # 🧏🏻‍♂ E12.0 deaf man: light skin tone
1F9CF 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧏🏼‍♂️ E12.0 deaf man: medium-light skin tone
1F9CF 1F3FC 200D 2642                      ; minimally-qualified # 🧏🏼‍♂ E12.0 deaf man: medium-light skin tone
1F9CF 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧏🏽‍♂️ E12.0 deaf man: medium skin tone
1F9CF 1F3FD 200D 2642                      ; minimally-qualified # 🧏🏽‍♂ E12.0 deaf man: medium skin tone
1F9CF 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧏🏾‍♂️ E12.0 deaf man: medium-dark skin tone
1F9CF 1F3FE 200D 2642                      ; minimally-qualified # 🧏🏾‍♂ E12.0 deaf man: medium-dark skin tone
1F9CF 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧏🏿‍♂️ E12.0 deaf man: dark skin tone
1F9CF 1F3FF 200D 2642                      ; minimally-qualified # 🧏🏿‍♂ E12.0 deaf man: dark skin tone
1F9CF 200D 2640 FE0F                       ; fully-qualified     # 🧏‍♀️ E12.0 deaf woman
1F9CF 200D 2640                            ; minimally-qualified # 🧏‍♀ E12.0 deaf woman
1F9CF 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧏🏻‍♀️ E12.0 deaf woman: light skin tone
1F9CF 1F3FB 200D 2640                      ; minimally-qualified # 🧏🏻‍♀ E12.0 deaf woman: light skin tone
1F9CF 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧏🏼‍♀️ E12.0 deaf woman: medium-light skin tone
1F9CF 1F3FC 200D 2640                      ; minimally-qualified # 🧏🏼‍♀ E12.0 deaf woman: medium-light skin tone
1F9CF 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧏🏽‍♀️ E12.0 deaf woman: medium skin tone
1F9CF 1F3FD 200D 2640                      ; minimally-qualified # 🧏🏽‍♀ E12.0 deaf woman: medium skin tone
1F9CF 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧏🏾‍♀️ E12.0 deaf woman: medium-dark skin tone
1F9CF 1F3FE 200D 2640                      ; minimally-qualified # 🧏🏾‍♀ E12.0 deaf woman: medium-dark skin tone
1F9CF 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧏🏿‍♀️ E12.0 deaf woman: dark skin tone
1F9CF 1F3FF 200D 2640                      ; minimally-qualified # 🧏🏿‍♀ E12.0 deaf woman: dark skin tone
1F647                                      ; fully-qualified     # 🙇 E0.6 person bowing
1F647 1F3FB                                ; fully-qualified     # 🙇🏻 E1.0 person bowing: light skin tone
1F647 1F3FC                                ; fully-qualified     # 🙇🏼 E1.0 person bowing: medium-light skin tone
1F647 1F3FD                                ; fully-qualified     # 🙇🏽 E1.0 person bowing: medium skin tone
1F647 1F3FE                                ; fully-qualified     # 🙇🏾 E1.0 person bowing: medium-dark skin tone
1F647 1F3FF                                ; fully-qualified     # 🙇🏿 E1.0 person bowing: dark skin tone
1F647 200D 2642 FE0F                       ; fully-qualified     # 🙇‍♂️ E4.0 man bowing
1F647 200D 2642                            ; minimally-qualified # 🙇‍♂ E4.0 man bowing
1F647 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🙇🏻‍♂️ E4.0 man bowing: light skin tone
1F647 1F3FB 200D 2642                      ; minimally-qualified # 🙇🏻‍♂ E4.0 man bowing: light skin tone
1F647 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🙇🏼‍♂️ E4.0 man bowing: medium-light skin tone
1F647 1F3FC 200D 2642                      ; minimally-qualified # 🙇🏼‍♂ E4.0 man bowing: medium-light skin tone
1F647 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🙇🏽‍♂️ E4.0 man bowing: medium skin tone
1F647 1F3FD 200D 2642                      ; minimally-qualified # 🙇🏽‍♂ E4.0 man bowing: medium skin tone
1F647 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🙇🏾‍♂️ E4.0 man bowing: medium-dark skin tone
1F647 1F3FE 200D 2642                      ; minimally-qualified # 🙇🏾‍♂ E4.0 man bowing: medium-dark skin tone
1F647 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🙇🏿‍♂️ E4.0 man bowing: dark skin tone
1F647 1F3FF 200D 2642                      ; minimally-qualified # 🙇🏿‍♂ E4.0 man bowing: dark skin tone
1F647 200D 2640 FE0F                       ; fully-qualified     # 🙇‍♀️ E4.0 woman bowing
1F647 200D 2640                            ; minimally-qualified # 🙇‍♀ E4.0 woman bowing
1F647 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🙇🏻‍♀️ E4.0 woman bowing: light skin tone
1F647 1F3FB 200D 2640                      ; minimally-qualified # 🙇🏻‍♀ E4.0 woman bowing: light skin tone
1F647 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🙇🏼‍♀️ E4.0 woman bowing: medium-light skin tone
1F647 1F3FC 200D 2640                      ; minimally-qualified # 🙇🏼‍♀ E4.0 woman bowing: medium-light skin tone
1F647 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🙇🏽‍♀️ E4.0 woman bowing: medium skin tone
1F647 1F3FD 200D 2640                      ; minimally-qualified # 🙇🏽‍♀ E4.0 woman bowing: medium skin tone
1F647 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🙇🏾‍♀️ E4.0 woman bowing: medium-dark skin tone
1F647 1F3FE 200D 2640                      ; minimally-qualified # 🙇🏾‍♀ E4.0 woman bowing: medium-dark skin tone
1F647 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🙇🏿‍♀️ E4.0 woman bowing: dark skin tone
1F647 1F3FF 200D 2640                      ; minimally-qualified # 🙇🏿‍♀ E4.0 woman bowing: dark skin tone
1F926                                      ; fully-qualified     # 🤦 E3.0 person facepalming
1F926 1F3FB                                ; fully-qualified     # 🤦🏻 E3.0 person facepalming: light skin tone
1F926 1F3FC                                ; fully-qualified     # 🤦🏼 E3.0 person facepalming: medium-light skin tone
1F926 1F3FD                                ; fully-qualified     # 🤦🏽 E3.0 person facepalming: medium skin tone
1F926 1F3FE                                ; fully-qualified     # 🤦🏾 E3.0 person facepalming: medium-dark skin tone
1F926 1F3FF                                ; fully-qualified     # 🤦🏿 E3.0 person facepalming: dark skin tone
1F926 200D 2642 FE0F                       ; fully-qualified     # 🤦‍♂️ E4.0 man facepalming
1F926 200D 2642                            ; minimally-qualified # 🤦‍♂ E4.0 man facepalming
1F926 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🤦🏻‍♂️ E4.0 man facepalming: light skin tone
1F926 1F3FB 200D 2642                      ; minimally-qualified # 🤦🏻‍♂ E4.0 man facepalming: light skin tone
1F926 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🤦🏼‍♂️ E4.0 man facepalming: medium-light skin tone
1F926 1F3FC 200D 2642                      ; minimally-qualified # 🤦🏼‍♂ E4.0 man facepalming: medium-light skin tone
1F926 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🤦🏽‍♂️ E4.0 man facepalming: medium skin tone
1F926 1F3FD 200D 2642                      ; minimally-qualified # 🤦🏽‍♂ E4.0 man facepalming: medium skin tone
1F926 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🤦🏾‍♂️ E4.0 man facepalming: medium-dark skin tone
1F926 1F3FE 200D 2642                      ; minimally-qualified # 🤦🏾‍♂ E4.0 man facepalming: medium-dark skin tone
1F926 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🤦🏿‍♂️ E4.0 man facepalming: dark skin tone
1F926 1F3FF 200D 2642                      ; minimally-qualified # 🤦🏿‍♂ E4.0 man facepalming: dark skin tone
1F926 200D 2640 FE0F                       ; fully-qualified     # 🤦‍♀️ E4.0 woman facepalming
1F926 200D 2640                            ; minimally-qualified # 🤦‍♀ E4.0 woman facepalming
1F926 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🤦🏻‍♀️ E4.0 woman facepalming: light skin tone
1F926 1F3FB 200D 2640                      ; minimally-qualified # 🤦🏻‍♀ E4.0 woman facepalming: light skin tone
1F926 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🤦🏼‍♀️ E4.0 woman facepalming: medium-light skin tone
1F926 1F3FC 200D 2640                      ; minimally-qualified # 🤦🏼‍♀ E4.0 woman facepalming: medium-light skin tone
1F926 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🤦🏽‍♀️ E4.0 woman facepalming: medium skin tone
1F926 1F3FD 200D 2640                      ; minimally-qualified # 🤦🏽‍♀ E4.0 woman facepalming: medium skin tone
1F926 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🤦🏾‍♀️ E4.0 woman facepalming: medium-dark skin tone
1F926 1F3FE 200D 2640                      ; minimally-qualified # 🤦🏾‍♀ E4.0 woman facepalming: medium-dark skin tone
1F926 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🤦🏿‍♀️ E4.0 woman facepalming: dark skin tone
1F926 1F3FF 200D 2640                      ; minimally-qualified # 🤦🏿‍♀ E4.0 woman facepalming: dark skin tone
1F937                                      ; fully-qualified     # 🤷 E3.0 person shrugging
1F937 1F3FB                                ; fully-qualified     # 🤷🏻 E3.0 person shrugging: light skin tone
1F937 1F3FC                                ; fully-qualified     # 🤷🏼 E3.0 person shrugging: medium-light skin tone
1F937 1F3FD                                ; fully-qualified     # 🤷🏽 E3.0 person shrugging: medium skin tone
1F937 1F3FE                                ; fully-qualified     # 🤷🏾 E3.0 person shrugging: medium-dark skin tone
1F937 1F3FF                                ; fully-qualified     # 🤷🏿 E3.0 person shrugging: dark skin tone
1F937 200D 2642 FE0F                       ; fully-qualified     # 🤷‍♂️ E4.0 man shrugging
1F937 200D 2642                            ; minimally-qualified # 🤷‍♂ E4.0 man shrugging
1F937 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🤷🏻‍♂️ E4.0 man shrugging: light skin tone
1F937 1F3FB 200D 2642                      ; minimally-qualified # 🤷🏻‍♂ E4.0 man shrugging: light skin tone
1F937 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🤷🏼‍♂️ E4.0 man shrugging: medium-light skin tone
1F937 1F3FC 200D 2642                      ; minimally-qualified # 🤷🏼‍♂ E4.0 man shrugging: medium-light skin tone
1F937 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🤷🏽‍♂️ E4.0 man shrugging: medium skin tone
1F937 1F3FD 200D 2642                      ; minimally-qualified # 🤷🏽‍♂ E4.0 man shrugging: medium skin tone
1F937 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🤷🏾‍♂️ E4.0 man shrugging: medium-dark skin tone
1F937 1F3FE 200D 2642                      ; minimally-qualified # 🤷🏾‍♂ E4.0 man shrugging: medium-dark skin tone
1F937 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🤷🏿‍♂️ E4.0 man shrugging: dark skin tone
1F937 1F3FF 200D 2642                      ; minimally-qualified # 🤷🏿‍♂ E4.0 man shrugging: dark skin tone
1F937 200D 2640 FE0F                       ; fully-qualified     # 🤷‍♀️ E4.0 woman shrugging
1F937 200D 2640                            ; minimally-qualified # 🤷‍♀ E4.0 woman shrugging
1F937 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🤷🏻‍♀️ E4.0 woman shrugging: light skin tone
1F937 1F3FB 200D 2640                      ; minimally-qualified # 🤷🏻‍♀ E4.0 woman shrugging: light skin tone
1F937 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🤷🏼‍♀️ E4.0 woman shrugging: medium-light skin tone
1F937 1F3FC 200D 2640                      ; minimally-qualified # 🤷🏼‍♀ E4.0 woman shrugging: medium-light skin tone
1F937 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🤷🏽‍♀️ E4.0 woman shrugging: medium skin tone
1F937 1F3FD 200D 2640                      ; minimally-qualified # 🤷🏽‍♀ E4.0 woman shrugging: medium skin tone
1F937 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🤷🏾‍♀️ E4.0 woman shrugging: medium-dark skin tone
1F937 1F3FE 200D 2640                      ; minimally-qualified # 🤷🏾‍♀ E4.0 woman shrugging: medium-dark skin tone
1F937 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🤷🏿‍♀️ E4.0 woman shrugging: dark skin tone
1F937 1F3FF 200D 2640                      ; minimally-qualified # 🤷🏿‍♀ E4.0 woman shrugging: dark skin tone

# subgroup: person-role
1F9D1 200D 2695 FE0F                       ; fully-qualified     # 🧑‍⚕️ E12.1 health worker
1F9D1 200D 2695                            ; minimally-qualified # 🧑‍⚕ E12.1 health worker
1F9D1 1F3FB 200D 2695 FE0F                 ; fully-qualified     # 🧑🏻‍⚕️ E12.1 health worker: light skin tone
1F9D1 1F3FB 200D 2695                      ; minimally-qualified # 🧑🏻‍⚕ E12.1 health worker: light skin tone
1F9D1 1F3FC 200D 2695 FE0F                 ; fully-qualified     # 🧑🏼‍⚕️ E12.1 health worker: medium-light skin tone
1F9D1 1F3FC 200D 2695                      ; minimally-qualified # 🧑🏼‍⚕ E12.1 health worker: medium-light skin tone
1F9D1 1F3FD 200D 2695 FE0F                 ; fully-qualified     # 🧑🏽‍⚕️ E12.1 health worker: medium skin tone
1F9D1 1F3FD 200D 2695                      ; minimally-qualified # 🧑🏽‍⚕ E12.1 health worker: medium skin tone
1F9D1 1F3FE 200D 2695 FE0F                 ; fully-qualified     # 🧑🏾‍⚕️ E12.1 health worker: medium-dark skin tone
1F9D1 1F3FE 200D 2695                      ; minimally-qualified # 🧑🏾‍⚕ E12.1 health worker: medium-dark skin tone
1F9D1 1F3FF 200D 2695 FE0F                 ; fully-qualified     # 🧑🏿‍⚕️ E12.1 health worker: dark skin tone
1F9D1 1F3FF 200D 2695                      ; minimally-qualified # 🧑🏿‍⚕ E12.1 health worker: dark skin tone
1F468 200D 2695 FE0F                       ; fully-qualified     # 👨‍⚕️ E4.0 man health worker
1F468 200D 2695                            ; minimally-qualified # 👨‍⚕ E4.0 man health worker
1F468 1F3FB 200D 2695 FE0F                 ; fully-qualified     # 👨🏻‍⚕️ E4.0 man health worker: light skin tone
1F468 1F3FB 200D 2695                      ; minimally-qualified # 👨🏻‍⚕ E4.0 man health worker: light skin tone
1F468 1F3FC 200D 2695 FE0F                 ; fully-qualified     # 👨🏼‍⚕️ E4.0 man health worker: medium-light skin tone
1F468 1F3FC 200D 2695                      ; minimally-qualified # 👨🏼‍⚕ E4.0 man health worker: medium-light skin tone
1F468 1F3FD 200D 2695 FE0F                 ; fully-qualified     # 👨🏽‍⚕️ E4.0 man health worker: medium skin tone
1F468 1F3FD 200D 2695                      ; minimally-qualified # 👨🏽‍⚕ E4.0 man health worker: medium skin tone
1F468 1F3FE 200D 2695 FE0F                 ; fully-qualified     # 👨🏾‍⚕️ E4.0 man health worker: medium-dark skin tone
1F468 1F3FE 200D 2695                      ; minimally-qualified # 👨🏾‍⚕ E4.0 man health worker: medium-dark skin tone
1F468 1F3FF 200D 2695 FE0F                 ; fully-qualified     # 👨🏿‍⚕️ E4.0 man health worker: dark skin tone
1F468 1F3FF 200D 2695                      ; minimally-qualified # 👨🏿‍⚕ E4.0 man health worker: dark skin tone
1F469 200D 2695 FE0F                       ; fully-qualified     # 👩‍⚕️ E4.0 woman health worker
1F469 200D 2695                            ; minimally-qualified # 👩‍⚕ E4.0 woman health worker
1F469 1F3FB 200D 2695 FE0F                 ; fully-qualified     # 👩🏻‍⚕️ E4.0 woman health worker: light skin tone
1F469 1F3FB 200D 2695                      ; minimally-qualified # 👩🏻‍⚕ E4.0 woman health worker: light skin tone
1F469 1F3FC 200D 2695 FE0F                 ; fully-qualified     # 👩🏼‍⚕️ E4.0 woman health worker: medium-light skin tone
1F469 1F3FC 200D 2695                      ; minimally-qualified # 👩🏼‍⚕ E4.0 woman health worker: medium-light skin tone
1F469 1F3FD 200D 2695 FE0F                 ; fully-qualified     # 👩🏽‍⚕️ E4.0 woman health worker: medium skin tone
1F469 1F3FD 200D 2695                      ; minimally-qualified # 👩🏽‍⚕ E4.0 woman health worker: medium skin tone
1F469 1F3FE 200D 2695 FE0F                 ; fully-qualified     # 👩🏾‍⚕️ E4.0 woman health worker: medium-dark skin tone
1F469 1F3FE 200D 2695                      ; minimally-qualified # 👩🏾‍⚕ E4.0 woman health worker: medium-dark skin tone
1F469 1F3FF 200D 2695 FE0F                 ; fully-qualified     # 👩🏿‍⚕️ E4.0 woman health worker: dark skin tone
1F469 1F3FF 200D 2695                      ; minimally-qualified # 👩🏿‍⚕ E4.0 woman health worker: dark skin tone
1F9D1 200D 1F393                           ; fully-qualified     # 🧑‍🎓 E12.1 student
1F9D1 1F3FB 200D 1F393                     ; fully-qualified     # 🧑🏻‍🎓 E12.1 student: light skin tone
1F9D1 1F3FC 200D 1F393                     ; fully-qualified     # 🧑🏼‍🎓 E12.1 student: medium-light skin tone
1F9D1 1F3FD 200D 1F393                     ; fully-qualified     # 🧑🏽‍🎓 E12.1 student: medium skin tone
1F9D1 1F3FE 200D 1F393                     ; fully-qualified     # 🧑🏾‍🎓 E12.1 student: medium-dark skin tone
1F9D1 1F3FF 200D 1F393                     ; fully-qualified     # 🧑🏿‍🎓 E12.1 student: dark skin tone
1F468 200D 1F393                           ; fully-qualified     # 👨‍🎓 E4.0 man student
1F468 1F3FB 200D 1F393                     ; fully-qualified     # 👨🏻‍🎓 E4.0 man student: light skin tone
1F468 1F3FC 200D 1F393                     ; fully-qualified     # 👨🏼‍🎓 E4.0 man student: medium-light skin tone
1F468 1F3FD 200D 1F393                     ; fully-qualified     # 👨🏽‍🎓 E4.0 man student: medium skin tone
1F468 1F3FE 200D 1F393                     ; fully-qualified     # 👨🏾‍🎓 E4.0 man student: medium-dark skin tone
1F468 1F3FF 200D 1F393                     ; fully-qualified     # 👨🏿‍🎓 E4.0 man student: dark skin tone
1F469 200D 1F393                           ; fully-qualified     # 👩‍🎓 E4.0 woman student
1F469 1F3FB 200D 1F393                     ; fully-qualified     # 👩🏻‍🎓 E4.0 woman student: light skin tone
1F469 1F3FC 200D 1F393                     ; fully-qualified     # 👩🏼‍🎓 E4.0 woman student: medium-light skin tone
1F469 1F3FD 200D 1F393                     ; fully-qualified     # 👩🏽‍🎓 E4.0 woman student: medium skin tone
1F469 1F3FE 200D 1F393                     ; fully-qualified     # 👩🏾‍🎓 E4.0 woman student: medium-dark skin tone
1F469 1F3FF 200D 1F393                     ; fully-qualified     # 👩🏿‍🎓 E4.0 woman student: dark skin tone
1F9D1 200D 1F3EB                           ; fully-qualified     # 🧑‍🏫 E12.1 teacher
1F9D1 1F3FB 200D 1F3EB                     ; fully-qualified     # 🧑🏻‍🏫 E12.1 teacher: light skin tone
1F9D1 1F3FC 200D 1F3EB                     ; fully-qualified     # 🧑🏼‍🏫 E12.1 teacher: medium-light skin tone
1F9D1 1F3FD 200D 1F3EB                     ; fully-qualified     # 🧑🏽‍🏫 E12.1 teacher: medium skin tone
1F9D1 1F3FE 200D 1F3EB                     ; fully-qualified     # 🧑🏾‍🏫 E12.1 teacher: medium-dark skin tone
1F9D1 1F3FF 200D 1F3EB                     ; fully-qualified     # 🧑🏿‍🏫 E12.1 teacher: dark skin tone
1F468 200D 1F3EB                           ; fully-qualified     # 👨‍🏫 E4.0 man teacher
1F468 1F3FB 200D 1F3EB                     ; fully-qualified     # 👨🏻‍🏫 E4.0 man teacher: light skin tone
1F468 1F3FC 200D 1F3EB                     ; fully-qualified     # 👨🏼‍🏫 E4.0 man teacher: medium-light skin tone
1F468 1F3FD 200D 1F3EB                     ; fully-qualified     # 👨🏽‍🏫 E4.0 man teacher: medium skin tone
1F468 1F3FE 200D 1F3EB                     ; fully-qualified     # 👨🏾‍🏫 E4.0 man teacher: medium-dark skin tone
1F468 1F3FF 200D 1F3EB                     ; fully-qualified     # 👨🏿‍🏫 E4.0 man teacher: dark skin tone
1F469 200D 1F3EB                           ; fully-qualified     # 👩‍🏫 E4.0 woman teacher
1F469 1F3FB 200D 1F3EB                     ; fully-qualified     # 👩🏻‍🏫 E4.0 woman teacher: light skin tone
1F469 1F3FC 200D 1F3EB                     ; fully-qualified     # 👩🏼‍🏫 E4.0 woman teacher: medium-light skin tone
1F469 1F3FD 200D 1F3EB                     ; fully-qualified     # 👩🏽‍🏫 E4.0 woman teacher: medium skin tone
1F469 1F3FE 200D 1F3EB                     ; fully-qualified     # 👩🏾‍🏫 E4.0 woman teacher: medium-dark skin tone
1F469 1F3FF 200D 1F3EB                     ; fully-qualified     # 👩🏿‍🏫 E4.0 woman teacher: dark skin tone
1F9D1 200D 2696 FE0F                       ; fully-qualified     # 🧑‍⚖️ E12.1 judge
1F9D1 200D 2696                            ; minimally-qualified # 🧑‍⚖ E12.1 judge
1F9D1 1F3FB 200D 2696 FE0F                 ; fully-qualified     # 🧑🏻‍⚖️ E12.1 judge: light skin tone
1F9D1 1F3FB 200D 2696                      ; minimally-qualified # 🧑🏻‍⚖ E12.1 judge: light skin tone
1F9D1 1F3FC 200D 2696 FE0F                 ; fully-qualified     # 🧑🏼‍⚖️ E12.1 judge: medium-light skin tone
1F9D1 1F3FC 200D 2696                      ; minimally-qualified # 🧑🏼‍⚖ E12.1 judge: medium-light skin tone
1F9D1 1F3FD 200D 2696 FE0F                 ; fully-qualified     # 🧑🏽‍⚖️ E12.1 judge: medium skin tone
1F9D1 1F3FD 200D 2696                      ; minimally-qualified # 🧑🏽‍⚖ E12.1 judge: medium skin tone
1F9D1 1F3FE 200D 2696 FE0F                 ; fully-qualified     # 🧑🏾‍⚖️ E12.1 judge: medium-dark skin tone
1F9D1 1F3FE 200D 2696                      ; minimally-qualified # 🧑🏾‍⚖ E12.1 judge: medium-dark skin tone
1F9D1 1F3FF 200D 2696 FE0F                 ; fully-qualified     # 🧑🏿‍⚖️ E12.1 judge: dark skin tone
1F9D1 1F3FF 200D 2696                      ; minimally-qualified # 🧑🏿‍⚖ E12.1 judge: dark skin tone
1F468 200D 2696 FE0F                       ; fully-qualified     # 👨‍⚖️ E4.0 man judge
1F468 200D 2696                            ; minimally-qualified # 👨‍⚖ E4.0 man judge
1F468 1F3FB 200D 2696 FE0F                 ; fully-qualified     # 👨🏻‍⚖️ E4.0 man judge: light skin tone
1F468 1F3FB 200D 2696                      ; minimally-qualified # 👨🏻‍⚖ E4.0 man judge: light skin tone
1F468 1F3FC 200D 2696 FE0F                 ; fully-qualified     # 👨🏼‍⚖️ E4.0 man judge: medium-light skin tone
1F468 1F3FC 200D 2696                      ; minimally-qualified # 👨🏼‍⚖ E4.0 man judge: medium-light skin tone
1F468 1F3FD 200D 2696 FE0F                 ; fully-qualified     # 👨🏽‍⚖️ E4.0 man judge: medium skin tone
1F468 1F3FD 200D 2696                      ; minimally-qualified # 👨🏽‍⚖ E4.0 man judge: medium skin tone
1F468 1F3FE 200D 2696 FE0F                 ; fully-qualified     # 👨🏾‍⚖️ E4.0 man judge: medium-dark skin tone
1F468 1F3FE 200D 2696                      ; minimally-qualified # 👨🏾‍⚖ E4.0 man judge: medium-dark skin tone
1F468 1F3FF 200D 2696 FE0F                 ; fully-qualified     # 👨🏿‍⚖️ E4.0 man judge: dark skin tone
1F468 1F3FF 200D 2696                      ; minimally-qualified # 👨🏿‍⚖ E4.0 man judge: dark skin tone
1F469 200D 2696 FE0F                       ; fully-qualified     # 👩‍⚖️ E4.0 woman judge
1F469 200D 2696                            ; minimally-qualified # 👩‍⚖ E4.0 woman judge
1F469 1F3FB 200D 2696 FE0F                 ; fully-qualified     # 👩🏻‍⚖️ E4.0 woman judge: light skin tone
1F469 1F3FB 200D 2696                      ; minimally-qualified # 👩🏻‍⚖ E4.0 woman judge: light skin tone
1F469 1F3FC 200D 2696 FE0F                 ; fully-qualified     # 👩🏼‍⚖️ E4.0 woman judge: medium-light skin tone
1F469 1F3FC 200D 2696                      ; minimally-qualified # 👩🏼‍⚖ E4.0 woman judge: medium-light skin tone
1F469 1F3FD 200D 2696 FE0F                 ; fully-qualified     # 👩🏽‍⚖️ E4.0 woman judge: medium skin tone
1F469 1F3FD 200D 2696                      ; minimally-qualified # 👩🏽‍⚖ E4.0 woman judge: medium skin tone
1F469 1F3FE 200D 2696 FE0F                 ; fully-qualified     # 👩🏾‍⚖️ E4.0 woman judge: medium-dark skin tone
1F469 1F3FE 200D 2696                      ; minimally-qualified # 👩🏾‍⚖ E4.0 woman judge: medium-dark skin tone
1F469 1F3FF 200D 2696 FE0F                 ; fully-qualified     # 👩🏿‍⚖️ E4.0 woman judge: dark skin tone
1F469 1F3FF 200D 2696                      ; minimally-qualified # 👩🏿‍⚖ E4.0 woman judge: dark skin tone
1F9D1 200D 1F33E                           ; fully-qualified     # 🧑‍🌾 E12.1 farmer
1F9D1 1F3FB 200D 1F33E                     ; fully-qualified     # 🧑🏻‍🌾 E12.1 farmer: light skin tone
1F9D1 1F3FC 200D 1F33E                     ; fully-qualified     # 🧑🏼‍🌾 E12.1 farmer: medium-light skin tone
1F9D1 1F3FD 200D 1F33E                     ; fully-qualified     # 🧑🏽‍🌾 E12.1 farmer: medium skin tone
1F9D1 1F3FE 200D 1F33E                     ; fully-qualified     # 🧑🏾‍🌾 E12.1 farmer: medium-dark skin tone
1F9D1 1F3FF 200D 1F33E                     ; fully-qualified     # 🧑🏿‍🌾 E12.1 farmer: dark skin tone
1F468 200D 1F33E                           ; fully-qualified     # 👨‍🌾 E4.0 man farmer
1F468 1F3FB 200D 1F33E                     ; fully-qualified     # 👨🏻‍🌾 E4.0 man farmer: light skin tone
1F468 1F3FC 200D 1F33E                     ; fully-qualified     # 👨🏼‍🌾 E4.0 man farmer: medium-light skin tone
1F468 1F3FD 200D 1F33E                     ; fully-qualified     # 👨🏽‍🌾 E4.0 man farmer: medium skin tone
1F468 1F3FE 200D 1F33E                     ; fully-qualified     # 👨🏾‍🌾 E4.0 man farmer: medium-dark skin tone
1F468 1F3FF 200D 1F33E                     ; fully-qualified     # 👨🏿‍🌾 E4.0 man farmer: dark skin tone
1F469 200D 1F33E                           ; fully-qualified     # 👩‍🌾 E4.0 woman farmer
1F469 1F3FB 200D 1F33E                     ; fully-qualified     # 👩🏻‍🌾 E4.0 woman farmer: light skin tone
1F469 1F3FC 200D 1F33E                     ; fully-qualified     # 👩🏼‍🌾 E4.0 woman farmer: medium-light skin tone
1F469 1F3FD 200D 1F33E                     ; fully-qualified     # 👩🏽‍🌾 E4.0 woman farmer: medium skin tone
1F469 1F3FE 200D 1F33E                     ; fully-qualified     # 👩🏾‍🌾 E4.0 woman farmer: medium-dark skin tone
1F469 1F3FF 200D 1F33E                     ; fully-qualified     # 👩🏿‍🌾 E4.0 woman farmer: dark skin tone
1F9D1 200D 1F373                           ; fully-qualified     # 🧑‍🍳 E12.1 cook
1F9D1 1F3FB 200D 1F373                     ; fully-qualified     # 🧑🏻‍🍳 E12.1 cook: light skin tone
1F9D1 1F3FC 200D 1F373                     ; fully-qualified     # 🧑🏼‍🍳 E12.1 cook: medium-light skin tone
1F9D1 1F3FD 200D 1F373                     ; fully-qualified     # 🧑🏽‍🍳 E12.1 cook: medium skin tone
1F9D1 1F3FE 200D 1F373                     ; fully-qualified     # 🧑🏾‍🍳 E12.1 cook: medium-dark skin tone
1F9D1 1F3FF 200D 1F373                     ; fully-qualified     # 🧑🏿‍🍳 E12.1 cook: dark skin tone
1F468 200D 1F373                           ; fully-qualified     # 👨‍🍳 E4.0 man cook
1F468 1F3FB 200D 1F373                     ; fully-qualified     # 👨🏻‍🍳 E4.0 man cook: light skin tone
1F468 1F3FC 200D 1F373                     ; fully-qualified     # 👨🏼‍🍳 E4.0 man cook: medium-light skin tone
1F468 1F3FD 200D 1F373                     ; fully-qualified     # 👨🏽‍🍳 E4.0 man cook: medium skin tone
1F468 1F3FE 200D 1F373                     ; fully-qualified     # 👨🏾‍🍳 E4.0 man cook: medium-dark skin tone
1F468 1F3FF 200D 1F373                     ; fully-qualified     # 👨🏿‍🍳 E4.0 man cook: dark skin tone
1F469 200D 1F373                           ; fully-qualified     # 👩‍🍳 E4.0 woman cook
1F469 1F3FB 200D 1F373                     ; fully-qualified     # 👩🏻‍🍳 E4.0 woman cook: light skin tone
1F469 1F3FC 200D 1F373                     ; fully-qualified     # 👩🏼‍🍳 E4.0 woman cook: medium-light skin tone
1F469 1F3FD 200D 1F373                     ; fully-qualified     # 👩🏽‍🍳 E4.0 woman cook: medium skin tone
1F469 1F3FE 200D 1F373                     ; fully-qualified     # 👩🏾‍🍳 E4.0 woman cook: medium-dark skin tone
1F469 1F3FF 200D 1F373                     ; fully-qualified     # 👩🏿‍🍳 E4.0 woman cook: dark skin tone
1F9D1 200D 1F527                           ; fully-qualified     # 🧑‍🔧 E12.1 mechanic
1F9D1 1F3FB 200D 1F527                     ; fully-qualified     # 🧑🏻‍🔧 E12.1 mechanic: light skin tone
1F9D1 1F3FC 200D 1F527                     ; fully-qualified     # 🧑🏼‍🔧 E12.1 mechanic: medium-light skin tone
1F9D1 1F3FD 200D 1F527                     ; fully-qualified     # 🧑🏽‍🔧 E12.1 mechanic: medium skin tone
1F9D1 1F3FE 200D 1F527                     ; fully-qualified     # 🧑🏾‍🔧 E12.1 mechanic: medium-dark skin tone
1F9D1 1F3FF 200D 1F527                     ; fully-qualified     # 🧑🏿‍🔧 E12.1 mechanic: dark skin tone
1F468 200D 1F527                           ; fully-qualified     # 👨‍🔧 E4.0 man mechanic
1F468 1F3FB 200D 1F527                     ; fully-qualified     # 👨🏻‍🔧 E4.0 man mechanic: light skin tone
1F468 1F3FC 200D 1F527                     ; fully-qualified     # 👨🏼‍🔧 E4.0 man mechanic: medium-light skin tone
1F468 1F3FD 200D 1F527                     ; fully-qualified     # 👨🏽‍🔧 E4.0 man mechanic: medium skin tone
1F468 1F3FE 200D 1F527                     ; fully-qualified     # 👨🏾‍🔧 E4.0 man mechanic: medium-dark skin tone
1F468 1F3FF 200D 1F527                     ; fully-qualified     # 👨🏿‍🔧 E4.0 man mechanic: dark skin tone
1F469 200D 1F527                           ; fully-qualified     # 👩‍🔧 E4.0 woman mechanic
1F469 1F3FB 200D 1F527                     ; fully-qualified     # 👩🏻‍🔧 E4.0 woman mechanic: light skin tone
1F469 1F3FC 200D 1F527                     ; fully-qualified     # 👩🏼‍🔧 E4.0 woman mechanic: medium-light skin tone
1F469 1F3FD 200D 1F527                     ; fully-qualified     # 👩🏽‍🔧 E4.0 woman mechanic: medium skin tone
1F469 1F3FE 200D 1F527                     ; fully-qualified     # 👩🏾‍🔧 E4.0 woman mechanic: medium-dark skin tone
1F469 1F3FF 200D 1F527                     ; fully-qualified     # 👩🏿‍🔧 E4.0 woman mechanic: dark skin tone
1F9D1 200D 1F3ED                           ; fully-qualified     # 🧑‍🏭 E12.1 factory worker
1F9D1 1F3FB 200D 1F3ED                     ; fully-qualified     # 🧑🏻‍🏭 E12.1 factory worker: light skin tone
1F9D1 1F3FC 200D 1F3ED                     ; fully-qualified     # 🧑🏼‍🏭 E12.1 factory worker: medium-light skin tone
1F9D1 1F3FD 200D 1F3ED                     ; fully-qualified     # 🧑🏽‍🏭 E12.1 factory worker: medium skin tone
1F9D1 1F3FE 200D 1F3ED                     ; fully-qualified     # 🧑🏾‍🏭 E12.1 factory worker: medium-dark skin tone
1F9D1 1F3FF 200D 1F3ED                     ; fully-qualified     # 🧑🏿‍🏭 E12.1 factory worker: dark skin tone
1F468 200D 1F3ED                           ; fully-qualified     # 👨‍🏭 E4.0 man factory worker
1F468 1F3FB 200D 1F3ED                     ; fully-qualified     # 👨🏻‍🏭 E4.0 man factory worker: light skin tone
1F468 1F3FC 200D 1F3ED                     ; fully-qualified     # 👨🏼‍🏭 E4.0 man factory worker: medium-light skin tone
1F468 1F3FD 200D 1F3ED                     ; fully-qualified     # 👨🏽‍🏭 E4.0 man factory worker: medium skin tone
1F468 1F3FE 200D 1F3ED                     ; fully-qualified     # 👨🏾‍🏭 E4.0 man factory worker: medium-dark skin tone
1F468 1F3FF 200D 1F3ED                     ; fully-qualified     # 👨🏿‍🏭 E4.0 man factory worker: dark skin tone
1F469 200D 1F3ED                           ; fully-qualified     # 👩‍🏭 E4.0 woman factory worker
1F469 1F3FB 200D 1F3ED                     ; fully-qualified     # 👩🏻‍🏭 E4.0 woman factory worker: light skin tone
1F469 1F3FC 200D 1F3ED                     ; fully-qualified     # 👩🏼‍🏭 E4.0 woman factory worker: medium-light skin tone
1F469 1F3FD 200D 1F3ED                     ; fully-qualified     # 👩🏽‍🏭 E4.0 woman factory worker: medium skin tone
1F469 1F3FE 200D 1F3ED                     ; fully-qualified     # 👩🏾‍🏭 E4.0 woman factory worker: medium-dark skin tone
1F469 1F3FF 200D 1F3ED                     ; fully-qualified     # 👩🏿‍🏭 E4.0 woman factory worker: dark skin tone
1F9D1 200D 1F4BC                           ; fully-qualified     # 🧑‍💼 E12.1 office worker
1F9D1 1F3FB 200D 1F4BC                     ; fully-qualified     # 🧑🏻‍💼 E12.1 office worker: light skin tone
1F9D1 1F3FC 200D 1F4BC                     ; fully-qualified     # 🧑🏼‍💼 E12.1 office worker: medium-light skin tone
1F9D1 1F3FD 200D 1F4BC                     ; fully-qualified     # 🧑🏽‍💼 E12.1 office worker: medium skin tone
1F9D1 1F3FE 200D 1F4BC                     ; fully-qualified     # 🧑🏾‍💼 E12.1 office worker: medium-dark skin tone
1F9D1 1F3FF 200D 1F4BC                     ; fully-qualified     # 🧑🏿‍💼 E12.1 office worker: dark skin tone
1F468 200D 1F4BC                           ; fully-qualified     # 👨‍💼 E4.0 man office worker
1F468 1F3FB 200D 1F4BC                     ; fully-qualified     # 👨🏻‍💼 E4.0 man office worker: light skin tone
1F468 1F3FC 200D 1F4BC                     ; fully-qualified     # 👨🏼‍💼 E4.0 man office worker: medium-light skin tone
1F468 1F3FD 200D 1F4BC                     ; fully-qualified     # 👨🏽‍💼 E4.0 man office worker: medium skin tone
1F468 1F3FE 200D 1F4BC                     ; fully-qualified     # 👨🏾‍💼 E4.0 man office worker: medium-dark skin tone
1F468 1F3FF 200D 1F4BC                     ; fully-qualified     # 👨🏿‍💼 E4.0 man office worker: dark skin tone
1F469 200D 1F4BC                           ; fully-qualified     # 👩‍💼 E4.0 woman office worker
1F469 1F3FB 200D 1F4BC                     ; fully-qualified     # 👩🏻‍💼 E4.0 woman office worker: light skin tone
1F469 1F3FC 200D 1F4BC                     ; fully-qualified     # 👩🏼‍💼 E4.0 woman office worker: medium-light skin tone
1F469 1F3FD 200D 1F4BC                     ; fully-qualified     # 👩🏽‍💼 E4.0 woman office worker: medium skin tone
1F469 1F3FE 200D 1F4BC                     ; fully-qualified     # 👩🏾‍💼 E4.0 woman office worker: medium-dark skin tone
1F469 1F3FF 200D 1F4BC                     ; fully-qualified     # 👩🏿‍💼 E4.0 woman office worker: dark skin tone
1F9D1 200D 1F52C                           ; fully-qualified     # 🧑‍🔬 E12.1 scientist
1F9D1 1F3FB 200D 1F52C                     ; fully-qualified     # 🧑🏻‍🔬 E12.1 scientist: light skin tone
1F9D1 1F3FC 200D 1F52C                     ; fully-qualified     # 🧑🏼‍🔬 E12.1 scientist: medium-light skin tone
1F9D1 1F3FD 200D 1F52C                     ; fully-qualified     # 🧑🏽‍🔬 E12.1 scientist: medium skin tone
1F9D1 1F3FE 200D 1F52C                     ; fully-qualified     # 🧑🏾‍🔬 E12.1 scientist: medium-dark skin tone
1F9D1 1F3FF 200D 1F52C                     ; fully-qualified     # 🧑🏿‍🔬 E12.1 scientist: dark skin tone
1F468 200D 1F52C                           ; fully-qualified     # 👨‍🔬 E4.0 man scientist
1F468 1F3FB 200D 1F52C                     ; fully-qualified     # 👨🏻‍🔬 E4.0 man scientist: light skin tone
1F468 1F3FC 200D 1F52C                     ; fully-qualified     # 👨🏼‍🔬 E4.0 man scientist: medium-light skin tone
1F468 1F3FD 200D 1F52C                     ; fully-qualified     # 👨🏽‍🔬 E4.0 man scientist: medium skin tone
1F468 1F3FE 200D 1F52C                     ; fully-qualified     # 👨🏾‍🔬 E4.0 man scientist: medium-dark skin tone
1F468 1F3FF 200D 1F52C                     ; fully-qualified     # 👨🏿‍🔬 E4.0 man scientist: dark skin tone
1F469 200D 1F52C                           ; fully-qualified     # 👩‍🔬 E4.0 woman scientist
1F469 1F3FB 200D 1F52C                     ; fully-qualified     # 👩🏻‍🔬 E4.0 woman scientist: light skin tone
1F469 1F3FC 200D 1F52C                     ; fully-qualified     # 👩🏼‍🔬 E4.0 woman scientist: medium-light skin tone
1F469 1F3FD 200D 1F52C                     ; fully-qualified     # 👩🏽‍🔬 E4.0 woman scientist: medium skin tone
1F469 1F3FE 200D 1F52C                     ; fully-qualified     # 👩🏾‍🔬 E4.0 woman scientist: medium-dark skin tone
1F469 1F3FF 200D 1F52C                     ; fully-qualified     # 👩🏿‍🔬 E4.0 woman scientist: dark skin tone
1F9D1 200D 1F4BB                           ; fully-qualified     # 🧑‍💻 E12.1 technologist
1F9D1 1F3FB 200D 1F4BB                     ; fully-qualified     # 🧑🏻‍💻 E12.1 technologist: light skin tone
1F9D1 1F3FC 200D 1F4BB                     ; fully-qualified     # 🧑🏼‍💻 E12.1 technologist: medium-light skin tone
1F9D1 1F3FD 200D 1F4BB                     ; fully-qualified     # 🧑🏽‍💻 E12.1 technologist: medium skin tone
1F9D1 1F3FE 200D 1F4BB                     ; fully-qualified     # 🧑🏾‍💻 E12.1 technologist: medium-dark skin tone
1F9D1 1F3FF 200D 1F4BB                     ; fully-qualified     # 🧑🏿‍💻 E12.1 technologist: dark skin tone
1F468 200D 1F4BB                           ; fully-qualified     # 👨‍💻 E4.0 man technologist
1F468 1F3FB 200D 1F4BB                     ; fully-qualified     # 👨🏻‍💻 E4.0 man technologist: light skin tone
1F468 1F3FC 200D 1F4BB                     ; fully-qualified     # 👨🏼‍💻 E4.0 man technologist: medium-light skin tone
1F468 1F3FD 200D 1F4BB                     ; fully-qualified     # 👨🏽‍💻 E4.0 man technologist: medium skin tone
1F468 1F3FE 200D 1F4BB                     ; fully-qualified     # 👨🏾‍💻 E4.0 man technologist: medium-dark skin tone
1F468 1F3FF 200D 1F4BB                     ; fully-qualified     # 👨🏿‍💻 E4.0 man technologist: dark skin tone
1F469 200D 1F4BB                           ; fully-qualified     # 👩‍💻 E4.0 woman technologist
1F469 1F3FB 200D 1F4BB                     ; fully-qualified     # 👩🏻‍💻 E4.0 woman technologist: light skin tone
1F469 1F3FC 200D 1F4BB                     ; fully-qualified     # 👩🏼‍💻 E4.0 woman technologist: medium-light skin tone
1F469 1F3FD 200D 1F4BB                     ; fully-qualified     # 👩🏽‍💻 E4.0 woman technologist: medium skin tone
1F469 1F3FE 200D 1F4BB                     ; fully-qualified     # 👩🏾‍💻 E4.0 woman technologist: medium-dark skin tone
1F469 1F3FF 200D 1F4BB                     ; fully-qualified     # 👩🏿‍💻 E4.0 woman technologist: dark skin tone
1F9D1 200D 1F3A4                           ; fully-qualified     # 🧑‍🎤 E12.1 singer
1F9D1 1F3FB 200D 1F3A4                     ; fully-qualified     # 🧑🏻‍🎤 E12.1 singer: light skin tone
1F9D1 1F3FC 200D 1F3A4                     ; fully-qualified     # 🧑🏼‍🎤 E12.1 singer: medium-light skin tone
1F9D1 1F3FD 200D 1F3A4                     ; fully-qualified     # 🧑🏽‍🎤 E12.1 singer: medium skin tone
1F9D1 1F3FE 200D 1F3A4                     ; fully-qualified     # 🧑🏾‍🎤 E12.1 singer: medium-dark skin tone
1F9D1 1F3FF 200D 1F3A4                     ; fully-qualified     # 🧑🏿‍🎤 E12.1 singer: dark skin tone
1F468 200D 1F3A4                           ; fully-qualified     # 👨‍🎤 E4.0 man singer
1F468 1F3FB 200D 1F3A4                     ; fully-qualified     # 👨🏻‍🎤 E4.0 man singer: light skin tone
1F468 1F3FC 200D 1F3A4                     ; fully-qualified     # 👨🏼‍🎤 E4.0 man singer: medium-light skin tone
1F468 1F3FD 200D 1F3A4                     ; fully-qualified     # 👨🏽‍🎤 E4.0 man singer: medium skin tone
1F468 1F3FE 200D 1F3A4                     ; fully-qualified     # 👨🏾‍🎤 E4.0 man singer: medium-dark skin tone
1F468 1F3FF 200D 1F3A4                     ; fully-qualified     # 👨🏿‍🎤 E4.0 man singer: dark skin tone
1F469 200D 1F3A4                           ; fully-qualified     # 👩‍🎤 E4.0 woman singer
1F469 1F3FB 200D 1F3A4                     ; fully-qualified     # 👩🏻‍🎤 E4.0 woman singer: light skin tone
1F469 1F3FC 200D 1F3A4                     ; fully-qualified     # 👩🏼‍🎤 E4.0 woman singer: medium-light skin tone
1F469 1F3FD 200D 1F3A4                     ; fully-qualified     # 👩🏽‍🎤 E4.0 woman singer: medium skin tone
1F469 1F3FE 200D 1F3A4                     ; fully-qualified     # 👩🏾‍🎤 E4.0 woman singer: medium-dark skin tone
1F469 1F3FF 200D 1F3A4                     ; fully-qualified     # 👩🏿‍🎤 E4.0 woman singer: dark skin tone
1F9D1 200D 1F3A8                           ; fully-qualified     # 🧑‍🎨 E12.1 artist
1F9D1 1F3FB 200D 1F3A8                     ; fully-qualified     # 🧑🏻‍🎨 E12.1 artist: light skin tone
1F9D1 1F3FC 200D 1F3A8                     ; fully-qualified     # 🧑🏼‍🎨 E12.1 artist: medium-light skin tone
1F9D1 1F3FD 200D 1F3A8                     ; fully-qualified     # 🧑🏽‍🎨 E12.1 artist: medium skin tone
1F9D1 1F3FE 200D 1F3A8                     ; fully-qualified     # 🧑🏾‍🎨 E12.1 artist: medium-dark skin tone
1F9D1 1F3FF 200D 1F3A8                     ; fully-qualified     # 🧑🏿‍🎨 E12.1 artist: dark skin tone
1F468 200D 1F3A8                           ; fully-qualified     # 👨‍🎨 E4.0 man artist
1F468 1F3FB 200D 1F3A8                     ; fully-qualified     # 👨🏻‍🎨 E4.0 man artist: light skin tone
1F468 1F3FC 200D 1F3A8                     ; fully-qualified     # 👨🏼‍🎨 E4.0 man artist: medium-light skin tone
1F468 1F3FD 200D 1F3A8                     ; fully-qualified     # 👨🏽‍🎨 E4.0 man artist: medium skin tone
1F468 1F3FE 200D 1F3A8                     ; fully-qualified     # 👨🏾‍🎨 E4.0 man artist: medium-dark skin tone
1F468 1F3FF 200D 1F3A8                     ; fully-qualified     # 👨🏿‍🎨 E4.0 man artist: dark skin tone
1F469 200D 1F3A8                           ; fully-qualified     # 👩‍🎨 E4.0 woman artist
1F469 1F3FB 200D 1F3A8                     ; fully-qualified     # 👩🏻‍🎨 E4.0 woman artist: light skin tone
1F469 1F3FC 200D 1F3A8                     ; fully-qualified     # 👩🏼‍🎨 E4.0 woman artist: medium-light skin tone
1F469 1F3FD 200D 1F3A8                     ; fully-qualified     # 👩🏽‍🎨 E4.0 woman artist: medium skin tone
1F469 1F3FE 200D 1F3A8                     ; fully-qualified     # 👩🏾‍🎨 E4.0 woman artist: medium-dark skin tone
1F469 1F3FF 200D 1F3A8                     ; fully-qualified     # 👩🏿‍🎨 E4.0 woman artist: dark skin tone
1F9D1 200D 2708 FE0F                       ; fully-qualified     # 🧑‍✈️ E12.1 pilot
1F9D1 200D 2708                            ; minimally-qualified # 🧑‍✈ E12.1 pilot
1F9D1 1F3FB 200D 2708 FE0F                 ; fully-qualified     # 🧑🏻‍✈️ E12.1 pilot: light skin tone
1F9D1 1F3FB 200D 2708                      ; minimally-qualified # 🧑🏻‍✈ E12.1 pilot: light skin tone
1F9D1 1F3FC 200D 2708 FE0F                 ; fully-qualified     # 🧑🏼‍✈️ E12.1 pilot: medium-light skin tone
1F9D1 1F3FC 200D 2708                      ; minimally-qualified # 🧑🏼‍✈ E12.1 pilot: medium-light skin tone
1F9D1 1F3FD 200D 2708 FE0F                 ; fully-qualified     # 🧑🏽‍✈️ E12.1 pilot: medium skin tone
1F9D1 1F3FD 200D 2708                      ; minimally-qualified # 🧑🏽‍✈ E12.1 pilot: medium skin tone
1F9D1 1F3FE 200D 2708 FE0F                 ; fully-qualified     # 🧑🏾‍✈️ E12.1 pilot: medium-dark skin tone
1F9D1 1F3FE 200D 2708                      ; minimally-qualified # 🧑🏾‍✈ E12.1 pilot: medium-dark skin tone
1F9D1 1F3FF 200D 2708 FE0F                 ; fully-qualified     # 🧑🏿‍✈️ E12.1 pilot: dark skin tone
1F9D1 1F3FF 200D 2708                      ; minimally-qualified # 🧑🏿‍✈ E12.1 pilot: dark skin tone
1F468 200D 2708 FE0F                       ; fully-qualified     # 👨‍✈️ E4.0 man pilot
1F468 200D 2708                            ; minimally-qualified # 👨‍✈ E4.0 man pilot
1F468 1F3FB 200D 2708 FE0F                 ; fully-qualified     # 👨🏻‍✈️ E4.0 man pilot: light skin tone
1F468 1F3FB 200D 2708                      ; minimally-qualified # 👨🏻‍✈ E4.0 man pilot: light skin tone
1F468 1F3FC 200D 2708 FE0F                 ; fully-qualified     # 👨🏼‍✈️ E4.0 man pilot: medium-light skin tone
1F468 1F3FC 200D 2708                      ; minimally-qualified # 👨🏼‍✈ E4.0 man pilot: medium-light skin tone
1F468 1F3FD 200D 2708 FE0F                 ; fully-qualified     # 👨🏽‍✈️ E4.0 man pilot: medium skin tone
1F468 1F3FD 200D 2708                      ; minimally-qualified # 👨🏽‍✈ E4.0 man pilot: medium skin tone
1F468 1F3FE 200D 2708 FE0F                 ; fully-qualified     # 👨🏾‍✈️ E4.0 man pilot: medium-dark skin tone
1F468 1F3FE 200D 2708                      ; minimally-qualified # 👨🏾‍✈ E4.0 man pilot: medium-dark skin tone
1F468 1F3FF 200D 2708 FE0F                 ; fully-qualified     # 👨🏿‍✈️ E4.0 man pilot: dark skin tone
1F468 1F3FF 200D 2708                      ; minimally-qualified # 👨🏿‍✈ E4.0 man pilot: dark skin tone
1F469 200D 2708 FE0F                       ; fully-qualified     # 👩‍✈️ E4.0 woman pilot
1F469 200D 2708                            ; minimally-qualified # 👩‍✈ E4.0 woman pilot
1F469 1F3FB 200D 2708 FE0F                 ; fully-qualified     # 👩🏻‍✈️ E4.0 woman pilot: light skin tone
1F469 1F3FB 200D 2708                      ; minimally-qualified # 👩🏻‍✈ E4.0 woman pilot: light skin tone
1F469 1F3FC 200D 2708 FE0F                 ; fully-qualified     # 👩🏼‍✈️ E4.0 woman pilot: medium-light skin tone
1F469 1F3FC 200D 2708                      ; minimally-qualified # 👩🏼‍✈ E4.0 woman pilot: medium-light skin tone
1F469 1F3FD 200D 2708 FE0F                 ; fully-qualified     # 👩🏽‍✈️ E4.0 woman pilot: medium skin tone
1F469 1F3FD 200D 2708                      ; minimally-qualified # 👩🏽‍✈ E4.0 woman pilot: medium skin tone
1F469 1F3FE 200D 2708 FE0F                 ; fully-qualified     # 👩🏾‍✈️ E4.0 woman pilot: medium-dark skin tone
1F469 1F3FE 200D 2708                      ; minimally-qualified # 👩🏾‍✈ E4.0 woman pilot: medium-dark skin tone
1F469 1F3FF 200D 2708 FE0F                 ; fully-qualified     # 👩🏿‍✈️ E4.0 woman pilot: dark skin tone
1F469 1F3FF 200D 2708                      ; minimally-qualified # 👩🏿‍✈ E4.0 woman pilot: dark skin tone
1F9D1 200D 1F680                           ; fully-qualified     # 🧑‍🚀 E12.1 astronaut
1F9D1 1F3FB 200D 1F680                     ; fully-qualified     # 🧑🏻‍🚀 E12.1 astronaut: light skin tone
1F9D1 1F3FC 200D 1F680                     ; fully-qualified     # 🧑🏼‍🚀 E12.1 astronaut: medium-light skin tone
1F9D1 1F3FD 200D 1F680                     ; fully-qualified     # 🧑🏽‍🚀 E12.1 astronaut: medium skin tone
1F9D1 1F3FE 200D 1F680                     ; fully-qualified     # 🧑🏾‍🚀 E12.1 astronaut: medium-dark skin tone
1F9D1 1F3FF 200D 1F680                     ; fully-qualified     # 🧑🏿‍🚀 E12.1 astronaut: dark skin tone
1F468 200D 1F680                           ; fully-qualified     # 👨‍🚀 E4.0 man astronaut
1F468 1F3FB 200D 1F680                     ; fully-qualified     # 👨🏻‍🚀 E4.0 man astronaut: light skin tone
1F468 1F3FC 200D 1F680                     ; fully-qualified     # 👨🏼‍🚀 E4.0 man astronaut: medium-light skin tone
1F468 1F3FD 200D 1F680                     ; fully-qualified     # 👨🏽‍🚀 E4.0 man astronaut: medium skin tone
1F468 1F3FE 200D 1F680                     ; fully-qualified     # 👨🏾‍🚀 E4.0 man astronaut: medium-dark skin tone
1F468 1F3FF 200D 1F680                     ; fully-qualified     # 👨🏿‍🚀 E4.0 man astronaut: dark skin tone
1F469 200D 1F680                           ; fully-qualified     # 👩‍🚀 E4.0 woman astronaut
1F469 1F3FB 200D 1F680                     ; fully-qualified     # 👩🏻‍🚀 E4.0 woman astronaut: light skin tone
1F469 1F3FC 200D 1F680                     ; fully-qualified     # 👩🏼‍🚀 E4.0 woman astronaut: medium-light skin tone
1F469 1F3FD 200D 1F680                     ; fully-qualified     # 👩🏽‍🚀 E4.0 woman astronaut: medium skin tone
1F469 1F3FE 200D 1F680                     ; fully-qualified     # 👩🏾‍🚀 E4.0 woman astronaut: medium-dark skin tone
1F469 1F3FF 200D 1F680                     ; fully-qualified     # 👩🏿‍🚀 E4.0 woman astronaut: dark skin tone
1F9D1 200D 1F692                           ; fully-qualified     # 🧑‍🚒 E12.1 firefighter
1F9D1 1F3FB 200D 1F692                     ; fully-qualified     # 🧑🏻‍🚒 E12.1 firefighter: light skin tone
1F9D1 1F3FC 200D 1F692                     ; fully-qualified     # 🧑🏼‍🚒 E12.1 firefighter: medium-light skin tone
1F9D1 1F3FD 200D 1F692                     ; fully-qualified     # 🧑🏽‍🚒 E12.1 firefighter: medium skin tone
1F9D1 1F3FE 200D 1F692                     ; fully-qualified     # 🧑🏾‍🚒 E12.1 firefighter: medium-dark skin tone
1F9D1 1F3FF 200D 1F692                     ; fully-qualified     # 🧑🏿‍🚒 E12.1 firefighter: dark skin tone
1F468 200D 1F692                           ; fully-qualified     # 👨‍🚒 E4.0 man firefighter
1F468 1F3FB 200D 1F692                     ; fully-qualified     # 👨🏻‍🚒 E4.0 man firefighter: light skin tone
1F468 1F3FC 200D 1F692                     ; fully-qualified     # 👨🏼‍🚒 E4.0 man firefighter: medium-light skin tone
1F468 1F3FD 200D 1F692                     ; fully-qualified     # 👨🏽‍🚒 E4.0 man firefighter: medium skin tone
1F468 1F3FE 200D 1F692                     ; fully-qualified     # 👨🏾‍🚒 E4.0 man firefighter: medium-dark skin tone
1F468 1F3FF 200D 1F692                     ; fully-qualified     # 👨🏿‍🚒 E4.0 man firefighter: dark skin tone
1F469 200D 1F692                           ; fully-qualified     # 👩‍🚒 E4.0 woman firefighter
1F469 1F3FB 200D 1F692                     ; fully-qualified     # 👩🏻‍🚒 E4.0 woman firefighter: light skin tone
1F469 1F3FC 200D 1F692                     ; fully-qualified     # 👩🏼‍🚒 E4.0 woman firefighter: medium-light skin tone
1F469 1F3FD 200D 1F692                     ; fully-qualified     # 👩🏽‍🚒 E4.0 woman firefighter: medium skin tone
1F469 1F3FE 200D 1F692                     ; fully-qualified     # 👩🏾‍🚒 E4.0 woman firefighter: medium-dark skin tone
1F469 1F3FF 200D 1F692                     ; fully-qualified     # 👩🏿‍🚒 E4.0 woman firefighter: dark skin tone
1F46E                                      ; fully-qualified     # 👮 E0.6 police officer
1F46E 1F3FB                                ; fully-qualified     # 👮🏻 E1.0 police officer: light skin tone
1F46E 1F3FC                                ; fully-qualified     # 👮🏼 E1.0 police officer: medium-light skin tone
1F46E 1F3FD                                ; fully-qualified     # 👮🏽 E1.0 police officer: medium skin tone
1F46E 1F3FE                                ; fully-qualified     # 👮🏾 E1.0 police officer: medium-dark skin tone
1F46E 1F3FF                                ; fully-qualified     # 👮🏿 E1.0 police officer: dark skin tone
1F46E 200D 2642 FE0F                       ; fully-qualified     # 👮‍♂️ E4.0 man police officer
1F46E 200D 2642                            ; minimally-qualified # 👮‍♂ E4.0 man police officer
1F46E 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 👮🏻‍♂️ E4.0 man police officer: light skin tone
1F46E 1F3FB 200D 2642                      ; minimally-qualified # 👮🏻‍♂ E4.0 man police officer: light skin tone
1F46E 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 👮🏼‍♂️ E4.0 man police officer: medium-light skin tone
1F46E 1F3FC 200D 2642                      ; minimally-qualified # 👮🏼‍♂ E4.0 man police officer: medium-light skin tone
1F46E 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 👮🏽‍♂️ E4.0 man police officer: medium skin tone
1F46E 1F3FD 200D 2642                      ; minimally-qualified # 👮🏽‍♂ E4.0 man police officer: medium skin tone
1F46E 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 👮🏾‍♂️ E4.0 man police officer: medium-dark skin tone
1F46E 1F3FE 200D 2642                      ; minimally-qualified # 👮🏾‍♂ E4.0 man police officer: medium-dark skin tone
1F46E 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 👮🏿‍♂️ E4.0 man police officer: dark skin tone
1F46E 1F3FF 200D 2642                      ; minimally-qualified # 👮🏿‍♂ E4.0 man police officer: dark skin tone
1F46E 200D 2640 FE0F                       ; fully-qualified     # 👮‍♀️ E4.0 woman police officer
1F46E 200D 2640                            ; minimally-qualified # 👮‍♀ E4.0 woman police officer
1F46E 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 👮🏻‍♀️ E4.0 woman police officer: light skin tone
1F46E 1F3FB 200D 2640                      ; minimally-qualified # 👮🏻‍♀ E4.0 woman police officer: light skin tone
1F46E 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 👮🏼‍♀️ E4.0 woman police officer: medium-light skin tone
1F46E 1F3FC 200D 2640                      ; minimally-qualified # 👮🏼‍♀ E4.0 woman police officer: medium-light skin tone
1F46E 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 👮🏽‍♀️ E4.0 woman police officer: medium skin tone
1F46E 1F3FD 200D 2640                      ; minimally-qualified # 👮🏽‍♀ E4.0 woman police officer: medium skin tone
1F46E 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 👮🏾‍♀️ E4.0 woman police officer: medium-dark skin tone
1F46E 1F3FE 200D 2640                      ; minimally-qualified # 👮🏾‍♀ E4.0 woman police officer: medium-dark skin tone
1F46E 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 👮🏿‍♀️ E4.0 woman police officer: dark skin tone
1F46E 1F3FF 200D 2640                      ; minimally-qualified # 👮🏿‍♀ E4.0 woman police officer: dark skin tone
1F575 FE0F                                 ; fully-qualified     # 🕵️ E0.7 detective
1F575                                      ; unqualified         # 🕵 E0.7 detective
1F575 1F3FB                                ; fully-qualified     # 🕵🏻 E2.0 detective: light skin tone
1F575 1F3FC                                ; fully-qualified     # 🕵🏼 E2.0 detective: medium-light skin tone
1F575 1F3FD                                ; fully-qualified     # 🕵🏽 E2.0 detective: medium skin tone
1F575 1F3FE                                ; fully-qualified     # 🕵🏾 E2.0 detective: medium-dark skin tone
1F575 1F3FF                                ; fully-qualified     # 🕵🏿 E2.0 detective: dark skin tone
1F575 FE0F 200D 2642 FE0F                  ; fully-qualified     # 🕵️‍♂️ E4.0 man detective
1F575 200D 2642 FE0F                       ; unqualified         # 🕵‍♂️ E4.0 man detective
1F575 FE0F 200D 2642                       ; unqualified         # 🕵️‍♂ E4.0 man detective
1F575 200D 2642                            ; unqualified         # 🕵‍♂ E4.0 man detective
1F575 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🕵🏻‍♂️ E4.0 man detective: light skin tone
1F575 1F3FB 200D 2642                      ; minimally-qualified # 🕵🏻‍♂ E4.0 man detective: light skin tone
1F575 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🕵🏼‍♂️ E4.0 man detective: medium-light skin tone
1F575 1F3FC 200D 2642                      ; minimally-qualified # 🕵🏼‍♂ E4.0 man detective: medium-light skin tone
1F575 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🕵🏽‍♂️ E4.0 man detective: medium skin tone
1F575 1F3FD 200D 2642                      ; minimally-qualified # 🕵🏽‍♂ E4.0 man detective: medium skin tone
1F575 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🕵🏾‍♂️ E4.0 man detective: medium-dark skin tone
1F575 1F3FE 200D 2642                      ; minimally-qualified # 🕵🏾‍♂ E4.0 man detective: medium-dark skin tone
1F575 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🕵🏿‍♂️ E4.0 man detective: dark skin tone
1F575 1F3FF 200D 2642                      ; minimally-qualified # 🕵🏿‍♂ E4.0 man detective: dark skin tone
1F575 FE0F 200D 2640 FE0F                  ; fully-qualified     # 🕵️‍♀️ E4.0 woman detective
1F575 200D 2640 FE0F                       ; unqualified         # 🕵‍♀️ E4.0 woman detective
1F575 FE0F 200D 2640                       ; unqualified         # 🕵️‍♀ E4.0 woman detective
1F575 200D 2640                            ; unqualified         # 🕵‍♀ E4.0 woman detective
1F575 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🕵🏻‍♀️ E4.0 woman detective: light skin tone
1F575 1F3FB 200D 2640                      ; minimally-qualified # 🕵🏻‍♀ E4.0 woman detective: light skin tone
1F575 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🕵🏼‍♀️ E4.0 woman detective: medium-light skin tone
1F575 1F3FC 200D 2640                      ; minimally-qualified # 🕵🏼‍♀ E4.0 woman detective: medium-light skin tone
1F575 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🕵🏽‍♀️ E4.0 woman detective: medium skin tone
1F575 1F3FD 200D 2640                      ; minimally-qualified # 🕵🏽‍♀ E4.0 woman detective: medium skin tone
1F575 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🕵🏾‍♀️ E4.0 woman detective: medium-dark skin tone
1F575 1F3FE 200D 2640                      ; minimally-qualified # 🕵🏾‍♀ E4.0 woman detective: medium-dark skin tone
1F575 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🕵🏿‍♀️ E4.0 woman detective: dark skin tone
1F575 1F3FF 200D 2640                      ; minimally-qualified # 🕵🏿‍♀ E4.0 woman detective: dark skin tone
1F482                                      ; fully-qualified     # 💂 E0.6 guard
1F482 1F3FB                                ; fully-qualified     # 💂🏻 E1.0 guard: light skin tone
1F482 1F3FC                                ; fully-qualified     # 💂🏼 E1.0 guard: medium-light skin tone
1F482 1F3FD                                ; fully-qualified     # 💂🏽 E1.0 guard: medium skin tone
1F482 1F3FE                                ; fully-qualified     # 💂🏾 E1.0 guard: medium-dark skin tone
1F482 1F3FF                                ; fully-qualified     # 💂🏿 E1.0 guard: dark skin tone
1F482 200D 2642 FE0F                       ; fully-qualified     # 💂‍♂️ E4.0 man guard
1F482 200D 2642                            ; minimally-qualified # 💂‍♂ E4.0 man guard
1F482 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 💂🏻‍♂️ E4.0 man guard: light skin tone
1F482 1F3FB 200D 2642                      ; minimally-qualified # 💂🏻‍♂ E4.0 man guard: light skin tone
1F482 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 💂🏼‍♂️ E4.0 man guard: medium-light skin tone
1F482 1F3FC 200D 2642                      ; minimally-qualified # 💂🏼‍♂ E4.0 man guard: medium-light skin tone
1F482 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 💂🏽‍♂️ E4.0 man guard: medium skin tone
1F482 1F3FD 200D 2642                      ; minimally-qualified # 💂🏽‍♂ E4.0 man guard: medium skin tone
1F482 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 💂🏾‍♂️ E4.0 man guard: medium-dark skin tone
1F482 1F3FE 200D 2642                      ; minimally-qualified # 💂🏾‍♂ E4.0 man guard: medium-dark skin tone
1F482 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 💂🏿‍♂️ E4.0 man guard: dark skin tone
1F482 1F3FF 200D 2642                      ; minimally-qualified # 💂🏿‍♂ E4.0 man guard: dark skin tone
1F482 200D 2640 FE0F                       ; fully-qualified     # 💂‍♀️ E4.0 woman guard
1F482 200D 2640                            ; minimally-qualified # 💂‍♀ E4.0 woman guard
1F482 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 💂🏻‍♀️ E4.0 woman guard: light skin tone
1F482 1F3FB 200D 2640                      ; minimally-qualified # 💂🏻‍♀ E4.0 woman guard: light skin tone
1F482 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 💂🏼‍♀️ E4.0 woman guard: medium-light skin tone
1F482 1F3FC 200D 2640                      ; minimally-qualified # 💂🏼‍♀ E4.0 woman guard: medium-light skin tone
1F482 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 💂🏽‍♀️ E4.0 woman guard: medium skin tone
1F482 1F3FD 200D 2640                      ; minimally-qualified # 💂🏽‍♀ E4.0 woman guard: medium skin tone
1F482 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 💂🏾‍♀️ E4.0 woman guard: medium-dark skin tone
1F482 1F3FE 200D 2640                      ; minimally-qualified # 💂🏾‍♀ E4.0 woman guard: medium-dark skin tone
1F482 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 💂🏿‍♀️ E4.0 woman guard: dark skin tone
1F482 1F3FF 200D 2640                      ; minimally-qualified # 💂🏿‍♀ E4.0 woman guard: dark skin tone
1F977                                      ; fully-qualified     # 🥷 E13.0 ninja
1F977 1F3FB                                ; fully-qualified     # 🥷🏻 E13.0 ninja: light skin tone
1F977 1F3FC                                ; fully-qualified     # 🥷🏼 E13.0 ninja: medium-light skin tone
1F977 1F3FD                                ; fully-qualified     # 🥷🏽 E13.0 ninja: medium skin tone
1F977 1F3FE                                ; fully-qualified     # 🥷🏾 E13.0 ninja: medium-dark skin tone
1F977 1F3FF                                ; fully-qualified     # 🥷🏿 E13.0 ninja: dark skin tone
1F477                                      ; fully-qualified     # 👷 E0.6 construction worker
1F477 1F3FB                                ; fully-qualified     # 👷🏻 E1.0 construction worker: light skin tone
1F477 1F3FC                                ; fully-qualified     # 👷🏼 E1.0 construction worker: medium-light skin tone
1F477 1F3FD                                ; fully-qualified     # 👷🏽 E1.0 construction worker: medium skin tone
1F477 1F3FE                                ; fully-qualified     # 👷🏾 E1.0 construction worker: medium-dark skin tone
1F477 1F3FF                                ; fully-qualified     # 👷🏿 E1.0 construction worker: dark skin tone
1F477 200D 2642 FE0F                       ; fully-qualified     # 👷‍♂️ E4.0 man construction worker
1F477 200D 2642                            ; minimally-qualified # 👷‍♂ E4.0 man construction worker
1F477 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 👷🏻‍♂️ E4.0 man construction worker: light skin tone
1F477 1F3FB 200D 2642                      ; minimally-qualified # 👷🏻‍♂ E4.0 man construction worker: light skin tone
1F477 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 👷🏼‍♂️ E4.0 man construction worker: medium-light skin tone
1F477 1F3FC 200D 2642                      ; minimally-qualified # 👷🏼‍♂ E4.0 man construction worker: medium-light skin tone
1F477 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 👷🏽‍♂️ E4.0 man construction worker: medium skin tone
1F477 1F3FD 200D 2642                      ; minimally-qualified # 👷🏽‍♂ E4.0 man construction worker: medium skin tone
1F477 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 👷🏾‍♂️ E4.0 man construction worker: medium-dark skin tone
1F477 1F3FE 200D 2642                      ; minimally-qualified # 👷🏾‍♂ E4.0 man construction worker: medium-dark skin tone
1F477 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 👷🏿‍♂️ E4.0 man construction worker: dark skin tone
1F477 1F3FF 200D 2642                      ; minimally-qualified # 👷🏿‍♂ E4.0 man construction worker: dark skin tone
1F477 200D 2640 FE0F                       ; fully-qualified     # 👷‍♀️ E4.0 woman construction worker
1F477 200D 2640                            ; minimally-qualified # 👷‍♀ E4.0 woman construction worker
1F477 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 👷🏻‍♀️ E4.0 woman construction worker: light skin tone
1F477 1F3FB 200D 2640                      ; minimally-qualified # 👷🏻‍♀ E4.0 woman construction worker: light skin tone
1F477 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 👷🏼‍♀️ E4.0 woman construction worker: medium-light skin tone
1F477 1F3FC 200D 2640                      ; minimally-qualified # 👷🏼‍♀ E4.0 woman construction worker: medium-light skin tone
1F477 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 👷🏽‍♀️ E4.0 woman construction worker: medium skin tone
1F477 1F3FD 200D 2640                      ; minimally-qualified # 👷🏽‍♀ E4.0 woman construction worker: medium skin tone
1F477 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 👷🏾‍♀️ E4.0 woman construction worker: medium-dark skin tone
1F477 1F3FE 200D 2640                      ; minimally-qualified # 👷🏾‍♀ E4.0 woman construction worker: medium-dark skin tone
1F477 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 👷🏿‍♀️ E4.0 woman construction worker: dark skin tone
1F477 1F3FF 200D 2640                      ; minimally-qualified # 👷🏿‍♀ E4.0 woman construction worker: dark skin tone
1F934                                      ; fully-qualified     # 🤴 E3.0 prince
1F934 1F3FB                                ; fully-qualified     # 🤴🏻 E3.0 prince: light skin tone
1F934 1F3FC                                ; fully-qualified     # 🤴🏼 E3.0 prince: medium-light skin tone
1F934 1F3FD                                ; fully-qualified     # 🤴🏽 E3.0 prince: medium skin tone
1F934 1F3FE                                ; fully-qualified     # 🤴🏾 E3.0 prince: medium-dark skin tone
1F934 1F3FF                                ; fully-qualified     # 🤴🏿 E3.0 prince: dark skin tone
1F478                                      ; fully-qualified     # 👸 E0.6 princess
1F478 1F3FB                                ; fully-qualified     # 👸🏻 E1.0 princess: light skin tone
1F478 1F3FC                                ; fully-qualified     # 👸🏼 E1.0 princess: medium-light skin tone
1F478 1F3FD                                ; fully-qualified     # 👸🏽 E1.0 princess: medium skin tone
1F478 1F3FE                                ; fully-qualified     # 👸🏾 E1.0 princess: medium-dark skin tone
1F478 1F3FF                                ; fully-qualified     # 👸🏿 E1.0 princess: dark skin tone
1F473                                      ; fully-qualified     # 👳 E0.6 person wearing turban
1F473 1F3FB                                ; fully-qualified     # 👳🏻 E1.0 person wearing turban: light skin tone
1F473 1F3FC                                ; fully-qualified     # 👳🏼 E1.0 person wearing turban: medium-light skin tone
1F473 1F3FD                                ; fully-qualified     # 👳🏽 E1.0 person wearing turban: medium skin tone
1F473 1F3FE                                ; fully-qualified     # 👳🏾 E1.0 person wearing turban: medium-dark skin tone
1F473 1F3FF                                ; fully-qualified     # 👳🏿 E1.0 person wearing turban: dark skin tone
1F473 200D 2642 FE0F                       ; fully-qualified     # 👳‍♂️ E4.0 man wearing turban
1F473 200D 2642                            ; minimally-qualified # 👳‍♂ E4.0 man wearing turban
1F473 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 👳🏻‍♂️ E4.0 man wearing turban: light skin tone
1F473 1F3FB 200D 2642                      ; minimally-qualified # 👳🏻‍♂ E4.0 man wearing turban: light skin tone
1F473 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 👳🏼‍♂️ E4.0 man wearing turban: medium-light skin tone
1F473 1F3FC 200D 2642                      ; minimally-qualified # 👳🏼‍♂ E4.0 man wearing turban: medium-light skin tone
1F473 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 👳🏽‍♂️ E4.0 man wearing turban: medium skin tone
1F473 1F3FD 200D 2642                      ; minimally-qualified # 👳🏽‍♂ E4.0 man wearing turban: medium skin tone
1F473 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 👳🏾‍♂️ E4.0 man wearing turban: medium-dark skin tone
1F473 1F3FE 200D 2642                      ; minimally-qualified # 👳🏾‍♂ E4.0 man wearing turban: medium-dark skin tone
1F473 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 👳🏿‍♂️ E4.0 man wearing turban: dark skin tone
1F473 1F3FF 200D 2642                      ; minimally-qualified # 👳🏿‍♂ E4.0 man wearing turban: dark skin tone
1F473 200D 2640 FE0F                       ; fully-qualified     # 👳‍♀️ E4.0 woman wearing turban
1F473 200D 2640                            ; minimally-qualified # 👳‍♀ E4.0 woman wearing turban
1F473 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 👳🏻‍♀️ E4.0 woman wearing turban: light skin tone
1F473 1F3FB 200D 2640                      ; minimally-qualified # 👳🏻‍♀ E4.0 woman wearing turban: light skin tone
1F473 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 👳🏼‍♀️ E4.0 woman wearing turban: medium-light skin tone
1F473 1F3FC 200D 2640                      ; minimally-qualified # 👳🏼‍♀ E4.0 woman wearing turban: medium-light skin tone
1F473 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 👳🏽‍♀️ E4.0 woman wearing turban: medium skin tone
1F473 1F3FD 200D 2640                      ; minimally-qualified # 👳🏽‍♀ E4.0 woman wearing turban: medium skin tone
1F473 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 👳🏾‍♀️ E4.0 woman wearing turban: medium-dark skin tone
1F473 1F3FE 200D 2640                      ; minimally-qualified # 👳🏾‍♀ E4.0 woman wearing turban: medium-dark skin tone
1F473 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 👳🏿‍♀️ E4.0 woman wearing turban: dark skin tone
1F473 1F3FF 200D 2640                      ; minimally-qualified # 👳🏿‍♀ E4.0 woman wearing turban: dark skin tone
1F472                                      ; fully-qualified     # 👲 E0.6 person with skullcap
1F472 1F3FB                                ; fully-qualified     # 👲🏻 E1.0 person with skullcap: light skin tone
1F472 1F3FC                                ; fully-qualified     # 👲🏼 E1.0 person with skullcap: medium-light skin tone
1F472 1F3FD                                ; fully-qualified     # 👲🏽 E1.0 person with skullcap: medium skin tone
1F472 1F3FE                                ; fully-qualified     # 👲🏾 E1.0 person with skullcap: medium-dark skin tone
1F472 1F3FF                                ; fully-qualified     # 👲🏿 E1.0 person with skullcap: dark skin tone
1F9D5                                      ; fully-qualified     # 🧕 E5.0 woman with headscarf
1F9D5 1F3FB                                ; fully-qualified     # 🧕🏻 E5.0 woman with headscarf: light skin tone
1F9D5 1F3FC                                ; fully-qualified     # 🧕🏼 E5.0 woman with headscarf: medium-light skin tone
1F9D5 1F3FD                                ; fully-qualified     # 🧕🏽 E5.0 woman with headscarf: medium skin tone
1F9D5 1F3FE                                ; fully-qualified     # 🧕🏾 E5.0 woman with headscarf: medium-dark skin tone
1F9D5 1F3FF                                ; fully-qualified     # 🧕🏿 E5.0 woman with headscarf: dark skin tone
1F935                                      ; fully-qualified     # 🤵 E3.0 person in tuxedo
1F935 1F3FB                                ; fully-qualified     # 🤵🏻 E3.0 person in tuxedo: light skin tone
1F935 1F3FC                                ; fully-qualified     # 🤵🏼 E3.0 person in tuxedo: medium-light skin tone
1F935 1F3FD                                ; fully-qualified     # 🤵🏽 E3.0 person in tuxedo: medium skin tone
1F935 1F3FE                                ; fully-qualified     # 🤵🏾 E3.0 person in tuxedo: medium-dark skin tone
1F935 1F3FF                                ; fully-qualified     # 🤵🏿 E3.0 person in tuxedo: dark skin tone
1F935 200D 2642 FE0F                       ; fully-qualified     # 🤵‍♂️ E13.0 man in tuxedo
1F935 200D 2642                            ; minimally-qualified # 🤵‍♂ E13.0 man in tuxedo
1F935 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🤵🏻‍♂️ E13.0 man in tuxedo: light skin tone
1F935 1F3FB 200D 2642                      ; minimally-qualified # 🤵🏻‍♂ E13.0 man in tuxedo: light skin tone
1F935 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🤵🏼‍♂️ E13.0 man in tuxedo: medium-light skin tone
1F935 1F3FC 200D 2642                      ; minimally-qualified # 🤵🏼‍♂ E13.0 man in tuxedo: medium-light skin tone
1F935 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🤵🏽‍♂️ E13.0 man in tuxedo: medium skin tone
1F935 1F3FD 200D 2642                      ; minimally-qualified # 🤵🏽‍♂ E13.0 man in tuxedo: medium skin tone
1F935 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🤵🏾‍♂️ E13.0 man in tuxedo: medium-dark skin tone
1F935 1F3FE 200D 2642                      ; minimally-qualified # 🤵🏾‍♂ E13.0 man in tuxedo: medium-dark skin tone
1F935 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🤵🏿‍♂️ E13.0 man in tuxedo: dark skin tone
1F935 1F3FF 200D 2642                      ; minimally-qualified # 🤵🏿‍♂ E13.0 man in tuxedo: dark skin tone
1F935 200D 2640 FE0F                       ; fully-qualified     # 🤵‍♀️ E13.0 woman in tuxedo
1F935 200D 2640                            ; minimally-qualified # 🤵‍♀ E13.0 woman in tuxedo
1F935 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🤵🏻‍♀️ E13.0 woman in tuxedo: light skin tone
1F935 1F3FB 200D 2640                      ; minimally-qualified # 🤵🏻‍♀ E13.0 woman in tuxedo: light skin tone
1F935 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🤵🏼‍♀️ E13.0 woman in tuxedo: medium-light skin tone
1F935 1F3FC 200D 2640                      ; minimally-qualified # 🤵🏼‍♀ E13.0 woman in tuxedo: medium-light skin tone
1F935 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🤵🏽‍♀️ E13.0 woman in tuxedo: medium skin tone
1F935 1F3FD 200D 2640                      ; minimally-qualified # 🤵🏽‍♀ E13.0 woman in tuxedo: medium skin tone
1F935 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🤵🏾‍♀️ E13.0 woman in tuxedo: medium-dark skin tone
1F935 1F3FE 200D 2640                      ; minimally-qualified # 🤵🏾‍♀ E13.0 woman in tuxedo: medium-dark skin tone
1F935 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🤵🏿‍♀️ E13.0 woman in tuxedo: dark skin tone
1F935 1F3FF 200D 2640                      ; minimally-qualified # 🤵🏿‍♀ E13.0 woman in tuxedo: dark skin tone
1F470                                      ; fully-qualified     # 👰 E0.6 person with veil
1F470 1F3FB                                ; fully-qualified     # 👰🏻 E1.0 person with veil: light skin tone
1F470 1F3FC                                ; fully-qualified     # 👰🏼 E1.0 person with veil: medium-light skin tone
1F470 1F3FD                                ; fully-qualified     # 👰🏽 E1.0 person with veil: medium skin tone
1F470 1F3FE                                ; fully-qualified     # 👰🏾 E1.0 person with veil: medium-dark skin tone
1F470 1F3FF                                ; fully-qualified     # 👰🏿 E1.0 person with veil: dark skin tone
1F470 200D 2642 FE0F                       ; fully-qualified     # 👰‍♂️ E13.0 man with veil
1F470 200D 2642                            ; minimally-qualified # 👰‍♂ E13.0 man with veil
1F470 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 👰🏻‍♂️ E13.0 man with veil: light skin tone
1F470 1F3FB 200D 2642                      ; minimally-qualified # 👰🏻‍♂ E13.0 man with veil: light skin tone
1F470 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 👰🏼‍♂️ E13.0 man with veil: medium-light skin tone
1F470 1F3FC 200D 2642                      ; minimally-qualified # 👰🏼‍♂ E13.0 man with veil: medium-light skin tone
1F470 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 👰🏽‍♂️ E13.0 man with veil: medium skin tone
1F470 1F3FD 200D 2642                      ; minimally-qualified # 👰🏽‍♂ E13.0 man with veil: medium skin tone
1F470 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 👰🏾‍♂️ E13.0 man with veil: medium-dark skin tone
1F470 1F3FE 200D 2642                      ; minimally-qualified # 👰🏾‍♂ E13.0 man with veil: medium-dark skin tone
1F470 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 👰🏿‍♂️ E13.0 man with veil: dark skin tone
1F470 1F3FF 200D 2642                      ; minimally-qualified # 👰🏿‍♂ E13.0 man with veil: dark skin tone
1F470 200D 2640 FE0F                       ; fully-qualified     # 👰‍♀️ E13.0 woman with veil
1F470 200D 2640                            ; minimally-qualified # 👰‍♀ E13.0 woman with veil
1F470 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 👰🏻‍♀️ E13.0 woman with veil: light skin tone
1F470 1F3FB 200D 2640                      ; minimally-qualified # 👰🏻‍♀ E13.0 woman with veil: light skin tone
1F470 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 👰🏼‍♀️ E13.0 woman with veil: medium-light skin tone
1F470 1F3FC 200D 2640                      ; minimally-qualified # 👰🏼‍♀ E13.0 woman with veil: medium-light skin tone
1F470 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 👰🏽‍♀️ E13.0 woman with veil: medium skin tone
1F470 1F3FD 200D 2640                      ; minimally-qualified # 👰🏽‍♀ E13.0 woman with veil: medium skin tone
1F470 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 👰🏾‍♀️ E13.0 woman with veil: medium-dark skin tone
1F470 1F3FE 200D 2640                      ; minimally-qualified # 👰🏾‍♀ E13.0 woman with veil: medium-dark skin tone
1F470 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 👰🏿‍♀️ E13.0 woman with veil: dark skin tone
1F470 1F3FF 200D 2640                      ; minimally-qualified # 👰🏿‍♀ E13.0 woman with veil: dark skin tone
1F930                                      ; fully-qualified     # 🤰 E3.0 pregnant woman
1F930 1F3FB                                ; fully-qualified     # 🤰🏻 E3.0 pregnant woman: light skin tone
1F930 1F3FC                                ; fully-qualified     # 🤰🏼 E3.0 pregnant woman: medium-light skin tone
1F930 1F3FD                                ; fully-qualified     # 🤰🏽 E3.0 pregnant woman: medium skin tone
1F930 1F3FE                                ; fully-qualified     # 🤰🏾 E3.0 pregnant woman: medium-dark skin tone
1F930 1F3FF                                ; fully-qualified     # 🤰🏿 E3.0 pregnant woman: dark skin tone
1F931                                      ; fully-qualified     # 🤱 E5.0 breast-feeding
1F931 1F3FB                                ; fully-qualified     # 🤱🏻 E5.0 breast-feeding: light skin tone
1F931 1F3FC                                ; fully-qualified     # 🤱🏼 E5.0 breast-feeding: medium-light skin tone
1F931 1F3FD                                ; fully-qualified     # 🤱🏽 E5.0 breast-feeding: medium skin tone
1F931 1F3FE                                ; fully-qualified     # 🤱🏾 E5.0 breast-feeding: medium-dark skin tone
1F931 1F3FF                                ; fully-qualified     # 🤱🏿 E5.0 breast-feeding: dark skin tone
1F469 200D 1F37C                           ; fully-qualified     # 👩‍🍼 E13.0 woman feeding baby
1F469 1F3FB 200D 1F37C                     ; fully-qualified     # 👩🏻‍🍼 E13.0 woman feeding baby: light skin tone
1F469 1F3FC 200D 1F37C                     ; fully-qualified     # 👩🏼‍🍼 E13.0 woman feeding baby: medium-light skin tone
1F469 1F3FD 200D 1F37C                     ; fully-qualified     # 👩🏽‍🍼 E13.0 woman feeding baby: medium skin tone
1F469 1F3FE 200D 1F37C                     ; fully-qualified     # 👩🏾‍🍼 E13.0 woman feeding baby: medium-dark skin tone
1F469 1F3FF 200D 1F37C                     ; fully-qualified     # 👩🏿‍🍼 E13.0 woman feeding baby: dark skin tone
1F468 200D 1F37C                           ; fully-qualified     # 👨‍🍼 E13.0 man feeding baby
1F468 1F3FB 200D 1F37C                     ; fully-qualified     # 👨🏻‍🍼 E13.0 man feeding baby: light skin tone
1F468 1F3FC 200D 1F37C                     ; fully-qualified     # 👨🏼‍🍼 E13.0 man feeding baby: medium-light skin tone
1F468 1F3FD 200D 1F37C                     ; fully-qualified     # 👨🏽‍🍼 E13.0 man feeding baby: medium skin tone
1F468 1F3FE 200D 1F37C                     ; fully-qualified     # 👨🏾‍🍼 E13.0 man feeding baby: medium-dark skin tone
1F468 1F3FF 200D 1F37C                     ; fully-qualified     # 👨🏿‍🍼 E13.0 man feeding baby: dark skin tone
1F9D1 200D 1F37C                           ; fully-qualified     # 🧑‍🍼 E13.0 person feeding baby
1F9D1 1F3FB 200D 1F37C                     ; fully-qualified     # 🧑🏻‍🍼 E13.0 person feeding baby: light skin tone
1F9D1 1F3FC 200D 1F37C                     ; fully-qualified     # 🧑🏼‍🍼 E13.0 person feeding baby: medium-light skin tone
1F9D1 1F3FD 200D 1F37C                     ; fully-qualified     # 🧑🏽‍🍼 E13.0 person feeding baby: medium skin tone
1F9D1 1F3FE 200D 1F37C                     ; fully-qualified     # 🧑🏾‍🍼 E13.0 person feeding baby: medium-dark skin tone
1F9D1 1F3FF 200D 1F37C                     ; fully-qualified     # 🧑🏿‍🍼 E13.0 person feeding baby: dark skin tone

# subgroup: person-fantasy
1F47C                                      ; fully-qualified     # 👼 E0.6 baby angel
1F47C 1F3FB                                ; fully-qualified     # 👼🏻 E1.0 baby angel: light skin tone
1F47C 1F3FC                                ; fully-qualified     # 👼🏼 E1.0 baby angel: medium-light skin tone
1F47C 1F3FD                                ; fully-qualified     # 👼🏽 E1.0 baby angel: medium skin tone
1F47C 1F3FE                                ; fully-qualified     # 👼🏾 E1.0 baby angel: medium-dark skin tone
1F47C 1F3FF                                ; fully-qualified     # 👼🏿 E1.0 baby angel: dark skin tone
1F385                                      ; fully-qualified     # 🎅 E0.6 Santa Claus
1F385 1F3FB                                ; fully-qualified     # 🎅🏻 E1.0 Santa Claus: light skin tone
1F385 1F3FC                                ; fully-qualified     # 🎅🏼 E1.0 Santa Claus: medium-light skin tone
1F385 1F3FD                                ; fully-qualified     # 🎅🏽 E1.0 Santa Claus: medium skin tone
1F385 1F3FE                                ; fully-qualified     # 🎅🏾 E1.0 Santa Claus: medium-dark skin tone
1F385 1F3FF                                ; fully-qualified     # 🎅🏿 E1.0 Santa Claus: dark skin tone
1F936                                      ; fully-qualified     # 🤶 E3.0 Mrs. Claus
1F936 1F3FB                                ; fully-qualified     # 🤶🏻 E3.0 Mrs. Claus: light skin tone
1F936 1F3FC                                ; fully-qualified     # 🤶🏼 E3.0 Mrs. Claus: medium-light skin tone
1F936 1F3FD                                ; fully-qualified     # 🤶🏽 E3.0 Mrs. Claus: medium skin tone
1F936 1F3FE                                ; fully-qualified     # 🤶🏾 E3.0 Mrs. Claus: medium-dark skin tone
1F936 1F3FF                                ; fully-qualified     # 🤶🏿 E3.0 Mrs. Claus: dark skin tone
1F9D1 200D 1F384                           ; fully-qualified     # 🧑‍🎄 E13.0 mx claus
1F9D1 1F3FB 200D 1F384                     ; fully-qualified     # 🧑🏻‍🎄 E13.0 mx claus: light skin tone
1F9D1 1F3FC 200D 1F384                     ; fully-qualified     # 🧑🏼‍🎄 E13.0 mx claus: medium-light skin tone
1F9D1 1F3FD 200D 1F384                     ; fully-qualified     # 🧑🏽‍🎄 E13.0 mx claus: medium skin tone
1F9D1 1F3FE 200D 1F384                     ; fully-qualified     # 🧑🏾‍🎄 E13.0 mx claus: medium-dark skin tone
1F9D1 1F3FF 200D 1F384                     ; fully-qualified     # 🧑🏿‍🎄 E13.0 mx claus: dark skin tone
1F9B8                                      ; fully-qualified     # 🦸 E11.0 superhero
1F9B8 1F3FB                                ; fully-qualified     # 🦸🏻 E11.0 superhero: light skin tone
1F9B8 1F3FC                                ; fully-qualified     # 🦸🏼 E11.0 superhero: medium-light skin tone
1F9B8 1F3FD                                ; fully-qualified     # 🦸🏽 E11.0 superhero: medium skin tone
1F9B8 1F3FE                                ; fully-qualified     # 🦸🏾 E11.0 superhero: medium-dark skin tone
1F9B8 1F3FF                                ; fully-qualified     # 🦸🏿 E11.0 superhero: dark skin tone
1F9B8 200D 2642 FE0F                       ; fully-qualified     # 🦸‍♂️ E11.0 man superhero
1F9B8 200D 2642                            ; minimally-qualified # 🦸‍♂ E11.0 man superhero
1F9B8 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🦸🏻‍♂️ E11.0 man superhero: light skin tone
1F9B8 1F3FB 200D 2642                      ; minimally-qualified # 🦸🏻‍♂ E11.0 man superhero: light skin tone
1F9B8 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🦸🏼‍♂️ E11.0 man superhero: medium-light skin tone
1F9B8 1F3FC 200D 2642                      ; minimally-qualified # 🦸🏼‍♂ E11.0 man superhero: medium-light skin tone
1F9B8 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🦸🏽‍♂️ E11.0 man superhero: medium skin tone
1F9B8 1F3FD 200D 2642                      ; minimally-qualified # 🦸🏽‍♂ E11.0 man superhero: medium skin tone
1F9B8 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🦸🏾‍♂️ E11.0 man superhero: medium-dark skin tone
1F9B8 1F3FE 200D 2642                      ; minimally-qualified # 🦸🏾‍♂ E11.0 man superhero: medium-dark skin tone
1F9B8 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🦸🏿‍♂️ E11.0 man superhero: dark skin tone
1F9B8 1F3FF 200D 2642                      ; minimally-qualified # 🦸🏿‍♂ E11.0 man superhero: dark skin tone
1F9B8 200D 2640 FE0F                       ; fully-qualified     # 🦸‍♀️ E11.0 woman superhero
1F9B8 200D 2640                            ; minimally-qualified # 🦸‍♀ E11.0 woman superhero
1F9B8 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🦸🏻‍♀️ E11.0 woman superhero: light skin tone
1F9B8 1F3FB 200D 2640                      ; minimally-qualified # 🦸🏻‍♀ E11.0 woman superhero: light skin tone
1F9B8 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🦸🏼‍♀️ E11.0 woman superhero: medium-light skin tone
1F9B8 1F3FC 200D 2640                      ; minimally-qualified # 🦸🏼‍♀ E11.0 woman superhero: medium-light skin tone
1F9B8 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🦸🏽‍♀️ E11.0 woman superhero: medium skin tone
1F9B8 1F3FD 200D 2640                      ; minimally-qualified # 🦸🏽‍♀ E11.0 woman superhero: medium skin tone
1F9B8 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🦸🏾‍♀️ E11.0 woman superhero: medium-dark skin tone
1F9B8 1F3FE 200D 2640                      ; minimally-qualified # 🦸🏾‍♀ E11.0 woman superhero: medium-dark skin tone
1F9B8 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🦸🏿‍♀️ E11.0 woman superhero: dark skin tone
1F9B8 1F3FF 200D 2640                      ; minimally-qualified # 🦸🏿‍♀ E11.0 woman superhero: dark skin tone
1F9B9                                      ; fully-qualified     # 🦹 E11.0 supervillain
1F9B9 1F3FB                                ; fully-qualified     # 🦹🏻 E11.0 supervillain: light skin tone
1F9B9 1F3FC                                ; fully-qualified     # 🦹🏼 E11.0 supervillain: medium-light skin tone
1F9B9 1F3FD                                ; fully-qualified     # 🦹🏽 E11.0 supervillain: medium skin tone
1F9B9 1F3FE                                ; fully-qualified     # 🦹🏾 E11.0 supervillain: medium-dark skin tone
1F9B9 1F3FF                                ; fully-qualified     # 🦹🏿 E11.0 supervillain: dark skin tone
1F9B9 200D 2642 FE0F                       ; fully-qualified     # 🦹‍♂️ E11.0 man supervillain
1F9B9 200D 2642                            ; minimally-qualified # 🦹‍♂ E11.0 man supervillain
1F9B9 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🦹🏻‍♂️ E11.0 man supervillain: light skin tone
1F9B9 1F3FB 200D 2642                      ; minimally-qualified # 🦹🏻‍♂ E11.0 man supervillain: light skin tone
1F9B9 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🦹🏼‍♂️ E11.0 man supervillain: medium-light skin tone
1F9B9 1F3FC 200D 2642                      ; minimally-qualified # 🦹🏼‍♂ E11.0 man supervillain: medium-light skin tone
1F9B9 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🦹🏽‍♂️ E11.0 man supervillain: medium skin tone
1F9B9 1F3FD 200D 2642                      ; minimally-qualified # 🦹🏽‍♂ E11.0 man supervillain: medium skin tone
1F9B9 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🦹🏾‍♂️ E11.0 man supervillain: medium-dark skin tone
1F9B9 1F3FE 200D 2642                      ; minimally-qualified # 🦹🏾‍♂ E11.0 man supervillain: medium-dark skin tone
1F9B9 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🦹🏿‍♂️ E11.0 man supervillain: dark skin tone
1F9B9 1F3FF 200D 2642                      ; minimally-qualified # 🦹🏿‍♂ E11.0 man supervillain: dark skin tone
1F9B9 200D 2640 FE0F                       ; fully-qualified     # 🦹‍♀️ E11.0 woman supervillain
1F9B9 200D 2640                            ; minimally-qualified # 🦹‍♀ E11.0 woman supervillain
1F9B9 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🦹🏻‍♀️ E11.0 woman supervillain: light skin tone
1F9B9 1F3FB 200D 2640                      ; minimally-qualified # 🦹🏻‍♀ E11.0 woman supervillain: light skin tone
1F9B9 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🦹🏼‍♀️ E11.0 woman supervillain: medium-light skin tone
1F9B9 1F3FC 200D 2640                      ; minimally-qualified # 🦹🏼‍♀ E11.0 woman supervillain: medium-light skin tone
1F9B9 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🦹🏽‍♀️ E11.0 woman supervillain: medium skin tone
1F9B9 1F3FD 200D 2640                      ; minimally-qualified # 🦹🏽‍♀ E11.0 woman supervillain: medium skin tone
1F9B9 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🦹🏾‍♀️ E11.0 woman supervillain: medium-dark skin tone
1F9B9 1F3FE 200D 2640                      ; minimally-qualified # 🦹🏾‍♀ E11.0 woman supervillain: medium-dark skin tone
1F9B9 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🦹🏿‍♀️ E11.0 woman supervillain: dark skin tone
1F9B9 1F3FF 200D 2640                      ; minimally-qualified # 🦹🏿‍♀ E11.0 woman supervillain: dark skin tone
1F9D9                                      ; fully-qualified     # 🧙 E5.0 mage
1F9D9 1F3FB                                ; fully-qualified     # 🧙🏻 E5.0 mage: light skin tone
1F9D9 1F3FC                                ; fully-qualified     # 🧙🏼 E5.0 mage: medium-light skin tone
1F9D9 1F3FD                                ; fully-qualified     # 🧙🏽 E5.0 mage: medium skin tone
1F9D9 1F3FE                                ; fully-qualified     # 🧙🏾 E5.0 mage: medium-dark skin tone
1F9D9 1F3FF                                ; fully-qualified     # 🧙🏿 E5.0 mage: dark skin tone
1F9D9 200D 2642 FE0F                       ; fully-qualified     # 🧙‍♂️ E5.0 man mage
1F9D9 200D 2642                            ; minimally-qualified # 🧙‍♂ E5.0 man mage
1F9D9 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧙🏻‍♂️ E5.0 man mage: light skin tone
1F9D9 1F3FB 200D 2642                      ; minimally-qualified # 🧙🏻‍♂ E5.0 man mage: light skin tone
1F9D9 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧙🏼‍♂️ E5.0 man mage: medium-light skin tone
1F9D9 1F3FC 200D 2642                      ; minimally-qualified # 🧙🏼‍♂ E5.0 man mage: medium-light skin tone
1F9D9 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧙🏽‍♂️ E5.0 man mage: medium skin tone
1F9D9 1F3FD 200D 2642                      ; minimally-qualified # 🧙🏽‍♂ E5.0 man mage: medium skin tone
1F9D9 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧙🏾‍♂️ E5.0 man mage: medium-dark skin tone
1F9D9 1F3FE 200D 2642                      ; minimally-qualified # 🧙🏾‍♂ E5.0 man mage: medium-dark skin tone
1F9D9 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧙🏿‍♂️ E5.0 man mage: dark skin tone
1F9D9 1F3FF 200D 2642                      ; minimally-qualified # 🧙🏿‍♂ E5.0 man mage: dark skin tone
1F9D9 200D 2640 FE0F                       ; fully-qualified     # 🧙‍♀️ E5.0 woman mage
1F9D9 200D 2640                            ; minimally-qualified # 🧙‍♀ E5.0 woman mage
1F9D9 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧙🏻‍♀️ E5.0 woman mage: light skin tone
1F9D9 1F3FB 200D 2640                      ; minimally-qualified # 🧙🏻‍♀ E5.0 woman mage: light skin tone
1F9D9 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧙🏼‍♀️ E5.0 woman mage: medium-light skin tone
1F9D9 1F3FC 200D 2640                      ; minimally-qualified # 🧙🏼‍♀ E5.0 woman mage: medium-light skin tone
1F9D9 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧙🏽‍♀️ E5.0 woman mage: medium skin tone
1F9D9 1F3FD 200D 2640                      ; minimally-qualified # 🧙🏽‍♀ E5.0 woman mage: medium skin tone
1F9D9 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧙🏾‍♀️ E5.0 woman mage: medium-dark skin tone
1F9D9 1F3FE 200D 2640                      ; minimally-qualified # 🧙🏾‍♀ E5.0 woman mage: medium-dark skin tone
1F9D9 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧙🏿‍♀️ E5.0 woman mage: dark skin tone
1F9D9 1F3FF 200D 2640                      ; minimally-qualified # 🧙🏿‍♀ E5.0 woman mage: dark skin tone
1F9DA                                      ; fully-qualified     # 🧚 E5.0 fairy
1F9DA 1F3FB                                ; fully-qualified     # 🧚🏻 E5.0 fairy: light skin tone
1F9DA 1F3FC                                ; fully-qualified     # 🧚🏼 E5.0 fairy: medium-light skin tone
1F9DA 1F3FD                                ; fully-qualified     # 🧚🏽 E5.0 fairy: medium skin tone
1F9DA 1F3FE                                ; fully-qualified     # 🧚🏾 E5.0 fairy: medium-dark skin tone
1F9DA 1F3FF                                ; fully-qualified     # 🧚🏿 E5.0 fairy: dark skin tone
1F9DA 200D 2642 FE0F                       ; fully-qualified     # 🧚‍♂️ E5.0 man fairy
1F9DA 200D 2642                            ; minimally-qualified # 🧚‍♂ E5.0 man fairy
1F9DA 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧚🏻‍♂️ E5.0 man fairy: light skin tone
1F9DA 1F3FB 200D 2642                      ; minimally-qualified # 🧚🏻‍♂ E5.0 man fairy: light skin tone
1F9DA 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧚🏼‍♂️ E5.0 man fairy: medium-light skin tone
1F9DA 1F3FC 200D 2642                      ; minimally-qualified # 🧚🏼‍♂ E5.0 man fairy: medium-light skin tone
1F9DA 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧚🏽‍♂️ E5.0 man fairy: medium skin tone
1F9DA 1F3FD 200D 2642                      ; minimally-qualified # 🧚🏽‍♂ E5.0 man fairy: medium skin tone
1F9DA 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧚🏾‍♂️ E5.0 man fairy: medium-dark skin tone
1F9DA 1F3FE 200D 2642                      ; minimally-qualified # 🧚🏾‍♂ E5.0 man fairy: medium-dark skin tone
1F9DA 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧚🏿‍♂️ E5.0 man fairy: dark skin tone
1F9DA 1F3FF 200D 2642                      ; minimally-qualified # 🧚🏿‍♂ E5.0 man fairy: dark skin tone
1F9DA 200D 2640 FE0F                       ; fully-qualified     # 🧚‍♀️ E5.0 woman fairy
1F9DA 200D 2640                            ; minimally-qualified # 🧚‍♀ E5.0 woman fairy
1F9DA 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧚🏻‍♀️ E5.0 woman fairy: light skin tone
1F9DA 1F3FB 200D 2640                      ; minimally-qualified # 🧚🏻‍♀ E5.0 woman fairy: light skin tone
1F9DA 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧚🏼‍♀️ E5.0 woman fairy: medium-light skin tone
1F9DA 1F3FC 200D 2640                      ; minimally-qualified # 🧚🏼‍♀ E5.0 woman fairy: medium-light skin tone
1F9DA 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧚🏽‍♀️ E5.0 woman fairy: medium skin tone
1F9DA 1F3FD 200D 2640                      ; minimally-qualified # 🧚🏽‍♀ E5.0 woman fairy: medium skin tone
1F9DA 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧚🏾‍♀️ E5.0 woman fairy: medium-dark skin tone
1F9DA 1F3FE 200D 2640                      ; minimally-qualified # 🧚🏾‍♀ E5.0 woman fairy: medium-dark skin tone
1F9DA 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧚🏿‍♀️ E5.0 woman fairy: dark skin tone
1F9DA 1F3FF 200D 2640                      ; minimally-qualified # 🧚🏿‍♀ E5.0 woman fairy: dark skin tone
1F9DB                                      ; fully-qualified     # 🧛 E5.0 vampire
1F9DB 1F3FB                                ; fully-qualified     # 🧛🏻 E5.0 vampire: light skin tone
1F9DB 1F3FC                                ; fully-qualified     # 🧛🏼 E5.0 vampire: medium-light skin tone
1F9DB 1F3FD                                ; fully-qualified     # 🧛🏽 E5.0 vampire: medium skin tone
1F9DB 1F3FE                                ; fully-qualified     # 🧛🏾 E5.0 vampire: medium-dark skin tone
1F9DB 1F3FF                                ; fully-qualified     # 🧛🏿 E5.0 vampire: dark skin tone
1F9DB 200D 2642 FE0F                       ; fully-qualified     # 🧛‍♂️ E5.0 man vampire
1F9DB 200D 2642                            ; minimally-qualified # 🧛‍♂ E5.0 man vampire
1F9DB 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧛🏻‍♂️ E5.0 man vampire: light skin tone
1F9DB 1F3FB 200D 2642                      ; minimally-qualified # 🧛🏻‍♂ E5.0 man vampire: light skin tone
1F9DB 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧛🏼‍♂️ E5.0 man vampire: medium-light skin tone
1F9DB 1F3FC 200D 2642                      ; minimally-qualified # 🧛🏼‍♂ E5.0 man vampire: medium-light skin tone
1F9DB 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧛🏽‍♂️ E5.0 man vampire: medium skin tone
1F9DB 1F3FD 200D 2642                      ; minimally-qualified # 🧛🏽‍♂ E5.0 man vampire: medium skin tone
1F9DB 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧛🏾‍♂️ E5.0 man vampire: medium-dark skin tone
1F9DB 1F3FE 200D 2642                      ; minimally-qualified # 🧛🏾‍♂ E5.0 man vampire: medium-dark skin tone
1F9DB 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧛🏿‍♂️ E5.0 man vampire: dark skin tone
1F9DB 1F3FF 200D 2642                      ; minimally-qualified # 🧛🏿‍♂ E5.0 man vampire: dark skin tone
1F9DB 200D 2640 FE0F                       ; fully-qualified     # 🧛‍♀️ E5.0 woman vampire
1F9DB 200D 2640                            ; minimally-qualified # 🧛‍♀ E5.0 woman vampire
1F9DB 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧛🏻‍♀️ E5.0 woman vampire: light skin tone
1F9DB 1F3FB 200D 2640                      ; minimally-qualified # 🧛🏻‍♀ E5.0 woman vampire: light skin tone
1F9DB 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧛🏼‍♀️ E5.0 woman vampire: medium-light skin tone
1F9DB 1F3FC 200D 2640                      ; minimally-qualified # 🧛🏼‍♀ E5.0 woman vampire: medium-light skin tone
1F9DB 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧛🏽‍♀️ E5.0 woman vampire: medium skin tone
1F9DB 1F3FD 200D 2640                      ; minimally-qualified # 🧛🏽‍♀ E5.0 woman vampire: medium skin tone
1F9DB 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧛🏾‍♀️ E5.0 woman vampire: medium-dark skin tone
1F9DB 1F3FE 200D 2640                      ; minimally-qualified # 🧛🏾‍♀ E5.0 woman vampire: medium-dark skin tone
1F9DB 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧛🏿‍♀️ E5.0 woman vampire: dark skin tone
1F9DB 1F3FF 200D 2640                      ; minimally-qualified # 🧛🏿‍♀ E5.0 woman vampire: dark skin tone
1F9DC                                      ; fully-qualified     # 🧜 E5.0 merperson
1F9DC 1F3FB                                ; fully-qualified     # 🧜🏻 E5.0 merperson: light skin tone
1F9DC 1F3FC                                ; fully-qualified     # 🧜🏼 E5.0 merperson: medium-light skin tone
1F9DC 1F3FD                                ; fully-qualified     # 🧜🏽 E5.0 merperson: medium skin tone
1F9DC 1F3FE                                ; fully-qualified     # 🧜🏾 E5.0 merperson: medium-dark skin tone
1F9DC 1F3FF                                ; fully-qualified     # 🧜🏿 E5.0 merperson: dark skin tone
1F9DC 200D 2642 FE0F                       ; fully-qualified     # 🧜‍♂️ E5.0 merman
1F9DC 200D 2642                            ; minimally-qualified # 🧜‍♂ E5.0 merman
1F9DC 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧜🏻‍♂️ E5.0 merman: light skin tone
1F9DC 1F3FB 200D 2642                      ; minimally-qualified # 🧜🏻‍♂ E5.0 merman: light skin tone
1F9DC 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧜🏼‍♂️ E5.0 merman: medium-light skin tone
1F9DC 1F3FC 200D 2642                      ; minimally-qualified # 🧜🏼‍♂ E5.0 merman: medium-light skin tone
1F9DC 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧜🏽‍♂️ E5.0 merman: medium skin tone
1F9DC 1F3FD 200D 2642                      ; minimally-qualified # 🧜🏽‍♂ E5.0 merman: medium skin tone
1F9DC 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧜🏾‍♂️ E5.0 merman: medium-dark skin tone
1F9DC 1F3FE 200D 2642                      ; minimally-qualified # 🧜🏾‍♂ E5.0 merman: medium-dark skin tone
1F9DC 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧜🏿‍♂️ E5.0 merman: dark skin tone
1F9DC 1F3FF 200D 2642                      ; minimally-qualified # 🧜🏿‍♂ E5.0 merman: dark skin tone
1F9DC 200D 2640 FE0F                       ; fully-qualified     # 🧜‍♀️ E5.0 mermaid
1F9DC 200D 2640                            ; minimally-qualified # 🧜‍♀ E5.0 mermaid
1F9DC 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧜🏻‍♀️ E5.0 mermaid: light skin tone
1F9DC 1F3FB 200D 2640                      ; minimally-qualified # 🧜🏻‍♀ E5.0 mermaid: light skin tone
1F9DC 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧜🏼‍♀️ E5.0 mermaid: medium-light skin tone
1F9DC 1F3FC 200D 2640                      ; minimally-qualified # 🧜🏼‍♀ E5.0 mermaid: medium-light skin tone
1F9DC 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧜🏽‍♀️ E5.0 mermaid: medium skin tone
1F9DC 1F3FD 200D 2640                      ; minimally-qualified # 🧜🏽‍♀ E5.0 mermaid: medium skin tone
1F9DC 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧜🏾‍♀️ E5.0 mermaid: medium-dark skin tone
1F9DC 1F3FE 200D 2640                      ; minimally-qualified # 🧜🏾‍♀ E5.0 mermaid: medium-dark skin tone
1F9DC 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧜🏿‍♀️ E5.0 mermaid: dark skin tone
1F9DC 1F3FF 200D 2640                      ; minimally-qualified # 🧜🏿‍♀ E5.0 mermaid: dark skin tone
1F9DD                                      ; fully-qualified     # 🧝 E5.0 elf
1F9DD 1F3FB                                ; fully-qualified     # 🧝🏻 E5.0 elf: light skin tone
1F9DD 1F3FC                                ; fully-qualified     # 🧝🏼 E5.0 elf: medium-light skin tone
1F9DD 1F3FD                                ; fully-qualified     # 🧝🏽 E5.0 elf: medium skin tone
1F9DD 1F3FE                                ; fully-qualified     # 🧝🏾 E5.0 elf: medium-dark skin tone
1F9DD 1F3FF                                ; fully-qualified     # 🧝🏿 E5.0 elf: dark skin tone
1F9DD 200D 2642 FE0F                       ; fully-qualified     # 🧝‍♂️ E5.0 man elf
1F9DD 200D 2642                            ; minimally-qualified # 🧝‍♂ E5.0 man elf
1F9DD 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧝🏻‍♂️ E5.0 man elf: light skin tone
1F9DD 1F3FB 200D 2642                      ; minimally-qualified # 🧝🏻‍♂ E5.0 man elf: light skin tone
1F9DD 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧝🏼‍♂️ E5.0 man elf: medium-light skin tone
1F9DD 1F3FC 200D 2642                      ; minimally-qualified # 🧝🏼‍♂ E5.0 man elf: medium-light skin tone
1F9DD 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧝🏽‍♂️ E5.0 man elf: medium skin tone
1F9DD 1F3FD 200D 2642                      ; minimally-qualified # 🧝🏽‍♂ E5.0 man elf: medium skin tone
1F9DD 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧝🏾‍♂️ E5.0 man elf: medium-dark skin tone
1F9DD 1F3FE 200D 2642                      ; minimally-qualified # 🧝🏾‍♂ E5.0 man elf: medium-dark skin tone
1F9DD 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧝🏿‍♂️ E5.0 man elf: dark skin tone
1F9DD 1F3FF 200D 2642                      ; minimally-qualified # 🧝🏿‍♂ E5.0 man elf: dark skin tone
1F9DD 200D 2640 FE0F                       ; fully-qualified     # 🧝‍♀️ E5.0 woman elf
1F9DD 200D 2640                            ; minimally-qualified # 🧝‍♀ E5.0 woman elf
1F9DD 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧝🏻‍♀️ E5.0 woman elf: light skin tone
1F9DD 1F3FB 200D 2640                      ; minimally-qualified # 🧝🏻‍♀ E5.0 woman elf: light skin tone
1F9DD 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧝🏼‍♀️ E5.0 woman elf: medium-light skin tone
1F9DD 1F3FC 200D 2640                      ; minimally-qualified # 🧝🏼‍♀ E5.0 woman elf: medium-light skin tone
1F9DD 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧝🏽‍♀️ E5.0 woman elf: medium skin tone
1F9DD 1F3FD 200D 2640                      ; minimally-qualified # 🧝🏽‍♀ E5.0 woman elf: medium skin tone
1F9DD 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧝🏾‍♀️ E5.0 woman elf: medium-dark skin tone
1F9DD 1F3FE 200D 2640                      ; minimally-qualified # 🧝🏾‍♀ E5.0 woman elf: medium-dark skin tone
1F9DD 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧝🏿‍♀️ E5.0 woman elf: dark skin tone
1F9DD 1F3FF 200D 2640                      ; minimally-qualified # 🧝🏿‍♀ E5.0 woman elf: dark skin tone
1F9DE                                      ; fully-qualified     # 🧞 E5.0 genie
1F9DE 200D 2642 FE0F                       ; fully-qualified     # 🧞‍♂️ E5.0 man genie
1F9DE 200D 2642                            ; minimally-qualified # 🧞‍♂ E5.0 man genie
1F9DE 200D 2640 FE0F                       ; fully-qualified     # 🧞‍♀️ E5.0 woman genie
1F9DE 200D 2640                            ; minimally-qualified # 🧞‍♀ E5.0 woman genie
1F9DF                                      ; fully-qualified     # 🧟 E5.0 zombie
1F9DF 200D 2642 FE0F                       ; fully-qualified     # 🧟‍♂️ E5.0 man zombie
1F9DF 200D 2642                            ; minimally-qualified # 🧟‍♂ E5.0 man zombie
1F9DF 200D 2640 FE0F                       ; fully-qualified     # 🧟‍♀️ E5.0 woman zombie
1F9DF 200D 2640                            ; minimally-qualified # 🧟‍♀ E5.0 woman zombie

# subgroup: person-activity
1F486                                      ; fully-qualified     # 💆 E0.6 person getting massage
1F486 1F3FB                                ; fully-qualified     # 💆🏻 E1.0 person getting massage: light skin tone
1F486 1F3FC                                ; fully-qualified     # 💆🏼 E1.0 person getting massage: medium-light skin tone
1F486 1F3FD                                ; fully-qualified     # 💆🏽 E1.0 person getting massage: medium skin tone
1F486 1F3FE                                ; fully-qualified     # 💆🏾 E1.0 person getting massage: medium-dark skin tone
1F486 1F3FF                                ; fully-qualified     # 💆🏿 E1.0 person getting massage: dark skin tone
1F486 200D 2642 FE0F                       ; fully-qualified     # 💆‍♂️ E4.0 man getting massage
1F486 200D 2642                            ; minimally-qualified # 💆‍♂ E4.0 man getting massage
1F486 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 💆🏻‍♂️ E4.0 man getting massage: light skin tone
1F486 1F3FB 200D 2642                      ; minimally-qualified # 💆🏻‍♂ E4.0 man getting massage: light skin tone
1F486 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 💆🏼‍♂️ E4.0 man getting massage: medium-light skin tone
1F486 1F3FC 200D 2642                      ; minimally-qualified # 💆🏼‍♂ E4.0 man getting massage: medium-light skin tone
1F486 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 💆🏽‍♂️ E4.0 man getting massage: medium skin tone
1F486 1F3FD 200D 2642                      ; minimally-qualified # 💆🏽‍♂ E4.0 man getting massage: medium skin tone
1F486 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 💆🏾‍♂️ E4.0 man getting massage: medium-dark skin tone
1F486 1F3FE 200D 2642                      ; minimally-qualified # 💆🏾‍♂ E4.0 man getting massage: medium-dark skin tone
1F486 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 💆🏿‍♂️ E4.0 man getting massage: dark skin tone
1F486 1F3FF 200D 2642                      ; minimally-qualified # 💆🏿‍♂ E4.0 man getting massage: dark skin tone
1F486 200D 2640 FE0F                       ; fully-qualified     # 💆‍♀️ E4.0 woman getting massage
1F486 200D 2640                            ; minimally-qualified # 💆‍♀ E4.0 woman getting massage
1F486 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 💆🏻‍♀️ E4.0 woman getting massage: light skin tone
1F486 1F3FB 200D 2640                      ; minimally-qualified # 💆🏻‍♀ E4.0 woman getting massage: light skin tone
1F486 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 💆🏼‍♀️ E4.0 woman getting massage: medium-light skin tone
1F486 1F3FC 200D 2640                      ; minimally-qualified # 💆🏼‍♀ E4.0 woman getting massage: medium-light skin tone
1F486 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 💆🏽‍♀️ E4.0 woman getting massage: medium skin tone
1F486 1F3FD 200D 2640                      ; minimally-qualified # 💆🏽‍♀ E4.0 woman getting massage: medium skin tone
1F486 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 💆🏾‍♀️ E4.0 woman getting massage: medium-dark skin tone
1F486 1F3FE 200D 2640                      ; minimally-qualified # 💆🏾‍♀ E4.0 woman getting massage: medium-dark skin tone
1F486 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 💆🏿‍♀️ E4.0 woman getting massage: dark skin tone
1F486 1F3FF 200D 2640                      ; minimally-qualified # 💆🏿‍♀ E4.0 woman getting massage: dark skin tone
1F487                                      ; fully-qualified     # 💇 E0.6 person getting haircut
1F487 1F3FB                                ; fully-qualified     # 💇🏻 E1.0 person getting haircut: light skin tone
1F487 1F3FC                                ; fully-qualified     # 💇🏼 E1.0 person getting haircut: medium-light skin tone
1F487 1F3FD                                ; fully-qualified     # 💇🏽 E1.0 person getting haircut: medium skin tone
1F487 1F3FE                                ; fully-qualified     # 💇🏾 E1.0 person getting haircut: medium-dark skin tone
1F487 1F3FF                                ; fully-qualified     # 💇🏿 E1.0 person getting haircut: dark skin tone
1F487 200D 2642 FE0F                       ; fully-qualified     # 💇‍♂️ E4.0 man getting haircut
1F487 200D 2642                            ; minimally-qualified # 💇‍♂ E4.0 man getting haircut
1F487 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 💇🏻‍♂️ E4.0 man getting haircut: light skin tone
1F487 1F3FB 200D 2642                      ; minimally-qualified # 💇🏻‍♂ E4.0 man getting haircut: light skin tone
1F487 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 💇🏼‍♂️ E4.0 man getting haircut: medium-light skin tone
1F487 1F3FC 200D 2642                      ; minimally-qualified # 💇🏼‍♂ E4.0 man getting haircut: medium-light skin tone
1F487 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 💇🏽‍♂️ E4.0 man getting haircut: medium skin tone
1F487 1F3FD 200D 2642                      ; minimally-qualified # 💇🏽‍♂ E4.0 man getting haircut: medium skin tone
1F487 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 💇🏾‍♂️ E4.0 man getting haircut: medium-dark skin tone
1F487 1F3FE 200D 2642                      ; minimally-qualified # 💇🏾‍♂ E4.0 man getting haircut: medium-dark skin tone
1F487 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 💇🏿‍♂️ E4.0 man getting haircut: dark skin tone
1F487 1F3FF 200D 2642                      ; minimally-qualified # 💇🏿‍♂ E4.0 man getting haircut: dark skin tone
1F487 200D 2640 FE0F                       ; fully-qualified     # 💇‍♀️ E4.0 woman getting haircut
1F487 200D 2640                            ; minimally-qualified # 💇‍♀ E4.0 woman getting haircut
1F487 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 💇🏻‍♀️ E4.0 woman getting haircut: light skin tone
1F487 1F3FB 200D 2640                      ; minimally-qualified # 💇🏻‍♀ E4.0 woman getting haircut: light skin tone
1F487 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 💇🏼‍♀️ E4.0 woman getting haircut: medium-light skin tone
1F487 1F3FC 200D 2640                      ; minimally-qualified # 💇🏼‍♀ E4.0 woman getting haircut: medium-light skin tone
1F487 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 💇🏽‍♀️ E4.0 woman getting haircut: medium skin tone
1F487 1F3FD 200D 2640                      ; minimally-qualified # 💇🏽‍♀ E4.0 woman getting haircut: medium skin tone
1F487 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 💇🏾‍♀️ E4.0 woman getting haircut: medium-dark skin tone
1F487 1F3FE 200D 2640                      ; minimally-qualified # 💇🏾‍♀ E4.0 woman getting haircut: medium-dark skin tone
1F487 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 💇🏿‍♀️ E4.0 woman getting haircut: dark skin tone
1F487 1F3FF 200D 2640                      ; minimally-qualified # 💇🏿‍♀ E4.0 woman getting haircut: dark skin tone
1F6B6                                      ; fully-qualified     # 🚶 E0.6 person walking
1F6B6 1F3FB                                ; fully-qualified     # 🚶🏻 E1.0 person walking: light skin tone
1F6B6 1F3FC                                ; fully-qualified     # 🚶🏼 E1.0 person walking: medium-light skin tone
1F6B6 1F3FD                                ; fully-qualified     # 🚶🏽 E1.0 person walking: medium skin tone
1F6B6 1F3FE                                ; fully-qualified     # 🚶🏾 E1.0 person walking: medium-dark skin tone
1F6B6 1F3FF                                ; fully-qualified     # 🚶🏿 E1.0 person walking: dark skin tone
1F6B6 200D 2642 FE0F                       ; fully-qualified     # 🚶‍♂️ E4.0 man walking
1F6B6 200D 2642                            ; minimally-qualified # 🚶‍♂ E4.0 man walking
1F6B6 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🚶🏻‍♂️ E4.0 man walking: light skin tone
1F6B6 1F3FB 200D 2642                      ; minimally-qualified # 🚶🏻‍♂ E4.0 man walking: light skin tone
1F6B6 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🚶🏼‍♂️ E4.0 man walking: medium-light skin tone
1F6B6 1F3FC 200D 2642                      ; minimally-qualified # 🚶🏼‍♂ E4.0 man walking: medium-light skin tone
1F6B6 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🚶🏽‍♂️ E4.0 man walking: medium skin tone
1F6B6 1F3FD 200D 2642                      ; minimally-qualified # 🚶🏽‍♂ E4.0 man walking: medium skin tone
1F6B6 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🚶🏾‍♂️ E4.0 man walking: medium-dark skin tone
1F6B6 1F3FE 200D 2642                      ; minimally-qualified # 🚶🏾‍♂ E4.0 man walking: medium-dark skin tone
1F6B6 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🚶🏿‍♂️ E4.0 man walking: dark skin tone
1F6B6 1F3FF 200D 2642                      ; minimally-qualified # 🚶🏿‍♂ E4.0 man walking: dark skin tone
1F6B6 200D 2640 FE0F                       ; fully-qualified     # 🚶‍♀️ E4.0 woman walking
1F6B6 200D 2640                            ; minimally-qualified # 🚶‍♀ E4.0 woman walking
1F6B6 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🚶🏻‍♀️ E4.0 woman walking: light skin tone
1F6B6 1F3FB 200D 2640                      ; minimally-qualified # 🚶🏻‍♀ E4.0 woman walking: light skin tone
1F6B6 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🚶🏼‍♀️ E4.0 woman walking: medium-light skin tone
1F6B6 1F3FC 200D 2640                      ; minimally-qualified # 🚶🏼‍♀ E4.0 woman walking: medium-light skin tone
1F6B6 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🚶🏽‍♀️ E4.0 woman walking: medium skin tone
1F6B6 1F3FD 200D 2640                      ; minimally-qualified # 🚶🏽‍♀ E4.0 woman walking: medium skin tone
1F6B6 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🚶🏾‍♀️ E4.0 woman walking: medium-dark skin tone
1F6B6 1F3FE 200D 2640                      ; minimally-qualified # 🚶🏾‍♀ E4.0 woman walking: medium-dark skin tone
1F6B6 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🚶🏿‍♀️ E4.0 woman walking: dark skin tone
1F6B6 1F3FF 200D 2640                      ; minimally-qualified # 🚶🏿‍♀ E4.0 woman walking: dark skin tone
1F9CD                                      ; fully-qualified     # 🧍 E12.0 person standing
1F9CD 1F3FB                                ; fully-qualified     # 🧍🏻 E12.0 person standing: light skin tone
1F9CD 1F3FC                                ; fully-qualified     # 🧍🏼 E12.0 person standing: medium-light skin tone
1F9CD 1F3FD                                ; fully-qualified     # 🧍🏽 E12.0 person standing: medium skin tone
1F9CD 1F3FE                                ; fully-qualified     # 🧍🏾 E12.0 person standing: medium-dark skin tone
1F9CD 1F3FF                                ; fully-qualified     # 🧍🏿 E12.0 person standing: dark skin tone
1F9CD 200D 2642 FE0F                       ; fully-qualified     # 🧍‍♂️ E12.0 man standing
1F9CD 200D 2642                            ; minimally-qualified # 🧍‍♂ E12.0 man standing
1F9CD 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧍🏻‍♂️ E12.0 man standing: light skin tone
1F9CD 1F3FB 200D 2642                      ; minimally-qualified # 🧍🏻‍♂ E12.0 man standing: light skin tone
1F9CD 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧍🏼‍♂️ E12.0 man standing: medium-light skin tone
1F9CD 1F3FC 200D 2642                      ; minimally-qualified # 🧍🏼‍♂ E12.0 man standing: medium-light skin tone
1F9CD 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧍🏽‍♂️ E12.0 man standing: medium skin tone
1F9CD 1F3FD 200D 2642                      ; minimally-qualified # 🧍🏽‍♂ E12.0 man standing: medium skin tone
1F9CD 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧍🏾‍♂️ E12.0 man standing: medium-dark skin tone
1F9CD 1F3FE 200D 2642                      ; minimally-qualified # 🧍🏾‍♂ E12.0 man standing: medium-dark skin tone
1F9CD 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧍🏿‍♂️ E12.0 man standing: dark skin tone
1F9CD 1F3FF 200D 2642                      ; minimally-qualified # 🧍🏿‍♂ E12.0 man standing: dark skin tone
1F9CD 200D 2640 FE0F                       ; fully-qualified     # 🧍‍♀️ E12.0 woman standing
1F9CD 200D 2640                            ; minimally-qualified # 🧍‍♀ E12.0 woman standing
1F9CD 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧍🏻‍♀️ E12.0 woman standing: light skin tone
1F9CD 1F3FB 200D 2640                      ; minimally-qualified # 🧍🏻‍♀ E12.0 woman standing: light skin tone
1F9CD 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧍🏼‍♀️ E12.0 woman standing: medium-light skin tone
1F9CD 1F3FC 200D 2640                      ; minimally-qualified # 🧍🏼‍♀ E12.0 woman standing: medium-light skin tone
1F9CD 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧍🏽‍♀️ E12.0 woman standing: medium skin tone
1F9CD 1F3FD 200D 2640                      ; minimally-qualified # 🧍🏽‍♀ E12.0 woman standing: medium skin tone
1F9CD 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧍🏾‍♀️ E12.0 woman standing: medium-dark skin tone
1F9CD 1F3FE 200D 2640                      ; minimally-qualified # 🧍🏾‍♀ E12.0 woman standing: medium-dark skin tone
1F9CD 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧍🏿‍♀️ E12.0 woman standing: dark skin tone
1F9CD 1F3FF 200D 2640                      ; minimally-qualified # 🧍🏿‍♀ E12.0 woman standing: dark skin tone
1F9CE                                      ; fully-qualified     # 🧎 E12.0 person kneeling
1F9CE 1F3FB                                ; fully-qualified     # 🧎🏻 E12.0 person kneeling: light skin tone
1F9CE 1F3FC                                ; fully-qualified     # 🧎🏼 E12.0 person kneeling: medium-light skin tone
1F9CE 1F3FD                                ; fully-qualified     # 🧎🏽 E12.0 person kneeling: medium skin tone
1F9CE 1F3FE                                ; fully-qualified     # 🧎🏾 E12.0 person kneeling: medium-dark skin tone
1F9CE 1F3FF                                ; fully-qualified     # 🧎🏿 E12.0 person kneeling: dark skin tone
1F9CE 200D 2642 FE0F                       ; fully-qualified     # 🧎‍♂️ E12.0 man kneeling
1F9CE 200D 2642                            ; minimally-qualified # 🧎‍♂ E12.0 man kneeling
1F9CE 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧎🏻‍♂️ E12.0 man kneeling: light skin tone
1F9CE 1F3FB 200D 2642                      ; minimally-qualified # 🧎🏻‍♂ E12.0 man kneeling: light skin tone
1F9CE 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧎🏼‍♂️ E12.0 man kneeling: medium-light skin tone
1F9CE 1F3FC 200D 2642                      ; minimally-qualified # 🧎🏼‍♂ E12.0 man kneeling: medium-light skin tone
1F9CE 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧎🏽‍♂️ E12.0 man kneeling: medium skin tone
1F9CE 1F3FD 200D 2642                      ; minimally-qualified # 🧎🏽‍♂ E12.0 man kneeling: medium skin tone
1F9CE 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧎🏾‍♂️ E12.0 man kneeling: medium-dark skin tone
1F9CE 1F3FE 200D 2642                      ; minimally-qualified # 🧎🏾‍♂ E12.0 man kneeling: medium-dark skin tone
1F9CE 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧎🏿‍♂️ E12.0 man kneeling: dark skin tone
1F9CE 1F3FF 200D 2642                      ; minimally-qualified # 🧎🏿‍♂ E12.0 man kneeling: dark skin tone
1F9CE 200D 2640 FE0F                       ; fully-qualified     # 🧎‍♀️ E12.0 woman kneeling
1F9CE 200D 2640                            ; minimally-qualified # 🧎‍♀ E12.0 woman kneeling
1F9CE 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧎🏻‍♀️ E12.0 woman kneeling: light skin tone
1F9CE 1F3FB 200D 2640                      ; minimally-qualified # 🧎🏻‍♀ E12.0 woman kneeling: light skin tone
1F9CE 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧎🏼‍♀️ E12.0 woman kneeling: medium-light skin tone
1F9CE 1F3FC 200D 2640                      ; minimally-qualified # 🧎🏼‍♀ E12.0 woman kneeling: medium-light skin tone
1F9CE 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧎🏽‍♀️ E12.0 woman kneeling: medium skin tone
1F9CE 1F3FD 200D 2640                      ; minimally-qualified # 🧎🏽‍♀ E12.0 woman kneeling: medium skin tone
1F9CE 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧎🏾‍♀️ E12.0 woman kneeling: medium-dark skin tone
1F9CE 1F3FE 200D 2640                      ; minimally-qualified # 🧎🏾‍♀ E12.0 woman kneeling: medium-dark skin tone
1F9CE 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧎🏿‍♀️ E12.0 woman kneeling: dark skin tone
1F9CE 1F3FF 200D 2640                      ; minimally-qualified # 🧎🏿‍♀ E12.0 woman kneeling: dark skin tone
1F9D1 200D 1F9AF                           ; fully-qualified     # 🧑‍🦯 E12.1 person with white cane
1F9D1 1F3FB 200D 1F9AF                     ; fully-qualified     # 🧑🏻‍🦯 E12.1 person with white cane: light skin tone
1F9D1 1F3FC 200D 1F9AF                     ; fully-qualified     # 🧑🏼‍🦯 E12.1 person with white cane: medium-light skin tone
1F9D1 1F3FD 200D 1F9AF                     ; fully-qualified     # 🧑🏽‍🦯 E12.1 person with white cane: medium skin tone
1F9D1 1F3FE 200D 1F9AF                     ; fully-qualified     # 🧑🏾‍🦯 E12.1 person with white cane: medium-dark skin tone
1F9D1 1F3FF 200D 1F9AF                     ; fully-qualified     # 🧑🏿‍🦯 E12.1 person with white cane: dark skin tone
1F468 200D 1F9AF                           ; fully-qualified     # 👨‍🦯 E12.0 man with white cane
1F468 1F3FB 200D 1F9AF                     ; fully-qualified     # 👨🏻‍🦯 E12.0 man with white cane: light skin tone
1F468 1F3FC 200D 1F9AF                     ; fully-qualified     # 👨🏼‍🦯 E12.0 man with white cane: medium-light skin tone
1F468 1F3FD 200D 1F9AF                     ; fully-qualified     # 👨🏽‍🦯 E12.0 man with white cane: medium skin tone
1F468 1F3FE 200D 1F9AF                     ; fully-qualified     # 👨🏾‍🦯 E12.0 man with white cane: medium-dark skin tone
1F468 1F3FF 200D 1F9AF                     ; fully-qualified     # 👨🏿‍🦯 E12.0 man with white cane: dark skin tone
1F469 200D 1F9AF                           ; fully-qualified     # 👩‍🦯 E12.0 woman with white cane
1F469 1F3FB 200D 1F9AF                     ; fully-qualified     # 👩🏻‍🦯 E12.0 woman with white cane: light skin tone
1F469 1F3FC 200D 1F9AF                     ; fully-qualified     # 👩🏼‍🦯 E12.0 woman with white cane: medium-light skin tone
1F469 1F3FD 200D 1F9AF                     ; fully-qualified     # 👩🏽‍🦯 E12.0 woman with white cane: medium skin tone
1F469 1F3FE 200D 1F9AF                     ; fully-qualified     # 👩🏾‍🦯 E12.0 woman with white cane: medium-dark skin tone
1F469 1F3FF 200D 1F9AF                     ; fully-qualified     # 👩🏿‍🦯 E12.0 woman with white cane: dark skin tone
1F9D1 200D 1F9BC                           ; fully-qualified     # 🧑‍🦼 E12.1 person in motorized wheelchair
1F9D1 1F3FB 200D 1F9BC                     ; fully-qualified     # 🧑🏻‍🦼 E12.1 person in motorized wheelchair: light skin tone
1F9D1 1F3FC 200D 1F9BC                     ; fully-qualified     # 🧑🏼‍🦼 E12.1 person in motorized wheelchair: medium-light skin tone
1F9D1 1F3FD 200D 1F9BC                     ; fully-qualified     # 🧑🏽‍🦼 E12.1 person in motorized wheelchair: medium skin tone
1F9D1 1F3FE 200D 1F9BC                     ; fully-qualified     # 🧑🏾‍🦼 E12.1 person in motorized wheelchair: medium-dark skin tone
1F9D1 1F3FF 200D 1F9BC                     ; fully-qualified     # 🧑🏿‍🦼 E12.1 person in motorized wheelchair: dark skin tone
1F468 200D 1F9BC                           ; fully-qualified     # 👨‍🦼 E12.0 man in motorized wheelchair
1F468 1F3FB 200D 1F9BC                     ; fully-qualified     # 👨🏻‍🦼 E12.0 man in motorized wheelchair: light skin tone
1F468 1F3FC 200D 1F9BC                     ; fully-qualified     # 👨🏼‍🦼 E12.0 man in motorized wheelchair: medium-light skin tone
1F468 1F3FD 200D 1F9BC                     ; fully-qualified     # 👨🏽‍🦼 E12.0 man in motorized wheelchair: medium skin tone
1F468 1F3FE 200D 1F9BC                     ; fully-qualified     # 👨🏾‍🦼 E12.0 man in motorized wheelchair: medium-dark skin tone
1F468 1F3FF 200D 1F9BC                     ; fully-qualified     # 👨🏿‍🦼 E12.0 man in motorized wheelchair: dark skin tone
1F469 200D 1F9BC                           ; fully-qualified     # 👩‍🦼 E12.0 woman in motorized wheelchair
1F469 1F3FB 200D 1F9BC                     ; fully-qualified     # 👩🏻‍🦼 E12.0 woman in motorized wheelchair: light skin tone
1F469 1F3FC 200D 1F9BC                     ; fully-qualified     # 👩🏼‍🦼 E12.0 woman in motorized wheelchair: medium-light skin tone
1F469 1F3FD 200D 1F9BC                     ; fully-qualified     # 👩🏽‍🦼 E12.0 woman in motorized wheelchair: medium skin tone
1F469 1F3FE 200D 1F9BC                     ; fully-qualified     # 👩🏾‍🦼 E12.0 woman in motorized wheelchair: medium-dark skin tone
1F469 1F3FF 200D 1F9BC                     ; fully-qualified     # 👩🏿‍🦼 E12.0 woman in motorized wheelchair: dark skin tone
1F9D1 200D 1F9BD                           ; fully-qualified     # 🧑‍🦽 E12.1 person in manual wheelchair
1F9D1 1F3FB 200D 1F9BD                     ; fully-qualified     # 🧑🏻‍🦽 E12.1 person in manual wheelchair: light skin tone
1F9D1 1F3FC 200D 1F9BD                     ; fully-qualified     # 🧑🏼‍🦽 E12.1 person in manual wheelchair: medium-light skin tone
1F9D1 1F3FD 200D 1F9BD                     ; fully-qualified     # 🧑🏽‍🦽 E12.1 person in manual wheelchair: medium skin tone
1F9D1 1F3FE 200D 1F9BD                     ; fully-qualified     # 🧑🏾‍🦽 E12.1 person in manual wheelchair: medium-dark skin tone
1F9D1 1F3FF 200D 1F9BD                     ; fully-qualified     # 🧑🏿‍🦽 E12.1 person in manual wheelchair: dark skin tone
1F468 200D 1F9BD                           ; fully-qualified     # 👨‍🦽 E12.0 man in manual wheelchair
1F468 1F3FB 200D 1F9BD                     ; fully-qualified     # 👨🏻‍🦽 E12.0 man in manual wheelchair: light skin tone
1F468 1F3FC 200D 1F9BD                     ; fully-qualified     # 👨🏼‍🦽 E12.0 man in manual wheelchair: medium-light skin tone
1F468 1F3FD 200D 1F9BD                     ; fully-qualified     # 👨🏽‍🦽 E12.0 man in manual wheelchair: medium skin tone
1F468 1F3FE 200D 1F9BD                     ; fully-qualified     # 👨🏾‍🦽 E12.0 man in manual wheelchair: medium-dark skin tone
1F468 1F3FF 200D 1F9BD                     ; fully-qualified     # 👨🏿‍🦽 E12.0 man in manual wheelchair: dark skin tone
1F469 200D 1F9BD                           ; fully-qualified     # 👩‍🦽 E12.0 woman in manual wheelchair
1F469 1F3FB 200D 1F9BD                     ; fully-qualified     # 👩🏻‍🦽 E12.0 woman in manual wheelchair: light skin tone
1F469 1F3FC 200D 1F9BD                     ; fully-qualified     # 👩🏼‍🦽 E12.0 woman in manual wheelchair: medium-light skin tone
1F469 1F3FD 200D 1F9BD                     ; fully-qualified     # 👩🏽‍🦽 E12.0 woman in manual wheelchair: medium skin tone
1F469 1F3FE 200D 1F9BD                     ; fully-qualified     # 👩🏾‍🦽 E12.0 woman in manual wheelchair: medium-dark skin tone
1F469 1F3FF 200D 1F9BD                     ; fully-qualified     # 👩🏿‍🦽 E12.0 woman in manual wheelchair: dark skin tone
1F3C3                                      ; fully-qualified     # 🏃 E0.6 person running
1F3C3 1F3FB                                ; fully-qualified     # 🏃🏻 E1.0 person running: light skin tone
1F3C3 1F3FC                                ; fully-qualified     # 🏃🏼 E1.0 person running: medium-light skin tone
1F3C3 1F3FD                                ; fully-qualified     # 🏃🏽 E1.0 person running: medium skin tone
1F3C3 1F3FE                                ; fully-qualified     # 🏃🏾 E1.0 person running: medium-dark skin tone
1F3C3 1F3FF                                ; fully-qualified     # 🏃🏿 E1.0 person running: dark skin tone
1F3C3 200D 2642 FE0F                       ; fully-qualified     # 🏃‍♂️ E4.0 man running
1F3C3 200D 2642                            ; minimally-qualified # 🏃‍♂ E4.0 man running
1F3C3 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🏃🏻‍♂️ E4.0 man running: light skin tone
1F3C3 1F3FB 200D 2642                      ; minimally-qualified # 🏃🏻‍♂ E4.0 man running: light skin tone
1F3C3 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🏃🏼‍♂️ E4.0 man running: medium-light skin tone
1F3C3 1F3FC 200D 2642                      ; minimally-qualified # 🏃🏼‍♂ E4.0 man running: medium-light skin tone
1F3C3 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🏃🏽‍♂️ E4.0 man running: medium skin tone
1F3C3 1F3FD 200D 2642                      ; minimally-qualified # 🏃🏽‍♂ E4.0 man running: medium skin tone
1F3C3 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🏃🏾‍♂️ E4.0 man running: medium-dark skin tone
1F3C3 1F3FE 200D 2642                      ; minimally-qualified # 🏃🏾‍♂ E4.0 man running: medium-dark skin tone
1F3C3 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🏃🏿‍♂️ E4.0 man running: dark skin tone
1F3C3 1F3FF 200D 2642                      ; minimally-qualified # 🏃🏿‍♂ E4.0 man running: dark skin tone
1F3C3 200D 2640 FE0F                       ; fully-qualified     # 🏃‍♀️ E4.0 woman running
1F3C3 200D 2640                            ; minimally-qualified # 🏃‍♀ E4.0 woman running
1F3C3 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🏃🏻‍♀️ E4.0 woman running: light skin tone
1F3C3 1F3FB 200D 2640                      ; minimally-qualified # 🏃🏻‍♀ E4.0 woman running: light skin tone
1F3C3 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🏃🏼‍♀️ E4.0 woman running: medium-light skin tone
1F3C3 1F3FC 200D 2640                      ; minimally-qualified # 🏃🏼‍♀ E4.0 woman running: medium-light skin tone
1F3C3 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🏃🏽‍♀️ E4.0 woman running: medium skin tone
1F3C3 1F3FD 200D 2640                      ; minimally-qualified # 🏃🏽‍♀ E4.0 woman running: medium skin tone
1F3C3 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🏃🏾‍♀️ E4.0 woman running: medium-dark skin tone
1F3C3 1F3FE 200D 2640                      ; minimally-qualified # 🏃🏾‍♀ E4.0 woman running: medium-dark skin tone
1F3C3 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🏃🏿‍♀️ E4.0 woman running: dark skin tone
1F3C3 1F3FF 200D 2640                      ; minimally-qualified # 🏃🏿‍♀ E4.0 woman running: dark skin tone
1F483                                      ; fully-qualified     # 💃 E0.6 woman dancing
1F483 1F3FB                                ; fully-qualified     # 💃🏻 E1.0 woman dancing: light skin tone
1F483 1F3FC                                ; fully-qualified     # 💃🏼 E1.0 woman dancing: medium-light skin tone
1F483 1F3FD                                ; fully-qualified     # 💃🏽 E1.0 woman dancing: medium skin tone
1F483 1F3FE                                ; fully-qualified     # 💃🏾 E1.0 woman dancing: medium-dark skin tone
1F483 1F3FF                                ; fully-qualified     # 💃🏿 E1.0 woman dancing: dark skin tone
1F57A                                      ; fully-qualified     # 🕺 E3.0 man dancing
1F57A 1F3FB                                ; fully-qualified     # 🕺🏻 E3.0 man dancing: light skin tone
1F57A 1F3FC                                ; fully-qualified     # 🕺🏼 E3.0 man dancing: medium-light skin tone
1F57A 1F3FD                                ; fully-qualified     # 🕺🏽 E3.0 man dancing: medium skin tone
1F57A 1F3FE                                ; fully-qualified     # 🕺🏾 E3.0 man dancing: medium-dark skin tone
1F57A 1F3FF                                ; fully-qualified     # 🕺🏿 E3.0 man dancing: dark skin tone
1F574 FE0F                                 ; fully-qualified     # 🕴️ E0.7 person in suit levitating
1F574                                      ; unqualified         # 🕴 E0.7 person in suit levitating
1F574 1F3FB                                ; fully-qualified     # 🕴🏻 E4.0 person in suit levitating: light skin tone
1F574 1F3FC                                ; fully-qualified     # 🕴🏼 E4.0 person in suit levitating: medium-light skin tone
1F574 1F3FD                                ; fully-qualified     # 🕴🏽 E4.0 person in suit levitating: medium skin tone
1F574 1F3FE                                ; fully-qualified     # 🕴🏾 E4.0 person in suit levitating: medium-dark skin tone
1F574 1F3FF                                ; fully-qualified     # 🕴🏿 E4.0 person in suit levitating: dark skin tone
1F46F                                      ; fully-qualified     # 👯 E0.6 people with bunny ears
1F46F 200D 2642 FE0F                       ; fully-qualified     # 👯‍♂️ E4.0 men with bunny ears
1F46F 200D 2642                            ; minimally-qualified # 👯‍♂ E4.0 men with bunny ears
1F46F 200D 2640 FE0F                       ; fully-qualified     # 👯‍♀️ E4.0 women with bunny ears
1F46F 200D 2640                            ; minimally-qualified # 👯‍♀ E4.0 women with bunny ears
1F9D6                                      ; fully-qualified     # 🧖 E5.0 person in steamy room
1F9D6 1F3FB                                ; fully-qualified     # 🧖🏻 E5.0 person in steamy room: light skin tone
1F9D6 1F3FC                                ; fully-qualified     # 🧖🏼 E5.0 person in steamy room: medium-light skin tone
1F9D6 1F3FD                                ; fully-qualified     # 🧖🏽 E5.0 person in steamy room: medium skin tone
1F9D6 1F3FE                                ; fully-qualified     # 🧖🏾 E5.0 person in steamy room: medium-dark skin tone
1F9D6 1F3FF                                ; fully-qualified     # 🧖🏿 E5.0 person in steamy room: dark skin tone
1F9D6 200D 2642 FE0F                       ; fully-qualified     # 🧖‍♂️ E5.0 man in steamy room
1F9D6 200D 2642                            ; minimally-qualified # 🧖‍♂ E5.0 man in steamy room
1F9D6 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧖🏻‍♂️ E5.0 man in steamy room: light skin tone
1F9D6 1F3FB 200D 2642                      ; minimally-qualified # 🧖🏻‍♂ E5.0 man in steamy room: light skin tone
1F9D6 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧖🏼‍♂️ E5.0 man in steamy room: medium-light skin tone
1F9D6 1F3FC 200D 2642                      ; minimally-qualified # 🧖🏼‍♂ E5.0 man in steamy room: medium-light skin tone
1F9D6 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧖🏽‍♂️ E5.0 man in steamy room: medium skin tone
1F9D6 1F3FD 200D 2642                      ; minimally-qualified # 🧖🏽‍♂ E5.0 man in steamy room: medium skin tone
1F9D6 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧖🏾‍♂️ E5.0 man in steamy room: medium-dark skin tone
1F9D6 1F3FE 200D 2642                      ; minimally-qualified # 🧖🏾‍♂ E5.0 man in steamy room: medium-dark skin tone
1F9D6 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧖🏿‍♂️ E5.0 man in steamy room: dark skin tone
1F9D6 1F3FF 200D 2642                      ; minimally-qualified # 🧖🏿‍♂ E5.0 man in steamy room: dark skin tone
1F9D6 200D 2640 FE0F                       ; fully-qualified     # 🧖‍♀️ E5.0 woman in steamy room
1F9D6 200D 2640                            ; minimally-qualified # 🧖‍♀ E5.0 woman in steamy room
1F9D6 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧖🏻‍♀️ E5.0 woman in steamy room: light skin tone
1F9D6 1F3FB 200D 2640                      ; minimally-qualified # 🧖🏻‍♀ E5.0 woman in steamy room: light skin tone
1F9D6 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧖🏼‍♀️ E5.0 woman in steamy room: medium-light skin tone
1F9D6 1F3FC 200D 2640                      ; minimally-qualified # 🧖🏼‍♀ E5.0 woman in steamy room: medium-light skin tone
1F9D6 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧖🏽‍♀️ E5.0 woman in steamy room: medium skin tone
1F9D6 1F3FD 200D 2640                      ; minimally-qualified # 🧖🏽‍♀ E5.0 woman in steamy room: medium skin tone
1F9D6 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧖🏾‍♀️ E5.0 woman in steamy room: medium-dark skin tone
1F9D6 1F3FE 200D 2640                      ; minimally-qualified # 🧖🏾‍♀ E5.0 woman in steamy room: medium-dark skin tone
1F9D6 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧖🏿‍♀️ E5.0 woman in steamy room: dark skin tone
1F9D6 1F3FF 200D 2640                      ; minimally-qualified # 🧖🏿‍♀ E5.0 woman in steamy room: dark skin tone
1F9D7                                      ; fully-qualified     # 🧗 E5.0 person climbing
1F9D7 1F3FB                                ; fully-qualified     # 🧗🏻 E5.0 person climbing: light skin tone
1F9D7 1F3FC                                ; fully-qualified     # 🧗🏼 E5.0 person climbing: medium-light skin tone
1F9D7 1F3FD                                ; fully-qualified     # 🧗🏽 E5.0 person climbing: medium skin tone
1F9D7 1F3FE                                ; fully-qualified     # 🧗🏾 E5.0 person climbing: medium-dark skin tone
1F9D7 1F3FF                                ; fully-qualified     # 🧗🏿 E5.0 person climbing: dark skin tone
1F9D7 200D 2642 FE0F                       ; fully-qualified     # 🧗‍♂️ E5.0 man climbing
1F9D7 200D 2642                            ; minimally-qualified # 🧗‍♂ E5.0 man climbing
1F9D7 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧗🏻‍♂️ E5.0 man climbing: light skin tone
1F9D7 1F3FB 200D 2642                      ; minimally-qualified # 🧗🏻‍♂ E5.0 man climbing: light skin tone
1F9D7 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧗🏼‍♂️ E5.0 man climbing: medium-light skin tone
1F9D7 1F3FC 200D 2642                      ; minimally-qualified # 🧗🏼‍♂ E5.0 man climbing: medium-light skin tone
1F9D7 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧗🏽‍♂️ E5.0 man climbing: medium skin tone
1F9D7 1F3FD 200D 2642                      ; minimally-qualified # 🧗🏽‍♂ E5.0 man climbing: medium skin tone
1F9D7 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧗🏾‍♂️ E5.0 man climbing: medium-dark skin tone
1F9D7 1F3FE 200D 2642                      ; minimally-qualified # 🧗🏾‍♂ E5.0 man climbing: medium-dark skin tone
1F9D7 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧗🏿‍♂️ E5.0 man climbing: dark skin tone
1F9D7 1F3FF 200D 2642                      ; minimally-qualified # 🧗🏿‍♂ E5.0 man climbing: dark skin tone
1F9D7 200D 2640 FE0F                       ; fully-qualified     # 🧗‍♀️ E5.0 woman climbing
1F9D7 200D 2640                            ; minimally-qualified # 🧗‍♀ E5.0 woman climbing
1F9D7 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧗🏻‍♀️ E5.0 woman climbing: light skin tone
1F9D7 1F3FB 200D 2640                      ; minimally-qualified # 🧗🏻‍♀ E5.0 woman climbing: light skin tone
1F9D7 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧗🏼‍♀️ E5.0 woman climbing: medium-light skin tone
1F9D7 1F3FC 200D 2640                      ; minimally-qualified # 🧗🏼‍♀ E5.0 woman climbing: medium-light skin tone
1F9D7 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧗🏽‍♀️ E5.0 woman climbing: medium skin tone
1F9D7 1F3FD 200D 2640                      ; minimally-qualified # 🧗🏽‍♀ E5.0 woman climbing: medium skin tone
1F9D7 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧗🏾‍♀️ E5.0 woman climbing: medium-dark skin tone
1F9D7 1F3FE 200D 2640                      ; minimally-qualified # 🧗🏾‍♀ E5.0 woman climbing: medium-dark skin tone
1F9D7 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧗🏿‍♀️ E5.0 woman climbing: dark skin tone
1F9D7 1F3FF 200D 2640                      ; minimally-qualified # 🧗🏿‍♀ E5.0 woman climbing: dark skin tone

# subgroup: person-sport
1F93A                                      ; fully-qualified     # 🤺 E3.0 person fencing
1F3C7                                      ; fully-qualified     # 🏇 E1.0 horse racing
1F3C7 1F3FB                                ; fully-qualified     # 🏇🏻 E1.0 horse racing: light skin tone
1F3C7 1F3FC                                ; fully-qualified     # 🏇🏼 E1.0 horse racing: medium-light skin tone
1F3C7 1F3FD                                ; fully-qualified     # 🏇🏽 E1.0 horse racing: medium skin tone
1F3C7 1F3FE                                ; fully-qualified     # 🏇🏾 E1.0 horse racing: medium-dark skin tone
1F3C7 1F3FF                                ; fully-qualified     # 🏇🏿 E1.0 horse racing: dark skin tone
26F7 FE0F                                  ; fully-qualified     # ⛷️ E0.7 skier
26F7                                       ; unqualified         # ⛷ E0.7 skier
1F3C2                                      ; fully-qualified     # 🏂 E0.6 snowboarder
1F3C2 1F3FB                                ; fully-qualified     # 🏂🏻 E1.0 snowboarder: light skin tone
1F3C2 1F3FC                                ; fully-qualified     # 🏂🏼 E1.0 snowboarder: medium-light skin tone
1F3C2 1F3FD                                ; fully-qualified     # 🏂🏽 E1.0 snowboarder: medium skin tone
1F3C2 1F3FE                                ; fully-qualified     # 🏂🏾 E1.0 snowboarder: medium-dark skin tone
1F3C2 1F3FF                                ; fully-qualified     # 🏂🏿 E1.0 snowboarder: dark skin tone
1F3CC FE0F                                 ; fully-qualified     # 🏌️ E0.7 person golfing
1F3CC                                      ; unqualified         # 🏌 E0.7 person golfing
1F3CC 1F3FB                                ; fully-qualified     # 🏌🏻 E4.0 person golfing: light skin tone
1F3CC 1F3FC                                ; fully-qualified     # 🏌🏼 E4.0 person golfing: medium-light skin tone
1F3CC 1F3FD                                ; fully-qualified     # 🏌🏽 E4.0 person golfing: medium skin tone
1F3CC 1F3FE                                ; fully-qualified     # 🏌🏾 E4.0 person golfing: medium-dark skin tone
1F3CC 1F3FF                                ; fully-qualified     # 🏌🏿 E4.0 person golfing: dark skin tone
1F3CC FE0F 200D 2642 FE0F                  ; fully-qualified     # 🏌️‍♂️ E4.0 man golfing
1F3CC 200D 2642 FE0F                       ; unqualified         # 🏌‍♂️ E4.0 man golfing
1F3CC FE0F 200D 2642                       ; unqualified         # 🏌️‍♂ E4.0 man golfing
1F3CC 200D 2642                            ; unqualified         # 🏌‍♂ E4.0 man golfing
1F3CC 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🏌🏻‍♂️ E4.0 man golfing: light skin tone
1F3CC 1F3FB 200D 2642                      ; minimally-qualified # 🏌🏻‍♂ E4.0 man golfing: light skin tone
1F3CC 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🏌🏼‍♂️ E4.0 man golfing: medium-light skin tone
1F3CC 1F3FC 200D 2642                      ; minimally-qualified # 🏌🏼‍♂ E4.0 man golfing: medium-light skin tone
1F3CC 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🏌🏽‍♂️ E4.0 man golfing: medium skin tone
1F3CC 1F3FD 200D 2642                      ; minimally-qualified # 🏌🏽‍♂ E4.0 man golfing: medium skin tone
1F3CC 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🏌🏾‍♂️ E4.0 man golfing: medium-dark skin tone
1F3CC 1F3FE 200D 2642                      ; minimally-qualified # 🏌🏾‍♂ E4.0 man golfing: medium-dark skin tone
1F3CC 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🏌🏿‍♂️ E4.0 man golfing: dark skin tone
1F3CC 1F3FF 200D 2642                      ; minimally-qualified # 🏌🏿‍♂ E4.0 man golfing: dark skin tone
1F3CC FE0F 200D 2640 FE0F                  ; fully-qualified     # 🏌️‍♀️ E4.0 woman golfing
1F3CC 200D 2640 FE0F                       ; unqualified         # 🏌‍♀️ E4.0 woman golfing
1F3CC FE0F 200D 2640                       ; unqualified         # 🏌️‍♀ E4.0 woman golfing
1F3CC 200D 2640                            ; unqualified         # 🏌‍♀ E4.0 woman golfing
1F3CC 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🏌🏻‍♀️ E4.0 woman golfing: light skin tone
1F3CC 1F3FB 200D 2640                      ; minimally-qualified # 🏌🏻‍♀ E4.0 woman golfing: light skin tone
1F3CC 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🏌🏼‍♀️ E4.0 woman golfing: medium-light skin tone
1F3CC 1F3FC 200D 2640                      ; minimally-qualified # 🏌🏼‍♀ E4.0 woman golfing: medium-light skin tone
1F3CC 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🏌🏽‍♀️ E4.0 woman golfing: medium skin tone
1F3CC 1F3FD 200D 2640                      ; minimally-qualified # 🏌🏽‍♀ E4.0 woman golfing: medium skin tone
1F3CC 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🏌🏾‍♀️ E4.0 woman golfing: medium-dark skin tone
1F3CC 1F3FE 200D 2640                      ; minimally-qualified # 🏌🏾‍♀ E4.0 woman golfing: medium-dark skin tone
1F3CC 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🏌🏿‍♀️ E4.0 woman golfing: dark skin tone
1F3CC 1F3FF 200D 2640                      ; minimally-qualified # 🏌🏿‍♀ E4.0 woman golfing: dark skin tone
1F3C4                                      ; fully-qualified     # 🏄 E0.6 person surfing
1F3C4 1F3FB                                ; fully-qualified     # 🏄🏻 E1.0 person surfing: light skin tone
1F3C4 1F3FC                                ; fully-qualified     # 🏄🏼 E1.0 person surfing: medium-light skin tone
1F3C4 1F3FD                                ; fully-qualified     # 🏄🏽 E1.0 person surfing: medium skin tone
1F3C4 1F3FE                                ; fully-qualified     # 🏄🏾 E1.0 person surfing: medium-dark skin tone
1F3C4 1F3FF                                ; fully-qualified     # 🏄🏿 E1.0 person surfing: dark skin tone
1F3C4 200D 2642 FE0F                       ; fully-qualified     # 🏄‍♂️ E4.0 man surfing
1F3C4 200D 2642                            ; minimally-qualified # 🏄‍♂ E4.0 man surfing
1F3C4 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🏄🏻‍♂️ E4.0 man surfing: light skin tone
1F3C4 1F3FB 200D 2642                      ; minimally-qualified # 🏄🏻‍♂ E4.0 man surfing: light skin tone
1F3C4 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🏄🏼‍♂️ E4.0 man surfing: medium-light skin tone
1F3C4 1F3FC 200D 2642                      ; minimally-qualified # 🏄🏼‍♂ E4.0 man surfing: medium-light skin tone
1F3C4 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🏄🏽‍♂️ E4.0 man surfing: medium skin tone
1F3C4 1F3FD 200D 2642                      ; minimally-qualified # 🏄🏽‍♂ E4.0 man surfing: medium skin tone
1F3C4 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🏄🏾‍♂️ E4.0 man surfing: medium-dark skin tone
1F3C4 1F3FE 200D 2642                      ; minimally-qualified # 🏄🏾‍♂ E4.0 man surfing: medium-dark skin tone
1F3C4 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🏄🏿‍♂️ E4.0 man surfing: dark skin tone
1F3C4 1F3FF 200D 2642                      ; minimally-qualified # 🏄🏿‍♂ E4.0 man surfing: dark skin tone
1F3C4 200D 2640 FE0F                       ; fully-qualified     # 🏄‍♀️ E4.0 woman surfing
1F3C4 200D 2640                            ; minimally-qualified # 🏄‍♀ E4.0 woman surfing
1F3C4 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🏄🏻‍♀️ E4.0 woman surfing: light skin tone
1F3C4 1F3FB 200D 2640                      ; minimally-qualified # 🏄🏻‍♀ E4.0 woman surfing: light skin tone
1F3C4 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🏄🏼‍♀️ E4.0 woman surfing: medium-light skin tone
1F3C4 1F3FC 200D 2640                      ; minimally-qualified # 🏄🏼‍♀ E4.0 woman surfing: medium-light skin tone
1F3C4 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🏄🏽‍♀️ E4.0 woman surfing: medium skin tone
1F3C4 1F3FD 200D 2640                      ; minimally-qualified # 🏄🏽‍♀ E4.0 woman surfing: medium skin tone
1F3C4 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🏄🏾‍♀️ E4.0 woman surfing: medium-dark skin tone
1F3C4 1F3FE 200D 2640                      ; minimally-qualified # 🏄🏾‍♀ E4.0 woman surfing: medium-dark skin tone
1F3C4 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🏄🏿‍♀️ E4.0 woman surfing: dark skin tone
1F3C4 1F3FF 200D 2640                      ; minimally-qualified # 🏄🏿‍♀ E4.0 woman surfing: dark skin tone
1F6A3                                      ; fully-qualified     # 🚣 E1.0 person rowing boat
1F6A3 1F3FB                                ; fully-qualified     # 🚣🏻 E1.0 person rowing boat: light skin tone
1F6A3 1F3FC                                ; fully-qualified     # 🚣🏼 E1.0 person rowing boat: medium-light skin tone
1F6A3 1F3FD                                ; fully-qualified     # 🚣🏽 E1.0 person rowing boat: medium skin tone
1F6A3 1F3FE                                ; fully-qualified     # 🚣🏾 E1.0 person rowing boat: medium-dark skin tone
1F6A3 1F3FF                                ; fully-qualified     # 🚣🏿 E1.0 person rowing boat: dark skin tone
1F6A3 200D 2642 FE0F                       ; fully-qualified     # 🚣‍♂️ E4.0 man rowing boat
1F6A3 200D 2642                            ; minimally-qualified # 🚣‍♂ E4.0 man rowing boat
1F6A3 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🚣🏻‍♂️ E4.0 man rowing boat: light skin tone
1F6A3 1F3FB 200D 2642                      ; minimally-qualified # 🚣🏻‍♂ E4.0 man rowing boat: light skin tone
1F6A3 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🚣🏼‍♂️ E4.0 man rowing boat: medium-light skin tone
1F6A3 1F3FC 200D 2642                      ; minimally-qualified # 🚣🏼‍♂ E4.0 man rowing boat: medium-light skin tone
1F6A3 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🚣🏽‍♂️ E4.0 man rowing boat: medium skin tone
1F6A3 1F3FD 200D 2642                      ; minimally-qualified # 🚣🏽‍♂ E4.0 man rowing boat: medium skin tone
1F6A3 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🚣🏾‍♂️ E4.0 man rowing boat: medium-dark skin tone
1F6A3 1F3FE 200D 2642                      ; minimally-qualified # 🚣🏾‍♂ E4.0 man rowing boat: medium-dark skin tone
1F6A3 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🚣🏿‍♂️ E4.0 man rowing boat: dark skin tone
1F6A3 1F3FF 200D 2642                      ; minimally-qualified # 🚣🏿‍♂ E4.0 man rowing boat: dark skin tone
1F6A3 200D 2640 FE0F                       ; fully-qualified     # 🚣‍♀️ E4.0 woman rowing boat
1F6A3 200D 2640                            ; minimally-qualified # 🚣‍♀ E4.0 woman rowing boat
1F6A3 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🚣🏻‍♀️ E4.0 woman rowing boat: light skin tone
1F6A3 1F3FB 200D 2640                      ; minimally-qualified # 🚣🏻‍♀ E4.0 woman rowing boat: light skin tone
1F6A3 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🚣🏼‍♀️ E4.0 woman rowing boat: medium-light skin tone
1F6A3 1F3FC 200D 2640                      ; minimally-qualified # 🚣🏼‍♀ E4.0 woman rowing boat: medium-light skin tone
1F6A3 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🚣🏽‍♀️ E4.0 woman rowing boat: medium skin tone
1F6A3 1F3FD 200D 2640                      ; minimally-qualified # 🚣🏽‍♀ E4.0 woman rowing boat: medium skin tone
1F6A3 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🚣🏾‍♀️ E4.0 woman rowing boat: medium-dark skin tone
1F6A3 1F3FE 200D 2640                      ; minimally-qualified # 🚣🏾‍♀ E4.0 woman rowing boat: medium-dark skin tone
1F6A3 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🚣🏿‍♀️ E4.0 woman rowing boat: dark skin tone
1F6A3 1F3FF 200D 2640                      ; minimally-qualified # 🚣🏿‍♀ E4.0 woman rowing boat: dark skin tone
1F3CA                                      ; fully-qualified     # 🏊 E0.6 person swimming
1F3CA 1F3FB                                ; fully-qualified     # 🏊🏻 E1.0 person swimming: light skin tone
1F3CA 1F3FC                                ; fully-qualified     # 🏊🏼 E1.0 person swimming: medium-light skin tone
1F3CA 1F3FD                                ; fully-qualified     # 🏊🏽 E1.0 person swimming: medium skin tone
1F3CA 1F3FE                                ; fully-qualified     # 🏊🏾 E1.0 person swimming: medium-dark skin tone
1F3CA 1F3FF                                ; fully-qualified     # 🏊🏿 E1.0 person swimming: dark skin tone
1F3CA 200D 2642 FE0F                       ; fully-qualified     # 🏊‍♂️ E4.0 man swimming
1F3CA 200D 2642                            ; minimally-qualified # 🏊‍♂ E4.0 man swimming
1F3CA 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🏊🏻‍♂️ E4.0 man swimming: light skin tone
1F3CA 1F3FB 200D 2642                      ; minimally-qualified # 🏊🏻‍♂ E4.0 man swimming: light skin tone
1F3CA 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🏊🏼‍♂️ E4.0 man swimming: medium-light skin tone
1F3CA 1F3FC 200D 2642                      ; minimally-qualified # 🏊🏼‍♂ E4.0 man swimming: medium-light skin tone
1F3CA 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🏊🏽‍♂️ E4.0 man swimming: medium skin tone
1F3CA 1F3FD 200D 2642                      ; minimally-qualified # 🏊🏽‍♂ E4.0 man swimming: medium skin tone
1F3CA 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🏊🏾‍♂️ E4.0 man swimming: medium-dark skin tone
1F3CA 1F3FE 200D 2642                      ; minimally-qualified # 🏊🏾‍♂ E4.0 man swimming: medium-dark skin tone
1F3CA 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🏊🏿‍♂️ E4.0 man swimming: dark skin tone
1F3CA 1F3FF 200D 2642                      ; minimally-qualified # 🏊🏿‍♂ E4.0 man swimming: dark skin tone
1F3CA 200D 2640 FE0F                       ; fully-qualified     # 🏊‍♀️ E4.0 woman swimming
1F3CA 200D 2640                            ; minimally-qualified # 🏊‍♀ E4.0 woman swimming
1F3CA 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🏊🏻‍♀️ E4.0 woman swimming: light skin tone
1F3CA 1F3FB 200D 2640                      ; minimally-qualified # 🏊🏻‍♀ E4.0 woman swimming: light skin tone
1F3CA 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🏊🏼‍♀️ E4.0 woman swimming: medium-light skin tone
1F3CA 1F3FC 200D 2640                      ; minimally-qualified # 🏊🏼‍♀ E4.0 woman swimming: medium-light skin tone
1F3CA 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🏊🏽‍♀️ E4.0 woman swimming: medium skin tone
1F3CA 1F3FD 200D 2640                      ; minimally-qualified # 🏊🏽‍♀ E4.0 woman swimming: medium skin tone
1F3CA 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🏊🏾‍♀️ E4.0 woman swimming: medium-dark skin tone
1F3CA 1F3FE 200D 2640                      ; minimally-qualified # 🏊🏾‍♀ E4.0 woman swimming: medium-dark skin tone
1F3CA 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🏊🏿‍♀️ E4.0 woman swimming: dark skin tone
1F3CA 1F3FF 200D 2640                      ; minimally-qualified # 🏊🏿‍♀ E4.0 woman swimming: dark skin tone
26F9 FE0F                                  ; fully-qualified     # ⛹️ E0.7 person bouncing ball
26F9                                       ; unqualified         # ⛹ E0.7 person bouncing ball
26F9 1F3FB                                 ; fully-qualified     # ⛹🏻 E2.0 person bouncing ball: light skin tone
26F9 1F3FC                                 ; fully-qualified     # ⛹🏼 E2.0 person bouncing ball: medium-light skin tone
26F9 1F3FD                                 ; fully-qualified     # ⛹🏽 E2.0 person bouncing ball: medium skin tone
26F9 1F3FE                                 ; fully-qualified     # ⛹🏾 E2.0 person bouncing ball: medium-dark skin tone
26F9 1F3FF                                 ; fully-qualified     # ⛹🏿 E2.0 person bouncing ball: dark skin tone
26F9 FE0F 200D 2642 FE0F                   ; fully-qualified     # ⛹️‍♂️ E4.0 man bouncing ball
26F9 200D 2642 FE0F                        ; unqualified         # ⛹‍♂️ E4.0 man bouncing ball
26F9 FE0F 200D 2642                        ; unqualified         # ⛹️‍♂ E4.0 man bouncing ball
26F9 200D 2642                             ; unqualified         # ⛹‍♂ E4.0 man bouncing ball
26F9 1F3FB 200D 2642 FE0F                  ; fully-qualified     # ⛹🏻‍♂️ E4.0 man bouncing ball: light skin tone
26F9 1F3FB 200D 2642                       ; minimally-qualified # ⛹🏻‍♂ E4.0 man bouncing ball: light skin tone
26F9 1F3FC 200D 2642 FE0F                  ; fully-qualified     # ⛹🏼‍♂️ E4.0 man bouncing ball: medium-light skin tone
26F9 1F3FC 200D 2642                       ; minimally-qualified # ⛹🏼‍♂ E4.0 man bouncing ball: medium-light skin tone
26F9 1F3FD 200D 2642 FE0F                  ; fully-qualified     # ⛹🏽‍♂️ E4.0 man bouncing ball: medium skin tone
26F9 1F3FD 200D 2642                       ; minimally-qualified # ⛹🏽‍♂ E4.0 man bouncing ball: medium skin tone
26F9 1F3FE 200D 2642 FE0F                  ; fully-qualified     # ⛹🏾‍♂️ E4.0 man bouncing ball: medium-dark skin tone
26F9 1F3FE 200D 2642                       ; minimally-qualified # ⛹🏾‍♂ E4.0 man bouncing ball: medium-dark skin tone
26F9 1F3FF 200D 2642 FE0F                  ; fully-qualified     # ⛹🏿‍♂️ E4.0 man bouncing ball: dark skin tone
26F9 1F3FF 200D 2642                       ; minimally-qualified # ⛹🏿‍♂ E4.0 man bouncing ball: dark skin tone
26F9 FE0F 200D 2640 FE0F                   ; fully-qualified     # ⛹️‍♀️ E4.0 woman bouncing ball
26F9 200D 2640 FE0F                        ; unqualified         # ⛹‍♀️ E4.0 woman bouncing ball
26F9 FE0F 200D 2640                        ; unqualified         # ⛹️‍♀ E4.0 woman bouncing ball
26F9 200D 2640                             ; unqualified         # ⛹‍♀ E4.0 woman bouncing ball
26F9 1F3FB 200D 2640 FE0F                  ; fully-qualified     # ⛹🏻‍♀️ E4.0 woman bouncing ball: light skin tone
26F9 1F3FB 200D 2640                       ; minimally-qualified # ⛹🏻‍♀ E4.0 woman bouncing ball: light skin tone
26F9 1F3FC 200D 2640 FE0F                  ; fully-qualified     # ⛹🏼‍♀️ E4.0 woman bouncing ball: medium-light skin tone
26F9 1F3FC 200D 2640                       ; minimally-qualified # ⛹🏼‍♀ E4.0 woman bouncing ball: medium-light skin tone
26F9 1F3FD 200D 2640 FE0F                  ; fully-qualified     # ⛹🏽‍♀️ E4.0 woman bouncing ball: medium skin tone
26F9 1F3FD 200D 2640                       ; minimally-qualified # ⛹🏽‍♀ E4.0 woman bouncing ball: medium skin tone
26F9 1F3FE 200D 2640 FE0F                  ; fully-qualified     # ⛹🏾‍♀️ E4.0 woman bouncing ball: medium-dark skin tone
26F9 1F3FE 200D 2640                       ; minimally-qualified # ⛹🏾‍♀ E4.0 woman bouncing ball: medium-dark skin tone
26F9 1F3FF 200D 2640 FE0F                  ; fully-qualified     # ⛹🏿‍♀️ E4.0 woman bouncing ball: dark skin tone
26F9 1F3FF 200D 2640                       ; minimally-qualified # ⛹🏿‍♀ E4.0 woman bouncing ball: dark skin tone
1F3CB FE0F                                 ; fully-qualified     # 🏋️ E0.7 person lifting weights
1F3CB                                      ; unqualified         # 🏋 E0.7 person lifting weights
1F3CB 1F3FB                                ; fully-qualified     # 🏋🏻 E2.0 person lifting weights: light skin tone
1F3CB 1F3FC                                ; fully-qualified     # 🏋🏼 E2.0 person lifting weights: medium-light skin tone
1F3CB 1F3FD                                ; fully-qualified     # 🏋🏽 E2.0 person lifting weights: medium skin tone
1F3CB 1F3FE                                ; fully-qualified     # 🏋🏾 E2.0 person lifting weights: medium-dark skin tone
1F3CB 1F3FF                                ; fully-qualified     # 🏋🏿 E2.0 person lifting weights: dark skin tone
1F3CB FE0F 200D 2642 FE0F                  ; fully-qualified     # 🏋️‍♂️ E4.0 man lifting weights
1F3CB 200D 2642 FE0F                       ; unqualified         # 🏋‍♂️ E4.0 man lifting weights
1F3CB FE0F 200D 2642                       ; unqualified         # 🏋️‍♂ E4.0 man lifting weights
1F3CB 200D 2642                            ; unqualified         # 🏋‍♂ E4.0 man lifting weights
1F3CB 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🏋🏻‍♂️ E4.0 man lifting weights: light skin tone
1F3CB 1F3FB 200D 2642                      ; minimally-qualified # 🏋🏻‍♂ E4.0 man lifting weights: light skin tone
1F3CB 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🏋🏼‍♂️ E4.0 man lifting weights: medium-light skin tone
1F3CB 1F3FC 200D 2642                      ; minimally-qualified # 🏋🏼‍♂ E4.0 man lifting weights: medium-light skin tone
1F3CB 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🏋🏽‍♂️ E4.0 man lifting weights: medium skin tone
1F3CB 1F3FD 200D 2642                      ; minimally-qualified # 🏋🏽‍♂ E4.0 man lifting weights: medium skin tone
1F3CB 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🏋🏾‍♂️ E4.0 man lifting weights: medium-dark skin tone
1F3CB 1F3FE 200D 2642                      ; minimally-qualified # 🏋🏾‍♂ E4.0 man lifting weights: medium-dark skin tone
1F3CB 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🏋🏿‍♂️ E4.0 man lifting weights: dark skin tone
1F3CB 1F3FF 200D 2642                      ; minimally-qualified # 🏋🏿‍♂ E4.0 man lifting weights: dark skin tone
1F3CB FE0F 200D 2640 FE0F                  ; fully-qualified     # 🏋️‍♀️ E4.0 woman lifting weights
1F3CB 200D 2640 FE0F                       ; unqualified         # 🏋‍♀️ E4.0 woman lifting weights
1F3CB FE0F 200D 2640                       ; unqualified         # 🏋️‍♀ E4.0 woman lifting weights
1F3CB 200D 2640                            ; unqualified         # 🏋‍♀ E4.0 woman lifting weights
1F3CB 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🏋🏻‍♀️ E4.0 woman lifting weights: light skin tone
1F3CB 1F3FB 200D 2640                      ; minimally-qualified # 🏋🏻‍♀ E4.0 woman lifting weights: light skin tone
1F3CB 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🏋🏼‍♀️ E4.0 woman lifting weights: medium-light skin tone
1F3CB 1F3FC 200D 2640                      ; minimally-qualified # 🏋🏼‍♀ E4.0 woman lifting weights: medium-light skin tone
1F3CB 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🏋🏽‍♀️ E4.0 woman lifting weights: medium skin tone
1F3CB 1F3FD 200D 2640                      ; minimally-qualified # 🏋🏽‍♀ E4.0 woman lifting weights: medium skin tone
1F3CB 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🏋🏾‍♀️ E4.0 woman lifting weights: medium-dark skin tone
1F3CB 1F3FE 200D 2640                      ; minimally-qualified # 🏋🏾‍♀ E4.0 woman lifting weights: medium-dark skin tone
1F3CB 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🏋🏿‍♀️ E4.0 woman lifting weights: dark skin tone
1F3CB 1F3FF 200D 2640                      ; minimally-qualified # 🏋🏿‍♀ E4.0 woman lifting weights: dark skin tone
1F6B4                                      ; fully-qualified     # 🚴 E1.0 person biking
1F6B4 1F3FB                                ; fully-qualified     # 🚴🏻 E1.0 person biking: light skin tone
1F6B4 1F3FC                                ; fully-qualified     # 🚴🏼 E1.0 person biking: medium-light skin tone
1F6B4 1F3FD                                ; fully-qualified     # 🚴🏽 E1.0 person biking: medium skin tone
1F6B4 1F3FE                                ; fully-qualified     # 🚴🏾 E1.0 person biking: medium-dark skin tone
1F6B4 1F3FF                                ; fully-qualified     # 🚴🏿 E1.0 person biking: dark skin tone
1F6B4 200D 2642 FE0F                       ; fully-qualified     # 🚴‍♂️ E4.0 man biking
1F6B4 200D 2642                            ; minimally-qualified # 🚴‍♂ E4.0 man biking
1F6B4 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🚴🏻‍♂️ E4.0 man biking: light skin tone
1F6B4 1F3FB 200D 2642                      ; minimally-qualified # 🚴🏻‍♂ E4.0 man biking: light skin tone
1F6B4 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🚴🏼‍♂️ E4.0 man biking: medium-light skin tone
1F6B4 1F3FC 200D 2642                      ; minimally-qualified # 🚴🏼‍♂ E4.0 man biking: medium-light skin tone
1F6B4 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🚴🏽‍♂️ E4.0 man biking: medium skin tone
1F6B4 1F3FD 200D 2642                      ; minimally-qualified # 🚴🏽‍♂ E4.0 man biking: medium skin tone
1F6B4 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🚴🏾‍♂️ E4.0 man biking: medium-dark skin tone
1F6B4 1F3FE 200D 2642                      ; minimally-qualified # 🚴🏾‍♂ E4.0 man biking: medium-dark skin tone
1F6B4 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🚴🏿‍♂️ E4.0 man biking: dark skin tone
1F6B4 1F3FF 200D 2642                      ; minimally-qualified # 🚴🏿‍♂ E4.0 man biking: dark skin tone
1F6B4 200D 2640 FE0F                       ; fully-qualified     # 🚴‍♀️ E4.0 woman biking
1F6B4 200D 2640                            ; minimally-qualified # 🚴‍♀ E4.0 woman biking
1F6B4 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🚴🏻‍♀️ E4.0 woman biking: light skin tone
1F6B4 1F3FB 200D 2640                      ; minimally-qualified # 🚴🏻‍♀ E4.0 woman biking: light skin tone
1F6B4 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🚴🏼‍♀️ E4.0 woman biking: medium-light skin tone
1F6B4 1F3FC 200D 2640                      ; minimally-qualified # 🚴🏼‍♀ E4.0 woman biking: medium-light skin tone
1F6B4 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🚴🏽‍♀️ E4.0 woman biking: medium skin tone
1F6B4 1F3FD 200D 2640                      ; minimally-qualified # 🚴🏽‍♀ E4.0 woman biking: medium skin tone
1F6B4 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🚴🏾‍♀️ E4.0 woman biking: medium-dark skin tone
1F6B4 1F3FE 200D 2640                      ; minimally-qualified # 🚴🏾‍♀ E4.0 woman biking: medium-dark skin tone
1F6B4 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🚴🏿‍♀️ E4.0 woman biking: dark skin tone
1F6B4 1F3FF 200D 2640                      ; minimally-qualified # 🚴🏿‍♀ E4.0 woman biking: dark skin tone
1F6B5                                      ; fully-qualified     # 🚵 E1.0 person mountain biking
1F6B5 1F3FB                                ; fully-qualified     # 🚵🏻 E1.0 person mountain biking: light skin tone
1F6B5 1F3FC                                ; fully-qualified     # 🚵🏼 E1.0 person mountain biking: medium-light skin tone
1F6B5 1F3FD                                ; fully-qualified     # 🚵🏽 E1.0 person mountain biking: medium skin tone
1F6B5 1F3FE                                ; fully-qualified     # 🚵🏾 E1.0 person mountain biking: medium-dark skin tone
1F6B5 1F3FF                                ; fully-qualified     # 🚵🏿 E1.0 person mountain biking: dark skin tone
1F6B5 200D 2642 FE0F                       ; fully-qualified     # 🚵‍♂️ E4.0 man mountain biking
1F6B5 200D 2642                            ; minimally-qualified # 🚵‍♂ E4.0 man mountain biking
1F6B5 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🚵🏻‍♂️ E4.0 man mountain biking: light skin tone
1F6B5 1F3FB 200D 2642                      ; minimally-qualified # 🚵🏻‍♂ E4.0 man mountain biking: light skin tone
1F6B5 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🚵🏼‍♂️ E4.0 man mountain biking: medium-light skin tone
1F6B5 1F3FC 200D 2642                      ; minimally-qualified # 🚵🏼‍♂ E4.0 man mountain biking: medium-light skin tone
1F6B5 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🚵🏽‍♂️ E4.0 man mountain biking: medium skin tone
1F6B5 1F3FD 200D 2642                      ; minimally-qualified # 🚵🏽‍♂ E4.0 man mountain biking: medium skin tone
1F6B5 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🚵🏾‍♂️ E4.0 man mountain biking: medium-dark skin tone
1F6B5 1F3FE 200D 2642                      ; minimally-qualified # 🚵🏾‍♂ E4.0 man mountain biking: medium-dark skin tone
1F6B5 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🚵🏿‍♂️ E4.0 man mountain biking: dark skin tone
1F6B5 1F3FF 200D 2642                      ; minimally-qualified # 🚵🏿‍♂ E4.0 man mountain biking: dark skin tone
1F6B5 200D 2640 FE0F                       ; fully-qualified     # 🚵‍♀️ E4.0 woman mountain biking
1F6B5 200D 2640                            ; minimally-qualified # 🚵‍♀ E4.0 woman mountain biking
1F6B5 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🚵🏻‍♀️ E4.0 woman mountain biking: light skin tone
1F6B5 1F3FB 200D 2640                      ; minimally-qualified # 🚵🏻‍♀ E4.0 woman mountain biking: light skin tone
1F6B5 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🚵🏼‍♀️ E4.0 woman mountain biking: medium-light skin tone
1F6B5 1F3FC 200D 2640                      ; minimally-qualified # 🚵🏼‍♀ E4.0 woman mountain biking: medium-light skin tone
1F6B5 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🚵🏽‍♀️ E4.0 woman mountain biking: medium skin tone
1F6B5 1F3FD 200D 2640                      ; minimally-qualified # 🚵🏽‍♀ E4.0 woman mountain biking: medium skin tone
1F6B5 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🚵🏾‍♀️ E4.0 woman mountain biking: medium-dark skin tone
1F6B5 1F3FE 200D 2640                      ; minimally-qualified # 🚵🏾‍♀ E4.0 woman mountain biking: medium-dark skin tone
1F6B5 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🚵🏿‍♀️ E4.0 woman mountain biking: dark skin tone
1F6B5 1F3FF 200D 2640                      ; minimally-qualified # 🚵🏿‍♀ E4.0 woman mountain biking: dark skin tone
1F938                                      ; fully-qualified     # 🤸 E3.0 person cartwheeling
1F938 1F3FB                                ; fully-qualified     # 🤸🏻 E3.0 person cartwheeling: light skin tone
1F938 1F3FC                                ; fully-qualified     # 🤸🏼 E3.0 person cartwheeling: medium-light skin tone
1F938 1F3FD                                ; fully-qualified     # 🤸🏽 E3.0 person cartwheeling: medium skin tone
1F938 1F3FE                                ; fully-qualified     # 🤸🏾 E3.0 person cartwheeling: medium-dark skin tone
1F938 1F3FF                                ; fully-qualified     # 🤸🏿 E3.0 person cartwheeling: dark skin tone
1F938 200D 2642 FE0F                       ; fully-qualified     # 🤸‍♂️ E4.0 man cartwheeling
1F938 200D 2642                            ; minimally-qualified # 🤸‍♂ E4.0 man cartwheeling
1F938 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🤸🏻‍♂️ E4.0 man cartwheeling: light skin tone
1F938 1F3FB 200D 2642                      ; minimally-qualified # 🤸🏻‍♂ E4.0 man cartwheeling: light skin tone
1F938 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🤸🏼‍♂️ E4.0 man cartwheeling: medium-light skin tone
1F938 1F3FC 200D 2642                      ; minimally-qualified # 🤸🏼‍♂ E4.0 man cartwheeling: medium-light skin tone
1F938 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🤸🏽‍♂️ E4.0 man cartwheeling: medium skin tone
1F938 1F3FD 200D 2642                      ; minimally-qualified # 🤸🏽‍♂ E4.0 man cartwheeling: medium skin tone
1F938 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🤸🏾‍♂️ E4.0 man cartwheeling: medium-dark skin tone
1F938 1F3FE 200D 2642                      ; minimally-qualified # 🤸🏾‍♂ E4.0 man cartwheeling: medium-dark skin tone
1F938 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🤸🏿‍♂️ E4.0 man cartwheeling: dark skin tone
1F938 1F3FF 200D 2642                      ; minimally-qualified # 🤸🏿‍♂ E4.0 man cartwheeling: dark skin tone
1F938 200D 2640 FE0F                       ; fully-qualified     # 🤸‍♀️ E4.0 woman cartwheeling
1F938 200D 2640                            ; minimally-qualified # 🤸‍♀ E4.0 woman cartwheeling
1F938 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🤸🏻‍♀️ E4.0 woman cartwheeling: light skin tone
1F938 1F3FB 200D 2640                      ; minimally-qualified # 🤸🏻‍♀ E4.0 woman cartwheeling: light skin tone
1F938 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🤸🏼‍♀️ E4.0 woman cartwheeling: medium-light skin tone
1F938 1F3FC 200D 2640                      ; minimally-qualified # 🤸🏼‍♀ E4.0 woman cartwheeling: medium-light skin tone
1F938 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🤸🏽‍♀️ E4.0 woman cartwheeling: medium skin tone
1F938 1F3FD 200D 2640                      ; minimally-qualified # 🤸🏽‍♀ E4.0 woman cartwheeling: medium skin tone
1F938 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🤸🏾‍♀️ E4.0 woman cartwheeling: medium-dark skin tone
1F938 1F3FE 200D 2640                      ; minimally-qualified # 🤸🏾‍♀ E4.0 woman cartwheeling: medium-dark skin tone
1F938 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🤸🏿‍♀️ E4.0 woman cartwheeling: dark skin tone
1F938 1F3FF 200D 2640                      ; minimally-qualified # 🤸🏿‍♀ E4.0 woman cartwheeling: dark skin tone
1F93C                                      ; fully-qualified     # 🤼 E3.0 people wrestling
1F93C 200D 2642 FE0F                       ; fully-qualified     # 🤼‍♂️ E4.0 men wrestling
1F93C 200D 2642                            ; minimally-qualified # 🤼‍♂ E4.0 men wrestling
1F93C 200D 2640 FE0F                       ; fully-qualified     # 🤼‍♀️ E4.0 women wrestling
1F93C 200D 2640                            ; minimally-qualified # 🤼‍♀ E4.0 women wrestling
1F93D                                      ; fully-qualified     # 🤽 E3.0 person playing water polo
1F93D 1F3FB                                ; fully-qualified     # 🤽🏻 E3.0 person playing water polo: light skin tone
1F93D 1F3FC                                ; fully-qualified     # 🤽🏼 E3.0 person playing water polo: medium-light skin tone
1F93D 1F3FD                                ; fully-qualified     # 🤽🏽 E3.0 person playing water polo: medium skin tone
1F93D 1F3FE                                ; fully-qualified     # 🤽🏾 E3.0 person playing water polo: medium-dark skin tone
1F93D 1F3FF                                ; fully-qualified     # 🤽🏿 E3.0 person playing water polo: dark skin tone
1F93D 200D 2642 FE0F                       ; fully-qualified     # 🤽‍♂️ E4.0 man playing water polo
1F93D 200D 2642                            ; minimally-qualified # 🤽‍♂ E4.0 man playing water polo
1F93D 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🤽🏻‍♂️ E4.0 man playing water polo: light skin tone
1F93D 1F3FB 200D 2642                      ; minimally-qualified # 🤽🏻‍♂ E4.0 man playing water polo: light skin tone
1F93D 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🤽🏼‍♂️ E4.0 man playing water polo: medium-light skin tone
1F93D 1F3FC 200D 2642                      ; minimally-qualified # 🤽🏼‍♂ E4.0 man playing water polo: medium-light skin tone
1F93D 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🤽🏽‍♂️ E4.0 man playing water polo: medium skin tone
1F93D 1F3FD 200D 2642                      ; minimally-qualified # 🤽🏽‍♂ E4.0 man playing water polo: medium skin tone
1F93D 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🤽🏾‍♂️ E4.0 man playing water polo: medium-dark skin tone
1F93D 1F3FE 200D 2642                      ; minimally-qualified # 🤽🏾‍♂ E4.0 man playing water polo: medium-dark skin tone
1F93D 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🤽🏿‍♂️ E4.0 man playing water polo: dark skin tone
1F93D 1F3FF 200D 2642                      ; minimally-qualified # 🤽🏿‍♂ E4.0 man playing water polo: dark skin tone
1F93D 200D 2640 FE0F                       ; fully-qualified     # 🤽‍♀️ E4.0 woman playing water polo
1F93D 200D 2640                            ; minimally-qualified # 🤽‍♀ E4.0 woman playing water polo
1F93D 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🤽🏻‍♀️ E4.0 woman playing water polo: light skin tone
1F93D 1F3FB 200D 2640                      ; minimally-qualified # 🤽🏻‍♀ E4.0 woman playing water polo: light skin tone
1F93D 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🤽🏼‍♀️ E4.0 woman playing water polo: medium-light skin tone
1F93D 1F3FC 200D 2640                      ; minimally-qualified # 🤽🏼‍♀ E4.0 woman playing water polo: medium-light skin tone
1F93D 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🤽🏽‍♀️ E4.0 woman playing water polo: medium skin tone
1F93D 1F3FD 200D 2640                      ; minimally-qualified # 🤽🏽‍♀ E4.0 woman playing water polo: medium skin tone
1F93D 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🤽🏾‍♀️ E4.0 woman playing water polo: medium-dark skin tone
1F93D 1F3FE 200D 2640                      ; minimally-qualified # 🤽🏾‍♀ E4.0 woman playing water polo: medium-dark skin tone
1F93D 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🤽🏿‍♀️ E4.0 woman playing water polo: dark skin tone
1F93D 1F3FF 200D 2640                      ; minimally-qualified # 🤽🏿‍♀ E4.0 woman playing water polo: dark skin tone
1F93E                                      ; fully-qualified     # 🤾 E3.0 person playing handball
1F93E 1F3FB                                ; fully-qualified     # 🤾🏻 E3.0 person playing handball: light skin tone
1F93E 1F3FC                                ; fully-qualified     # 🤾🏼 E3.0 person playing handball: medium-light skin tone
1F93E 1F3FD                                ; fully-qualified     # 🤾🏽 E3.0 person playing handball: medium skin tone
1F93E 1F3FE                                ; fully-qualified     # 🤾🏾 E3.0 person playing handball: medium-dark skin tone
1F93E 1F3FF                                ; fully-qualified     # 🤾🏿 E3.0 person playing handball: dark skin tone
1F93E 200D 2642 FE0F                       ; fully-qualified     # 🤾‍♂️ E4.0 man playing handball
1F93E 200D 2642                            ; minimally-qualified # 🤾‍♂ E4.0 man playing handball
1F93E 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🤾🏻‍♂️ E4.0 man playing handball: light skin tone
1F93E 1F3FB 200D 2642                      ; minimally-qualified # 🤾🏻‍♂ E4.0 man playing handball: light skin tone
1F93E 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🤾🏼‍♂️ E4.0 man playing handball: medium-light skin tone
1F93E 1F3FC 200D 2642                      ; minimally-qualified # 🤾🏼‍♂ E4.0 man playing handball: medium-light skin tone
1F93E 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🤾🏽‍♂️ E4.0 man playing handball: medium skin tone
1F93E 1F3FD 200D 2642                      ; minimally-qualified # 🤾🏽‍♂ E4.0 man playing handball: medium skin tone
1F93E 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🤾🏾‍♂️ E4.0 man playing handball: medium-dark skin tone
1F93E 1F3FE 200D 2642                      ; minimally-qualified # 🤾🏾‍♂ E4.0 man playing handball: medium-dark skin tone
1F93E 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🤾🏿‍♂️ E4.0 man playing handball: dark skin tone
1F93E 1F3FF 200D 2642                      ; minimally-qualified # 🤾🏿‍♂ E4.0 man playing handball: dark skin tone
1F93E 200D 2640 FE0F                       ; fully-qualified     # 🤾‍♀️ E4.0 woman playing handball
1F93E 200D 2640                            ; minimally-qualified # 🤾‍♀ E4.0 woman playing handball
1F93E 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🤾🏻‍♀️ E4.0 woman playing handball: light skin tone
1F93E 1F3FB 200D 2640                      ; minimally-qualified # 🤾🏻‍♀ E4.0 woman playing handball: light skin tone
1F93E 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🤾🏼‍♀️ E4.0 woman playing handball: medium-light skin tone
1F93E 1F3FC 200D 2640                      ; minimally-qualified # 🤾🏼‍♀ E4.0 woman playing handball: medium-light skin tone
1F93E 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🤾🏽‍♀️ E4.0 woman playing handball: medium skin tone
1F93E 1F3FD 200D 2640                      ; minimally-qualified # 🤾🏽‍♀ E4.0 woman playing handball: medium skin tone
1F93E 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🤾🏾‍♀️ E4.0 woman playing handball: medium-dark skin tone
1F93E 1F3FE 200D 2640                      ; minimally-qualified # 🤾🏾‍♀ E4.0 woman playing handball: medium-dark skin tone
1F93E 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🤾🏿‍♀️ E4.0 woman playing handball: dark skin tone
1F93E 1F3FF 200D 2640                      ; minimally-qualified # 🤾🏿‍♀ E4.0 woman playing handball: dark skin tone
1F939                                      ; fully-qualified     # 🤹 E3.0 person juggling
1F939 1F3FB                                ; fully-qualified     # 🤹🏻 E3.0 person juggling: light skin tone
1F939 1F3FC                                ; fully-qualified     # 🤹🏼 E3.0 person juggling: medium-light skin tone
1F939 1F3FD                                ; fully-qualified     # 🤹🏽 E3.0 person juggling: medium skin tone
1F939 1F3FE                                ; fully-qualified     # 🤹🏾 E3.0 person juggling: medium-dark skin tone
1F939 1F3FF                                ; fully-qualified     # 🤹🏿 E3.0 person juggling: dark skin tone
1F939 200D 2642 FE0F                       ; fully-qualified     # 🤹‍♂️ E4.0 man juggling
1F939 200D 2642                            ; minimally-qualified # 🤹‍♂ E4.0 man juggling
1F939 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🤹🏻‍♂️ E4.0 man juggling: light skin tone
1F939 1F3FB 200D 2642                      ; minimally-qualified # 🤹🏻‍♂ E4.0 man juggling: light skin tone
1F939 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🤹🏼‍♂️ E4.0 man juggling: medium-light skin tone
1F939 1F3FC 200D 2642                      ; minimally-qualified # 🤹🏼‍♂ E4.0 man juggling: medium-light skin tone
1F939 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🤹🏽‍♂️ E4.0 man juggling: medium skin tone
1F939 1F3FD 200D 2642                      ; minimally-qualified # 🤹🏽‍♂ E4.0 man juggling: medium skin tone
1F939 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🤹🏾‍♂️ E4.0 man juggling: medium-dark skin tone
1F939 1F3FE 200D 2642                      ; minimally-qualified # 🤹🏾‍♂ E4.0 man juggling: medium-dark skin tone
1F939 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🤹🏿‍♂️ E4.0 man juggling: dark skin tone
1F939 1F3FF 200D 2642                      ; minimally-qualified # 🤹🏿‍♂ E4.0 man juggling: dark skin tone
1F939 200D 2640 FE0F                       ; fully-qualified     # 🤹‍♀️ E4.0 woman juggling
1F939 200D 2640                            ; minimally-qualified # 🤹‍♀ E4.0 woman juggling
1F939 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🤹🏻‍♀️ E4.0 woman juggling: light skin tone
1F939 1F3FB 200D 2640                      ; minimally-qualified # 🤹🏻‍♀ E4.0 woman juggling: light skin tone
1F939 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🤹🏼‍♀️ E4.0 woman juggling: medium-light skin tone
1F939 1F3FC 200D 2640                      ; minimally-qualified # 🤹🏼‍♀ E4.0 woman juggling: medium-light skin tone
1F939 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🤹🏽‍♀️ E4.0 woman juggling: medium skin tone
1F939 1F3FD 200D 2640                      ; minimally-qualified # 🤹🏽‍♀ E4.0 woman juggling: medium skin tone
1F939 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🤹🏾‍♀️ E4.0 woman juggling: medium-dark skin tone
1F939 1F3FE 200D 2640                      ; minimally-qualified # 🤹🏾‍♀ E4.0 woman juggling: medium-dark skin tone
1F939 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🤹🏿‍♀️ E4.0 woman juggling: dark skin tone
1F939 1F3FF 200D 2640                      ; minimally-qualified # 🤹🏿‍♀ E4.0 woman juggling: dark skin tone

# subgroup: person-resting
1F9D8                                      ; fully-qualified     # 🧘 E5.0 person in lotus position
1F9D8 1F3FB                                ; fully-qualified     # 🧘🏻 E5.0 person in lotus position: light skin tone
1F9D8 1F3FC                                ; fully-qualified     # 🧘🏼 E5.0 person in lotus position: medium-light skin tone
1F9D8 1F3FD                                ; fully-qualified     # 🧘🏽 E5.0 person in lotus position: medium skin tone
1F9D8 1F3FE                                ; fully-qualified     # 🧘🏾 E5.0 person in lotus position: medium-dark skin tone
1F9D8 1F3FF                                ; fully-qualified     # 🧘🏿 E5.0 person in lotus position: dark skin tone
1F9D8 200D 2642 FE0F                       ; fully-qualified     # 🧘‍♂️ E5.0 man in lotus position
1F9D8 200D 2642                            ; minimally-qualified # 🧘‍♂ E5.0 man in lotus position
1F9D8 1F3FB 200D 2642 FE0F                 ; fully-qualified     # 🧘🏻‍♂️ E5.0 man in lotus position: light skin tone
1F9D8 1F3FB 200D 2642                      ; minimally-qualified # 🧘🏻‍♂ E5.0 man in lotus position: light skin tone
1F9D8 1F3FC 200D 2642 FE0F                 ; fully-qualified     # 🧘🏼‍♂️ E5.0 man in lotus position: medium-light skin tone
1F9D8 1F3FC 200D 2642                      ; minimally-qualified # 🧘🏼‍♂ E5.0 man in lotus position: medium-light skin tone
1F9D8 1F3FD 200D 2642 FE0F                 ; fully-qualified     # 🧘🏽‍♂️ E5.0 man in lotus position: medium skin tone
1F9D8 1F3FD 200D 2642                      ; minimally-qualified # 🧘🏽‍♂ E5.0 man in lotus position: medium skin tone
1F9D8 1F3FE 200D 2642 FE0F                 ; fully-qualified     # 🧘🏾‍♂️ E5.0 man in lotus position: medium-dark skin tone
1F9D8 1F3FE 200D 2642                      ; minimally-qualified # 🧘🏾‍♂ E5.0 man in lotus position: medium-dark skin tone
1F9D8 1F3FF 200D 2642 FE0F                 ; fully-qualified     # 🧘🏿‍♂️ E5.0 man in lotus position: dark skin tone
1F9D8 1F3FF 200D 2642                      ; minimally-qualified # 🧘🏿‍♂ E5.0 man in lotus position: dark skin tone
1F9D8 200D 2640 FE0F                       ; fully-qualified     # 🧘‍♀️ E5.0 woman in lotus position
1F9D8 200D 2640                            ; minimally-qualified # 🧘‍♀ E5.0 woman in lotus position
1F9D8 1F3FB 200D 2640 FE0F                 ; fully-qualified     # 🧘🏻‍♀️ E5.0 woman in lotus position: light skin tone
1F9D8 1F3FB 200D 2640                      ; minimally-qualified # 🧘🏻‍♀ E5.0 woman in lotus position: light skin tone
1F9D8 1F3FC 200D 2640 FE0F                 ; fully-qualified     # 🧘🏼‍♀️ E5.0 woman in lotus position: medium-light skin tone
1F9D8 1F3FC 200D 2640                      ; minimally-qualified # 🧘🏼‍♀ E5.0 woman in lotus position: medium-light skin tone
1F9D8 1F3FD 200D 2640 FE0F                 ; fully-qualified     # 🧘🏽‍♀️ E5.0 woman in lotus position: medium skin tone
1F9D8 1F3FD 200D 2640                      ; minimally-qualified # 🧘🏽‍♀ E5.0 woman in lotus position: medium skin tone
1F9D8 1F3FE 200D 2640 FE0F                 ; fully-qualified     # 🧘🏾‍♀️ E5.0 woman in lotus position: medium-dark skin tone
1F9D8 1F3FE 200D 2640                      ; minimally-qualified # 🧘🏾‍♀ E5.0 woman in lotus position: medium-dark skin tone
1F9D8 1F3FF 200D 2640 FE0F                 ; fully-qualified     # 🧘🏿‍♀️ E5.0 woman in lotus position: dark skin tone
1F9D8 1F3FF 200D 2640                      ; minimally-qualified # 🧘🏿‍♀ E5.0 woman in lotus position: dark skin tone
1F6C0                                      ; fully-qualified     # 🛀 E0.6 person taking bath
1F6C0 1F3FB                                ; fully-qualified     # 🛀🏻 E1.0 person taking bath: light skin tone
1F6C0 1F3FC                                ; fully-qualified     # 🛀🏼 E1.0 person taking bath: medium-light skin tone
1F6C0 1F3FD                                ; fully-qualified     # 🛀🏽 E1.0 person taking bath: medium skin tone
1F6C0 1F3FE                                ; fully-qualified     # 🛀🏾 E1.0 person taking bath: medium-dark skin tone
1F6C0 1F3FF                                ; fully-qualified     # 🛀🏿 E1.0 person taking bath: dark skin tone
1F6CC                                      ; fully-qualified     # 🛌 E1.0 person in bed
1F6CC 1F3FB                                ; fully-qualified     # 🛌🏻 E4.0 person in bed: light skin tone
1F6CC 1F3FC                                ; fully-qualified     # 🛌🏼 E4.0 person in bed: medium-light skin tone
1F6CC 1F3FD                                ; fully-qualified     # 🛌🏽 E4.0 person in bed: medium skin tone
1F6CC 1F3FE                                ; fully-qualified     # 🛌🏾 E4.0 person in bed: medium-dark skin tone
1F6CC 1F3FF                                ; fully-qualified     # 🛌🏿 E4.0 person in bed: dark skin tone

# subgroup: family
1F9D1 200D 1F91D 200D 1F9D1                ; fully-qualified     # 🧑‍🤝‍🧑 E12.0 people holding hands
1F9D1 1F3FB 200D 1F91D 200D 1F9D1 1F3FB    ; fully-qualified     # 🧑🏻‍🤝‍🧑🏻 E12.0 people holding hands: light skin tone
1F9D1 1F3FB 200D 1F91D 200D 1F9D1 1F3FC    ; fully-qualified     # 🧑🏻‍🤝‍🧑🏼 E12.1 people holding hands: light skin tone, medium-light skin tone
1F9D1 1F3FB 200D 1F91D 200D 1F9D1 1F3FD    ; fully-qualified     # 🧑🏻‍🤝‍🧑🏽 E12.1 people holding hands: light skin tone, medium skin tone
1F9D1 1F3FB 200D 1F91D 200D 1F9D1 1F3FE    ; fully-qualified     # 🧑🏻‍🤝‍🧑🏾 E12.1 people holding hands: light skin tone, medium-dark skin tone
1F9D1 1F3FB 200D 1F91D 200D 1F9D1 1F3FF    ; fully-qualified     # 🧑🏻‍🤝‍🧑🏿 E12.1 people holding hands: light skin tone, dark skin tone
1F9D1 1F3FC 200D 1F91D 200D 1F9D1 1F3FB    ; fully-qualified     # 🧑🏼‍🤝‍🧑🏻 E12.0 people holding hands: medium-light skin tone, light skin tone
1F9D1 1F3FC 200D 1F91D 200D 1F9D1 1F3FC    ; fully-qualified     # 🧑🏼‍🤝‍🧑🏼 E12.0 people holding hands: medium-light skin tone
1F9D1 1F3FC 200D 1F91D 200D 1F9D1 1F3FD    ; fully-qualified     # 🧑🏼‍🤝‍🧑🏽 E12.1 people holding hands: medium-light skin tone, medium skin tone
1F9D1 1F3FC 200D 1F91D 200D 1F9D1 1F3FE    ; fully-qualified     # 🧑🏼‍🤝‍🧑🏾 E12.1 people holding hands: medium-light skin tone, medium-dark skin tone
1F9D1 1F3FC 200D 1F91D 200D 1F9D1 1F3FF    ; fully-qualified     # 🧑🏼‍🤝‍🧑🏿 E12.1 people holding hands: medium-light skin tone, dark skin tone
1F9D1 1F3FD 200D 1F91D 200D 1F9D1 1F3FB    ; fully-qualified     # 🧑🏽‍🤝‍🧑🏻 E12.0 people holding hands: medium skin tone, light skin tone
1F9D1 1F3FD 200D 1F91D 200D 1F9D1 1F3FC    ; fully-qualified     # 🧑🏽‍🤝‍🧑🏼 E12.0 people holding hands: medium skin tone, medium-light skin tone
1F9D1 1F3FD 200D 1F91D 200D 1F9D1 1F3FD    ; fully-qualified     # 🧑🏽‍🤝‍🧑🏽 E12.0 people holding hands: medium skin tone
1F9D1 1F3FD 200D 1F91D 200D 1F9D1 1F3FE    ; fully-qualified     # 🧑🏽‍🤝‍🧑🏾 E12.1 people holding hands: medium skin tone, medium-dark skin tone
1F9D1 1F3FD 200D 1F91D 200D 1F9D1 1F3FF    ; fully-qualified     # 🧑🏽‍🤝‍🧑🏿 E12.1 people holding hands: medium skin tone, dark skin tone
1F9D1 1F3FE 200D 1F91D 200D 1F9D1 1F3FB    ; fully-qualified     # 🧑🏾‍🤝‍🧑🏻 E12.0 people holding hands: medium-dark skin tone, light skin tone
1F9D1 1F3FE 200D 1F91D 200D 1F9D1 1F3FC    ; fully-qualified     # 🧑🏾‍🤝‍🧑🏼 E12.0 people holding hands: medium-dark skin tone, medium-light skin tone
1F9D1 1F3FE 200D 1F91D 200D 1F9D1 1F3FD    ; fully-qualified     # 🧑🏾‍🤝‍🧑🏽 E12.0 people holding hands: medium-dark skin tone, medium skin tone
1F9D1 1F3FE 200D 1F91D 200D 1F9D1 1F3FE    ; fully-qualified     # 🧑🏾‍🤝‍🧑🏾 E12.0 people holding hands: medium-dark skin tone
1F9D1 1F3FE 200D 1F91D 200D 1F9D1 1F3FF    ; fully-qualified     # 🧑🏾‍🤝‍🧑🏿 E12.1 people holding hands: medium-dark skin tone, dark skin tone
1F9D1 1F3FF 200D 1F91D 200D 1F9D1 1F3FB    ; fully-qualified     # 🧑🏿‍🤝‍🧑🏻 E12.0 people holding hands: dark skin tone, light skin tone
1F9D1 1F3FF 200D 1F91D 200D 1F9D1 1F3FC    ; fully-qualified     # 🧑🏿‍🤝‍🧑🏼 E12.0 people holding hands: dark skin tone, medium-light skin tone
1F9D1 1F3FF 200D 1F91D 200D 1F9D1 1F3FD    ; fully-qualified     # 🧑🏿‍🤝‍🧑🏽 E12.0 people holding hands: dark skin tone, medium skin tone
1F9D1 1F3FF 200D 1F91D 200D 1F9D1 1F3FE    ; fully-qualified     # 🧑🏿‍🤝‍🧑🏾 E12.0 people holding hands: dark skin tone, medium-dark skin tone
1F9D1 1F3FF 200D 1F91D 200D 1F9D1 1F3FF    ; fully-qualified     # 🧑🏿‍🤝‍🧑🏿 E12.0 people holding hands: dark skin tone
1F46D                                      ; fully-qualified     # 👭 E1.0 women holding hands
1F46D 1F3FB                                ; fully-qualified     # 👭🏻 E12.0 women holding hands: light skin tone
1F469 1F3FB 200D 1F91D 200D 1F469 1F3FC    ; fully-qualified     # 👩🏻‍🤝‍👩🏼 E12.1 women holding hands: light skin tone, medium-light skin tone
1F469 1F3FB 200D 1F91D 200D 1F469 1F3FD    ; fully-qualified     # 👩🏻‍🤝‍👩🏽 E12.1 women holding hands: light skin tone, medium skin tone
1F469 1F3FB 200D 1F91D 200D 1F469 1F3FE    ; fully-qualified     # 👩🏻‍🤝‍👩🏾 E12.1 women holding hands: light skin tone, medium-dark skin tone
1F469 1F3FB 200D 1F91D 200D 1F469 1F3FF    ; fully-qualified     # 👩🏻‍🤝‍👩🏿 E12.1 women holding hands: light skin tone, dark skin tone
1F469 1F3FC 200D 1F91D 200D 1F469 1F3FB    ; fully-qualified     # 👩🏼‍🤝‍👩🏻 E12.0 women holding hands: medium-light skin tone, light skin tone
1F46D 1F3FC                                ; fully-qualified     # 👭🏼 E12.0 women holding hands: medium-light skin tone
1F469 1F3FC 200D 1F91D 200D 1F469 1F3FD    ; fully-qualified     # 👩🏼‍🤝‍👩🏽 E12.1 women holding hands: medium-light skin tone, medium skin tone
1F469 1F3FC 200D 1F91D 200D 1F469 1F3FE    ; fully-qualified     # 👩🏼‍🤝‍👩🏾 E12.1 women holding hands: medium-light skin tone, medium-dark skin tone
1F469 1F3FC 200D 1F91D 200D 1F469 1F3FF    ; fully-qualified     # 👩🏼‍🤝‍👩🏿 E12.1 women holding hands: medium-light skin tone, dark skin tone
1F469 1F3FD 200D 1F91D 200D 1F469 1F3FB    ; fully-qualified     # 👩🏽‍🤝‍👩🏻 E12.0 women holding hands: medium skin tone, light skin tone
1F469 1F3FD 200D 1F91D 200D 1F469 1F3FC    ; fully-qualified     # 👩🏽‍🤝‍👩🏼 E12.0 women holding hands: medium skin tone, medium-light skin tone
1F46D 1F3FD                                ; fully-qualified     # 👭🏽 E12.0 women holding hands: medium skin tone
1F469 1F3FD 200D 1F91D 200D 1F469 1F3FE    ; fully-qualified     # 👩🏽‍🤝‍👩🏾 E12.1 women holding hands: medium skin tone, medium-dark skin tone
1F469 1F3FD 200D 1F91D 200D 1F469 1F3FF    ; fully-qualified     # 👩🏽‍🤝‍👩🏿 E12.1 women holding hands: medium skin tone, dark skin tone
1F469 1F3FE 200D 1F91D 200D 1F469 1F3FB    ; fully-qualified     # 👩🏾‍🤝‍👩🏻 E12.0 women holding hands: medium-dark skin tone, light skin tone
1F469 1F3FE 200D 1F91D 200D 1F469 1F3FC    ; fully-qualified     # 👩🏾‍🤝‍👩🏼 E12.0 women holding hands: medium-dark skin tone, medium-light skin tone
1F469 1F3FE 200D 1F91D 200D 1F469 1F3FD    ; fully-qualified     # 👩🏾‍🤝‍👩🏽 E12.0 women holding hands: medium-dark skin tone, medium skin tone
1F46D 1F3FE                                ; fully-qualified     # 👭🏾 E12.0 women holding hands: medium-dark skin tone
1F469 1F3FE 200D 1F91D 200D 1F469 1F3FF    ; fully-qualified     # 👩🏾‍🤝‍👩🏿 E12.1 women holding hands: medium-dark skin tone, dark skin tone
1F469 1F3FF 200D 1F91D 200D 1F469 1F3FB    ; fully-qualified     # 👩🏿‍🤝‍👩🏻 E12.0 women holding hands: dark skin tone, light skin tone
1F469 1F3FF 200D 1F91D 200D 1F469 1F3FC    ; fully-qualified     # 👩🏿‍🤝‍👩🏼 E12.0 women holding hands: dark skin tone, medium-light skin tone
1F469 1F3FF 200D 1F91D 200D 1F469 1F3FD    ; fully-qualified     # 👩🏿‍🤝‍👩🏽 E12.0 women holding hands: dark skin tone, medium skin tone
1F469 1F3FF 200D 1F91D 200D 1F469 1F3FE    ; fully-qualified     # 👩🏿‍🤝‍👩🏾 E12.0 women holding hands: dark skin tone, medium-dark skin tone
1F46D 1F3FF                                ; fully-qualified     # 👭🏿 E12.0 women holding hands: dark skin tone
1F46B                                      ; fully-qualified     # 👫 E0.6 woman and man holding hands
1F46B 1F3FB                                ; fully-qualified     # 👫🏻 E12.0 woman and man holding hands: light skin tone
1F469 1F3FB 200D 1F91D 200D 1F468 1F3FC    ; fully-qualified     # 👩🏻‍🤝‍👨🏼 E12.0 woman and man holding hands: light skin tone, medium-light skin tone
1F469 1F3FB 200D 1F91D 200D 1F468 1F3FD    ; fully-qualified     # 👩🏻‍🤝‍👨🏽 E12.0 woman and man holding hands: light skin tone, medium skin tone
1F469 1F3FB 200D 1F91D 200D 1F468 1F3FE    ; fully-qualified     # 👩🏻‍🤝‍👨🏾 E12.0 woman and man holding hands: light skin tone, medium-dark skin tone
1F469 1F3FB 200D 1F91D 200D 1F468 1F3FF    ; fully-qualified     # 👩🏻‍🤝‍👨🏿 E12.0 woman and man holding hands: light skin tone, dark skin tone
1F469 1F3FC 200D 1F91D 200D 1F468 1F3FB    ; fully-qualified     # 👩🏼‍🤝‍👨🏻 E12.0 woman and man holding hands: medium-light skin tone, light skin tone
1F46B 1F3FC                                ; fully-qualified     # 👫🏼 E12.0 woman and man holding hands: medium-light skin tone
1F469 1F3FC 200D 1F91D 200D 1F468 1F3FD    ; fully-qualified     # 👩🏼‍🤝‍👨🏽 E12.0 woman and man holding hands: medium-light skin tone, medium skin tone
1F469 1F3FC 200D 1F91D 200D 1F468 1F3FE    ; fully-qualified     # 👩🏼‍🤝‍👨🏾 E12.0 woman and man holding hands: medium-light skin tone, medium-dark skin tone
1F469 1F3FC 200D 1F91D 200D 1F468 1F3FF    ; fully-qualified     # 👩🏼‍🤝‍👨🏿 E12.0 woman and man holding hands: medium-light skin tone, dark skin tone
1F469 1F3FD 200D 1F91D 200D 1F468 1F3FB    ; fully-qualified     # 👩🏽‍🤝‍👨🏻 E12.0 woman and man holding hands: medium skin tone, light skin tone
1F469 1F3FD 200D 1F91D 200D 1F468 1F3FC    ; fully-qualified     # 👩🏽‍🤝‍👨🏼 E12.0 woman and man holding hands: medium skin tone, medium-light skin tone
1F46B 1F3FD                                ; fully-qualified     # 👫🏽 E12.0 woman and man holding hands: medium skin tone
1F469 1F3FD 200D 1F91D 200D 1F468 1F3FE    ; fully-qualified     # 👩🏽‍🤝‍👨🏾 E12.0 woman and man holding hands: medium skin tone, medium-dark skin tone
1F469 1F3FD 200D 1F91D 200D 1F468 1F3FF    ; fully-qualified     # 👩🏽‍🤝‍👨🏿 E12.0 woman and man holding hands: medium skin tone, dark skin tone
1F469 1F3FE 200D 1F91D 200D 1F468 1F3FB    ; fully-qualified     # 👩🏾‍🤝‍👨🏻 E12.0 woman and man holding hands: medium-dark skin tone, light skin tone
1F469 1F3FE 200D 1F91D 200D 1F468 1F3FC    ; fully-qualified     # 👩🏾‍🤝‍👨🏼 E12.0 woman and man holding hands: medium-dark skin tone, medium-light skin tone
1F469 1F3FE 200D 1F91D 200D 1F468 1F3FD    ; fully-qualified     # 👩🏾‍🤝‍👨🏽 E12.0 woman and man holding hands: medium-dark skin tone, medium skin tone
1F46B 1F3FE                                ; fully-qualified     # 👫🏾 E12.0 woman and man holding hands: medium-dark skin tone
1F469 1F3FE 200D 1F91D 200D 1F468 1F3FF    ; fully-qualified     # 👩🏾‍🤝‍👨🏿 E12.0 woman and man holding hands: medium-dark skin tone, dark skin tone
1F469 1F3FF 200D 1F91D 200D 1F468 1F3FB    ; fully-qualified     # 👩🏿‍🤝‍👨🏻 E12.0 woman and man holding hands: dark skin tone, light skin tone
1F469 1F3FF 200D 1F91D 200D 1F468 1F3FC    ; fully-qualified     # 👩🏿‍🤝‍👨🏼 E12.0 woman and man holding hands: dark skin tone, medium-light skin tone
1F469 1F3FF 200D 1F91D 200D 1F468 1F3FD    ; fully-qualified     # 👩🏿‍🤝‍👨🏽 E12.0 woman and man holding hands: dark skin tone, medium skin tone
1F469 1F3FF 200D 1F91D 200D 1F468 1F3FE    ; fully-qualified     # 👩🏿‍🤝‍👨🏾 E12.0 woman and man holding hands: dark skin tone, medium-dark skin tone
1F46B 1F3FF                                ; fully-qualified     # 👫🏿 E12.0 woman and man holding hands: dark skin tone
1F46C                                      ; fully-qualified     # 👬 E1.0 men holding hands
1F46C 1F3FB                                ; fully-qualified     # 👬🏻 E12.0 men holding hands: light skin tone
1F468 1F3FB 200D 1F91D 200D 1F468 1F3FC    ; fully-qualified     # 👨🏻‍🤝‍👨🏼 E12.1 men holding hands: light skin tone, medium-light skin tone
1F468 1F3FB 200D 1F91D 200D 1F468 1F3FD    ; fully-qualified     # 👨🏻‍🤝‍👨🏽 E12.1 men holding hands: light skin tone, medium skin tone
1F468 1F3FB 200D 1F91D 200D 1F468 1F3FE    ; fully-qualified     # 👨🏻‍🤝‍👨🏾 E12.1 men holding hands: light skin tone, medium-dark skin tone
1F468 1F3FB 200D 1F91D 200D 1F468 1F3FF    ; fully-qualified     # 👨🏻‍🤝‍👨🏿 E12.1 men holding hands: light skin tone, dark skin tone
1F468 1F3FC 200D 1F91D 200D 1F468 1F3FB    ; fully-qualified     # 👨🏼‍🤝‍👨🏻 E12.0 men holding hands: medium-light skin tone, light skin tone
1F46C 1F3FC                                ; fully-qualified     # 👬🏼 E12.0 men holding hands: medium-light skin tone
1F468 1F3FC 200D 1F91D 200D 1F468 1F3FD    ; fully-qualified     # 👨🏼‍🤝‍👨🏽 E12.1 men holding hands: medium-light skin tone, medium skin tone
1F468 1F3FC 200D 1F91D 200D 1F468 1F3FE    ; fully-qualified     # 👨🏼‍🤝‍👨🏾 E12.1 men holding hands: medium-light skin tone, medium-dark skin tone
1F468 1F3FC 200D 1F91D 200D 1F468 1F3FF    ; fully-qualified     # 👨🏼‍🤝‍👨🏿 E12.1 men holding hands: medium-light skin tone, dark skin tone
1F468 1F3FD 200D 1F91D 200D 1F468 1F3FB    ; fully-qualified     # 👨🏽‍🤝‍👨🏻 E12.0 men holding hands: medium skin tone, light skin tone
1F468 1F3FD 200D 1F91D 200D 1F468 1F3FC    ; fully-qualified     # 👨🏽‍🤝‍👨🏼 E12.0 men holding hands: medium skin tone, medium-light skin tone
1F46C 1F3FD                                ; fully-qualified     # 👬🏽 E12.0 men holding hands: medium skin tone
1F468 1F3FD 200D 1F91D 200D 1F468 1F3FE    ; fully-qualified     # 👨🏽‍🤝‍👨🏾 E12.1 men holding hands: medium skin tone, medium-dark skin tone
1F468 1F3FD 200D 1F91D 200D 1F468 1F3FF    ; fully-qualified     # 👨🏽‍🤝‍👨🏿 E12.1 men holding hands: medium skin tone, dark skin tone
1F468 1F3FE 200D 1F91D 200D 1F468 1F3FB    ; fully-qualified     # 👨🏾‍🤝‍👨🏻 E12.0 men holding hands: medium-dark skin tone, light skin tone
1F468 1F3FE 200D 1F91D 200D 1F468 1F3FC    ; fully-qualified     # 👨🏾‍🤝‍👨🏼 E12.0 men holding hands: medium-dark skin tone, medium-light skin tone
1F468 1F3FE 200D 1F91D 200D 1F468 1F3FD    ; fully-qualified     # 👨🏾‍🤝‍👨🏽 E12.0 men holding hands: medium-dark skin tone, medium skin tone
1F46C 1F3FE                                ; fully-qualified     # 👬🏾 E12.0 men holding hands: medium-dark skin tone
1F468 1F3FE 200D 1F91D 200D 1F468 1F3FF    ; fully-qualified     # 👨🏾‍🤝‍👨🏿 E12.1 men holding hands: medium-dark skin tone, dark skin tone
1F468 1F3FF 200D 1F91D 200D 1F468 1F3FB    ; fully-qualified     # 👨🏿‍🤝‍👨🏻 E12.0 men holding hands: dark skin tone, light skin tone
1F468 1F3FF 200D 1F91D 200D 1F468 1F3FC    ; fully-qualified     # 👨🏿‍🤝‍👨🏼 E12.0 men holding hands: dark skin tone, medium-light skin tone
1F468 1F3FF 200D 1F91D 200D 1F468 1F3FD    ; fully-qualified     # 👨🏿‍🤝‍👨🏽 E12.0 men holding hands: dark skin tone, medium skin tone
1F468 1F3FF 200D 1F91D 200D 1F468 1F3FE    ; fully-qualified     # 👨🏿‍🤝‍👨🏾 E12.0 men holding hands: dark skin tone, medium-dark skin tone
1F46C 1F3FF                                ; fully-qualified     # 👬🏿 E12.0 men holding hands: dark skin tone
1F48F                                      ; fully-qualified     # 💏 E0.6 kiss
1F469 200D 2764 FE0F 200D 1F48B 200D 1F468 ; fully-qualified     # 👩‍❤️‍💋‍👨 E2.0 kiss: woman, man
1F469 200D 2764 200D 1F48B 200D 1F468      ; minimally-qualified # 👩‍❤‍💋‍👨 E2.0 kiss: woman, man
1F468 200D 2764 FE0F 200D 1F48B 200D 1F468 ; fully-qualified     # 👨‍❤️‍💋‍👨 E2.0 kiss: man, man
1F468 200D 2764 200D 1F48B 200D 1F468      ; minimally-qualified # 👨‍❤‍💋‍👨 E2.0 kiss: man, man
1F469 200D 2764 FE0F 200D 1F48B 200D 1F469 ; fully-qualified     # 👩‍❤️‍💋‍👩 E2.0 kiss: woman, woman
1F469 200D 2764 200D 1F48B 200D 1F469      ; minimally-qualified # 👩‍❤‍💋‍👩 E2.0 kiss: woman, woman
1F491                                      ; fully-qualified     # 💑 E0.6 couple with heart
1F469 200D 2764 FE0F 200D 1F468            ; fully-qualified     # 👩‍❤️‍👨 E2.0 couple with heart: woman, man
1F469 200D 2764 200D 1F468                 ; minimally-qualified # 👩‍❤‍👨 E2.0 couple with heart: woman, man
1F468 200D 2764 FE0F 200D 1F468            ; fully-qualified     # 👨‍❤️‍👨 E2.0 couple with heart: man, man
1F468 200D 2764 200D 1F468                 ; minimally-qualified # 👨‍❤‍👨 E2.0 couple with heart: man, man
1F469 200D 2764 FE0F 200D 1F469            ; fully-qualified     # 👩‍❤️‍👩 E2.0 couple with heart: woman, woman
1F469 200D 2764 200D 1F469                 ; minimally-qualified # 👩‍❤‍👩 E2.0 couple with heart: woman, woman
1F46A                                      ; fully-qualified     # 👪 E0.6 family
1F468 200D 1F469 200D 1F466                ; fully-qualified     # 👨‍👩‍👦 E2.0 family: man, woman, boy
1F468 200D 1F469 200D 1F467                ; fully-qualified     # 👨‍👩‍👧 E2.0 family: man, woman, girl
1F468 200D 1F469 200D 1F467 200D 1F466     ; fully-qualified     # 👨‍👩‍👧‍👦 E2.0 family: man, woman, girl, boy
1F468 200D 1F469 200D 1F466 200D 1F466     ; fully-qualified     # 👨‍👩‍👦‍👦 E2.0 family: man, woman, boy, boy
1F468 200D 1F469 200D 1F467 200D 1F467     ; fully-qualified     # 👨‍👩‍👧‍👧 E2.0 family: man, woman, girl, girl
1F468 200D 1F468 200D 1F466                ; fully-qualified     # 👨‍👨‍👦 E2.0 family: man, man, boy
1F468 200D 1F468 200D 1F467                ; fully-qualified     # 👨‍👨‍👧 E2.0 family: man, man, girl
1F468 200D 1F468 200D 1F467 200D 1F466     ; fully-qualified     # 👨‍👨‍👧‍👦 E2.0 family: man, man, girl, boy
1F468 200D 1F468 200D 1F466 200D 1F466     ; fully-qualified     # 👨‍👨‍👦‍👦 E2.0 family: man, man, boy, boy
1F468 200D 1F468 200D 1F467 200D 1F467     ; fully-qualified     # 👨‍👨‍👧‍👧 E2.0 family: man, man, girl, girl
1F469 200D 1F469 200D 1F466                ; fully-qualified     # 👩‍👩‍👦 E2.0 family: woman, woman, boy
1F469 200D 1F469 200D 1F467                ; fully-qualified     # 👩‍👩‍👧 E2.0 family: woman, woman, girl
1F469 200D 1F469 200D 1F467 200D 1F466     ; fully-qualified     # 👩‍👩‍👧‍👦 E2.0 family: woman, woman, girl, boy
1F469 200D 1F469 200D 1F466 200D 1F466     ; fully-qualified     # 👩‍👩‍👦‍👦 E2.0 family: woman, woman, boy, boy
1F469 200D 1F469 200D 1F467 200D 1F467     ; fully-qualified     # 👩‍👩‍👧‍👧 E2.0 family: woman, woman, girl, girl
1F468 200D 1F466                           ; fully-qualified     # 👨‍👦 E4.0 family: man, boy
1F468 200D 1F466 200D 1F466                ; fully-qualified     # 👨‍👦‍👦 E4.0 family: man, boy, boy
1F468 200D 1F467                           ; fully-qualified     # 👨‍👧 E4.0 family: man, girl
1F468 200D 1F467 200D 1F466                ; fully-qualified     # 👨‍👧‍👦 E4.0 family: man, girl, boy
1F468 200D 1F467 200D 1F467                ; fully-qualified     # 👨‍👧‍👧 E4.0 family: man, girl, girl
1F469 200D 1F466                           ; fully-qualified     # 👩‍👦 E4.0 family: woman, boy
1F469 200D 1F466 200D 1F466                ; fully-qualified     # 👩‍👦‍👦 E4.0 family: woman, boy, boy
1F469 200D 1F467                           ; fully-qualified     # 👩‍👧 E4.0 family: woman, girl
1F469 200D 1F467 200D 1F466                ; fully-qualified     # 👩‍👧‍👦 E4.0 family: woman, girl, boy
1F469 200D 1F467 200D 1F467                ; fully-qualified     # 👩‍👧‍👧 E4.0 family: woman, girl, girl

# subgroup: person-symbol
1F5E3 FE0F                                 ; fully-qualified     # 🗣️ E0.7 speaking head
1F5E3                                      ; unqualified         # 🗣 E0.7 speaking head
1F464                                      ; fully-qualified     # 👤 E0.6 bust in silhouette
1F465                                      ; fully-qualified     # 👥 E1.0 busts in silhouette
1FAC2                                      ; fully-qualified     # 🫂 E13.0 people hugging
1F463                                      ; fully-qualified     # 👣 E0.6 footprints

# People & Body subtotal:		2485
# People & Body subtotal:		490	w/o modifiers

# group: Component

# subgroup: skin-tone
1F3FB                                      ; component           # 🏻 E1.0 light skin tone
1F3FC                                      ; component           # 🏼 E1.0 medium-light skin tone
1F3FD                                      ; component           # 🏽 E1.0 medium skin tone
1F3FE                                      ; component           # 🏾 E1.0 medium-dark skin tone
1F3FF                                      ; component           # 🏿 E1.0 dark skin tone

# subgroup: hair-style
1F9B0                                      ; component           # 🦰 E11.0 red hair
1F9B1                                      ; component           # 🦱 E11.0 curly hair
1F9B3                                      ; component           # 🦳 E11.0 white hair
1F9B2                                      ; component           # 🦲 E11.0 bald

# Component subtotal:		9
# Component subtotal:		4	w/o modifiers

# group: Animals & Nature

# subgroup: animal-mammal
1F435                                      ; fully-qualified     # 🐵 E0.6 monkey face
1F412                                      ; fully-qualified     # 🐒 E0.6 monkey
1F98D                                      ; fully-qualified     # 🦍 E3.0 gorilla
1F9A7                                      ; fully-qualified     # 🦧 E12.0 orangutan
1F436                                      ; fully-qualified     # 🐶 E0.6 dog face
1F415                                      ; fully-qualified     # 🐕 E0.7 dog
1F9AE                                      ; fully-qualified     # 🦮 E12.0 guide dog
1F415 200D 1F9BA                           ; fully-qualified     # 🐕‍🦺 E12.0 service dog
1F429                                      ; fully-qualified     # 🐩 E0.6 poodle
1F43A                                      ; fully-qualified     # 🐺 E0.6 wolf
1F98A                                      ; fully-qualified     # 🦊 E3.0 fox
1F99D                                      ; fully-qualified     # 🦝 E11.0 raccoon
1F431                                      ; fully-qualified     # 🐱 E0.6 cat face
1F408                                      ; fully-qualified     # 🐈 E0.7 cat
1F408 200D 2B1B                            ; fully-qualified     # 🐈‍⬛ E13.0 black cat
1F981                                      ; fully-qualified     # 🦁 E1.0 lion
1F42F                                      ; fully-qualified     # 🐯 E0.6 tiger face
1F405                                      ; fully-qualified     # 🐅 E1.0 tiger
1F406                                      ; fully-qualified     # 🐆 E1.0 leopard
1F434                                      ; fully-qualified     # 🐴 E0.6 horse face
1F40E                                      ; fully-qualified     # 🐎 E0.6 horse
1F984                                      ; fully-qualified     # 🦄 E1.0 unicorn
1F993                                      ; fully-qualified     # 🦓 E5.0 zebra
1F98C                                      ; fully-qualified     # 🦌 E3.0 deer
1F9AC                                      ; fully-qualified     # 🦬 E13.0 bison
1F42E                                      ; fully-qualified     # 🐮 E0.6 cow face
1F402                                      ; fully-qualified     # 🐂 E1.0 ox
1F403                                      ; fully-qualified     # 🐃 E1.0 water buffalo
1F404                                      ; fully-qualified     # 🐄 E1.0 cow
1F437                                      ; fully-qualified     # 🐷 E0.6 pig face
1F416                                      ; fully-qualified     # 🐖 E1.0 pig
1F417                                      ; fully-qualified     # 🐗 E0.6 boar
1F43D                                      ; fully-qualified     # 🐽 E0.6 pig nose
1F40F                                      ; fully-qualified     # 🐏 E1.0 ram
1F411                                      ; fully-qualified     # 🐑 E0.6 ewe
1F410                                      ; fully-qualified     # 🐐 E1.0 goat
1F42A                                      ; fully-qualified     # 🐪 E1.0 camel
1F42B                                      ; fully-qualified     # 🐫 E0.6 two-hump camel
1F999                                      ; fully-qualified     # 🦙 E11.0 llama
1F992                                      ; fully-qualified     # 🦒 E5.0 giraffe
1F418                                      ; fully-qualified     # 🐘 E0.6 elephant
1F9A3                                      ; fully-qualified     # 🦣 E13.0 mammoth
1F98F                                      ; fully-qualified     # 🦏 E3.0 rhinoceros
1F99B                                      ; fully-qualified     # 🦛 E11.0 hippopotamus
1F42D                                      ; fully-qualified     # 🐭 E0.6 mouse face
1F401                                      ; fully-qualified     # 🐁 E1.0 mouse
1F400                                      ; fully-qualified     # 🐀 E1.0 rat
1F439                                      ; fully-qualified     # 🐹 E0.6 hamster
1F430                                      ; fully-qualified     # 🐰 E0.6 rabbit face
1F407                                      ; fully-qualified     # 🐇 E1.0 rabbit
1F43F FE0F                                 ; fully-qualified     # 🐿️ E0.7 chipmunk
1F43F                                      ; unqualified         # 🐿 E0.7 chipmunk
1F9AB                                      ; fully-qualified     # 🦫 E13.0 beaver
1F994                                      ; fully-qualified     # 🦔 E5.0 hedgehog
1F987                                      ; fully-qualified     # 🦇 E3.0 bat
1F43B                                      ; fully-qualified     # 🐻 E0.6 bear
1F43B 200D 2744 FE0F                       ; fully-qualified     # 🐻‍❄️ E13.0 polar bear
1F43B 200D 2744                            ; minimally-qualified # 🐻‍❄ E13.0 polar bear
1F428                                      ; fully-qualified     # 🐨 E0.6 koala
1F43C                                      ; fully-qualified     # 🐼 E0.6 panda
1F9A5                                      ; fully-qualified     # 🦥 E12.0 sloth
1F9A6                                      ; fully-qualified     # 🦦 E12.0 otter
1F9A8                                      ; fully-qualified     # 🦨 E12.0 skunk
1F998                                      ; fully-qualified     # 🦘 E11.0 kangaroo
1F9A1                                      ; fully-qualified     # 🦡 E11.0 badger
1F43E                                      ; fully-qualified     # 🐾 E0.6 paw prints

# subgroup: animal-bird
1F983                                      ; fully-qualified     # 🦃 E1.0 turkey
1F414                                      ; fully-qualified     # 🐔 E0.6 chicken
1F413                                      ; fully-qualified     # 🐓 E1.0 rooster
1F423                                      ; fully-qualified     # 🐣 E0.6 hatching chick
1F424                                      ; fully-qualified     # 🐤 E0.6 baby chick
1F425                                      ; fully-qualified     # 🐥 E0.6 front-facing baby chick
1F426                                      ; fully-qualified     # 🐦 E0.6 bird
1F427                                      ; fully-qualified     # 🐧 E0.6 penguin
1F54A FE0F                                 ; fully-qualified     # 🕊️ E0.7 dove
1F54A                                      ; unqualified         # 🕊 E0.7 dove
1F985                                      ; fully-qualified     # 🦅 E3.0 eagle
1F986                                      ; fully-qualified     # 🦆 E3.0 duck
1F9A2                                      ; fully-qualified     # 🦢 E11.0 swan
1F989                                      ; fully-qualified     # 🦉 E3.0 owl
1F9A4                                      ; fully-qualified     # 🦤 E13.0 dodo
1FAB6                                      ; fully-qualified     # 🪶 E13.0 feather
1F9A9                                      ; fully-qualified     # 🦩 E12.0 flamingo
1F99A                                      ; fully-qualified     # 🦚 E11.0 peacock
1F99C                                      ; fully-qualified     # 🦜 E11.0 parrot

# subgroup: animal-amphibian
1F438                                      ; fully-qualified     # 🐸 E0.6 frog

# subgroup: animal-reptile
1F40A                                      ; fully-qualified     # 🐊 E1.0 crocodile
1F422                                      ; fully-qualified     # 🐢 E0.6 turtle
1F98E                                      ; fully-qualified     # 🦎 E3.0 lizard
1F40D                                      ; fully-qualified     # 🐍 E0.6 snake
1F432                                      ; fully-qualified     # 🐲 E0.6 dragon face
1F409                                      ; fully-qualified     # 🐉 E1.0 dragon
1F995                                      ; fully-qualified     # 🦕 E5.0 sauropod
1F996                                      ; fully-qualified     # 🦖 E5.0 T-Rex

# subgroup: animal-marine
1F433                                      ; fully-qualified     # 🐳 E0.6 spouting whale
1F40B                                      ; fully-qualified     # 🐋 E1.0 whale
1F42C                                      ; fully-qualified     # 🐬 E0.6 dolphin
1F9AD                                      ; fully-qualified     # 🦭 E13.0 seal
1F41F                                      ; fully-qualified     # 🐟 E0.6 fish
1F420                                      ; fully-qualified     # 🐠 E0.6 tropical fish
1F421                                      ; fully-qualified     # 🐡 E0.6 blowfish
1F988                                      ; fully-qualified     # 🦈 E3.0 shark
1F419                                      ; fully-qualified     # 🐙 E0.6 octopus
1F41A                                      ; fully-qualified     # 🐚 E0.6 spiral shell

# subgroup: animal-bug
1F40C                                      ; fully-qualified     # 🐌 E0.6 snail
1F98B                                      ; fully-qualified     # 🦋 E3.0 butterfly
1F41B                                      ; fully-qualified     # 🐛 E0.6 bug
1F41C                                      ; fully-qualified     # 🐜 E0.6 ant
1F41D                                      ; fully-qualified     # 🐝 E0.6 honeybee
1FAB2                                      ; fully-qualified     # 🪲 E13.0 beetle
1F41E                                      ; fully-qualified     # 🐞 E0.6 lady beetle
1F997                                      ; fully-qualified     # 🦗 E5.0 cricket
1FAB3                                      ; fully-qualified     # 🪳 E13.0 cockroach
1F577 FE0F                                 ; fully-qualified     # 🕷️ E0.7 spider
1F577                                      ; unqualified         # 🕷 E0.7 spider
1F578 FE0F                                 ; fully-qualified     # 🕸️ E0.7 spider web
1F578                                      ; unqualified         # 🕸 E0.7 spider web
1F982                                      ; fully-qualified     # 🦂 E1.0 scorpion
1F99F                                      ; fully-qualified     # 🦟 E11.0 mosquito
1FAB0                                      ; fully-qualified     # 🪰 E13.0 fly
1FAB1                                      ; fully-qualified     # 🪱 E13.0 worm
1F9A0                                      ; fully-qualified     # 🦠 E11.0 microbe

# subgroup: plant-flower
1F490                                      ; fully-qualified     # 💐 E0.6 bouquet
1F338                                      ; fully-qualified     # 🌸 E0.6 cherry blossom
1F4AE                                      ; fully-qualified     # 💮 E0.6 white flower
1F3F5 FE0F                                 ; fully-qualified     # 🏵️ E0.7 rosette
1F3F5                                      ; unqualified         # 🏵 E0.7 rosette
1F339                                      ; fully-qualified     # 🌹 E0.6 rose
1F940                                      ; fully-qualified     # 🥀 E3.0 wilted flower
1F33A                                      ; fully-qualified     # 🌺 E0.6 hibiscus
1F33B                                      ; fully-qualified     # 🌻 E0.6 sunflower
1F33C                                      ; fully-qualified     # 🌼 E0.6 blossom
1F337                                      ; fully-qualified     # 🌷 E0.6 tulip

# subgroup: plant-other
1F331                                      ; fully-qualified     # 🌱 E0.6 seedling
1FAB4                                      ; fully-qualified     # 🪴 E13.0 potted plant
1F332                                      ; fully-qualified     # 🌲 E1.0 evergreen tree
1F333                                      ; fully-qualified     # 🌳 E1.0 deciduous tree
1F334                                      ; fully-qualified     # 🌴 E0.6 palm tree
1F335                                      ; fully-qualified     # 🌵 E0.6 cactus
1F33E                                      ; fully-qualified     # 🌾 E0.6 sheaf of rice
1F33F                                      ; fully-qualified     # 🌿 E0.6 herb
2618 FE0F                                  ; fully-qualified     # ☘️ E1.0 shamrock
2618                                       ; unqualified         # ☘ E1.0 shamrock
1F340                                      ; fully-qualified     # 🍀 E0.6 four leaf clover
1F341                                      ; fully-qualified     # 🍁 E0.6 maple leaf
1F342                                      ; fully-qualified     # 🍂 E0.6 fallen leaf
1F343                                      ; fully-qualified     # 🍃 E0.6 leaf fluttering in wind

# Animals & Nature subtotal:		147
# Animals & Nature subtotal:		147	w/o modifiers

# group: Food & Drink

# subgroup: food-fruit
1F347                                      ; fully-qualified     # 🍇 E0.6 grapes
1F348                                      ; fully-qualified     # 🍈 E0.6 melon
1F349                                      ; fully-qualified     # 🍉 E0.6 watermelon
1F34A                                      ; fully-qualified     # 🍊 E0.6 tangerine
1F34B                                      ; fully-qualified     # 🍋 E1.0 lemon
1F34C                                      ; fully-qualified     # 🍌 E0.6 banana
1F34D                                      ; fully-qualified     # 🍍 E0.6 pineapple
1F96D                                      ; fully-qualified     # 🥭 E11.0 mango
1F34E                                      ; fully-qualified     # 🍎 E0.6 red apple
1F34F                                      ; fully-qualified     # 🍏 E0.6 green apple
1F350                                      ; fully-qualified     # 🍐 E1.0 pear
1F351                                      ; fully-qualified     # 🍑 E0.6 peach
1F352                                      ; fully-qualified     # 🍒 E0.6 cherries
1F353                                      ; fully-qualified     # 🍓 E0.6 strawberry
1FAD0                                      ; fully-qualified     # 🫐 E13.0 blueberries
1F95D                                      ; fully-qualified     # 🥝 E3.0 kiwi fruit
1F345                                      ; fully-qualified     # 🍅 E0.6 tomato
1FAD2                                      ; fully-qualified     # 🫒 E13.0 olive
1F965                                      ; fully-qualified     # 🥥 E5.0 coconut

# subgroup: food-vegetable
1F951                                      ; fully-qualified     # 🥑 E3.0 avocado
1F346                                      ; fully-qualified     # 🍆 E0.6 eggplant
1F954                                      ; fully-qualified     # 🥔 E3.0 potato
1F955                                      ; fully-qualified     # 🥕 E3.0 carrot
1F33D                                      ; fully-qualified     # 🌽 E0.6 ear of corn
1F336 FE0F                                 ; fully-qualified     # 🌶️ E0.7 hot pepper
1F336                                      ; unqualified         # 🌶 E0.7 hot pepper
1FAD1                                      ; fully-qualified     # 🫑 E13.0 bell pepper
1F952                                      ; fully-qualified     # 🥒 E3.0 cucumber
1F96C                                      ; fully-qualified     # 🥬 E11.0 leafy green
1F966                                      ; fully-qualified     # 🥦 E5.0 broccoli
1F9C4                                      ; fully-qualified     # 🧄 E12.0 garlic
1F9C5                                      ; fully-qualified     # 🧅 E12.0 onion
1F344                                      ; fully-qualified     # 🍄 E0.6 mushroom
1F95C                                      ; fully-qualified     # 🥜 E3.0 peanuts
1F330                                      ; fully-qualified     # 🌰 E0.6 chestnut

# subgroup: food-prepared
1F35E                                      ; fully-qualified     # 🍞 E0.6 bread
1F950                                      ; fully-qualified     # 🥐 E3.0 croissant
1F956                                      ; fully-qualified     # 🥖 E3.0 baguette bread
1FAD3                                      ; fully-qualified     # 🫓 E13.0 flatbread
1F968                                      ; fully-qualified     # 🥨 E5.0 pretzel
1F96F                                      ; fully-qualified     # 🥯 E11.0 bagel
1F95E                                      ; fully-qualified     # 🥞 E3.0 pancakes
1F9C7                                      ; fully-qualified     # 🧇 E12.0 waffle
1F9C0                                      ; fully-qualified     # 🧀 E1.0 cheese wedge
1F356                                      ; fully-qualified     # 🍖 E0.6 meat on bone
1F357                                      ; fully-qualified     # 🍗 E0.6 poultry leg
1F969                                      ; fully-qualified     # 🥩 E5.0 cut of meat
1F953                                      ; fully-qualified     # 🥓 E3.0 bacon
1F354                                      ; fully-qualified     # 🍔 E0.6 hamburger
1F35F                                      ; fully-qualified     # 🍟 E0.6 french fries
1F355                                      ; fully-qualified     # 🍕 E0.6 pizza
1F32D                                      ; fully-qualified     # 🌭 E1.0 hot dog
1F96A                                      ; fully-qualified     # 🥪 E5.0 sandwich
1F32E                                      ; fully-qualified     # 🌮 E1.0 taco
1F32F                                      ; fully-qualified     # 🌯 E1.0 burrito
1FAD4                                      ; fully-qualified     # 🫔 E13.0 tamale
1F959                                      ; fully-qualified     # 🥙 E3.0 stuffed flatbread
1F9C6                                      ; fully-qualified     # 🧆 E12.0 falafel
1F95A                                      ; fully-qualified     # 🥚 E3.0 egg
1F373                                      ; fully-qualified     # 🍳 E0.6 cooking
1F958                                      ; fully-qualified     # 🥘 E3.0 shallow pan of food
1F372                                      ; fully-qualified     # 🍲 E0.6 pot of food
1FAD5                                      ; fully-qualified     # 🫕 E13.0 fondue
1F963                                      ; fully-qualified     # 🥣 E5.0 bowl with spoon
1F957                                      ; fully-qualified     # 🥗 E3.0 green salad
1F37F                                      ; fully-qualified     # 🍿 E1.0 popcorn
1F9C8                                      ; fully-qualified     # 🧈 E12.0 butter
1F9C2                                      ; fully-qualified     # 🧂 E11.0 salt
1F96B                                      ; fully-qualified     # 🥫 E5.0 canned food

# subgroup: food-asian
1F371                                      ; fully-qualified     # 🍱 E0.6 bento box
1F358                                      ; fully-qualified     # 🍘 E0.6 rice cracker
1F359                                      ; fully-qualified     # 🍙 E0.6 rice ball
1F35A                                      ; fully-qualified     # 🍚 E0.6 cooked rice
1F35B                                      ; fully-qualified     # 🍛 E0.6 curry rice
1F35C                                      ; fully-qualified     # 🍜 E0.6 steaming bowl
1F35D                                      ; fully-qualified     # 🍝 E0.6 spaghetti
1F360                                      ; fully-qualified     # 🍠 E0.6 roasted sweet potato
1F362                                      ; fully-qualified     # 🍢 E0.6 oden
1F363                                      ; fully-qualified     # 🍣 E0.6 sushi
1F364                                      ; fully-qualified     # 🍤 E0.6 fried shrimp
1F365                                      ; fully-qualified     # 🍥 E0.6 fish cake with swirl
1F96E                                      ; fully-qualified     # 🥮 E11.0 moon cake
1F361                                      ; fully-qualified     # 🍡 E0.6 dango
1F95F                                      ; fully-qualified     # 🥟 E5.0 dumpling
1F960                                      ; fully-qualified     # 🥠 E5.0 fortune cookie
1F961                                      ; fully-qualified     # 🥡 E5.0 takeout box

# subgroup: food-marine
1F980                                      ; fully-qualified     # 🦀 E1.0 crab
1F99E                                      ; fully-qualified     # 🦞 E11.0 lobster
1F990                                      ; fully-qualified     # 🦐 E3.0 shrimp
1F991                                      ; fully-qualified     # 🦑 E3.0 squid
1F9AA                                      ; fully-qualified     # 🦪 E12.0 oyster

# subgroup: food-sweet
1F366                                      ; fully-qualified     # 🍦 E0.6 soft ice cream
1F367                                      ; fully-qualified     # 🍧 E0.6 shaved ice
1F368                                      ; fully-qualified     # 🍨 E0.6 ice cream
1F369                                      ; fully-qualified     # 🍩 E0.6 doughnut
1F36A                                      ; fully-qualified     # 🍪 E0.6 cookie
1F382                                      ; fully-qualified     # 🎂 E0.6 birthday cake
1F370                                      ; fully-qualified     # 🍰 E0.6 shortcake
1F9C1                                      ; fully-qualified     # 🧁 E11.0 cupcake
1F967                                      ; fully-qualified     # 🥧 E5.0 pie
1F36B                                      ; fully-qualified     # 🍫 E0.6 chocolate bar
1F36C                                      ; fully-qualified     # 🍬 E0.6 candy
1F36D                                      ; fully-qualified     # 🍭 E0.6 lollipop
1F36E                                      ; fully-qualified     # 🍮 E0.6 custard
1F36F                                      ; fully-qualified     # 🍯 E0.6 honey pot

# subgroup: drink
1F37C                                      ; fully-qualified     # 🍼 E1.0 baby bottle
1F95B                                      ; fully-qualified     # 🥛 E3.0 glass of milk
2615                                       ; fully-qualified     # ☕ E0.6 hot beverage
1FAD6                                      ; fully-qualified     # 🫖 E13.0 teapot
1F375                                      ; fully-qualified     # 🍵 E0.6 teacup without handle
1F376                                      ; fully-qualified     # 🍶 E0.6 sake
1F37E                                      ; fully-qualified     # 🍾 E1.0 bottle with popping cork
1F377                                      ; fully-qualified     # 🍷 E0.6 wine glass
1F378                                      ; fully-qualified     # 🍸 E0.6 cocktail glass
1F379                                      ; fully-qualified     # 🍹 E0.6 tropical drink
1F37A                                      ; fully-qualified     # 🍺 E0.6 beer mug
1F37B                                      ; fully-qualified     # 🍻 E0.6 clinking beer mugs
1F942                                      ; fully-qualified     # 🥂 E3.0 clinking glasses
1F943                                      ; fully-qualified     # 🥃 E3.0 tumbler glass
1F964                                      ; fully-qualified     # 🥤 E5.0 cup with straw
1F9CB                                      ; fully-qualified     # 🧋 E13.0 bubble tea
1F9C3                                      ; fully-qualified     # 🧃 E12.0 beverage box
1F9C9                                      ; fully-qualified     # 🧉 E12.0 mate
1F9CA                                      ; fully-qualified     # 🧊 E12.0 ice

# subgroup: dishware
1F962                                      ; fully-qualified     # 🥢 E5.0 chopsticks
1F37D FE0F                                 ; fully-qualified     # 🍽️ E0.7 fork and knife with plate
1F37D                                      ; unqualified         # 🍽 E0.7 fork and knife with plate
1F374                                      ; fully-qualified     # 🍴 E0.6 fork and knife
1F944                                      ; fully-qualified     # 🥄 E3.0 spoon
1F52A                                      ; fully-qualified     # 🔪 E0.6 kitchen knife
1F3FA                                      ; fully-qualified     # 🏺 E1.0 amphora

# Food & Drink subtotal:		131
# Food & Drink subtotal:		131	w/o modifiers

# group: Travel & Places

# subgroup: place-map
1F30D                                      ; fully-qualified     # 🌍 E0.7 globe showing Europe-Africa
1F30E                                      ; fully-qualified     # 🌎 E0.7 globe showing Americas
1F30F                                      ; fully-qualified     # 🌏 E0.6 globe showing Asia-Australia
1F310                                      ; fully-qualified     # 🌐 E1.0 globe with meridians
1F5FA FE0F                                 ; fully-qualified     # 🗺️ E0.7 world map
1F5FA                                      ; unqualified         # 🗺 E0.7 world map
1F5FE                                      ; fully-qualified     # 🗾 E0.6 map of Japan
1F9ED                                      ; fully-qualified     # 🧭 E11.0 compass

# subgroup: place-geographic
1F3D4 FE0F                                 ; fully-qualified     # 🏔️ E0.7 snow-capped mountain
1F3D4                                      ; unqualified         # 🏔 E0.7 snow-capped mountain
26F0 FE0F                                  ; fully-qualified     # ⛰️ E0.7 mountain
26F0                                       ; unqualified         # ⛰ E0.7 mountain
1F30B                                      ; fully-qualified     # 🌋 E0.6 volcano
1F5FB                                      ; fully-qualified     # 🗻 E0.6 mount fuji
1F3D5 FE0F                                 ; fully-qualified     # 🏕️ E0.7 camping
1F3D5                                      ; unqualified         # 🏕 E0.7 camping
1F3D6 FE0F                                 ; fully-qualified     # 🏖️ E0.7 beach with umbrella
1F3D6                                      ; unqualified         # 🏖 E0.7 beach with umbrella
1F3DC FE0F                                 ; fully-qualified     # 🏜️ E0.7 desert
1F3DC                                      ; unqualified         # 🏜 E0.7 desert
1F3DD FE0F                                 ; fully-qualified     # 🏝️ E0.7 desert island
1F3DD                                      ; unqualified         # 🏝 E0.7 desert island
1F3DE FE0F                                 ; fully-qualified     # 🏞️ E0.7 national park
1F3DE                                      ; unqualified         # 🏞 E0.7 national park

# subgroup: place-building
1F3DF FE0F                                 ; fully-qualified     # 🏟️ E0.7 stadium
1F3DF                                      ; unqualified         # 🏟 E0.7 stadium
1F3DB FE0F                                 ; fully-qualified     # 🏛️ E0.7 classical building
1F3DB                                      ; unqualified         # 🏛 E0.7 classical building
1F3D7 FE0F                                 ; fully-qualified     # 🏗️ E0.7 building construction
1F3D7                                      ; unqualified         # 🏗 E0.7 building construction
1F9F1                                      ; fully-qualified     # 🧱 E11.0 brick
1FAA8                                      ; fully-qualified     # 🪨 E13.0 rock
1FAB5                                      ; fully-qualified     # 🪵 E13.0 wood
1F6D6                                      ; fully-qualified     # 🛖 E13.0 hut
1F3D8 FE0F                                 ; fully-qualified     # 🏘️ E0.7 houses
1F3D8                                      ; unqualified         # 🏘 E0.7 houses
1F3DA FE0F                                 ; fully-qualified     # 🏚️ E0.7 derelict house
1F3DA                                      ; unqualified         # 🏚 E0.7 derelict house
1F3E0                                      ; fully-qualified     # 🏠 E0.6 house
1F3E1                                      ; fully-qualified     # 🏡 E0.6 house with garden
1F3E2                                      ; fully-qualified     # 🏢 E0.6 office building
1F3E3                                      ; fully-qualified     # 🏣 E0.6 Japanese post office
1F3E4                                      ; fully-qualified     # 🏤 E1.0 post office
1F3E5                                      ; fully-qualified     # 🏥 E0.6 hospital
1F3E6                                      ; fully-qualified     # 🏦 E0.6 bank
1F3E8                                      ; fully-qualified     # 🏨 E0.6 hotel
1F3E9                                      ; fully-qualified     # 🏩 E0.6 love hotel
1F3EA                                      ; fully-qualified     # 🏪 E0.6 convenience store
1F3EB                                      ; fully-qualified     # 🏫 E0.6 school
1F3EC                                      ; fully-qualified     # 🏬 E0.6 department store
1F3ED                                      ; fully-qualified     # 🏭 E0.6 factory
1F3EF                                      ; fully-qualified     # 🏯 E0.6 Japanese castle
1F3F0                                      ; fully-qualified     # 🏰 E0.6 castle
1F492                                      ; fully-qualified     # 💒 E0.6 wedding
1F5FC                                      ; fully-qualified     # 🗼 E0.6 Tokyo tower
1F5FD                                      ; fully-qualified     # 🗽 E0.6 Statue of Liberty

# subgroup: place-religious
26EA                                       ; fully-qualified     # ⛪ E0.6 church
1F54C                                      ; fully-qualified     # 🕌 E1.0 mosque
1F6D5                                      ; fully-qualified     # 🛕 E12.0 hindu temple
1F54D                                      ; fully-qualified     # 🕍 E1.0 synagogue
26E9 FE0F                                  ; fully-qualified     # ⛩️ E0.7 shinto shrine
26E9                                       ; unqualified         # ⛩ E0.7 shinto shrine
1F54B                                      ; fully-qualified     # 🕋 E1.0 kaaba

# subgroup: place-other
26F2                                       ; fully-qualified     # ⛲ E0.6 fountain
26FA                                       ; fully-qualified     # ⛺ E0.6 tent
1F301                                      ; fully-qualified     # 🌁 E0.6 foggy
1F303                                      ; fully-qualified     # 🌃 E0.6 night with stars
1F3D9 FE0F                                 ; fully-qualified     # 🏙️ E0.7 cityscape
1F3D9                                      ; unqualified         # 🏙 E0.7 cityscape
1F304                                      ; fully-qualified     # 🌄 E0.6 sunrise over mountains
1F305                                      ; fully-qualified     # 🌅 E0.6 sunrise
1F306                                      ; fully-qualified     # 🌆 E0.6 cityscape at dusk
1F307                                      ; fully-qualified     # 🌇 E0.6 sunset
1F309                                      ; fully-qualified     # 🌉 E0.6 bridge at night
2668 FE0F                                  ; fully-qualified     # ♨️ E0.6 hot springs
2668                                       ; unqualified         # ♨ E0.6 hot springs
1F3A0                                      ; fully-qualified     # 🎠 E0.6 carousel horse
1F3A1                                      ; fully-qualified     # 🎡 E0.6 ferris wheel
1F3A2                                      ; fully-qualified     # 🎢 E0.6 roller coaster
1F488                                      ; fully-qualified     # 💈 E0.6 barber pole
1F3AA                                      ; fully-qualified     # 🎪 E0.6 circus tent

# subgroup: transport-ground
1F682                                      ; fully-qualified     # 🚂 E1.0 locomotive
1F683                                      ; fully-qualified     # 🚃 E0.6 railway car
1F684                                      ; fully-qualified     # 🚄 E0.6 high-speed train
1F685                                      ; fully-qualified     # 🚅 E0.6 bullet train
1F686                                      ; fully-qualified     # 🚆 E1.0 train
1F687                                      ; fully-qualified     # 🚇 E0.6 metro
1F688                                      ; fully-qualified     # 🚈 E1.0 light rail
1F689                                      ; fully-qualified     # 🚉 E0.6 station
1F68A                                      ; fully-qualified     # 🚊 E1.0 tram
1F69D                                      ; fully-qualified     # 🚝 E1.0 monorail
1F69E                                      ; fully-qualified     # 🚞 E1.0 mountain railway
1F68B                                      ; fully-qualified     # 🚋 E1.0 tram car
1F68C                                      ; fully-qualified     # 🚌 E0.6 bus
1F68D                                      ; fully-qualified     # 🚍 E0.7 oncoming bus
1F68E                                      ; fully-qualified     # 🚎 E1.0 trolleybus
1F690                                      ; fully-qualified     # 🚐 E1.0 minibus
1F691                                      ; fully-qualified     # 🚑 E0.6 ambulance
1F692                                      ; fully-qualified     # 🚒 E0.6 fire engine
1F693                                      ; fully-qualified     # 🚓 E0.6 police car
1F694                                      ; fully-qualified     # 🚔 E0.7 oncoming police car
1F695                                      ; fully-qualified     # 🚕 E0.6 taxi
1F696                                      ; fully-qualified     # 🚖 E1.0 oncoming taxi
1F697                                      ; fully-qualified     # 🚗 E0.6 automobile
1F698                                      ; fully-qualified     # 🚘 E0.7 oncoming automobile
1F699                                      ; fully-qualified     # 🚙 E0.6 sport utility vehicle
1F6FB                                      ; fully-qualified     # 🛻 E13.0 pickup truck
1F69A                                      ; fully-qualified     # 🚚 E0.6 delivery truck
1F69B                                      ; fully-qualified     # 🚛 E1.0 articulated lorry
1F69C                                      ; fully-qualified     # 🚜 E1.0 tractor
1F3CE FE0F                                 ; fully-qualified     # 🏎️ E0.7 racing car
1F3CE                                      ; unqualified         # 🏎 E0.7 racing car
1F3CD FE0F                                 ; fully-qualified     # 🏍️ E0.7 motorcycle
1F3CD                                      ; unqualified         # 🏍 E0.7 motorcycle
1F6F5                                      ; fully-qualified     # 🛵 E3.0 motor scooter
1F9BD                                      ; fully-qualified     # 🦽 E12.0 manual wheelchair
1F9BC                                      ; fully-qualified     # 🦼 E12.0 motorized wheelchair
1F6FA                                      ; fully-qualified     # 🛺 E12.0 auto rickshaw
1F6B2                                      ; fully-qualified     # 🚲 E0.6 bicycle
1F6F4                                      ; fully-qualified     # 🛴 E3.0 kick scooter
1F6F9                                      ; fully-qualified     # 🛹 E11.0 skateboard
1F6FC                                      ; fully-qualified     # 🛼 E13.0 roller skate
1F68F                                      ; fully-qualified     # 🚏 E0.6 bus stop
1F6E3 FE0F                                 ; fully-qualified     # 🛣️ E0.7 motorway
1F6E3                                      ; unqualified         # 🛣 E0.7 motorway
1F6E4 FE0F                                 ; fully-qualified     # 🛤️ E0.7 railway track
1F6E4                                      ; unqualified         # 🛤 E0.7 railway track
1F6E2 FE0F                                 ; fully-qualified     # 🛢️ E0.7 oil drum
1F6E2                                      ; unqualified         # 🛢 E0.7 oil drum
26FD                                       ; fully-qualified     # ⛽ E0.6 fuel pump
1F6A8                                      ; fully-qualified     # 🚨 E0.6 police car light
1F6A5                                      ; fully-qualified     # 🚥 E0.6 horizontal traffic light
1F6A6                                      ; fully-qualified     # 🚦 E1.0 vertical traffic light
1F6D1                                      ; fully-qualified     # 🛑 E3.0 stop sign
1F6A7                                      ; fully-qualified     # 🚧 E0.6 construction

# subgroup: transport-water
2693                                       ; fully-qualified     # ⚓ E0.6 anchor
26F5                                       ; fully-qualified     # ⛵ E0.6 sailboat
1F6F6                                      ; fully-qualified     # 🛶 E3.0 canoe
1F6A4                                      ; fully-qualified     # 🚤 E0.6 speedboat
1F6F3 FE0F                                 ; fully-qualified     # 🛳️ E0.7 passenger ship
1F6F3                                      ; unqualified         # 🛳 E0.7 passenger ship
26F4 FE0F                                  ; fully-qualified     # ⛴️ E0.7 ferry
26F4                                       ; unqualified         # ⛴ E0.7 ferry
1F6E5 FE0F                                 ; fully-qualified     # 🛥️ E0.7 motor boat
1F6E5                                      ; unqualified         # 🛥 E0.7 motor boat
1F6A2                                      ; fully-qualified     # 🚢 E0.6 ship

# subgroup: transport-air
2708 FE0F                                  ; fully-qualified     # ✈️ E0.6 airplane
2708                                       ; unqualified         # ✈ E0.6 airplane
1F6E9 FE0F                                 ; fully-qualified     # 🛩️ E0.7 small airplane
1F6E9                                      ; unqualified         # 🛩 E0.7 small airplane
1F6EB                                      ; fully-qualified     # 🛫 E1.0 airplane departure
1F6EC                                      ; fully-qualified     # 🛬 E1.0 airplane arrival
1FA82                                      ; fully-qualified     # 🪂 E12.0 parachute
1F4BA                                      ; fully-qualified     # 💺 E0.6 seat
1F681                                      ; fully-qualified     # 🚁 E1.0 helicopter
1F69F                                      ; fully-qualified     # 🚟 E1.0 suspension railway
1F6A0                                      ; fully-qualified     # 🚠 E1.0 mountain cableway
1F6A1                                      ; fully-qualified     # 🚡 E1.0 aerial tramway
1F6F0 FE0F                                 ; fully-qualified     # 🛰️ E0.7 satellite
1F6F0                                      ; unqualified         # 🛰 E0.7 satellite
1F680                                      ; fully-qualified     # 🚀 E0.6 rocket
1F6F8                                      ; fully-qualified     # 🛸 E5.0 flying saucer

# subgroup: hotel
1F6CE FE0F                                 ; fully-qualified     # 🛎️ E0.7 bellhop bell
1F6CE                                      ; unqualified         # 🛎 E0.7 bellhop bell
1F9F3                                      ; fully-qualified     # 🧳 E11.0 luggage

# subgroup: time
231B                                       ; fully-qualified     # ⌛ E0.6 hourglass done
23F3                                       ; fully-qualified     # ⏳ E0.6 hourglass not done
231A                                       ; fully-qualified     # ⌚ E0.6 watch
23F0                                       ; fully-qualified     # ⏰ E0.6 alarm clock
23F1 FE0F                                  ; fully-qualified     # ⏱️ E1.0 stopwatch
23F1                                       ; unqualified         # ⏱ E1.0 stopwatch
23F2 FE0F                                  ; fully-qualified     # ⏲️ E1.0 timer clock
23F2                                       ; unqualified         # ⏲ E1.0 timer clock
1F570 FE0F                                 ; fully-qualified     # 🕰️ E0.7 mantelpiece clock
1F570                                      ; unqualified         # 🕰 E0.7 mantelpiece clock
1F55B                                      ; fully-qualified     # 🕛 E0.6 twelve o’clock
1F567                                      ; fully-qualified     # 🕧 E0.7 twelve-thirty
1F550                                      ; fully-qualified     # 🕐 E0.6 one o’clock
1F55C                                      ; fully-qualified     # 🕜 E0.7 one-thirty
1F551                                      ; fully-qualified     # 🕑 E0.6 two o’clock
1F55D                                      ; fully-qualified     # 🕝 E0.7 two-thirty
1F552                                      ; fully-qualified     # 🕒 E0.6 three o’clock
1F55E                                      ; fully-qualified     # 🕞 E0.7 three-thirty
1F553                                      ; fully-qualified     # 🕓 E0.6 four o’clock
1F55F                                      ; fully-qualified     # 🕟 E0.7 four-thirty
1F554                                      ; fully-qualified     # 🕔 E0.6 five o’clock
1F560                                      ; fully-qualified     # 🕠 E0.7 five-thirty
1F555                                      ; fully-qualified     # 🕕 E0.6 six o’clock
1F561                                      ; fully-qualified     # 🕡 E0.7 six-thirty
1F556                                      ; fully-qualified     # 🕖 E0.6 seven o’clock
1F562                                      ; fully-qualified     # 🕢 E0.7 seven-thirty
1F557                                      ; fully-qualified     # 🕗 E0.6 eight o’clock
1F563                                      ; fully-qualified     # 🕣 E0.7 eight-thirty
1F558                                      ; fully-qualified     # 🕘 E0.6 nine o’clock
1F564                                      ; fully-qualified     # 🕤 E0.7 nine-thirty
1F559                                      ; fully-qualified     # 🕙 E0.6 ten o’clock
1F565                                      ; fully-qualified     # 🕥 E0.7 ten-thirty
1F55A                                      ; fully-qualified     # 🕚 E0.6 eleven o’clock
1F566                                      ; fully-qualified     # 🕦 E0.7 eleven-thirty

# subgroup: sky & weather
1F311                                      ; fully-qualified     # 🌑 E0.6 new moon
1F312                                      ; fully-qualified     # 🌒 E1.0 waxing crescent moon
1F313                                      ; fully-qualified     # 🌓 E0.6 first quarter moon
1F314                                      ; fully-qualified     # 🌔 E0.6 waxing gibbous moon
1F315                                      ; fully-qualified     # 🌕 E0.6 full moon
1F316                                      ; fully-qualified     # 🌖 E1.0 waning gibbous moon
1F317                                      ; fully-qualified     # 🌗 E1.0 last quarter moon
1F318                                      ; fully-qualified     # 🌘 E1.0 waning crescent moon
1F319                                      ; fully-qualified     # 🌙 E0.6 crescent moon
1F31A                                      ; fully-qualified     # 🌚 E1.0 new moon face
1F31B                                      ; fully-qualified     # 🌛 E0.6 first quarter moon face
1F31C                                      ; fully-qualified     # 🌜 E0.7 last quarter moon face
1F321 FE0F                                 ; fully-qualified     # 🌡️ E0.7 thermometer
1F321                                      ; unqualified         # 🌡 E0.7 thermometer
2600 FE0F                                  ; fully-qualified     # ☀️ E0.6 sun
2600                                       ; unqualified         # ☀ E0.6 sun
1F31D                                      ; fully-qualified     # 🌝 E1.0 full moon face
1F31E                                      ; fully-qualified     # 🌞 E1.0 sun with face
1FA90                                      ; fully-qualified     # 🪐 E12.0 ringed planet
2B50                                       ; fully-qualified     # ⭐ E0.6 star
1F31F                                      ; fully-qualified     # 🌟 E0.6 glowing star
1F320                                      ; fully-qualified     # 🌠 E0.6 shooting star
1F30C                                      ; fully-qualified     # 🌌 E0.6 milky way
2601 FE0F                                  ; fully-qualified     # ☁️ E0.6 cloud
2601                                       ; unqualified         # ☁ E0.6 cloud
26C5                                       ; fully-qualified     # ⛅ E0.6 sun behind cloud
26C8 FE0F                                  ; fully-qualified     # ⛈️ E0.7 cloud with lightning and rain
26C8                                       ; unqualified         # ⛈ E0.7 cloud with lightning and rain
1F324 FE0F                                 ; fully-qualified     # 🌤️ E0.7 sun behind small cloud
1F324                                      ; unqualified         # 🌤 E0.7 sun behind small cloud
1F325 FE0F                                 ; fully-qualified     # 🌥️ E0.7 sun behind large cloud
1F325                                      ; unqualified         # 🌥 E0.7 sun behind large cloud
1F326 FE0F                                 ; fully-qualified     # 🌦️ E0.7 sun behind rain cloud
1F326                                      ; unqualified         # 🌦 E0.7 sun behind rain cloud
1F327 FE0F                                 ; fully-qualified     # 🌧️ E0.7 cloud with rain
1F327                                      ; unqualified         # 🌧 E0.7 cloud with rain
1F328 FE0F                                 ; fully-qualified     # 🌨️ E0.7 cloud with snow
1F328                                      ; unqualified         # 🌨 E0.7 cloud with snow
1F329 FE0F                                 ; fully-qualified     # 🌩️ E0.7 cloud with lightning
1F329                                      ; unqualified         # 🌩 E0.7 cloud with lightning
1F32A FE0F                                 ; fully-qualified     # 🌪️ E0.7 tornado
1F32A                                      ; unqualified         # 🌪 E0.7 tornado
1F32B FE0F                                 ; fully-qualified     # 🌫️ E0.7 fog
1F32B                                      ; unqualified         # 🌫 E0.7 fog
1F32C FE0F                                 ; fully-qualified     # 🌬️ E0.7 wind face
1F32C                                      ; unqualified         # 🌬 E0.7 wind face
1F300                                      ; fully-qualified     # 🌀 E0.6 cyclone
1F308                                      ; fully-qualified     # 🌈 E0.6 rainbow
1F302                                      ; fully-qualified     # 🌂 E0.6 closed umbrella
2602 FE0F                                  ; fully-qualified     # ☂️ E0.7 umbrella
2602                                       ; unqualified         # ☂ E0.7 umbrella
2614                                       ; fully-qualified     # ☔ E0.6 umbrella with rain drops
26F1 FE0F                                  ; fully-qualified     # ⛱️ E0.7 umbrella on ground
26F1                                       ; unqualified         # ⛱ E0.7 umbrella on ground
26A1                                       ; fully-qualified     # ⚡ E0.6 high voltage
2744 FE0F                                  ; fully-qualified     # ❄️ E0.6 snowflake
2744                                       ; unqualified         # ❄ E0.6 snowflake
2603 FE0F                                  ; fully-qualified     # ☃️ E0.7 snowman
2603                                       ; unqualified         # ☃ E0.7 snowman
26C4                                       ; fully-qualified     # ⛄ E0.6 snowman without snow
2604 FE0F                                  ; fully-qualified     # ☄️ E1.0 comet
2604                                       ; unqualified         # ☄ E1.0 comet
1F525                                      ; fully-qualified     # 🔥 E0.6 fire
1F4A7                                      ; fully-qualified     # 💧 E0.6 droplet
1F30A                                      ; fully-qualified     # 🌊 E0.6 water wave

# Travel & Places subtotal:		264
# Travel & Places subtotal:		264	w/o modifiers

# group: Activities

# subgroup: event
1F383                                      ; fully-qualified     # 🎃 E0.6 jack-o-lantern
1F384                                      ; fully-qualified     # 🎄 E0.6 Christmas tree
1F386                                      ; fully-qualified     # 🎆 E0.6 fireworks
1F387                                      ; fully-qualified     # 🎇 E0.6 sparkler
1F9E8                                      ; fully-qualified     # 🧨 E11.0 firecracker
2728                                       ; fully-qualified     # ✨ E0.6 sparkles
1F388                                      ; fully-qualified     # 🎈 E0.6 balloon
1F389                                      ; fully-qualified     # 🎉 E0.6 party popper
1F38A                                      ; fully-qualified     # 🎊 E0.6 confetti ball
1F38B                                      ; fully-qualified     # 🎋 E0.6 tanabata tree
1F38D                                      ; fully-qualified     # 🎍 E0.6 pine decoration
1F38E                                      ; fully-qualified     # 🎎 E0.6 Japanese dolls
1F38F                                      ; fully-qualified     # 🎏 E0.6 carp streamer
1F390                                      ; fully-qualified     # 🎐 E0.6 wind chime
1F391                                      ; fully-qualified     # 🎑 E0.6 moon viewing ceremony
1F9E7                                      ; fully-qualified     # 🧧 E11.0 red envelope
1F380                                      ; fully-qualified     # 🎀 E0.6 ribbon
1F381                                      ; fully-qualified     # 🎁 E0.6 wrapped gift
1F397 FE0F                                 ; fully-qualified     # 🎗️ E0.7 reminder ribbon
1F397                                      ; unqualified         # 🎗 E0.7 reminder ribbon
1F39F FE0F                                 ; fully-qualified     # 🎟️ E0.7 admission tickets
1F39F                                      ; unqualified         # 🎟 E0.7 admission tickets
1F3AB                                      ; fully-qualified     # 🎫 E0.6 ticket

# subgroup: award-medal
1F396 FE0F                                 ; fully-qualified     # 🎖️ E0.7 military medal
1F396                                      ; unqualified         # 🎖 E0.7 military medal
1F3C6                                      ; fully-qualified     # 🏆 E0.6 trophy
1F3C5                                      ; fully-qualified     # 🏅 E1.0 sports medal
1F947                                      ; fully-qualified     # 🥇 E3.0 1st place medal
1F948                                      ; fully-qualified     # 🥈 E3.0 2nd place medal
1F949                                      ; fully-qualified     # 🥉 E3.0 3rd place medal

# subgroup: sport
26BD                                       ; fully-qualified     # ⚽ E0.6 soccer ball
26BE                                       ; fully-qualified     # ⚾ E0.6 baseball
1F94E                                      ; fully-qualified     # 🥎 E11.0 softball
1F3C0                                      ; fully-qualified     # 🏀 E0.6 basketball
1F3D0                                      ; fully-qualified     # 🏐 E1.0 volleyball
1F3C8                                      ; fully-qualified     # 🏈 E0.6 american football
1F3C9                                      ; fully-qualified     # 🏉 E1.0 rugby football
1F3BE                                      ; fully-qualified     # 🎾 E0.6 tennis
1F94F                                      ; fully-qualified     # 🥏 E11.0 flying disc
1F3B3                                      ; fully-qualified     # 🎳 E0.6 bowling
1F3CF                                      ; fully-qualified     # 🏏 E1.0 cricket game
1F3D1                                      ; fully-qualified     # 🏑 E1.0 field hockey
1F3D2                                      ; fully-qualified     # 🏒 E1.0 ice hockey
1F94D                                      ; fully-qualified     # 🥍 E11.0 lacrosse
1F3D3                                      ; fully-qualified     # 🏓 E1.0 ping pong
1F3F8                                      ; fully-qualified     # 🏸 E1.0 badminton
1F94A                                      ; fully-qualified     # 🥊 E3.0 boxing glove
1F94B                                      ; fully-qualified     # 🥋 E3.0 martial arts uniform
1F945                                      ; fully-qualified     # 🥅 E3.0 goal net
26F3                                       ; fully-qualified     # ⛳ E0.6 flag in hole
26F8 FE0F                                  ; fully-qualified     # ⛸️ E0.7 ice skate
26F8                                       ; unqualified         # ⛸ E0.7 ice skate
1F3A3                                      ; fully-qualified     # 🎣 E0.6 fishing pole
1F93F                                      ; fully-qualified     # 🤿 E12.0 diving mask
1F3BD                                      ; fully-qualified     # 🎽 E0.6 running shirt
1F3BF                                      ; fully-qualified     # 🎿 E0.6 skis
1F6F7                                      ; fully-qualified     # 🛷 E5.0 sled
1F94C                                      ; fully-qualified     # 🥌 E5.0 curling stone

# subgroup: game
1F3AF                                      ; fully-qualified     # 🎯 E0.6 direct hit
1FA80                                      ; fully-qualified     # 🪀 E12.0 yo-yo
1FA81                                      ; fully-qualified     # 🪁 E12.0 kite
1F3B1                                      ; fully-qualified     # 🎱 E0.6 pool 8 ball
1F52E                                      ; fully-qualified     # 🔮 E0.6 crystal ball
1FA84                                      ; fully-qualified     # 🪄 E13.0 magic wand
1F9FF                                      ; fully-qualified     # 🧿 E11.0 nazar amulet
1F3AE                                      ; fully-qualified     # 🎮 E0.6 video game
1F579 FE0F                                 ; fully-qualified     # 🕹️ E0.7 joystick
1F579                                      ; unqualified         # 🕹 E0.7 joystick
1F3B0                                      ; fully-qualified     # 🎰 E0.6 slot machine
1F3B2                                      ; fully-qualified     # 🎲 E0.6 game die
1F9E9                                      ; fully-qualified     # 🧩 E11.0 puzzle piece
1F9F8                                      ; fully-qualified     # 🧸 E11.0 teddy bear
1FA85                                      ; fully-qualified     # 🪅 E13.0 piñata
1FA86                                      ; fully-qualified     # 🪆 E13.0 nesting dolls
2660 FE0F                                  ; fully-qualified     # ♠️ E0.6 spade suit
2660                                       ; unqualified         # ♠ E0.6 spade suit
2665 FE0F                                  ; fully-qualified     # ♥️ E0.6 heart suit
2665                                       ; unqualified         # ♥ E0.6 heart suit
2666 FE0F                                  ; fully-qualified     # ♦️ E0.6 diamond suit
2666                                       ; unqualified         # ♦ E0.6 diamond suit
2663 FE0F                                  ; fully-qualified     # ♣️ E0.6 club suit
2663                                       ; unqualified         # ♣ E0.6 club suit
265F FE0F                                  ; fully-qualified     # ♟️ E11.0 chess pawn
265F                                       ; unqualified         # ♟ E11.0 chess pawn
1F0CF                                      ; fully-qualified     # 🃏 E0.6 joker
1F004                                      ; fully-qualified     # 🀄 E0.6 mahjong red dragon
1F3B4                                      ; fully-qualified     # 🎴 E0.6 flower playing cards

# subgroup: arts & crafts
1F3AD                                      ; fully-qualified     # 🎭 E0.6 performing arts
1F5BC FE0F                                 ; fully-qualified     # 🖼️ E0.7 framed picture
1F5BC                                      ; unqualified         # 🖼 E0.7 framed picture
1F3A8                                      ; fully-qualified     # 🎨 E0.6 artist palette
1F9F5                                      ; fully-qualified     # 🧵 E11.0 thread
1FAA1                                      ; fully-qualified     # 🪡 E13.0 sewing needle
1F9F6                                      ; fully-qualified     # 🧶 E11.0 yarn
1FAA2                                      ; fully-qualified     # 🪢 E13.0 knot

# Activities subtotal:		95
# Activities subtotal:		95	w/o modifiers

# group: Objects

# subgroup: clothing
1F453                                      ; fully-qualified     # 👓 E0.6 glasses
1F576 FE0F                                 ; fully-qualified     # 🕶️ E0.7 sunglasses
1F576                                      ; unqualified         # 🕶 E0.7 sunglasses
1F97D                                      ; fully-qualified     # 🥽 E11.0 goggles
1F97C                                      ; fully-qualified     # 🥼 E11.0 lab coat
1F9BA                                      ; fully-qualified     # 🦺 E12.0 safety vest
1F454                                      ; fully-qualified     # 👔 E0.6 necktie
1F455                                      ; fully-qualified     # 👕 E0.6 t-shirt
1F456                                      ; fully-qualified     # 👖 E0.6 jeans
1F9E3                                      ; fully-qualified     # 🧣 E5.0 scarf
1F9E4                                      ; fully-qualified     # 🧤 E5.0 gloves
1F9E5                                      ; fully-qualified     # 🧥 E5.0 coat
1F9E6                                      ; fully-qualified     # 🧦 E5.0 socks
1F457                                      ; fully-qualified     # 👗 E0.6 dress
1F458                                      ; fully-qualified     # 👘 E0.6 kimono
1F97B                                      ; fully-qualified     # 🥻 E12.0 sari
1FA71                                      ; fully-qualified     # 🩱 E12.0 one-piece swimsuit
1FA72                                      ; fully-qualified     # 🩲 E12.0 briefs
1FA73                                      ; fully-qualified     # 🩳 E12.0 shorts
1F459                                      ; fully-qualified     # 👙 E0.6 bikini
1F45A                                      ; fully-qualified     # 👚 E0.6 woman’s clothes
1F45B                                      ; fully-qualified     # 👛 E0.6 purse
1F45C                                      ; fully-qualified     # 👜 E0.6 handbag
1F45D                                      ; fully-qualified     # 👝 E0.6 clutch bag
1F6CD FE0F                                 ; fully-qualified     # 🛍️ E0.7 shopping bags
1F6CD                                      ; unqualified         # 🛍 E0.7 shopping bags
1F392                                      ; fully-qualified     # 🎒 E0.6 backpack
1FA74                                      ; fully-qualified     # 🩴 E13.0 thong sandal
1F45E                                      ; fully-qualified     # 👞 E0.6 man’s shoe
1F45F                                      ; fully-qualified     # 👟 E0.6 running shoe
1F97E                                      ; fully-qualified     # 🥾 E11.0 hiking boot
1F97F                                      ; fully-qualified     # 🥿 E11.0 flat shoe
1F460                                      ; fully-qualified     # 👠 E0.6 high-heeled shoe
1F461                                      ; fully-qualified     # 👡 E0.6 woman’s sandal
1FA70                                      ; fully-qualified     # 🩰 E12.0 ballet shoes
1F462                                      ; fully-qualified     # 👢 E0.6 woman’s boot
1F451                                      ; fully-qualified     # 👑 E0.6 crown
1F452                                      ; fully-qualified     # 👒 E0.6 woman’s hat
1F3A9                                      ; fully-qualified     # 🎩 E0.6 top hat
1F393                                      ; fully-qualified     # 🎓 E0.6 graduation cap
1F9E2                                      ; fully-qualified     # 🧢 E5.0 billed cap
1FA96                                      ; fully-qualified     # 🪖 E13.0 military helmet
26D1 FE0F                                  ; fully-qualified     # ⛑️ E0.7 rescue worker’s helmet
26D1                                       ; unqualified         # ⛑ E0.7 rescue worker’s helmet
1F4FF                                      ; fully-qualified     # 📿 E1.0 prayer beads
1F484                                      ; fully-qualified     # 💄 E0.6 lipstick
1F48D                                      ; fully-qualified     # 💍 E0.6 ring
1F48E                                      ; fully-qualified     # 💎 E0.6 gem stone

# subgroup: sound
1F507                                      ; fully-qualified     # 🔇 E1.0 muted speaker
1F508                                      ; fully-qualified     # 🔈 E0.7 speaker low volume
1F509                                      ; fully-qualified     # 🔉 E1.0 speaker medium volume
1F50A                                      ; fully-qualified     # 🔊 E0.6 speaker high volume
1F4E2                                      ; fully-qualified     # 📢 E0.6 loudspeaker
1F4E3                                      ; fully-qualified     # 📣 E0.6 megaphone
1F4EF                                      ; fully-qualified     # 📯 E1.0 postal horn
1F514                                      ; fully-qualified     # 🔔 E0.6 bell
1F515                                      ; fully-qualified     # 🔕 E1.0 bell with slash

# subgroup: music
1F3BC                                      ; fully-qualified     # 🎼 E0.6 musical score
1F3B5                                      ; fully-qualified     # 🎵 E0.6 musical note
1F3B6                                      ; fully-qualified     # 🎶 E0.6 musical notes
1F399 FE0F                                 ; fully-qualified     # 🎙️ E0.7 studio microphone
1F399                                      ; unqualified         # 🎙 E0.7 studio microphone
1F39A FE0F                                 ; fully-qualified     # 🎚️ E0.7 level slider
1F39A                                      ; unqualified         # 🎚 E0.7 level slider
1F39B FE0F                                 ; fully-qualified     # 🎛️ E0.7 control knobs
1F39B                                      ; unqualified         # 🎛 E0.7 control knobs
1F3A4                                      ; fully-qualified     # 🎤 E0.6 microphone
1F3A7                                      ; fully-qualified     # 🎧 E0.6 headphone
1F4FB                                      ; fully-qualified     # 📻 E0.6 radio

# subgroup: musical-instrument
1F3B7                                      ; fully-qualified     # 🎷 E0.6 saxophone
1FA97                                      ; fully-qualified     # 🪗 E13.0 accordion
1F3B8                                      ; fully-qualified     # 🎸 E0.6 guitar
1F3B9                                      ; fully-qualified     # 🎹 E0.6 musical keyboard
1F3BA                                      ; fully-qualified     # 🎺 E0.6 trumpet
1F3BB                                      ; fully-qualified     # 🎻 E0.6 violin
1FA95                                      ; fully-qualified     # 🪕 E12.0 banjo
1F941                                      ; fully-qualified     # 🥁 E3.0 drum
1FA98                                      ; fully-qualified     # 🪘 E13.0 long drum

# subgroup: phone
1F4F1                                      ; fully-qualified     # 📱 E0.6 mobile phone
1F4F2                                      ; fully-qualified     # 📲 E0.6 mobile phone with arrow
260E FE0F                                  ; fully-qualified     # ☎️ E0.6 telephone
260E                                       ; unqualified         # ☎ E0.6 telephone
1F4DE                                      ; fully-qualified     # 📞 E0.6 telephone receiver
1F4DF                                      ; fully-qualified     # 📟 E0.6 pager
1F4E0                                      ; fully-qualified     # 📠 E0.6 fax machine

# subgroup: computer
1F50B                                      ; fully-qualified     # 🔋 E0.6 battery
1F50C                                      ; fully-qualified     # 🔌 E0.6 electric plug
1F4BB                                      ; fully-qualified     # 💻 E0.6 laptop
1F5A5 FE0F                                 ; fully-qualified     # 🖥️ E0.7 desktop computer
1F5A5                                      ; unqualified         # 🖥 E0.7 desktop computer
1F5A8 FE0F                                 ; fully-qualified     # 🖨️ E0.7 printer
1F5A8                                      ; unqualified         # 🖨 E0.7 printer
2328 FE0F                                  ; fully-qualified     # ⌨️ E1.0 keyboard
2328                                       ; unqualified         # ⌨ E1.0 keyboard
1F5B1 FE0F                                 ; fully-qualified     # 🖱️ E0.7 computer mouse
1F5B1                                      ; unqualified         # 🖱 E0.7 computer mouse
1F5B2 FE0F                                 ; fully-qualified     # 🖲️ E0.7 trackball
1F5B2                                      ; unqualified         # 🖲 E0.7 trackball
1F4BD                                      ; fully-qualified     # 💽 E0.6 computer disk
1F4BE                                      ; fully-qualified     # 💾 E0.6 floppy disk
1F4BF                                      ; fully-qualified     # 💿 E0.6 optical disk
1F4C0                                      ; fully-qualified     # 📀 E0.6 dvd
1F9EE                                      ; fully-qualified     # 🧮 E11.0 abacus

# subgroup: light & video
1F3A5                                      ; fully-qualified     # 🎥 E0.6 movie camera
1F39E FE0F                                 ; fully-qualified     # 🎞️ E0.7 film frames
1F39E                                      ; unqualified         # 🎞 E0.7 film frames
1F4FD FE0F                                 ; fully-qualified     # 📽️ E0.7 film projector
1F4FD                                      ; unqualified         # 📽 E0.7 film projector
1F3AC                                      ; fully-qualified     # 🎬 E0.6 clapper board
1F4FA                                      ; fully-qualified     # 📺 E0.6 television
1F4F7                                      ; fully-qualified     # 📷 E0.6 camera
1F4F8                                      ; fully-qualified     # 📸 E1.0 camera with flash
1F4F9                                      ; fully-qualified     # 📹 E0.6 video camera
1F4FC                                      ; fully-qualified     # 📼 E0.6 videocassette
1F50D                                      ; fully-qualified     # 🔍 E0.6 magnifying glass tilted left
1F50E                                      ; fully-qualified     # 🔎 E0.6 magnifying glass tilted right
1F56F FE0F                                 ; fully-qualified     # 🕯️ E0.7 candle
1F56F                                      ; unqualified         # 🕯 E0.7 candle
1F4A1                                      ; fully-qualified     # 💡 E0.6 light bulb
1F526                                      ; fully-qualified     # 🔦 E0.6 flashlight
1F3EE                                      ; fully-qualified     # 🏮 E0.6 red paper lantern
1FA94                                      ; fully-qualified     # 🪔 E12.0 diya lamp

# subgroup: book-paper
1F4D4                                      ; fully-qualified     # 📔 E0.6 notebook with decorative cover
1F4D5                                      ; fully-qualified     # 📕 E0.6 closed book
1F4D6                                      ; fully-qualified     # 📖 E0.6 open book
1F4D7                                      ; fully-qualified     # 📗 E0.6 green book
1F4D8                                      ; fully-qualified     # 📘 E0.6 blue book
1F4D9                                      ; fully-qualified     # 📙 E0.6 orange book
1F4DA                                      ; fully-qualified     # 📚 E0.6 books
1F4D3                                      ; fully-qualified     # 📓 E0.6 notebook
1F4D2                                      ; fully-qualified     # 📒 E0.6 ledger
1F4C3                                      ; fully-qualified     # 📃 E0.6 page with curl
1F4DC                                      ; fully-qualified     # 📜 E0.6 scroll
1F4C4                                      ; fully-qualified     # 📄 E0.6 page facing up
1F4F0                                      ; fully-qualified     # 📰 E0.6 newspaper
1F5DE FE0F                                 ; fully-qualified     # 🗞️ E0.7 rolled-up newspaper
1F5DE                                      ; unqualified         # 🗞 E0.7 rolled-up newspaper
1F4D1                                      ; fully-qualified     # 📑 E0.6 bookmark tabs
1F516                                      ; fully-qualified     # 🔖 E0.6 bookmark
1F3F7 FE0F                                 ; fully-qualified     # 🏷️ E0.7 label
1F3F7                                      ; unqualified         # 🏷 E0.7 label

# subgroup: money
1F4B0                                      ; fully-qualified     # 💰 E0.6 money bag
1FA99                                      ; fully-qualified     # 🪙 E13.0 coin
1F4B4                                      ; fully-qualified     # 💴 E0.6 yen banknote
1F4B5                                      ; fully-qualified     # 💵 E0.6 dollar banknote
1F4B6                                      ; fully-qualified     # 💶 E1.0 euro banknote
1F4B7                                      ; fully-qualified     # 💷 E1.0 pound banknote
1F4B8                                      ; fully-qualified     # 💸 E0.6 money with wings
1F4B3                                      ; fully-qualified     # 💳 E0.6 credit card
1F9FE                                      ; fully-qualified     # 🧾 E11.0 receipt
1F4B9                                      ; fully-qualified     # 💹 E0.6 chart increasing with yen

# subgroup: mail
2709 FE0F                                  ; fully-qualified     # ✉️ E0.6 envelope
2709                                       ; unqualified         # ✉ E0.6 envelope
1F4E7                                      ; fully-qualified     # 📧 E0.6 e-mail
1F4E8                                      ; fully-qualified     # 📨 E0.6 incoming envelope
1F4E9                                      ; fully-qualified     # 📩 E0.6 envelope with arrow
1F4E4                                      ; fully-qualified     # 📤 E0.6 outbox tray
1F4E5                                      ; fully-qualified     # 📥 E0.6 inbox tray
1F4E6                                      ; fully-qualified     # 📦 E0.6 package
1F4EB                                      ; fully-qualified     # 📫 E0.6 closed mailbox with raised flag
1F4EA                                      ; fully-qualified     # 📪 E0.6 closed mailbox with lowered flag
1F4EC                                      ; fully-qualified     # 📬 E0.7 open mailbox with raised flag
1F4ED                                      ; fully-qualified     # 📭 E0.7 open mailbox with lowered flag
1F4EE                                      ; fully-qualified     # 📮 E0.6 postbox
1F5F3 FE0F                                 ; fully-qualified     # 🗳️ E0.7 ballot box with ballot
1F5F3                                      ; unqualified         # 🗳 E0.7 ballot box with ballot

# subgroup: writing
270F FE0F                                  ; fully-qualified     # ✏️ E0.6 pencil
270F                                       ; unqualified         # ✏ E0.6 pencil
2712 FE0F                                  ; fully-qualified     # ✒️ E0.6 black nib
2712                                       ; unqualified         # ✒ E0.6 black nib
1F58B FE0F                                 ; fully-qualified     # 🖋️ E0.7 fountain pen
1F58B                                      ; unqualified         # 🖋 E0.7 fountain pen
1F58A FE0F                                 ; fully-qualified     # 🖊️ E0.7 pen
1F58A                                      ; unqualified         # 🖊 E0.7 pen
1F58C FE0F                                 ; fully-qualified     # 🖌️ E0.7 paintbrush
1F58C                                      ; unqualified         # 🖌 E0.7 paintbrush
1F58D FE0F                                 ; fully-qualified     # 🖍️ E0.7 crayon
1F58D                                      ; unqualified         # 🖍 E0.7 crayon
1F4DD                                      ; fully-qualified     # 📝 E0.6 memo

# subgroup: office
1F4BC                                      ; fully-qualified     # 💼 E0.6 briefcase
1F4C1                                      ; fully-qualified     # 📁 E0.6 file folder
1F4C2                                      ; fully-qualified     # 📂 E0.6 open file folder
1F5C2 FE0F                                 ; fully-qualified     # 🗂️ E0.7 card index dividers
1F5C2                                      ; unqualified         # 🗂 E0.7 card index dividers
1F4C5                                      ; fully-qualified     # 📅 E0.6 calendar
1F4C6                                      ; fully-qualified     # 📆 E0.6 tear-off calendar
1F5D2 FE0F                                 ; fully-qualified     # 🗒️ E0.7 spiral notepad
1F5D2                                      ; unqualified         # 🗒 E0.7 spiral notepad
1F5D3 FE0F                                 ; fully-qualified     # 🗓️ E0.7 spiral calendar
1F5D3                                      ; unqualified         # 🗓 E0.7 spiral calendar
1F4C7                                      ; fully-qualified     # 📇 E0.6 card index
1F4C8                                      ; fully-qualified     # 📈 E0.6 chart increasing
1F4C9                                      ; fully-qualified     # 📉 E0.6 chart decreasing
1F4CA                                      ; fully-qualified     # 📊 E0.6 bar chart
1F4CB                                      ; fully-qualified     # 📋 E0.6 clipboard
1F4CC                                      ; fully-qualified     # 📌 E0.6 pushpin
1F4CD                                      ; fully-qualified     # 📍 E0.6 round pushpin
1F4CE                                      ; fully-qualified     # 📎 E0.6 paperclip
1F587 FE0F                                 ; fully-qualified     # 🖇️ E0.7 linked paperclips
1F587                                      ; unqualified         # 🖇 E0.7 linked paperclips
1F4CF                                      ; fully-qualified     # 📏 E0.6 straight ruler
1F4D0                                      ; fully-qualified     # 📐 E0.6 triangular ruler
2702 FE0F                                  ; fully-qualified     # ✂️ E0.6 scissors
2702                                       ; unqualified         # ✂ E0.6 scissors
1F5C3 FE0F                                 ; fully-qualified     # 🗃️ E0.7 card file box
1F5C3                                      ; unqualified         # 🗃 E0.7 card file box
1F5C4 FE0F                                 ; fully-qualified     # 🗄️ E0.7 file cabinet
1F5C4                                      ; unqualified         # 🗄 E0.7 file cabinet
1F5D1 FE0F                                 ; fully-qualified     # 🗑️ E0.7 wastebasket
1F5D1                                      ; unqualified         # 🗑 E0.7 wastebasket

# subgroup: lock
1F512                                      ; fully-qualified     # 🔒 E0.6 locked
1F513                                      ; fully-qualified     # 🔓 E0.6 unlocked
1F50F                                      ; fully-qualified     # 🔏 E0.6 locked with pen
1F510                                      ; fully-qualified     # 🔐 E0.6 locked with key
1F511                                      ; fully-qualified     # 🔑 E0.6 key
1F5DD FE0F                                 ; fully-qualified     # 🗝️ E0.7 old key
1F5DD                                      ; unqualified         # 🗝 E0.7 old key

# subgroup: tool
1F528                                      ; fully-qualified     # 🔨 E0.6 hammer
1FA93                                      ; fully-qualified     # 🪓 E12.0 axe
26CF FE0F                                  ; fully-qualified     # ⛏️ E0.7 pick
26CF                                       ; unqualified         # ⛏ E0.7 pick
2692 FE0F                                  ; fully-qualified     # ⚒️ E1.0 hammer and pick
2692                                       ; unqualified         # ⚒ E1.0 hammer and pick
1F6E0 FE0F                                 ; fully-qualified     # 🛠️ E0.7 hammer and wrench
1F6E0                                      ; unqualified         # 🛠 E0.7 hammer and wrench
1F5E1 FE0F                                 ; fully-qualified     # 🗡️ E0.7 dagger
1F5E1                                      ; unqualified         # 🗡 E0.7 dagger
2694 FE0F                                  ; fully-qualified     # ⚔️ E1.0 crossed swords
2694                                       ; unqualified         # ⚔ E1.0 crossed swords
1F52B                                      ; fully-qualified     # 🔫 E0.6 pistol
1FA83                                      ; fully-qualified     # 🪃 E13.0 boomerang
1F3F9                                      ; fully-qualified     # 🏹 E1.0 bow and arrow
1F6E1 FE0F                                 ; fully-qualified     # 🛡️ E0.7 shield
1F6E1                                      ; unqualified         # 🛡 E0.7 shield
1FA9A                                      ; fully-qualified     # 🪚 E13.0 carpentry saw
1F527                                      ; fully-qualified     # 🔧 E0.6 wrench
1FA9B                                      ; fully-qualified     # 🪛 E13.0 screwdriver
1F529                                      ; fully-qualified     # 🔩 E0.6 nut and bolt
2699 FE0F                                  ; fully-qualified     # ⚙️ E1.0 gear
2699                                       ; unqualified         # ⚙ E1.0 gear
1F5DC FE0F                                 ; fully-qualified     # 🗜️ E0.7 clamp
1F5DC                                      ; unqualified         # 🗜 E0.7 clamp
2696 FE0F                                  ; fully-qualified     # ⚖️ E1.0 balance scale
2696                                       ; unqualified         # ⚖ E1.0 balance scale
1F9AF                                      ; fully-qualified     # 🦯 E12.0 white cane
1F517                                      ; fully-qualified     # 🔗 E0.6 link
26D3 FE0F                                  ; fully-qualified     # ⛓️ E0.7 chains
26D3                                       ; unqualified         # ⛓ E0.7 chains
1FA9D                                      ; fully-qualified     # 🪝 E13.0 hook
1F9F0                                      ; fully-qualified     # 🧰 E11.0 toolbox
1F9F2                                      ; fully-qualified     # 🧲 E11.0 magnet
1FA9C                                      ; fully-qualified     # 🪜 E13.0 ladder

# subgroup: science
2697 FE0F                                  ; fully-qualified     # ⚗️ E1.0 alembic
2697                                       ; unqualified         # ⚗ E1.0 alembic
1F9EA                                      ; fully-qualified     # 🧪 E11.0 test tube
1F9EB                                      ; fully-qualified     # 🧫 E11.0 petri dish
1F9EC                                      ; fully-qualified     # 🧬 E11.0 dna
1F52C                                      ; fully-qualified     # 🔬 E1.0 microscope
1F52D                                      ; fully-qualified     # 🔭 E1.0 telescope
1F4E1                                      ; fully-qualified     # 📡 E0.6 satellite antenna

# subgroup: medical
1F489                                      ; fully-qualified     # 💉 E0.6 syringe
1FA78                                      ; fully-qualified     # 🩸 E12.0 drop of blood
1F48A                                      ; fully-qualified     # 💊 E0.6 pill
1FA79                                      ; fully-qualified     # 🩹 E12.0 adhesive bandage
1FA7A                                      ; fully-qualified     # 🩺 E12.0 stethoscope

# subgroup: household
1F6AA                                      ; fully-qualified     # 🚪 E0.6 door
1F6D7                                      ; fully-qualified     # 🛗 E13.0 elevator
1FA9E                                      ; fully-qualified     # 🪞 E13.0 mirror
1FA9F                                      ; fully-qualified     # 🪟 E13.0 window
1F6CF FE0F                                 ; fully-qualified     # 🛏️ E0.7 bed
1F6CF                                      ; unqualified         # 🛏 E0.7 bed
1F6CB FE0F                                 ; fully-qualified     # 🛋️ E0.7 couch and lamp
1F6CB                                      ; unqualified         # 🛋 E0.7 couch and lamp
1FA91                                      ; fully-qualified     # 🪑 E12.0 chair
1F6BD                                      ; fully-qualified     # 🚽 E0.6 toilet
1FAA0                                      ; fully-qualified     # 🪠 E13.0 plunger
1F6BF                                      ; fully-qualified     # 🚿 E1.0 shower
1F6C1                                      ; fully-qualified     # 🛁 E1.0 bathtub
1FAA4                                      ; fully-qualified     # 🪤 E13.0 mouse trap
1FA92                                      ; fully-qualified     # 🪒 E12.0 razor
1F9F4                                      ; fully-qualified     # 🧴 E11.0 lotion bottle
1F9F7                                      ; fully-qualified     # 🧷 E11.0 safety pin
1F9F9                                      ; fully-qualified     # 🧹 E11.0 broom
1F9FA                                      ; fully-qualified     # 🧺 E11.0 basket
1F9FB                                      ; fully-qualified     # 🧻 E11.0 roll of paper
1FAA3                                      ; fully-qualified     # 🪣 E13.0 bucket
1F9FC                                      ; fully-qualified     # 🧼 E11.0 soap
1FAA5                                      ; fully-qualified     # 🪥 E13.0 toothbrush
1F9FD                                      ; fully-qualified     # 🧽 E11.0 sponge
1F9EF                                      ; fully-qualified     # 🧯 E11.0 fire extinguisher
1F6D2                                      ; fully-qualified     # 🛒 E3.0 shopping cart

# subgroup: other-object
1F6AC                                      ; fully-qualified     # 🚬 E0.6 cigarette
26B0 FE0F                                  ; fully-qualified     # ⚰️ E1.0 coffin
26B0                                       ; unqualified         # ⚰ E1.0 coffin
1FAA6                                      ; fully-qualified     # 🪦 E13.0 headstone
26B1 FE0F                                  ; fully-qualified     # ⚱️ E1.0 funeral urn
26B1                                       ; unqualified         # ⚱ E1.0 funeral urn
1F5FF                                      ; fully-qualified     # 🗿 E0.6 moai
1FAA7                                      ; fully-qualified     # 🪧 E13.0 placard

# Objects subtotal:		299
# Objects subtotal:		299	w/o modifiers

# group: Symbols

# subgroup: transport-sign
1F3E7                                      ; fully-qualified     # 🏧 E0.6 ATM sign
1F6AE                                      ; fully-qualified     # 🚮 E1.0 litter in bin sign
1F6B0                                      ; fully-qualified     # 🚰 E1.0 potable water
267F                                       ; fully-qualified     # ♿ E0.6 wheelchair symbol
1F6B9                                      ; fully-qualified     # 🚹 E0.6 men’s room
1F6BA                                      ; fully-qualified     # 🚺 E0.6 women’s room
1F6BB                                      ; fully-qualified     # 🚻 E0.6 restroom
1F6BC                                      ; fully-qualified     # 🚼 E0.6 baby symbol
1F6BE                                      ; fully-qualified     # 🚾 E0.6 water closet
1F6C2                                      ; fully-qualified     # 🛂 E1.0 passport control
1F6C3                                      ; fully-qualified     # 🛃 E1.0 customs
1F6C4                                      ; fully-qualified     # 🛄 E1.0 baggage claim
1F6C5                                      ; fully-qualified     # 🛅 E1.0 left luggage

# subgroup: warning
26A0 FE0F                                  ; fully-qualified     # ⚠️ E0.6 warning
26A0                                       ; unqualified         # ⚠ E0.6 warning
1F6B8                                      ; fully-qualified     # 🚸 E1.0 children crossing
26D4                                       ; fully-qualified     # ⛔ E0.6 no entry
1F6AB                                      ; fully-qualified     # 🚫 E0.6 prohibited
1F6B3                                      ; fully-qualified     # 🚳 E1.0 no bicycles
1F6AD                                      ; fully-qualified     # 🚭 E0.6 no smoking
1F6AF                                      ; fully-qualified     # 🚯 E1.0 no littering
1F6B1                                      ; fully-qualified     # 🚱 E1.0 non-potable water
1F6B7                                      ; fully-qualified     # 🚷 E1.0 no pedestrians
1F4F5                                      ; fully-qualified     # 📵 E1.0 no mobile phones
1F51E                                      ; fully-qualified     # 🔞 E0.6 no one under eighteen
2622 FE0F                                  ; fully-qualified     # ☢️ E1.0 radioactive
2622                                       ; unqualified         # ☢ E1.0 radioactive
2623 FE0F                                  ; fully-qualified     # ☣️ E1.0 biohazard
2623                                       ; unqualified         # ☣ E1.0 biohazard

# subgroup: arrow
2B06 FE0F                                  ; fully-qualified     # ⬆️ E0.6 up arrow
2B06                                       ; unqualified         # ⬆ E0.6 up arrow
2197 FE0F                                  ; fully-qualified     # ↗️ E0.6 up-right arrow
2197                                       ; unqualified         # ↗ E0.6 up-right arrow
27A1 FE0F                                  ; fully-qualified     # ➡️ E0.6 right arrow
27A1                                       ; unqualified         # ➡ E0.6 right arrow
2198 FE0F                                  ; fully-qualified     # ↘️ E0.6 down-right arrow
2198                                       ; unqualified         # ↘ E0.6 down-right arrow
2B07 FE0F                                  ; fully-qualified     # ⬇️ E0.6 down arrow
2B07                                       ; unqualified         # ⬇ E0.6 down arrow
2199 FE0F                                  ; fully-qualified     # ↙️ E0.6 down-left arrow
2199                                       ; unqualified         # ↙ E0.6 down-left arrow
2B05 FE0F                                  ; fully-qualified     # ⬅️ E0.6 left arrow
2B05                                       ; unqualified         # ⬅ E0.6 left arrow
2196 FE0F                                  ; fully-qualified     # ↖️ E0.6 up-left arrow
2196                                       ; unqualified         # ↖ E0.6 up-left arrow
2195 FE0F                                  ; fully-qualified     # ↕️ E0.6 up-down arrow
2195                                       ; unqualified         # ↕ E0.6 up-down arrow
2194 FE0F                                  ; fully-qualified     # ↔️ E0.6 left-right arrow
2194                                       ; unqualified         # ↔ E0.6 left-right arrow
21A9 FE0F                                  ; fully-qualified     # ↩️ E0.6 right arrow curving left
21A9                                       ; unqualified         # ↩ E0.6 right arrow curving left
21AA FE0F                                  ; fully-qualified     # ↪️ E0.6 left arrow curving right
21AA                                       ; unqualified         # ↪ E0.6 left arrow curving right
2934 FE0F                                  ; fully-qualified     # ⤴️ E0.6 right arrow curving up
2934                                       ; unqualified         # ⤴ E0.6 right arrow curving up
2935 FE0F                                  ; fully-qualified     # ⤵️ E0.6 right arrow curving down
2935                                       ; unqualified         # ⤵ E0.6 right arrow curving down
1F503                                      ; fully-qualified     # 🔃 E0.6 clockwise vertical arrows
1F504                                      ; fully-qualified     # 🔄 E1.0 counterclockwise arrows button
1F519                                      ; fully-qualified     # 🔙 E0.6 BACK arrow
1F51A                                      ; fully-qualified     # 🔚 E0.6 END arrow
1F51B                                      ; fully-qualified     # 🔛 E0.6 ON! arrow
1F51C                                      ; fully-qualified     # 🔜 E0.6 SOON arrow
1F51D                                      ; fully-qualified     # 🔝 E0.6 TOP arrow

# subgroup: religion
1F6D0                                      ; fully-qualified     # 🛐 E1.0 place of worship
269B FE0F                                  ; fully-qualified     # ⚛️ E1.0 atom symbol
269B                                       ; unqualified         # ⚛ E1.0 atom symbol
1F549 FE0F                                 ; fully-qualified     # 🕉️ E0.7 om
1F549                                      ; unqualified         # 🕉 E0.7 om
2721 FE0F                                  ; fully-qualified     # ✡️ E0.7 star of David
2721                                       ; unqualified         # ✡ E0.7 star of David
2638 FE0F                                  ; fully-qualified     # ☸️ E0.7 wheel of dharma
2638                                       ; unqualified         # ☸ E0.7 wheel of dharma
262F FE0F                                  ; fully-qualified     # ☯️ E0.7 yin yang
262F                                       ; unqualified         # ☯ E0.7 yin yang
271D FE0F                                  ; fully-qualified     # ✝️ E0.7 latin cross
271D                                       ; unqualified         # ✝ E0.7 latin cross
2626 FE0F                                  ; fully-qualified     # ☦️ E1.0 orthodox cross
2626                                       ; unqualified         # ☦ E1.0 orthodox cross
262A FE0F                                  ; fully-qualified     # ☪️ E0.7 star and crescent
262A                                       ; unqualified         # ☪ E0.7 star and crescent
262E FE0F                                  ; fully-qualified     # ☮️ E1.0 peace symbol
262E                                       ; unqualified         # ☮ E1.0 peace symbol
1F54E                                      ; fully-qualified     # 🕎 E1.0 menorah
1F52F                                      ; fully-qualified     # 🔯 E0.6 dotted six-pointed star

# subgroup: zodiac
2648                                       ; fully-qualified     # ♈ E0.6 Aries
2649                                       ; fully-qualified     # ♉ E0.6 Taurus
264A                                       ; fully-qualified     # ♊ E0.6 Gemini
264B                                       ; fully-qualified     # ♋ E0.6 Cancer
264C                                       ; fully-qualified     # ♌ E0.6 Leo
264D                                       ; fully-qualified     # ♍ E0.6 Virgo
264E                                       ; fully-qualified     # ♎ E0.6 Libra
264F                                       ; fully-qualified     # ♏ E0.6 Scorpio
2650                                       ; fully-qualified     # ♐ E0.6 Sagittarius
2651                                       ; fully-qualified     # ♑ E0.6 Capricorn
2652                                       ; fully-qualified     # ♒ E0.6 Aquarius
2653                                       ; fully-qualified     # ♓ E0.6 Pisces
26CE                                       ; fully-qualified     # ⛎ E0.6 Ophiuchus

# subgroup: av-symbol
1F500                                      ; fully-qualified     # 🔀 E1.0 shuffle tracks button
1F501                                      ; fully-qualified     # 🔁 E1.0 repeat button
1F502                                      ; fully-qualified     # 🔂 E1.0 repeat single button
25B6 FE0F                                  ; fully-qualified     # ▶️ E0.6 play button
25B6                                       ; unqualified         # ▶ E0.6 play button
23E9                                       ; fully-qualified     # ⏩ E0.6 fast-forward button
23ED FE0F                                  ; fully-qualified     # ⏭️ E0.7 next track button
23ED                                       ; unqualified         # ⏭ E0.7 next track button
23EF FE0F                                  ; fully-qualified     # ⏯️ E1.0 play or pause button
23EF                                       ; unqualified         # ⏯ E1.0 play or pause button
25C0 FE0F                                  ; fully-qualified     # ◀️ E0.6 reverse button
25C0                                       ; unqualified         # ◀ E0.6 reverse button
23EA                                       ; fully-qualified     # ⏪ E0.6 fast reverse button
23EE FE0F                                  ; fully-qualified     # ⏮️ E0.7 last track button
23EE                                       ; unqualified         # ⏮ E0.7 last track button
1F53C                                      ; fully-qualified     # 🔼 E0.6 upwards button
23EB                                       ; fully-qualified     # ⏫ E0.6 fast up button
1F53D                                      ; fully-qualified     # 🔽 E0.6 downwards button
23EC                                       ; fully-qualified     # ⏬ E0.6 fast down button
23F8 FE0F                                  ; fully-qualified     # ⏸️ E0.7 pause button
23F8                                       ; unqualified         # ⏸ E0.7 pause button
23F9 FE0F                                  ; fully-qualified     # ⏹️ E0.7 stop button
23F9                                       ; unqualified         # ⏹ E0.7 stop button
23FA FE0F                                  ; fully-qualified     # ⏺️ E0.7 record button
23FA                                       ; unqualified         # ⏺ E0.7 record button
23CF FE0F                                  ; fully-qualified     # ⏏️ E1.0 eject button
23CF                                       ; unqualified         # ⏏ E1.0 eject button
1F3A6                                      ; fully-qualified     # 🎦 E0.6 cinema
1F505                                      ; fully-qualified     # 🔅 E1.0 dim button
1F506                                      ; fully-qualified     # 🔆 E1.0 bright button
1F4F6                                      ; fully-qualified     # 📶 E0.6 antenna bars
1F4F3                                      ; fully-qualified     # 📳 E0.6 vibration mode
1F4F4                                      ; fully-qualified     # 📴 E0.6 mobile phone off

# subgroup: gender
2640 FE0F                                  ; fully-qualified     # ♀️ E4.0 female sign
2640                                       ; unqualified         # ♀ E4.0 female sign
2642 FE0F                                  ; fully-qualified     # ♂️ E4.0 male sign
2642                                       ; unqualified         # ♂ E4.0 male sign
26A7 FE0F                                  ; fully-qualified     # ⚧️ E13.0 transgender symbol
26A7                                       ; unqualified         # ⚧ E13.0 transgender symbol

# subgroup: math
2716 FE0F                                  ; fully-qualified     # ✖️ E0.6 multiply
2716                                       ; unqualified         # ✖ E0.6 multiply
2795                                       ; fully-qualified     # ➕ E0.6 plus
2796                                       ; fully-qualified     # ➖ E0.6 minus
2797                                       ; fully-qualified     # ➗ E0.6 divide
267E FE0F                                  ; fully-qualified     # ♾️ E11.0 infinity
267E                                       ; unqualified         # ♾ E11.0 infinity

# subgroup: punctuation
203C FE0F                                  ; fully-qualified     # ‼️ E0.6 double exclamation mark
203C                                       ; unqualified         # ‼ E0.6 double exclamation mark
2049 FE0F                                  ; fully-qualified     # ⁉️ E0.6 exclamation question mark
2049                                       ; unqualified         # ⁉ E0.6 exclamation question mark
2753                                       ; fully-qualified     # ❓ E0.6 question mark
2754                                       ; fully-qualified     # ❔ E0.6 white question mark
2755                                       ; fully-qualified     # ❕ E0.6 white exclamation mark
2757                                       ; fully-qualified     # ❗ E0.6 exclamation mark
3030 FE0F                                  ; fully-qualified     # 〰️ E0.6 wavy dash
3030                                       ; unqualified         # 〰 E0.6 wavy dash

# subgroup: currency
1F4B1                                      ; fully-qualified     # 💱 E0.6 currency exchange
1F4B2                                      ; fully-qualified     # 💲 E0.6 heavy dollar sign

# subgroup: other-symbol
2695 FE0F                                  ; fully-qualified     # ⚕️ E4.0 medical symbol
2695                                       ; unqualified         # ⚕ E4.0 medical symbol
267B FE0F                                  ; fully-qualified     # ♻️ E0.6 recycling symbol
267B                                       ; unqualified         # ♻ E0.6 recycling symbol
269C FE0F                                  ; fully-qualified     # ⚜️ E1.0 fleur-de-lis
269C                                       ; unqualified         # ⚜ E1.0 fleur-de-lis
1F531                                      ; fully-qualified     # 🔱 E0.6 trident emblem
1F4DB                                      ; fully-qualified     # 📛 E0.6 name badge
1F530                                      ; fully-qualified     # 🔰 E0.6 Japanese symbol for beginner
2B55                                       ; fully-qualified     # ⭕ E0.6 hollow red circle
2705                                       ; fully-qualified     # ✅ E0.6 check mark button
2611 FE0F                                  ; fully-qualified     # ☑️ E0.6 check box with check
2611                                       ; unqualified         # ☑ E0.6 check box with check
2714 FE0F                                  ; fully-qualified     # ✔️ E0.6 check mark
2714                                       ; unqualified         # ✔ E0.6 check mark
274C                                       ; fully-qualified     # ❌ E0.6 cross mark
274E                                       ; fully-qualified     # ❎ E0.6 cross mark button
27B0                                       ; fully-qualified     # ➰ E0.6 curly loop
27BF                                       ; fully-qualified     # ➿ E1.0 double curly loop
303D FE0F                                  ; fully-qualified     # 〽️ E0.6 part alternation mark
303D                                       ; unqualified         # 〽 E0.6 part alternation mark
2733 FE0F                                  ; fully-qualified     # ✳️ E0.6 eight-spoked asterisk
2733                                       ; unqualified         # ✳ E0.6 eight-spoked asterisk
2734 FE0F                                  ; fully-qualified     # ✴️ E0.6 eight-pointed star
2734                                       ; unqualified         # ✴ E0.6 eight-pointed star
2747 FE0F                                  ; fully-qualified     # ❇️ E0.6 sparkle
2747                                       ; unqualified         # ❇ E0.6 sparkle
00A9 FE0F                                  ; fully-qualified     # ©️ E0.6 copyright
00A9                                       ; unqualified         # © E0.6 copyright
00AE FE0F                                  ; fully-qualified     # ®️ E0.6 registered
00AE                                       ; unqualified         # ® E0.6 registered
2122 FE0F                                  ; fully-qualified     # ™️ E0.6 trade mark
2122                                       ; unqualified         # ™ E0.6 trade mark

# subgroup: keycap
0023 FE0F 20E3                             ; fully-qualified     # #️⃣ E0.6 keycap: #
0023 20E3                                  ; unqualified         # #⃣ E0.6 keycap: #
002A FE0F 20E3                             ; fully-qualified     # *️⃣ E2.0 keycap: *
002A 20E3                                  ; unqualified         # *⃣ E2.0 keycap: *
0030 FE0F 20E3                             ; fully-qualified     # 0️⃣ E0.6 keycap: 0
0030 20E3                                  ; unqualified         # 0⃣ E0.6 keycap: 0
0031 FE0F 20E3                             ; fully-qualified     # 1️⃣ E0.6 keycap: 1
0031 20E3                                  ; unqualified         # 1⃣ E0.6 keycap: 1
0032 FE0F 20E3                             ; fully-qualified     # 2️⃣ E0.6 keycap: 2
0032 20E3                                  ; unqualified         # 2⃣ E0.6 keycap: 2
0033 FE0F 20E3                             ; fully-qualified     # 3️⃣ E0.6 keycap: 3
0033 20E3                                  ; unqualified         # 3⃣ E0.6 keycap: 3
0034 FE0F 20E3                             ; fully-qualified     # 4️⃣ E0.6 keycap: 4
0034 20E3                                  ; unqualified         # 4⃣ E0.6 keycap: 4
0035 FE0F 20E3                             ; fully-qualified     # 5️⃣ E0.6 keycap: 5
0035 20E3                                  ; unqualified         # 5⃣ E0.6 keycap: 5
0036 FE0F 20E3                             ; fully-qualified     # 6️⃣ E0.6 keycap: 6
0036 20E3                                  ; unqualified         # 6⃣ E0.6 keycap: 6
0037 FE0F 20E3                             ; fully-qualified     # 7️⃣ E0.6 keycap: 7
0037 20E3                                  ; unqualified         # 7⃣ E0.6 keycap: 7
0038 FE0F 20E3                             ; fully-qualified     # 8️⃣ E0.6 keycap: 8
0038 20E3                                  ; unqualified         # 8⃣ E0.6 keycap: 8
0039 FE0F 20E3                             ; fully-qualified     # 9️⃣ E0.6 keycap: 9
0039 20E3                                  ; unqualified         # 9⃣ E0.6 keycap: 9
1F51F                                      ; fully-qualified     # 🔟 E0.6 keycap: 10

# subgroup: alphanum
1F520                                      ; fully-qualified     # 🔠 E0.6 input latin uppercase
1F521                                      ; fully-qualified     # 🔡 E0.6 input latin lowercase
1F522                                      ; fully-qualified     # 🔢 E0.6 input numbers
1F523                                      ; fully-qualified     # 🔣 E0.6 input symbols
1F524                                      ; fully-qualified     # 🔤 E0.6 input latin letters
1F170 FE0F                                 ; fully-qualified     # 🅰️ E0.6 A button (blood type)
1F170                                      ; unqualified         # 🅰 E0.6 A button (blood type)
1F18E                                      ; fully-qualified     # 🆎 E0.6 AB button (blood type)
1F171 FE0F                                 ; fully-qualified     # 🅱️ E0.6 B button (blood type)
1F171                                      ; unqualified         # 🅱 E0.6 B button (blood type)
1F191                                      ; fully-qualified     # 🆑 E0.6 CL button
1F192                                      ; fully-qualified     # 🆒 E0.6 COOL button
1F193                                      ; fully-qualified     # 🆓 E0.6 FREE button
2139 FE0F                                  ; fully-qualified     # ℹ️ E0.6 information
2139                                       ; unqualified         # ℹ E0.6 information
1F194                                      ; fully-qualified     # 🆔 E0.6 ID button
24C2 FE0F                                  ; fully-qualified     # Ⓜ️ E0.6 circled M
24C2                                       ; unqualified         # Ⓜ E0.6 circled M
1F195                                      ; fully-qualified     # 🆕 E0.6 NEW button
1F196                                      ; fully-qualified     # 🆖 E0.6 NG button
1F17E FE0F                                 ; fully-qualified     # 🅾️ E0.6 O button (blood type)
1F17E                                      ; unqualified         # 🅾 E0.6 O button (blood type)
1F197                                      ; fully-qualified     # 🆗 E0.6 OK button
1F17F FE0F                                 ; fully-qualified     # 🅿️ E0.6 P button
1F17F                                      ; unqualified         # 🅿 E0.6 P button
1F198                                      ; fully-qualified     # 🆘 E0.6 SOS button
1F199                                      ; fully-qualified     # 🆙 E0.6 UP! button
1F19A                                      ; fully-qualified     # 🆚 E0.6 VS button
1F201                                      ; fully-qualified     # 🈁 E0.6 Japanese “here” button
1F202 FE0F                                 ; fully-qualified     # 🈂️ E0.6 Japanese “service charge” button
1F202                                      ; unqualified         # 🈂 E0.6 Japanese “service charge” button
1F237 FE0F                                 ; fully-qualified     # 🈷️ E0.6 Japanese “monthly amount” button
1F237                                      ; unqualified         # 🈷 E0.6 Japanese “monthly amount” button
1F236                                      ; fully-qualified     # 🈶 E0.6 Japanese “not free of charge” button
1F22F                                      ; fully-qualified     # 🈯 E0.6 Japanese “reserved” button
1F250                                      ; fully-qualified     # 🉐 E0.6 Japanese “bargain” button
1F239                                      ; fully-qualified     # 🈹 E0.6 Japanese “discount” button
1F21A                                      ; fully-qualified     # 🈚 E0.6 Japanese “free of charge” button
1F232                                      ; fully-qualified     # 🈲 E0.6 Japanese “prohibited” button
1F251                                      ; fully-qualified     # 🉑 E0.6 Japanese “acceptable” button
1F238                                      ; fully-qualified     # 🈸 E0.6 Japanese “application” button
1F234                                      ; fully-qualified     # 🈴 E0.6 Japanese “passing grade” button
1F233                                      ; fully-qualified     # 🈳 E0.6 Japanese “vacancy” button
3297 FE0F                                  ; fully-qualified     # ㊗️ E0.6 Japanese “congratulations” button
3297                                       ; unqualified         # ㊗ E0.6 Japanese “congratulations” button
3299 FE0F                                  ; fully-qualified     # ㊙️ E0.6 Japanese “secret” button
3299                                       ; unqualified         # ㊙ E0.6 Japanese “secret” button
1F23A                                      ; fully-qualified     # 🈺 E0.6 Japanese “open for business” button
1F235                                      ; fully-qualified     # 🈵 E0.6 Japanese “no vacancy” button

# subgroup: geometric
1F534                                      ; fully-qualified     # 🔴 E0.6 red circle
1F7E0                                      ; fully-qualified     # 🟠 E12.0 orange circle
1F7E1                                      ; fully-qualified     # 🟡 E12.0 yellow circle
1F7E2                                      ; fully-qualified     # 🟢 E12.0 green circle
1F535                                      ; fully-qualified     # 🔵 E0.6 blue circle
1F7E3                                      ; fully-qualified     # 🟣 E12.0 purple circle
1F7E4                                      ; fully-qualified     # 🟤 E12.0 brown circle
26AB                                       ; fully-qualified     # ⚫ E0.6 black circle
26AA                                       ; fully-qualified     # ⚪ E0.6 white circle
1F7E5                                      ; fully-qualified     # 🟥 E12.0 red square
1F7E7                                      ; fully-qualified     # 🟧 E12.0 orange square
1F7E8                                      ; fully-qualified     # 🟨 E12.0 yellow square
1F7E9                                      ; fully-qualified     # 🟩 E12.0 green square
1F7E6                                      ; fully-qualified     # 🟦 E12.0 blue square
1F7EA                                      ; fully-qualified     # 🟪 E12.0 purple square
1F7EB                                      ; fully-qualified     # 🟫 E12.0 brown square
2B1B                                       ; fully-qualified     # ⬛ E0.6 black large square
2B1C                                       ; fully-qualified     # ⬜ E0.6 white large square
25FC FE0F                                  ; fully-qualified     # ◼️ E0.6 black medium square
25FC                                       ; unqualified         # ◼ E0.6 black medium square
25FB FE0F                                  ; fully-qualified     # ◻️ E0.6 white medium square
25FB                                       ; unqualified         # ◻ E0.6 white medium square
25FE                                       ; fully-qualified     # ◾ E0.6 black medium-small square
25FD                                       ; fully-qualified     # ◽ E0.6 white medium-small square
25AA FE0F                                  ; fully-qualified     # ▪️ E0.6 black small square
25AA                                       ; unqualified         # ▪ E0.6 black small square
25AB FE0F                                  ; fully-qualified     # ▫️ E0.6 white small square
25AB                                       ; unqualified         # ▫ E0.6 white small square
1F536                                      ; fully-qualified     # 🔶 E0.6 large orange diamond
1F537                                      ; fully-qualified     # 🔷 E0.6 large blue diamond
1F538                                      ; fully-qualified     # 🔸 E0.6 small orange diamond
1F539                                      ; fully-qualified     # 🔹 E0.6 small blue diamond
1F53A                                      ; fully-qualified     # 🔺 E0.6 red triangle pointed up
1F53B                                      ; fully-qualified     # 🔻 E0.6 red triangle pointed down
1F4A0                                      ; fully-qualified     # 💠 E0.6 diamond with a dot
1F518                                      ; fully-qualified     # 🔘 E0.6 radio button
1F533                                      ; fully-qualified     # 🔳 E0.6 white square button
1F532                                      ; fully-qualified     # 🔲 E0.6 black square button

# Symbols subtotal:		301
# Symbols subtotal:		301	w/o modifiers

# group: Flags

# subgroup: flag
1F3C1                                      ; fully-qualified     # 🏁 E0.6 chequered flag
1F6A9                                      ; fully-qualified     # 🚩 E0.6 triangular flag
1F38C                                      ; fully-qualified     # 🎌 E0.6 crossed flags
1F3F4                                      ; fully-qualified     # 🏴 E1.0 black flag
1F3F3 FE0F                                 ; fully-qualified     # 🏳️ E0.7 white flag
1F3F3                                      ; unqualified         # 🏳 E0.7 white flag
1F3F3 FE0F 200D 1F308                      ; fully-qualified     # 🏳️‍🌈 E4.0 rainbow flag
1F3F3 200D 1F308                           ; unqualified         # 🏳‍🌈 E4.0 rainbow flag
1F3F3 FE0F 200D 26A7 FE0F                  ; fully-qualified     # 🏳️‍⚧️ E13.0 transgender flag
1F3F3 200D 26A7 FE0F                       ; unqualified         # 🏳‍⚧️ E13.0 transgender flag
1F3F3 FE0F 200D 26A7                       ; unqualified         # 🏳️‍⚧ E13.0 transgender flag
1F3F3 200D 26A7                            ; unqualified         # 🏳‍⚧ E13.0 transgender flag
1F3F4 200D 2620 FE0F                       ; fully-qualified     # 🏴‍☠️ E11.0 pirate flag
1F3F4 200D 2620                            ; minimally-qualified # 🏴‍☠ E11.0 pirate flag

# subgroup: country-flag
1F1E6 1F1E8                                ; fully-qualified     # 🇦🇨 E2.0 flag: Ascension Island
1F1E6 1F1E9                                ; fully-qualified     # 🇦🇩 E2.0 flag: Andorra
1F1E6 1F1EA                                ; fully-qualified     # 🇦🇪 E2.0 flag: United Arab Emirates
1F1E6 1F1EB                                ; fully-qualified     # 🇦🇫 E2.0 flag: Afghanistan
1F1E6 1F1EC                                ; fully-qualified     # 🇦🇬 E2.0 flag: Antigua & Barbuda
1F1E6 1F1EE                                ; fully-qualified     # 🇦🇮 E2.0 flag: Anguilla
1F1E6 1F1F1                                ; fully-qualified     # 🇦🇱 E2.0 flag: Albania
1F1E6 1F1F2                                ; fully-qualified     # 🇦🇲 E2.0 flag: Armenia
1F1E6 1F1F4                                ; fully-qualified     # 🇦🇴 E2.0 flag: Angola
1F1E6 1F1F6                                ; fully-qualified     # 🇦🇶 E2.0 flag: Antarctica
1F1E6 1F1F7                                ; fully-qualified     # 🇦🇷 E2.0 flag: Argentina
1F1E6 1F1F8                                ; fully-qualified     # 🇦🇸 E2.0 flag: American Samoa
1F1E6 1F1F9                                ; fully-qualified     # 🇦🇹 E2.0 flag: Austria
1F1E6 1F1FA                                ; fully-qualified     # 🇦🇺 E2.0 flag: Australia
1F1E6 1F1FC                                ; fully-qualified     # 🇦🇼 E2.0 flag: Aruba
1F1E6 1F1FD                                ; fully-qualified     # 🇦🇽 E2.0 flag: Åland Islands
1F1E6 1F1FF                                ; fully-qualified     # 🇦🇿 E2.0 flag: Azerbaijan
1F1E7 1F1E6                                ; fully-qualified     # 🇧🇦 E2.0 flag: Bosnia & Herzegovina
1F1E7 1F1E7                                ; fully-qualified     # 🇧🇧 E2.0 flag: Barbados
1F1E7 1F1E9                                ; fully-qualified     # 🇧🇩 E2.0 flag: Bangladesh
1F1E7 1F1EA                                ; fully-qualified     # 🇧🇪 E2.0 flag: Belgium
1F1E7 1F1EB                                ; fully-qualified     # 🇧🇫 E2.0 flag: Burkina Faso
1F1E7 1F1EC                                ; fully-qualified     # 🇧🇬 E2.0 flag: Bulgaria
1F1E7 1F1ED                                ; fully-qualified     # 🇧🇭 E2.0 flag: Bahrain
1F1E7 1F1EE                                ; fully-qualified     # 🇧🇮 E2.0 flag: Burundi
1F1E7 1F1EF                                ; fully-qualified     # 🇧🇯 E2.0 flag: Benin
1F1E7 1F1F1                                ; fully-qualified     # 🇧🇱 E2.0 flag: St. Barthélemy
1F1E7 1F1F2                                ; fully-qualified     # 🇧🇲 E2.0 flag: Bermuda
1F1E7 1F1F3                                ; fully-qualified     # 🇧🇳 E2.0 flag: Brunei
1F1E7 1F1F4                                ; fully-qualified     # 🇧🇴 E2.0 flag: Bolivia
1F1E7 1F1F6                                ; fully-qualified     # 🇧🇶 E2.0 flag: Caribbean Netherlands
1F1E7 1F1F7                                ; fully-qualified     # 🇧🇷 E2.0 flag: Brazil
1F1E7 1F1F8                                ; fully-qualified     # 🇧🇸 E2.0 flag: Bahamas
1F1E7 1F1F9                                ; fully-qualified     # 🇧🇹 E2.0 flag: Bhutan
1F1E7 1F1FB                                ; fully-qualified     # 🇧🇻 E2.0 flag: Bouvet Island
1F1E7 1F1FC                                ; fully-qualified     # 🇧🇼 E2.0 flag: Botswana
1F1E7 1F1FE                                ; fully-qualified     # 🇧🇾 E2.0 flag: Belarus
1F1E7 1F1FF                                ; fully-qualified     # 🇧🇿 E2.0 flag: Belize
1F1E8 1F1E6                                ; fully-qualified     # 🇨🇦 E2.0 flag: Canada
1F1E8 1F1E8                                ; fully-qualified     # 🇨🇨 E2.0 flag: Cocos (Keeling) Islands
1F1E8 1F1E9                                ; fully-qualified     # 🇨🇩 E2.0 flag: Congo - Kinshasa
1F1E8 1F1EB                                ; fully-qualified     # 🇨🇫 E2.0 flag: Central African Republic
1F1E8 1F1EC                                ; fully-qualified     # 🇨🇬 E2.0 flag: Congo - Brazzaville
1F1E8 1F1ED                                ; fully-qualified     # 🇨🇭 E2.0 flag: Switzerland
1F1E8 1F1EE                                ; fully-qualified     # 🇨🇮 E2.0 flag: Côte d’Ivoire
1F1E8 1F1F0                                ; fully-qualified     # 🇨🇰 E2.0 flag: Cook Islands
1F1E8 1F1F1                                ; fully-qualified     # 🇨🇱 E2.0 flag: Chile
1F1E8 1F1F2                                ; fully-qualified     # 🇨🇲 E2.0 flag: Cameroon
1F1E8 1F1F3                                ; fully-qualified     # 🇨🇳 E0.6 flag: China
1F1E8 1F1F4                                ; fully-qualified     # 🇨🇴 E2.0 flag: Colombia
1F1E8 1F1F5                                ; fully-qualified     # 🇨🇵 E2.0 flag: Clipperton Island
1F1E8 1F1F7                                ; fully-qualified     # 🇨🇷 E2.0 flag: Costa Rica
1F1E8 1F1FA                                ; fully-qualified     # 🇨🇺 E2.0 flag: Cuba
1F1E8 1F1FB                                ; fully-qualified     # 🇨🇻 E2.0 flag: Cape Verde
1F1E8 1F1FC                                ; fully-qualified     # 🇨🇼 E2.0 flag: Curaçao
1F1E8 1F1FD                                ; fully-qualified     # 🇨🇽 E2.0 flag: Christmas Island
1F1E8 1F1FE                                ; fully-qualified     # 🇨🇾 E2.0 flag: Cyprus
1F1E8 1F1FF                                ; fully-qualified     # 🇨🇿 E2.0 flag: Czechia
1F1E9 1F1EA                                ; fully-qualified     # 🇩🇪 E0.6 flag: Germany
1F1E9 1F1EC                                ; fully-qualified     # 🇩🇬 E2.0 flag: Diego Garcia
1F1E9 1F1EF                                ; fully-qualified     # 🇩🇯 E2.0 flag: Djibouti
1F1E9 1F1F0                                ; fully-qualified     # 🇩🇰 E2.0 flag: Denmark
1F1E9 1F1F2                                ; fully-qualified     # 🇩🇲 E2.0 flag: Dominica
1F1E9 1F1F4                                ; fully-qualified     # 🇩🇴 E2.0 flag: Dominican Republic
1F1E9 1F1FF                                ; fully-qualified     # 🇩🇿 E2.0 flag: Algeria
1F1EA 1F1E6                                ; fully-qualified     # 🇪🇦 E2.0 flag: Ceuta & Melilla
1F1EA 1F1E8                                ; fully-qualified     # 🇪🇨 E2.0 flag: Ecuador
1F1EA 1F1EA                                ; fully-qualified     # 🇪🇪 E2.0 flag: Estonia
1F1EA 1F1EC                                ; fully-qualified     # 🇪🇬 E2.0 flag: Egypt
1F1EA 1F1ED                                ; fully-qualified     # 🇪🇭 E2.0 flag: Western Sahara
1F1EA 1F1F7                                ; fully-qualified     # 🇪🇷 E2.0 flag: Eritrea
1F1EA 1F1F8                                ; fully-qualified     # 🇪🇸 E0.6 flag: Spain
1F1EA 1F1F9                                ; fully-qualified     # 🇪🇹 E2.0 flag: Ethiopia
1F1EA 1F1FA                                ; fully-qualified     # 🇪🇺 E2.0 flag: European Union
1F1EB 1F1EE                                ; fully-qualified     # 🇫🇮 E2.0 flag: Finland
1F1EB 1F1EF                                ; fully-qualified     # 🇫🇯 E2.0 flag: Fiji
1F1EB 1F1F0                                ; fully-qualified     # 🇫🇰 E2.0 flag: Falkland Islands
1F1EB 1F1F2                                ; fully-qualified     # 🇫🇲 E2.0 flag: Micronesia
1F1EB 1F1F4                                ; fully-qualified     # 🇫🇴 E2.0 flag: Faroe Islands
1F1EB 1F1F7                                ; fully-qualified     # 🇫🇷 E0.6 flag: France
1F1EC 1F1E6                                ; fully-qualified     # 🇬🇦 E2.0 flag: Gabon
1F1EC 1F1E7                                ; fully-qualified     # 🇬🇧 E0.6 flag: United Kingdom
1F1EC 1F1E9                                ; fully-qualified     # 🇬🇩 E2.0 flag: Grenada
1F1EC 1F1EA                                ; fully-qualified     # 🇬🇪 E2.0 flag: Georgia
1F1EC 1F1EB                                ; fully-qualified     # 🇬🇫 E2.0 flag: French Guiana
1F1EC 1F1EC                                ; fully-qualified     # 🇬🇬 E2.0 flag: Guernsey
1F1EC 1F1ED                                ; fully-qualified     # 🇬🇭 E2.0 flag: Ghana
1F1EC 1F1EE                                ; fully-qualified     # 🇬🇮 E2.0 flag: Gibraltar
1F1EC 1F1F1                                ; fully-qualified     # 🇬🇱 E2.0 flag: Greenland
1F1EC 1F1F2                                ; fully-qualified     # 🇬🇲 E2.0 flag: Gambia
1F1EC 1F1F3                                ; fully-qualified     # 🇬🇳 E2.0 flag: Guinea
1F1EC 1F1F5                                ; fully-qualified     # 🇬🇵 E2.0 flag: Guadeloupe
1F1EC 1F1F6                                ; fully-qualified     # 🇬🇶 E2.0 flag: Equatorial Guinea
1F1EC 1F1F7                                ; fully-qualified     # 🇬🇷 E2.0 flag: Greece
1F1EC 1F1F8                                ; fully-qualified     # 🇬🇸 E2.0 flag: South Georgia & South Sandwich Islands
1F1EC 1F1F9                                ; fully-qualified     # 🇬🇹 E2.0 flag: Guatemala
1F1EC 1F1FA                                ; fully-qualified     # 🇬🇺 E2.0 flag: Guam
1F1EC 1F1FC                                ; fully-qualified     # 🇬🇼 E2.0 flag: Guinea-Bissau
1F1EC 1F1FE                                ; fully-qualified     # 🇬🇾 E2.0 flag: Guyana
1F1ED 1F1F0                                ; fully-qualified     # 🇭🇰 E2.0 flag: Hong Kong SAR China
1F1ED 1F1F2                                ; fully-qualified     # 🇭🇲 E2.0 flag: Heard & McDonald Islands
1F1ED 1F1F3                                ; fully-qualified     # 🇭🇳 E2.0 flag: Honduras
1F1ED 1F1F7                                ; fully-qualified     # 🇭🇷 E2.0 flag: Croatia
1F1ED 1F1F9                                ; fully-qualified     # 🇭🇹 E2.0 flag: Haiti
1F1ED 1F1FA                                ; fully-qualified     # 🇭🇺 E2.0 flag: Hungary
1F1EE 1F1E8                                ; fully-qualified     # 🇮🇨 E2.0 flag: Canary Islands
1F1EE 1F1E9                                ; fully-qualified     # 🇮🇩 E2.0 flag: Indonesia
1F1EE 1F1EA                                ; fully-qualified     # 🇮🇪 E2.0 flag: Ireland
1F1EE 1F1F1                                ; fully-qualified     # 🇮🇱 E2.0 flag: Israel
1F1EE 1F1F2                                ; fully-qualified     # 🇮🇲 E2.0 flag: Isle of Man
1F1EE 1F1F3                                ; fully-qualified     # 🇮🇳 E2.0 flag: India
1F1EE 1F1F4                                ; fully-qualified     # 🇮🇴 E2.0 flag: British Indian Ocean Territory
1F1EE 1F1F6                                ; fully-qualified     # 🇮🇶 E2.0 flag: Iraq
1F1EE 1F1F7                                ; fully-qualified     # 🇮🇷 E2.0 flag: Iran
1F1EE 1F1F8                                ; fully-qualified     # 🇮🇸 E2.0 flag: Iceland
1F1EE 1F1F9                                ; fully-qualified     # 🇮🇹 E0.6 flag: Italy
1F1EF 1F1EA                                ; fully-qualified     # 🇯🇪 E2.0 flag: Jersey
1F1EF 1F1F2                                ; fully-qualified     # 🇯🇲 E2.0 flag: Jamaica
1F1EF 1F1F4                                ; fully-qualified     # 🇯🇴 E2.0 flag: Jordan
1F1EF 1F1F5                                ; fully-qualified     # 🇯🇵 E0.6 flag: Japan
1F1F0 1F1EA                                ; fully-qualified     # 🇰🇪 E2.0 flag: Kenya
1F1F0 1F1EC                                ; fully-qualified     # 🇰🇬 E2.0 flag: Kyrgyzstan
1F1F0 1F1ED                                ; fully-qualified     # 🇰🇭 E2.0 flag: Cambodia
1F1F0 1F1EE                                ; fully-qualified     # 🇰🇮 E2.0 flag: Kiribati
1F1F0 1F1F2                                ; fully-qualified     # 🇰🇲 E2.0 flag: Comoros
1F1F0 1F1F3                                ; fully-qualified     # 🇰🇳 E2.0 flag: St. Kitts & Nevis
1F1F0 1F1F5                                ; fully-qualified     # 🇰🇵 E2.0 flag: North Korea
1F1F0 1F1F7                                ; fully-qualified     # 🇰🇷 E0.6 flag: South Korea
1F1F0 1F1FC                                ; fully-qualified     # 🇰🇼 E2.0 flag: Kuwait
1F1F0 1F1FE                                ; fully-qualified     # 🇰🇾 E2.0 flag: Cayman Islands
1F1F0 1F1FF                                ; fully-qualified     # 🇰🇿 E2.0 flag: Kazakhstan
1F1F1 1F1E6                                ; fully-qualified     # 🇱🇦 E2.0 flag: Laos
1F1F1 1F1E7                                ; fully-qualified     # 🇱🇧 E2.0 flag: Lebanon
1F1F1 1F1E8                                ; fully-qualified     # 🇱🇨 E2.0 flag: St. Lucia
1F1F1 1F1EE                                ; fully-qualified     # 🇱🇮 E2.0 flag: Liechtenstein
1F1F1 1F1F0                                ; fully-qualified     # 🇱🇰 E2.0 flag: Sri Lanka
1F1F1 1F1F7                                ; fully-qualified     # 🇱🇷 E2.0 flag: Liberia
1F1F1 1F1F8                                ; fully-qualified     # 🇱🇸 E2.0 flag: Lesotho
1F1F1 1F1F9                                ; fully-qualified     # 🇱🇹 E2.0 flag: Lithuania
1F1F1 1F1FA                                ; fully-qualified     # 🇱🇺 E2.0 flag: Luxembourg
1F1F1 1F1FB                                ; fully-qualified     # 🇱🇻 E2.0 flag: Latvia
1F1F1 1F1FE                                ; fully-qualified     # 🇱🇾 E2.0 flag: Libya
1F1F2 1F1E6                                ; fully-qualified     # 🇲🇦 E2.0 flag: Morocco
1F1F2 1F1E8                                ; fully-qualified     # 🇲🇨 E2.0 flag: Monaco
1F1F2 1F1E9                                ; fully-qualified     # 🇲🇩 E2.0 flag: Moldova
1F1F2 1F1EA                                ; fully-qualified     # 🇲🇪 E2.0 flag: Montenegro
1F1F2 1F1EB                                ; fully-qualified     # 🇲🇫 E2.0 flag: St. Martin
1F1F2 1F1EC                                ; fully-qualified     # 🇲🇬 E2.0 flag: Madagascar
1F1F2 1F1ED                                ; fully-qualified     # 🇲🇭 E2.0 flag: Marshall Islands
1F1F2 1F1F0                                ; fully-qualified     # 🇲🇰 E2.0 flag: North Macedonia
1F1F2 1F1F1                                ; fully-qualified     # 🇲🇱 E2.0 flag: Mali
1F1F2 1F1F2                                ; fully-qualified     # 🇲🇲 E2.0 flag: Myanmar (Burma)
1F1F2 1F1F3                                ; fully-qualified     # 🇲🇳 E2.0 flag: Mongolia
1F1F2 1F1F4                                ; fully-qualified     # 🇲🇴 E2.0 flag: Macao SAR China
1F1F2 1F1F5                                ; fully-qualified     # 🇲🇵 E2.0 flag: Northern Mariana Islands
1F1F2 1F1F6                                ; fully-qualified     # 🇲🇶 E2.0 flag: Martinique
1F1F2 1F1F7                                ; fully-qualified     # 🇲🇷 E2.0 flag: Mauritania
1F1F2 1F1F8                                ; fully-qualified     # 🇲🇸 E2.0 flag: Montserrat
1F1F2 1F1F9                                ; fully-qualified     # 🇲🇹 E2.0 flag: Malta
1F1F2 1F1FA                                ; fully-qualified     # 🇲🇺 E2.0 flag: Mauritius
1F1F2 1F1FB                                ; fully-qualified     # 🇲🇻 E2.0 flag: Maldives
1F1F2 1F1FC                                ; fully-qualified     # 🇲🇼 E2.0 flag: Malawi
1F1F2 1F1FD                                ; fully-qualified     # 🇲🇽 E2.0 flag: Mexico
1F1F2 1F1FE                                ; fully-qualified     # 🇲🇾 E2.0 flag: Malaysia
1F1F2 1F1FF                                ; fully-qualified     # 🇲🇿 E2.0 flag: Mozambique
1F1F3 1F1E6                                ; fully-qualified     # 🇳🇦 E2.0 flag: Namibia
1F1F3 1F1E8                                ; fully-qualified     # 🇳🇨 E2.0 flag: New Caledonia
1F1F3 1F1EA                                ; fully-qualified     # 🇳🇪 E2.0 flag: Niger
1F1F3 1F1EB                                ; fully-qualified     # 🇳🇫 E2.0 flag: Norfolk Island
1F1F3 1F1EC                                ; fully-qualified     # 🇳🇬 E2.0 flag: Nigeria
1F1F3 1F1EE                                ; fully-qualified     # 🇳🇮 E2.0 flag: Nicaragua
1F1F3 1F1F1                                ; fully-qualified     # 🇳🇱 E2.0 flag: Netherlands
1F1F3 1F1F4                                ; fully-qualified     # 🇳🇴 E2.0 flag: Norway
1F1F3 1F1F5                                ; fully-qualified     # 🇳🇵 E2.0 flag: Nepal
1F1F3 1F1F7                                ; fully-qualified     # 🇳🇷 E2.0 flag: Nauru
1F1F3 1F1FA                                ; fully-qualified     # 🇳🇺 E2.0 flag: Niue
1F1F3 1F1FF                                ; fully-qualified     # 🇳🇿 E2.0 flag: New Zealand
1F1F4 1F1F2                                ; fully-qualified     # 🇴🇲 E2.0 flag: Oman
1F1F5 1F1E6                                ; fully-qualified     # 🇵🇦 E2.0 flag: Panama
1F1F5 1F1EA                                ; fully-qualified     # 🇵🇪 E2.0 flag: Peru
1F1F5 1F1EB                                ; fully-qualified     # 🇵🇫 E2.0 flag: French Polynesia
1F1F5 1F1EC                                ; fully-qualified     # 🇵🇬 E2.0 flag: Papua New Guinea
1F1F5 1F1ED                                ; fully-qualified     # 🇵🇭 E2.0 flag: Philippines
1F1F5 1F1F0                                ; fully-qualified     # 🇵🇰 E2.0 flag: Pakistan
1F1F5 1F1F1                                ; fully-qualified     # 🇵🇱 E2.0 flag: Poland
1F1F5 1F1F2                                ; fully-qualified     # 🇵🇲 E2.0 flag: St. Pierre & Miquelon
1F1F5 1F1F3                                ; fully-qualified     # 🇵🇳 E2.0 flag: Pitcairn Islands
1F1F5 1F1F7                                ; fully-qualified     # 🇵🇷 E2.0 flag: Puerto Rico
1F1F5 1F1F8                                ; fully-qualified     # 🇵🇸 E2.0 flag: Palestinian Territories
1F1F5 1F1F9                                ; fully-qualified     # 🇵🇹 E2.0 flag: Portugal
1F1F5 1F1FC                                ; fully-qualified     # 🇵🇼 E2.0 flag: Palau
1F1F5 1F1FE                                ; fully-qualified     # 🇵🇾 E2.0 flag: Paraguay
1F1F6 1F1E6                                ; fully-qualified     # 🇶🇦 E2.0 flag: Qatar
1F1F7 1F1EA                                ; fully-qualified     # 🇷🇪 E2.0 flag: Réunion
1F1F7 1F1F4                                ; fully-qualified     # 🇷🇴 E2.0 flag: Romania
1F1F7 1F1F8                                ; fully-qualified     # 🇷🇸 E2.0 flag: Serbia
1F1F7 1F1FA                                ; fully-qualified     # 🇷🇺 E0.6 flag: Russia
1F1F7 1F1FC                                ; fully-qualified     # 🇷🇼 E2.0 flag: Rwanda
1F1F8 1F1E6                                ; fully-qualified     # 🇸🇦 E2.0 flag: Saudi Arabia
1F1F8 1F1E7                                ; fully-qualified     # 🇸🇧 E2.0 flag: Solomon Islands
1F1F8 1F1E8                                ; fully-qualified     # 🇸🇨 E2.0 flag: Seychelles
1F1F8 1F1E9                                ; fully-qualified     # 🇸🇩 E2.0 flag: Sudan
1F1F8 1F1EA                                ; fully-qualified     # 🇸🇪 E2.0 flag: Sweden
1F1F8 1F1EC                                ; fully-qualified     # 🇸🇬 E2.0 flag: Singapore
1F1F8 1F1ED                                ; fully-qualified     # 🇸🇭 E2.0 flag: St. Helena
1F1F8 1F1EE                                ; fully-qualified     # 🇸🇮 E2.0 flag: Slovenia
1F1F8 1F1EF                                ; fully-qualified     # 🇸🇯 E2.0 flag: Svalbard & Jan Mayen
1F1F8 1F1F0                                ; fully-qualified     # 🇸🇰 E2.0 flag: Slovakia
1F1F8 1F1F1                                ; fully-qualified     # 🇸🇱 E2.0 flag: Sierra Leone
1F1F8 1F1F2                                ; fully-qualified     # 🇸🇲 E2.0 flag: San Marino
1F1F8 1F1F3                                ; fully-qualified     # 🇸🇳 E2.0 flag: Senegal
1F1F8 1F1F4                                ; fully-qualified     # 🇸🇴 E2.0 flag: Somalia
1F1F8 1F1F7                                ; fully-qualified     # 🇸🇷 E2.0 flag: Suriname
1F1F8 1F1F8                                ; fully-qualified     # 🇸🇸 E2.0 flag: South Sudan
1F1F8 1F1F9                                ; fully-qualified     # 🇸🇹 E2.0 flag: São Tomé & Príncipe
1F1F8 1F1FB                                ; fully-qualified     # 🇸🇻 E2.0 flag: El Salvador
1F1F8 1F1FD                                ; fully-qualified     # 🇸🇽 E2.0 flag: Sint Maarten
1F1F8 1F1FE                                ; fully-qualified     # 🇸🇾 E2.0 flag: Syria
1F1F8 1F1FF                                ; fully-qualified     # 🇸🇿 E2.0 flag: Eswatini
1F1F9 1F1E6                                ; fully-qualified     # 🇹🇦 E2.0 flag: Tristan da Cunha
1F1F9 1F1E8                                ; fully-qualified     # 🇹🇨 E2.0 flag: Turks & Caicos Islands
1F1F9 1F1E9                                ; fully-qualified     # 🇹🇩 E2.0 flag: Chad
1F1F9 1F1EB                                ; fully-qualified     # 🇹🇫 E2.0 flag: French Southern Territories
1F1F9 1F1EC                                ; fully-qualified     # 🇹🇬 E2.0 flag: Togo
1F1F9 1F1ED                                ; fully-qualified     # 🇹🇭 E2.0 flag: Thailand
1F1F9 1F1EF                                ; fully-qualified     # 🇹🇯 E2.0 flag: Tajikistan
1F1F9 1F1F0                                ; fully-qualified     # 🇹🇰 E2.0 flag: Tokelau
1F1F9 1F1F1                                ; fully-qualified     # 🇹🇱 E2.0 flag: Timor-Leste
1F1F9 1F1F2                                ; fully-qualified     # 🇹🇲 E2.0 flag: Turkmenistan
1F1F9 1F1F3                                ; fully-qualified     # 🇹🇳 E2.0 flag: Tunisia
1F1F9 1F1F4                                ; fully-qualified     # 🇹🇴 E2.0 flag: Tonga
1F1F9 1F1F7                                ; fully-qualified     # 🇹🇷 E2.0 flag: Turkey
1F1F9 1F1F9                                ; fully-qualified     # 🇹🇹 E2.0 flag: Trinidad & Tobago
1F1F9 1F1FB                                ; fully-qualified     # 🇹🇻 E2.0 flag: Tuvalu
1F1F9 1F1FC                                ; fully-qualified     # 🇹🇼 E2.0 flag: Taiwan
1F1F9 1F1FF                                ; fully-qualified     # 🇹🇿 E2.0 flag: Tanzania
1F1FA 1F1E6                                ; fully-qualified     # 🇺🇦 E2.0 flag: Ukraine
1F1FA 1F1EC                                ; fully-qualified     # 🇺🇬 E2.0 flag: Uganda
1F1FA 1F1F2                                ; fully-qualified     # 🇺🇲 E2.0 flag: U.S. Outlying Islands
1F1FA 1F1F3                                ; fully-qualified     # 🇺🇳 E4.0 flag: United Nations
1F1FA 1F1F8                                ; fully-qualified     # 🇺🇸 E0.6 flag: United States
1F1FA 1F1FE                                ; fully-qualified     # 🇺🇾 E2.0 flag: Uruguay
1F1FA 1F1FF                                ; fully-qualified     # 🇺🇿 E2.0 flag: Uzbekistan
1F1FB 1F1E6                                ; fully-qualified     # 🇻🇦 E2.0 flag: Vatican City
1F1FB 1F1E8                                ; fully-qualified     # 🇻🇨 E2.0 flag: St. Vincent & Grenadines
1F1FB 1F1EA                                ; fully-qualified     # 🇻🇪 E2.0 flag: Venezuela
1F1FB 1F1EC                                ; fully-qualified     # 🇻🇬 E2.0 flag: British Virgin Islands
1F1FB 1F1EE                                ; fully-qualified     # 🇻🇮 E2.0 flag: U.S. Virgin Islands
1F1FB 1F1F3                                ; fully-qualified     # 🇻🇳 E2.0 flag: Vietnam
1F1FB 1F1FA                                ; fully-qualified     # 🇻🇺 E2.0 flag: Vanuatu
1F1FC 1F1EB                                ; fully-qualified     # 🇼🇫 E2.0 flag: Wallis & Futuna
1F1FC 1F1F8                                ; fully-qualified     # 🇼🇸 E2.0 flag: Samoa
1F1FD 1F1F0                                ; fully-qualified     # 🇽🇰 E2.0 flag: Kosovo
1F1FE 1F1EA                                ; fully-qualified     # 🇾🇪 E2.0 flag: Yemen
1F1FE 1F1F9                                ; fully-qualified     # 🇾🇹 E2.0 flag: Mayotte
1F1FF 1F1E6                                ; fully-qualified     # 🇿🇦 E2.0 flag: South Africa
1F1FF 1F1F2                                ; fully-qualified     # 🇿🇲 E2.0 flag: Zambia
1F1FF 1F1FC                                ; fully-qualified     # 🇿🇼 E2.0 flag: Zimbabwe

# subgroup: subdivision-flag
1F3F4 E0067 E0062 E0065 E006E E0067 E007F  ; fully-qualified     # 🏴󠁧󠁢󠁥󠁮󠁧󠁿 E5.0 flag: England
1F3F4 E0067 E0062 E0073 E0063 E0074 E007F  ; fully-qualified     # 🏴󠁧󠁢󠁳󠁣󠁴󠁿 E5.0 flag: Scotland
1F3F4 E0067 E0062 E0077 E006C E0073 E007F  ; fully-qualified     # 🏴󠁧󠁢󠁷󠁬󠁳󠁿 E5.0 flag: Wales

# Flags subtotal:		275
# Flags subtotal:		275	w/o modifiers

# Status Counts
# fully-qualified : 3295
# minimally-qualified : 614
# unqualified : 250
# component : 9

#EOF