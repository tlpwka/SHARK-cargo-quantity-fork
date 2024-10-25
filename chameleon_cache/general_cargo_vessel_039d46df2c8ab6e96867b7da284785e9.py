# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/templates/general_cargo_vessel.pynml'

__tokens = {0: ('${ship.render_debug_info()}\n\n// graphics\ntemplate spriteset_template_${ship.id}(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]}, ANIM]\n    [60,        y,          113,        71,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]}, ANIM]\n    [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]}, ANIM]\n    [328,       y,          113,        71,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]}, ANIM]\n    [454,       y,          28,         89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]}, ANIM]\n    [494,       y,          113,        71,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]}, ANIM]\n    [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]}, ANIM]\n    [762,       y,          113,        71,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]}, ANIM]\n}', 1, 0), 2: ('ship.render_debug_info()', 1, 2), 71: ('ship.id', 4, 30), 217: ('ship.offsets[0][0]', 6, 55), 240: ('ship.offsets[0][1]', 6, 78), 322: ('ship.offsets[1][0]', 7, 55), 345: ('ship.offsets[1][1]', 7, 78), 427: ('ship.offsets[2][0]', 8, 55), 450: ('ship.offsets[2][1]', 8, 78), 532: ('ship.offsets[3][0]', 9, 55), 555: ('ship.offsets[3][1]', 9, 78), 637: ('ship.offsets[4][0]', 10, 55), 660: ('ship.offsets[4][1]', 10, 78), 742: ('ship.offsets[5][0]', 11, 55), 765: ('ship.offsets[5][1]', 11, 78), 847: ('ship.offsets[6][0]', 12, 55), 870: ('ship.offsets[6][1]', 12, 78), 952: ('ship.offsets[7][0]', 13, 55), 975: ('ship.offsets[7][1]', 13, 78), 1059: ('python:range(ship.get_num_spritesets())', 17, 53), 1105: ('spriteset(${ship.id}_ss_not_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(10)\n    }\n    spriteset(${ship.id}_ss_not_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(110)\n    }\n    spriteset(${ship.id}_ss_loading_0_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(210)\n    }\n    spriteset(${ship.id}_ss_loading_1_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(310)\n    }\n    spriteset(${ship.id}_ss_loading_2_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(410)\n    }\n    spriteset(${ship.id}_ss_loading_3_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(510)\n    }\n    spriteset(${ship.id}_ss_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(610)\n    }\n    spriteset(${ship.id}_ss_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(710)\n    }\n\n    spritegroup ${ship.id}_sg_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_moving_${variation_num},\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n        loading: [ // can\'t be loading when moving, but we\'ll overlook that, it\'s required by nml ;)\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n    }\n\n    spritegroup ${ship.id}_sg_not_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_not_moving_${variation_num},\n            ${ship.id}_ss_loaded_not_moving_${variation_num},\n        ];\n        loading: [\n            ${ship.id}_ss_loading_0_${variation_num},\n            ${ship.id}_ss_loading_1_${variation_num},\n            ${ship.id}_ss_loading_2_${variation_num},\n            ${ship.id}_ss_loading_3_${variation_num},\n        ];\n    }\n\n    switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_${variation_num}, current_speed) {\n        0: return ${ship.id}_sg_not_moving_${variation_num};\n        return ${ship.id}_sg_moving_${variation_num};\n    }', 18, 4), 1117: ('ship.id', 18, 16), 1153: ('variation_num', 18, 52), 1185: ('ship.id', 18, 84), 1196: ('variation_num', 18, 95), 1246: ('ship.id', 19, 27), 1281: ('ship.id', 21, 16), 1313: ('variation_num', 21, 48), 1345: ('ship.id', 21, 80), 1356: ('variation_num', 21, 91), 1406: ('ship.id', 22, 27), 1442: ('ship.id', 24, 16), 1466: ('variation_num', 24, 40), 1498: ('ship.id', 24, 72), 1509: ('variation_num', 24, 83), 1559: ('ship.id', 25, 27), 1595: ('ship.id', 27, 16), 1619: ('variation_num', 27, 40), 1651: ('ship.id', 27, 72), 1662: ('variation_num', 27, 83), 1712: ('ship.id', 28, 27), 1748: ('ship.id', 30, 16), 1772: ('variation_num', 30, 40), 1804: ('ship.id', 30, 72), 1815: ('variation_num', 30, 83), 1865: ('ship.id', 31, 27), 1901: ('ship.id', 33, 16), 1925: ('variation_num', 33, 40), 1957: ('ship.id', 33, 72), 1968: ('variation_num', 33, 83), 2018: ('ship.id', 34, 27), 2054: ('ship.id', 36, 16), 2086: ('variation_num', 36, 48), 2118: ('ship.id', 36, 80), 2129: ('variation_num', 36, 91), 2179: ('ship.id', 37, 27), 2215: ('ship.id', 39, 16), 2243: ('variation_num', 39, 44), 2275: ('ship.id', 39, 76), 2286: ('variation_num', 39, 87), 2336: ('ship.id', 40, 27), 2375: ('ship.id', 43, 18), 2396: ('variation_num', 43, 39), 2446: ('ship.id', 45, 14), 2478: ('variation_num', 45, 46), 2508: ('ship.id', 46, 14), 2536: ('variation_num', 46, 42), 2678: ('ship.id', 49, 14), 2706: ('variation_num', 49, 42), 2758: ('ship.id', 53, 18), 2783: ('variation_num', 53, 43), 2833: ('ship.id', 55, 14), 2869: ('variation_num', 55, 50), 2899: ('ship.id', 56, 14), 2931: ('variation_num', 56, 46), 2991: ('ship.id', 59, 14), 3015: ('variation_num', 59, 38), 3045: ('ship.id', 60, 14), 3069: ('variation_num', 60, 38), 3099: ('ship.id', 61, 14), 3123: ('variation_num', 61, 38), 3153: ('ship.id', 62, 14), 3177: ('variation_num', 62, 38), 3243: ('ship.id', 66, 32), 3270: ('variation_num', 66, 59), 3323: ('ship.id', 67, 20), 3348: ('variation_num', 67, 45), 3381: ('ship.id', 68, 17), 3402: ('variation_num', 68, 38), 3504: ('load: graphics_random_switches.pynml', 72, 46), 3559: ('graphics_random_switches', 72, 101), 3559: ('graphics_random_switches', 72, 101), 3589: ('// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${ship.buy_menu_width}, 22, -${int(ship.buy_menu_width / 2)}, -10, ANIM]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}', 74, 0), 3650: ('ship.id', 76, 39), 3747: ('ship.buy_menu_bb_xy[0]', 78, 7), 3774: ('ship.buy_menu_bb_xy[1]', 78, 34), 3801: ('ship.buy_menu_width', 78, 61), 3830: ('int(ship.buy_menu_width / 2)', 78, 90), 3887: ('ship.id', 81, 12), 3925: ('ship.id', 81, 50), 3976: ('ship.id', 82, 32), 4004: ('ship.id', 85, 14), 4052: ('ship.id', 87, 10), 4106: ('ship.id', 90, 10), 4141: ('ship.render_speed_switches()', 95, 2), 4174: ('ship.render_cargo_capacity()', 97, 2), 4207: ('ship.render_properties()', 99, 2)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139842927946928 = 'graphics_random_switches'
_static_139842931246032 = {}

import re
import functools
from itertools import chain as __chain
from sys import intern
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Interpolation value=<Substitution '${ship.render_debug_info()}\n\n// graphics\ntemplate spriteset_template_${ship.id}(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]}, ANIM]\n    [60,        y,          113,        71,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]}, ANIM]\n    [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]}, ANIM]\n    [328,       y,          113,        71,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]}, ANIM]\n    [454,       y,          28,         89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]}, ANIM]\n    [494,       y,          113,        71,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]}, ANIM]\n    [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]}, ANIM]\n    [762,       y,          113,        71,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]}, ANIM]\n}\n\n\n' (1:0)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2fb814de50> -> __content_139842944183280
            __token = 0
            __token = 2
            __content_139842944183280 = _lookup_attr(getitem('ship'), 'render_debug_info')()
            __content_139842944183280 = __quote(__content_139842944183280, '\x00', '&#0;', None, None)
            __token = 71
            __content_139842944183280_69 = _lookup_attr(getitem('ship'), 'id')
            __content_139842944183280_69 = __quote(__content_139842944183280_69, '\x00', '&#0;', None, None)
            __token = 217
            __content_139842944183280_215 = _lookup_attr(getitem('ship'), 'offsets')[0][0]
            __content_139842944183280_215 = __quote(__content_139842944183280_215, '\x00', '&#0;', None, None)
            __token = 240
            __content_139842944183280_238 = _lookup_attr(getitem('ship'), 'offsets')[0][1]
            __content_139842944183280_238 = __quote(__content_139842944183280_238, '\x00', '&#0;', None, None)
            __token = 322
            __content_139842944183280_320 = _lookup_attr(getitem('ship'), 'offsets')[1][0]
            __content_139842944183280_320 = __quote(__content_139842944183280_320, '\x00', '&#0;', None, None)
            __token = 345
            __content_139842944183280_343 = _lookup_attr(getitem('ship'), 'offsets')[1][1]
            __content_139842944183280_343 = __quote(__content_139842944183280_343, '\x00', '&#0;', None, None)
            __token = 427
            __content_139842944183280_425 = _lookup_attr(getitem('ship'), 'offsets')[2][0]
            __content_139842944183280_425 = __quote(__content_139842944183280_425, '\x00', '&#0;', None, None)
            __token = 450
            __content_139842944183280_448 = _lookup_attr(getitem('ship'), 'offsets')[2][1]
            __content_139842944183280_448 = __quote(__content_139842944183280_448, '\x00', '&#0;', None, None)
            __token = 532
            __content_139842944183280_530 = _lookup_attr(getitem('ship'), 'offsets')[3][0]
            __content_139842944183280_530 = __quote(__content_139842944183280_530, '\x00', '&#0;', None, None)
            __token = 555
            __content_139842944183280_553 = _lookup_attr(getitem('ship'), 'offsets')[3][1]
            __content_139842944183280_553 = __quote(__content_139842944183280_553, '\x00', '&#0;', None, None)
            __token = 637
            __content_139842944183280_635 = _lookup_attr(getitem('ship'), 'offsets')[4][0]
            __content_139842944183280_635 = __quote(__content_139842944183280_635, '\x00', '&#0;', None, None)
            __token = 660
            __content_139842944183280_658 = _lookup_attr(getitem('ship'), 'offsets')[4][1]
            __content_139842944183280_658 = __quote(__content_139842944183280_658, '\x00', '&#0;', None, None)
            __token = 742
            __content_139842944183280_740 = _lookup_attr(getitem('ship'), 'offsets')[5][0]
            __content_139842944183280_740 = __quote(__content_139842944183280_740, '\x00', '&#0;', None, None)
            __token = 765
            __content_139842944183280_763 = _lookup_attr(getitem('ship'), 'offsets')[5][1]
            __content_139842944183280_763 = __quote(__content_139842944183280_763, '\x00', '&#0;', None, None)
            __token = 847
            __content_139842944183280_845 = _lookup_attr(getitem('ship'), 'offsets')[6][0]
            __content_139842944183280_845 = __quote(__content_139842944183280_845, '\x00', '&#0;', None, None)
            __token = 870
            __content_139842944183280_868 = _lookup_attr(getitem('ship'), 'offsets')[6][1]
            __content_139842944183280_868 = __quote(__content_139842944183280_868, '\x00', '&#0;', None, None)
            __token = 952
            __content_139842944183280_950 = _lookup_attr(getitem('ship'), 'offsets')[7][0]
            __content_139842944183280_950 = __quote(__content_139842944183280_950, '\x00', '&#0;', None, None)
            __token = 975
            __content_139842944183280_973 = _lookup_attr(getitem('ship'), 'offsets')[7][1]
            __content_139842944183280_973 = __quote(__content_139842944183280_973, '\x00', '&#0;', None, None)
            __content_139842944183280 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ((__content_139842944183280 if (__content_139842944183280 is not None) else ''), '\n\n// graphics\ntemplate spriteset_template_', (__content_139842944183280_69 if (__content_139842944183280_69 is not None) else ''), '(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ', (__content_139842944183280_215 if (__content_139842944183280_215 is not None) else ''), ', ', (__content_139842944183280_238 if (__content_139842944183280_238 is not None) else ''), ', ANIM]\n    [60,        y,          113,        71,          ', (__content_139842944183280_320 if (__content_139842944183280_320 is not None) else ''), ', ', (__content_139842944183280_343 if (__content_139842944183280_343 is not None) else ''), ', ANIM]\n    [186,       y,          138,        48,          ', (__content_139842944183280_425 if (__content_139842944183280_425 is not None) else ''), ', ', (__content_139842944183280_448 if (__content_139842944183280_448 is not None) else ''), ', ANIM]\n    [328,       y,          113,        71,          ', (__content_139842944183280_530 if (__content_139842944183280_530 is not None) else ''), ', ', (__content_139842944183280_553 if (__content_139842944183280_553 is not None) else ''), ', ANIM]\n    [454,       y,          28,         89,          ', (__content_139842944183280_635 if (__content_139842944183280_635 is not None) else ''), ', ', (__content_139842944183280_658 if (__content_139842944183280_658 is not None) else ''), ', ANIM]\n    [494,       y,          113,        71,          ', (__content_139842944183280_740 if (__content_139842944183280_740 is not None) else ''), ', ', (__content_139842944183280_763 if (__content_139842944183280_763 is not None) else ''), ', ANIM]\n    [620,       y,          138,        48,          ', (__content_139842944183280_845 if (__content_139842944183280_845 is not None) else ''), ', ', (__content_139842944183280_868 if (__content_139842944183280_868 is not None) else ''), ', ANIM]\n    [762,       y,          113,        71,          ', (__content_139842944183280_950 if (__content_139842944183280_950 is not None) else ''), ', ', (__content_139842944183280_973 if (__content_139842944183280_973 is not None) else ''), ', ANIM]\n}\n\n\n', ))
            if (__content_139842944183280 is None):
                pass
            else:
                if (__content_139842944183280 is None):
                    __content_139842944183280 = None
                else:
                    __tt = type(__content_139842944183280)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139842944183280 = str(__content_139842944183280)
                    else:
                        if (__tt is bytes):
                            __content_139842944183280 = decode(__content_139842944183280)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139842944183280 = __content_139842944183280.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139842944183280)
                                    __content_139842944183280 = (str(__content_139842944183280) if (__content_139842944183280 is __converted) else __converted)
                                else:
                                    __content_139842944183280 = __content_139842944183280()
            if (__content_139842944183280 is not None):
                __append(__content_139842944183280)

            # <Static value=<ast.Dict object at 0x7f2fb83dc3d0> name=None at 7f2fb8365f50> -> __attrs_139842929188496
            __attrs_139842929188496 = _static_139842931246032
            __backup_variation_num_139842944902160 = get('variation_num', __marker)

            # <Value 'python:range(ship.get_num_spritesets())' (17:53)> -> __iterator
            __token = 1059
            __iterator = get('range', range)(_lookup_attr(getitem('ship'), 'get_num_spritesets')())
            (__iterator, ____index_139842927838928, ) = getitem('repeat')('variation_num', __iterator)
            econtext['variation_num'] = None
            for __item in __iterator:
                econtext['variation_num'] = __item

                # <Interpolation value=<Substitution '\n    spriteset(${ship.id}_ss_not_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(10)\n    }\n    spriteset(${ship.id}_ss_not_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(110)\n    }\n    spriteset(${ship.id}_ss_loading_0_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(210)\n    }\n    spriteset(${ship.id}_ss_loading_1_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(310)\n    }\n    spriteset(${ship.id}_ss_loading_2_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(410)\n    }\n    spriteset(${ship.id}_ss_loading_3_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(510)\n    }\n    spriteset(${ship.id}_ss_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(610)\n    }\n    spriteset(${ship.id}_ss_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(710)\n    }\n\n    spritegroup ${ship.id}_sg_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_moving_${variation_num},\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n        loading: [ // can\'t be loading when moving, but we\'ll overlook that, it\'s required by nml ;)\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n    }\n\n    spritegroup ${ship.id}_sg_not_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_not_moving_${variation_num},\n            ${ship.id}_ss_loaded_not_moving_${variation_num},\n        ];\n        loading: [\n            ${ship.id}_ss_loading_0_${variation_num},\n            ${ship.id}_ss_loading_1_${variation_num},\n            ${ship.id}_ss_loading_2_${variation_num},\n            ${ship.id}_ss_loading_3_${variation_num},\n        ];\n    }\n\n    switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_${variation_num}, current_speed) {\n        0: return ${ship.id}_sg_not_moving_${variation_num};\n        return ${ship.id}_sg_moving_${variation_num};\n    }\n' (17:94)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2fb8070f10> -> __content_139842944183280
                __token = 1105
                __token = 1117
                __content_139842944183280 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280 = __quote(__content_139842944183280, '\x00', '&#0;', None, None)
                __token = 1153
                __content_139842944183280_1151 = getitem('variation_num')
                __content_139842944183280_1151 = __quote(__content_139842944183280_1151, '\x00', '&#0;', None, None)
                __token = 1185
                __content_139842944183280_1183 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1183 = __quote(__content_139842944183280_1183, '\x00', '&#0;', None, None)
                __token = 1196
                __content_139842944183280_1194 = getitem('variation_num')
                __content_139842944183280_1194 = __quote(__content_139842944183280_1194, '\x00', '&#0;', None, None)
                __token = 1246
                __content_139842944183280_1244 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1244 = __quote(__content_139842944183280_1244, '\x00', '&#0;', None, None)
                __token = 1281
                __content_139842944183280_1279 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1279 = __quote(__content_139842944183280_1279, '\x00', '&#0;', None, None)
                __token = 1313
                __content_139842944183280_1311 = getitem('variation_num')
                __content_139842944183280_1311 = __quote(__content_139842944183280_1311, '\x00', '&#0;', None, None)
                __token = 1345
                __content_139842944183280_1343 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1343 = __quote(__content_139842944183280_1343, '\x00', '&#0;', None, None)
                __token = 1356
                __content_139842944183280_1354 = getitem('variation_num')
                __content_139842944183280_1354 = __quote(__content_139842944183280_1354, '\x00', '&#0;', None, None)
                __token = 1406
                __content_139842944183280_1404 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1404 = __quote(__content_139842944183280_1404, '\x00', '&#0;', None, None)
                __token = 1442
                __content_139842944183280_1440 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1440 = __quote(__content_139842944183280_1440, '\x00', '&#0;', None, None)
                __token = 1466
                __content_139842944183280_1464 = getitem('variation_num')
                __content_139842944183280_1464 = __quote(__content_139842944183280_1464, '\x00', '&#0;', None, None)
                __token = 1498
                __content_139842944183280_1496 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1496 = __quote(__content_139842944183280_1496, '\x00', '&#0;', None, None)
                __token = 1509
                __content_139842944183280_1507 = getitem('variation_num')
                __content_139842944183280_1507 = __quote(__content_139842944183280_1507, '\x00', '&#0;', None, None)
                __token = 1559
                __content_139842944183280_1557 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1557 = __quote(__content_139842944183280_1557, '\x00', '&#0;', None, None)
                __token = 1595
                __content_139842944183280_1593 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1593 = __quote(__content_139842944183280_1593, '\x00', '&#0;', None, None)
                __token = 1619
                __content_139842944183280_1617 = getitem('variation_num')
                __content_139842944183280_1617 = __quote(__content_139842944183280_1617, '\x00', '&#0;', None, None)
                __token = 1651
                __content_139842944183280_1649 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1649 = __quote(__content_139842944183280_1649, '\x00', '&#0;', None, None)
                __token = 1662
                __content_139842944183280_1660 = getitem('variation_num')
                __content_139842944183280_1660 = __quote(__content_139842944183280_1660, '\x00', '&#0;', None, None)
                __token = 1712
                __content_139842944183280_1710 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1710 = __quote(__content_139842944183280_1710, '\x00', '&#0;', None, None)
                __token = 1748
                __content_139842944183280_1746 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1746 = __quote(__content_139842944183280_1746, '\x00', '&#0;', None, None)
                __token = 1772
                __content_139842944183280_1770 = getitem('variation_num')
                __content_139842944183280_1770 = __quote(__content_139842944183280_1770, '\x00', '&#0;', None, None)
                __token = 1804
                __content_139842944183280_1802 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1802 = __quote(__content_139842944183280_1802, '\x00', '&#0;', None, None)
                __token = 1815
                __content_139842944183280_1813 = getitem('variation_num')
                __content_139842944183280_1813 = __quote(__content_139842944183280_1813, '\x00', '&#0;', None, None)
                __token = 1865
                __content_139842944183280_1863 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1863 = __quote(__content_139842944183280_1863, '\x00', '&#0;', None, None)
                __token = 1901
                __content_139842944183280_1899 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1899 = __quote(__content_139842944183280_1899, '\x00', '&#0;', None, None)
                __token = 1925
                __content_139842944183280_1923 = getitem('variation_num')
                __content_139842944183280_1923 = __quote(__content_139842944183280_1923, '\x00', '&#0;', None, None)
                __token = 1957
                __content_139842944183280_1955 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_1955 = __quote(__content_139842944183280_1955, '\x00', '&#0;', None, None)
                __token = 1968
                __content_139842944183280_1966 = getitem('variation_num')
                __content_139842944183280_1966 = __quote(__content_139842944183280_1966, '\x00', '&#0;', None, None)
                __token = 2018
                __content_139842944183280_2016 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2016 = __quote(__content_139842944183280_2016, '\x00', '&#0;', None, None)
                __token = 2054
                __content_139842944183280_2052 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2052 = __quote(__content_139842944183280_2052, '\x00', '&#0;', None, None)
                __token = 2086
                __content_139842944183280_2084 = getitem('variation_num')
                __content_139842944183280_2084 = __quote(__content_139842944183280_2084, '\x00', '&#0;', None, None)
                __token = 2118
                __content_139842944183280_2116 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2116 = __quote(__content_139842944183280_2116, '\x00', '&#0;', None, None)
                __token = 2129
                __content_139842944183280_2127 = getitem('variation_num')
                __content_139842944183280_2127 = __quote(__content_139842944183280_2127, '\x00', '&#0;', None, None)
                __token = 2179
                __content_139842944183280_2177 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2177 = __quote(__content_139842944183280_2177, '\x00', '&#0;', None, None)
                __token = 2215
                __content_139842944183280_2213 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2213 = __quote(__content_139842944183280_2213, '\x00', '&#0;', None, None)
                __token = 2243
                __content_139842944183280_2241 = getitem('variation_num')
                __content_139842944183280_2241 = __quote(__content_139842944183280_2241, '\x00', '&#0;', None, None)
                __token = 2275
                __content_139842944183280_2273 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2273 = __quote(__content_139842944183280_2273, '\x00', '&#0;', None, None)
                __token = 2286
                __content_139842944183280_2284 = getitem('variation_num')
                __content_139842944183280_2284 = __quote(__content_139842944183280_2284, '\x00', '&#0;', None, None)
                __token = 2336
                __content_139842944183280_2334 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2334 = __quote(__content_139842944183280_2334, '\x00', '&#0;', None, None)
                __token = 2375
                __content_139842944183280_2373 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2373 = __quote(__content_139842944183280_2373, '\x00', '&#0;', None, None)
                __token = 2396
                __content_139842944183280_2394 = getitem('variation_num')
                __content_139842944183280_2394 = __quote(__content_139842944183280_2394, '\x00', '&#0;', None, None)
                __token = 2446
                __content_139842944183280_2444 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2444 = __quote(__content_139842944183280_2444, '\x00', '&#0;', None, None)
                __token = 2478
                __content_139842944183280_2476 = getitem('variation_num')
                __content_139842944183280_2476 = __quote(__content_139842944183280_2476, '\x00', '&#0;', None, None)
                __token = 2508
                __content_139842944183280_2506 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2506 = __quote(__content_139842944183280_2506, '\x00', '&#0;', None, None)
                __token = 2536
                __content_139842944183280_2534 = getitem('variation_num')
                __content_139842944183280_2534 = __quote(__content_139842944183280_2534, '\x00', '&#0;', None, None)
                __token = 2678
                __content_139842944183280_2676 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2676 = __quote(__content_139842944183280_2676, '\x00', '&#0;', None, None)
                __token = 2706
                __content_139842944183280_2704 = getitem('variation_num')
                __content_139842944183280_2704 = __quote(__content_139842944183280_2704, '\x00', '&#0;', None, None)
                __token = 2758
                __content_139842944183280_2756 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2756 = __quote(__content_139842944183280_2756, '\x00', '&#0;', None, None)
                __token = 2783
                __content_139842944183280_2781 = getitem('variation_num')
                __content_139842944183280_2781 = __quote(__content_139842944183280_2781, '\x00', '&#0;', None, None)
                __token = 2833
                __content_139842944183280_2831 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2831 = __quote(__content_139842944183280_2831, '\x00', '&#0;', None, None)
                __token = 2869
                __content_139842944183280_2867 = getitem('variation_num')
                __content_139842944183280_2867 = __quote(__content_139842944183280_2867, '\x00', '&#0;', None, None)
                __token = 2899
                __content_139842944183280_2897 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2897 = __quote(__content_139842944183280_2897, '\x00', '&#0;', None, None)
                __token = 2931
                __content_139842944183280_2929 = getitem('variation_num')
                __content_139842944183280_2929 = __quote(__content_139842944183280_2929, '\x00', '&#0;', None, None)
                __token = 2991
                __content_139842944183280_2989 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_2989 = __quote(__content_139842944183280_2989, '\x00', '&#0;', None, None)
                __token = 3015
                __content_139842944183280_3013 = getitem('variation_num')
                __content_139842944183280_3013 = __quote(__content_139842944183280_3013, '\x00', '&#0;', None, None)
                __token = 3045
                __content_139842944183280_3043 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_3043 = __quote(__content_139842944183280_3043, '\x00', '&#0;', None, None)
                __token = 3069
                __content_139842944183280_3067 = getitem('variation_num')
                __content_139842944183280_3067 = __quote(__content_139842944183280_3067, '\x00', '&#0;', None, None)
                __token = 3099
                __content_139842944183280_3097 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_3097 = __quote(__content_139842944183280_3097, '\x00', '&#0;', None, None)
                __token = 3123
                __content_139842944183280_3121 = getitem('variation_num')
                __content_139842944183280_3121 = __quote(__content_139842944183280_3121, '\x00', '&#0;', None, None)
                __token = 3153
                __content_139842944183280_3151 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_3151 = __quote(__content_139842944183280_3151, '\x00', '&#0;', None, None)
                __token = 3177
                __content_139842944183280_3175 = getitem('variation_num')
                __content_139842944183280_3175 = __quote(__content_139842944183280_3175, '\x00', '&#0;', None, None)
                __token = 3243
                __content_139842944183280_3241 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_3241 = __quote(__content_139842944183280_3241, '\x00', '&#0;', None, None)
                __token = 3270
                __content_139842944183280_3268 = getitem('variation_num')
                __content_139842944183280_3268 = __quote(__content_139842944183280_3268, '\x00', '&#0;', None, None)
                __token = 3323
                __content_139842944183280_3321 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_3321 = __quote(__content_139842944183280_3321, '\x00', '&#0;', None, None)
                __token = 3348
                __content_139842944183280_3346 = getitem('variation_num')
                __content_139842944183280_3346 = __quote(__content_139842944183280_3346, '\x00', '&#0;', None, None)
                __token = 3381
                __content_139842944183280_3379 = _lookup_attr(getitem('ship'), 'id')
                __content_139842944183280_3379 = __quote(__content_139842944183280_3379, '\x00', '&#0;', None, None)
                __token = 3402
                __content_139842944183280_3400 = getitem('variation_num')
                __content_139842944183280_3400 = __quote(__content_139842944183280_3400, '\x00', '&#0;', None, None)
                __content_139842944183280 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    spriteset(', (__content_139842944183280 if (__content_139842944183280 is not None) else ''), '_ss_not_loaded_not_moving_', (__content_139842944183280_1151 if (__content_139842944183280_1151 is not None) else ''), ', "src/graphics/', (__content_139842944183280_1183 if (__content_139842944183280_1183 is not None) else ''), '_', (__content_139842944183280_1194 if (__content_139842944183280_1194 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139842944183280_1244 if (__content_139842944183280_1244 is not None) else ''), '(10)\n    }\n    spriteset(', (__content_139842944183280_1279 if (__content_139842944183280_1279 is not None) else ''), '_ss_not_loaded_moving_', (__content_139842944183280_1311 if (__content_139842944183280_1311 is not None) else ''), ', "src/graphics/', (__content_139842944183280_1343 if (__content_139842944183280_1343 is not None) else ''), '_', (__content_139842944183280_1354 if (__content_139842944183280_1354 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139842944183280_1404 if (__content_139842944183280_1404 is not None) else ''), '(110)\n    }\n    spriteset(', (__content_139842944183280_1440 if (__content_139842944183280_1440 is not None) else ''), '_ss_loading_0_', (__content_139842944183280_1464 if (__content_139842944183280_1464 is not None) else ''), ', "src/graphics/', (__content_139842944183280_1496 if (__content_139842944183280_1496 is not None) else ''), '_', (__content_139842944183280_1507 if (__content_139842944183280_1507 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139842944183280_1557 if (__content_139842944183280_1557 is not None) else ''), '(210)\n    }\n    spriteset(', (__content_139842944183280_1593 if (__content_139842944183280_1593 is not None) else ''), '_ss_loading_1_', (__content_139842944183280_1617 if (__content_139842944183280_1617 is not None) else ''), ', "src/graphics/', (__content_139842944183280_1649 if (__content_139842944183280_1649 is not None) else ''), '_', (__content_139842944183280_1660 if (__content_139842944183280_1660 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139842944183280_1710 if (__content_139842944183280_1710 is not None) else ''), '(310)\n    }\n    spriteset(', (__content_139842944183280_1746 if (__content_139842944183280_1746 is not None) else ''), '_ss_loading_2_', (__content_139842944183280_1770 if (__content_139842944183280_1770 is not None) else ''), ', "src/graphics/', (__content_139842944183280_1802 if (__content_139842944183280_1802 is not None) else ''), '_', (__content_139842944183280_1813 if (__content_139842944183280_1813 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139842944183280_1863 if (__content_139842944183280_1863 is not None) else ''), '(410)\n    }\n    spriteset(', (__content_139842944183280_1899 if (__content_139842944183280_1899 is not None) else ''), '_ss_loading_3_', (__content_139842944183280_1923 if (__content_139842944183280_1923 is not None) else ''), ', "src/graphics/', (__content_139842944183280_1955 if (__content_139842944183280_1955 is not None) else ''), '_', (__content_139842944183280_1966 if (__content_139842944183280_1966 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139842944183280_2016 if (__content_139842944183280_2016 is not None) else ''), '(510)\n    }\n    spriteset(', (__content_139842944183280_2052 if (__content_139842944183280_2052 is not None) else ''), '_ss_loaded_not_moving_', (__content_139842944183280_2084 if (__content_139842944183280_2084 is not None) else ''), ', "src/graphics/', (__content_139842944183280_2116 if (__content_139842944183280_2116 is not None) else ''), '_', (__content_139842944183280_2127 if (__content_139842944183280_2127 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139842944183280_2177 if (__content_139842944183280_2177 is not None) else ''), '(610)\n    }\n    spriteset(', (__content_139842944183280_2213 if (__content_139842944183280_2213 is not None) else ''), '_ss_loaded_moving_', (__content_139842944183280_2241 if (__content_139842944183280_2241 is not None) else ''), ', "src/graphics/', (__content_139842944183280_2273 if (__content_139842944183280_2273 is not None) else ''), '_', (__content_139842944183280_2284 if (__content_139842944183280_2284 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139842944183280_2334 if (__content_139842944183280_2334 is not None) else ''), '(710)\n    }\n\n    spritegroup ', (__content_139842944183280_2373 if (__content_139842944183280_2373 is not None) else ''), '_sg_moving_', (__content_139842944183280_2394 if (__content_139842944183280_2394 is not None) else ''), ' {\n        loaded:  [\n            ', (__content_139842944183280_2444 if (__content_139842944183280_2444 is not None) else ''), '_ss_not_loaded_moving_', (__content_139842944183280_2476 if (__content_139842944183280_2476 is not None) else ''), ',\n            ', (__content_139842944183280_2506 if (__content_139842944183280_2506 is not None) else ''), '_ss_loaded_moving_', (__content_139842944183280_2534 if (__content_139842944183280_2534 is not None) else ''), ",\n        ];\n        loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n            ", (__content_139842944183280_2676 if (__content_139842944183280_2676 is not None) else ''), '_ss_loaded_moving_', (__content_139842944183280_2704 if (__content_139842944183280_2704 is not None) else ''), ',\n        ];\n    }\n\n    spritegroup ', (__content_139842944183280_2756 if (__content_139842944183280_2756 is not None) else ''), '_sg_not_moving_', (__content_139842944183280_2781 if (__content_139842944183280_2781 is not None) else ''), ' {\n        loaded:  [\n            ', (__content_139842944183280_2831 if (__content_139842944183280_2831 is not None) else ''), '_ss_not_loaded_not_moving_', (__content_139842944183280_2867 if (__content_139842944183280_2867 is not None) else ''), ',\n            ', (__content_139842944183280_2897 if (__content_139842944183280_2897 is not None) else ''), '_ss_loaded_not_moving_', (__content_139842944183280_2929 if (__content_139842944183280_2929 is not None) else ''), ',\n        ];\n        loading: [\n            ', (__content_139842944183280_2989 if (__content_139842944183280_2989 is not None) else ''), '_ss_loading_0_', (__content_139842944183280_3013 if (__content_139842944183280_3013 is not None) else ''), ',\n            ', (__content_139842944183280_3043 if (__content_139842944183280_3043 is not None) else ''), '_ss_loading_1_', (__content_139842944183280_3067 if (__content_139842944183280_3067 is not None) else ''), ',\n            ', (__content_139842944183280_3097 if (__content_139842944183280_3097 is not None) else ''), '_ss_loading_2_', (__content_139842944183280_3121 if (__content_139842944183280_3121 is not None) else ''), ',\n            ', (__content_139842944183280_3151 if (__content_139842944183280_3151 is not None) else ''), '_ss_loading_3_', (__content_139842944183280_3175 if (__content_139842944183280_3175 is not None) else ''), ',\n        ];\n    }\n\n    switch (FEAT_SHIPS, SELF, ', (__content_139842944183280_3241 if (__content_139842944183280_3241 is not None) else ''), '_switch_graphics_', (__content_139842944183280_3268 if (__content_139842944183280_3268 is not None) else ''), ', current_speed) {\n        0: return ', (__content_139842944183280_3321 if (__content_139842944183280_3321 is not None) else ''), '_sg_not_moving_', (__content_139842944183280_3346 if (__content_139842944183280_3346 is not None) else ''), ';\n        return ', (__content_139842944183280_3379 if (__content_139842944183280_3379 is not None) else ''), '_sg_moving_', (__content_139842944183280_3400 if (__content_139842944183280_3400 is not None) else ''), ';\n    }\n', ))
                if (__content_139842944183280 is None):
                    pass
                else:
                    if (__content_139842944183280 is None):
                        __content_139842944183280 = None
                    else:
                        __tt = type(__content_139842944183280)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139842944183280 = str(__content_139842944183280)
                        else:
                            if (__tt is bytes):
                                __content_139842944183280 = decode(__content_139842944183280)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139842944183280 = __content_139842944183280.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139842944183280)
                                        __content_139842944183280 = (str(__content_139842944183280) if (__content_139842944183280 is __converted) else __converted)
                                    else:
                                        __content_139842944183280 = __content_139842944183280()
                if (__content_139842944183280 is not None):
                    __append(__content_139842944183280)
                ____index_139842927838928 -= 1
                if (____index_139842927838928 > 0):
                    __append('')
            if (__backup_variation_num_139842944902160 is __marker):
                del econtext['variation_num']
            else:
                econtext['variation_num'] = __backup_variation_num_139842944902160
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f2fb83dc3d0> name=None at 7f2fb8365f50> -> __attrs_139842927576848
            __attrs_139842927576848 = _static_139842931246032
            __backup_graphics_random_switches_139842945200672 = get('graphics_random_switches', __marker)

            # <Value 'load: graphics_random_switches.pynml' (72:46)> -> __value
            __token = 3504
            __value = ' graphics_random_switches.pynml'
            __value = __loader(__value)
            econtext['graphics_random_switches'] = __value
            __backup_macroname_139842929119680 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f2fb80b6cb0> name=None at 7f2fb8072690> -> __value
            __value = _static_139842927946928
            econtext['macroname'] = __value

            # <Value 'graphics_random_switches' (72:101)> -> __macro
            __token = 3559
            __macro = getitem('graphics_random_switches')
            __token = 3559
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139842929119680 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139842929119680
            if (__backup_graphics_random_switches_139842945200672 is __marker):
                del econtext['graphics_random_switches']
            else:
                econtext['graphics_random_switches'] = __backup_graphics_random_switches_139842945200672

            # <Interpolation value=<Substitution '\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${ship.buy_menu_width}, 22, -${int(ship.buy_menu_width / 2)}, -10, ANIM]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}\n' (72:129)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2fb805c990> -> __content_139842944183280
            __token = 3589
            __token = 3650
            __content_139842944183280 = _lookup_attr(getitem('ship'), 'id')
            __content_139842944183280 = __quote(__content_139842944183280, '\x00', '&#0;', None, None)
            __token = 3747
            __content_139842944183280_3745 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[0]
            __content_139842944183280_3745 = __quote(__content_139842944183280_3745, '\x00', '&#0;', None, None)
            __token = 3774
            __content_139842944183280_3772 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[1]
            __content_139842944183280_3772 = __quote(__content_139842944183280_3772, '\x00', '&#0;', None, None)
            __token = 3801
            __content_139842944183280_3799 = _lookup_attr(getitem('ship'), 'buy_menu_width')
            __content_139842944183280_3799 = __quote(__content_139842944183280_3799, '\x00', '&#0;', None, None)
            __token = 3830
            __content_139842944183280_3828 = int((_lookup_attr(getitem('ship'), 'buy_menu_width') / 2))
            __content_139842944183280_3828 = __quote(__content_139842944183280_3828, '\x00', '&#0;', None, None)
            __token = 3887
            __content_139842944183280_3885 = _lookup_attr(getitem('ship'), 'id')
            __content_139842944183280_3885 = __quote(__content_139842944183280_3885, '\x00', '&#0;', None, None)
            __token = 3925
            __content_139842944183280_3923 = _lookup_attr(getitem('ship'), 'id')
            __content_139842944183280_3923 = __quote(__content_139842944183280_3923, '\x00', '&#0;', None, None)
            __token = 3976
            __content_139842944183280_3974 = _lookup_attr(getitem('ship'), 'id')
            __content_139842944183280_3974 = __quote(__content_139842944183280_3974, '\x00', '&#0;', None, None)
            __token = 4004
            __content_139842944183280_4002 = _lookup_attr(getitem('ship'), 'id')
            __content_139842944183280_4002 = __quote(__content_139842944183280_4002, '\x00', '&#0;', None, None)
            __token = 4052
            __content_139842944183280_4050 = _lookup_attr(getitem('ship'), 'id')
            __content_139842944183280_4050 = __quote(__content_139842944183280_4050, '\x00', '&#0;', None, None)
            __token = 4106
            __content_139842944183280_4104 = _lookup_attr(getitem('ship'), 'id')
            __content_139842944183280_4104 = __quote(__content_139842944183280_4104, '\x00', '&#0;', None, None)
            __token = 4141
            __content_139842944183280_4139 = _lookup_attr(getitem('ship'), 'render_speed_switches')()
            __content_139842944183280_4139 = __quote(__content_139842944183280_4139, '\x00', '&#0;', None, None)
            __token = 4174
            __content_139842944183280_4172 = _lookup_attr(getitem('ship'), 'render_cargo_capacity')()
            __content_139842944183280_4172 = __quote(__content_139842944183280_4172, '\x00', '&#0;', None, None)
            __token = 4207
            __content_139842944183280_4205 = _lookup_attr(getitem('ship'), 'render_properties')()
            __content_139842944183280_4205 = __quote(__content_139842944183280_4205, '\x00', '&#0;', None, None)
            __content_139842944183280 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_', (__content_139842944183280 if (__content_139842944183280 is not None) else ''), '() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [', (__content_139842944183280_3745 if (__content_139842944183280_3745 is not None) else ''), ', ', (__content_139842944183280_3772 if (__content_139842944183280_3772 is not None) else ''), ', ', (__content_139842944183280_3799 if (__content_139842944183280_3799 is not None) else ''), ', 22, -', (__content_139842944183280_3828 if (__content_139842944183280_3828 is not None) else ''), ', -10, ANIM]\n}\n\nspriteset(', (__content_139842944183280_3885 if (__content_139842944183280_3885 is not None) else ''), '_ss_purchase, "src/graphics/', (__content_139842944183280_3923 if (__content_139842944183280_3923 is not None) else ''), '_0.png") {\n  spriteset_template_purchase_', (__content_139842944183280_3974 if (__content_139842944183280_3974 is not None) else ''), '()\n}\n\nspritegroup ', (__content_139842944183280_4002 if (__content_139842944183280_4002 is not None) else ''), '_sg_purchase {\n    loaded:  [\n        ', (__content_139842944183280_4050 if (__content_139842944183280_4050 is not None) else ''), '_ss_purchase,\n    ];\n    loading: [\n        ', (__content_139842944183280_4104 if (__content_139842944183280_4104 is not None) else ''), '_ss_purchase,\n    ];\n}\n\n\n', (__content_139842944183280_4139 if (__content_139842944183280_4139 is not None) else ''), '\n\n', (__content_139842944183280_4172 if (__content_139842944183280_4172 is not None) else ''), '\n\n', (__content_139842944183280_4205 if (__content_139842944183280_4205 is not None) else ''), '\n', ))
            if (__content_139842944183280 is None):
                pass
            else:
                if (__content_139842944183280 is None):
                    __content_139842944183280 = None
                else:
                    __tt = type(__content_139842944183280)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139842944183280 = str(__content_139842944183280)
                    else:
                        if (__tt is bytes):
                            __content_139842944183280 = decode(__content_139842944183280)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139842944183280 = __content_139842944183280.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139842944183280)
                                    __content_139842944183280 = (str(__content_139842944183280) if (__content_139842944183280 is __converted) else __converted)
                                else:
                                    __content_139842944183280 = __content_139842944183280()
            if (__content_139842944183280 is not None):
                __append(__content_139842944183280)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }