# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/templates/capacity_not_refittable.pynml'

__tokens = {0: ('// -- capacity determined according to specific labels that might need to be handled, and otherwise cargo class -- //\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_cargo_capacity_classes, cargo_classes) {\n    bitmask(CC_PASSENGERS): return ${ship.capacity_pax};\n    bitmask(CC_MAIL): return ${ship.capacity_mail};\n    return ${ship.capacity_freight};\n}\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_cargo_capacity, cargo_type_in_veh) {', 1, 0), 146: ('ship.id', 2, 28), 240: ('ship.capacity_pax', 3, 37), 291: ('ship.capacity_mail', 4, 31), 325: ('ship.capacity_freight', 5, 13), 379: ('ship.id', 7, 28), 461: ("ship.str_type_info.lower()=='trawler'", 8, 29), 500: ('FISH: return ${ship.capacity_fish_holds};', 8, 68), 515: ('ship.capacity_fish_holds', 8, 83), 561: ('${ship.id}_switch_cargo_capacity_classes;\n}\n\n// -- handle subtype strings, used to aid players understand auto-refitting -- //\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_cargo_subtype_text, cargo_subtype) {\n    return CB_RESULT_NO_TEXT;\n}', 9, 4), 563: ('ship.id', 9, 6), 716: ('ship.id', 13, 28)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140681730573168 = {}

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

            # <Interpolation value=<Substitution '// -- capacity determined according to specific labels that might need to be handled, and otherwise cargo class -- //\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_cargo_capacity_classes, cargo_classes) {\n    bitmask(CC_PASSENGERS): return ${ship.capacity_pax};\n    bitmask(CC_MAIL): return ${ship.capacity_mail};\n    return ${ship.capacity_freight};\n}\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_cargo_capacity, cargo_type_in_veh) {\n    ' (1:0)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff30459cd50> -> __content_140681743329328
            __token = 0
            __token = 146
            __content_140681743329328 = _lookup_attr(getitem('ship'), 'id')
            __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
            __token = 240
            __content_140681743329328_238 = _lookup_attr(getitem('ship'), 'capacity_pax')
            __content_140681743329328_238 = __quote(__content_140681743329328_238, '\x00', '&#0;', None, None)
            __token = 291
            __content_140681743329328_289 = _lookup_attr(getitem('ship'), 'capacity_mail')
            __content_140681743329328_289 = __quote(__content_140681743329328_289, '\x00', '&#0;', None, None)
            __token = 325
            __content_140681743329328_323 = _lookup_attr(getitem('ship'), 'capacity_freight')
            __content_140681743329328_323 = __quote(__content_140681743329328_323, '\x00', '&#0;', None, None)
            __token = 379
            __content_140681743329328_377 = _lookup_attr(getitem('ship'), 'id')
            __content_140681743329328_377 = __quote(__content_140681743329328_377, '\x00', '&#0;', None, None)
            __content_140681743329328 = ('%s%s%s%s%s%s%s%s%s%s%s' % ('// -- capacity determined according to specific labels that might need to be handled, and otherwise cargo class -- //\nswitch (FEAT_SHIPS, SELF, ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), '_switch_cargo_capacity_classes, cargo_classes) {\n    bitmask(CC_PASSENGERS): return ', (__content_140681743329328_238 if (__content_140681743329328_238 is not None) else ''), ';\n    bitmask(CC_MAIL): return ', (__content_140681743329328_289 if (__content_140681743329328_289 is not None) else ''), ';\n    return ', (__content_140681743329328_323 if (__content_140681743329328_323 is not None) else ''), ';\n}\nswitch (FEAT_SHIPS, SELF, ', (__content_140681743329328_377 if (__content_140681743329328_377 is not None) else ''), '_switch_cargo_capacity, cargo_type_in_veh) {\n    ', ))
            if (__content_140681743329328 is None):
                pass
            else:
                if (__content_140681743329328 is None):
                    __content_140681743329328 = None
                else:
                    __tt = type(__content_140681743329328)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140681743329328 = str(__content_140681743329328)
                    else:
                        if (__tt is bytes):
                            __content_140681743329328 = decode(__content_140681743329328)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140681743329328 = __content_140681743329328.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140681743329328)
                                    __content_140681743329328 = (str(__content_140681743329328) if (__content_140681743329328 is __converted) else __converted)
                                else:
                                    __content_140681743329328 = __content_140681743329328()
            if (__content_140681743329328 is not None):
                __append(__content_140681743329328)

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726777744
            __attrs_140681726777744 = _static_140681730573168

            # <Value "ship.str_type_info.lower()=='trawler'" (8:29)> -> __condition
            __token = 461
            __condition = (_lookup_attr(_lookup_attr(getitem('ship'), 'str_type_info'), 'lower')() == 'trawler')
            if __condition:

                # <Interpolation value=<Substitution 'FISH: return ${ship.capacity_fish_holds};' (8:68)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304824310> -> __content_140681743329328
                __token = 500
                __token = 515
                __content_140681743329328 = _lookup_attr(getitem('ship'), 'capacity_fish_holds')
                __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                __content_140681743329328 = ('%s%s%s' % ('FISH: return ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), ';', ))
                if (__content_140681743329328 is None):
                    pass
                else:
                    if (__content_140681743329328 is None):
                        __content_140681743329328 = None
                    else:
                        __tt = type(__content_140681743329328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140681743329328 = str(__content_140681743329328)
                        else:
                            if (__tt is bytes):
                                __content_140681743329328 = decode(__content_140681743329328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140681743329328 = __content_140681743329328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140681743329328)
                                        __content_140681743329328 = (str(__content_140681743329328) if (__content_140681743329328 is __converted) else __converted)
                                    else:
                                        __content_140681743329328 = __content_140681743329328()
                if (__content_140681743329328 is not None):
                    __append(__content_140681743329328)

            # <Interpolation value=<Substitution '\n    ${ship.id}_switch_cargo_capacity_classes;\n}\n\n// -- handle subtype strings, used to aid players understand auto-refitting -- //\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_cargo_subtype_text, cargo_subtype) {\n    return CB_RESULT_NO_TEXT;\n}\n' (8:124)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff30459f550> -> __content_140681743329328
            __token = 561
            __token = 563
            __content_140681743329328 = _lookup_attr(getitem('ship'), 'id')
            __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
            __token = 716
            __content_140681743329328_714 = _lookup_attr(getitem('ship'), 'id')
            __content_140681743329328_714 = __quote(__content_140681743329328_714, '\x00', '&#0;', None, None)
            __content_140681743329328 = ('%s%s%s%s%s' % ('\n    ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), '_switch_cargo_capacity_classes;\n}\n\n// -- handle subtype strings, used to aid players understand auto-refitting -- //\nswitch (FEAT_SHIPS, SELF, ', (__content_140681743329328_714 if (__content_140681743329328_714 is not None) else ''), '_switch_cargo_subtype_text, cargo_subtype) {\n    return CB_RESULT_NO_TEXT;\n}\n', ))
            if (__content_140681743329328 is None):
                pass
            else:
                if (__content_140681743329328 is None):
                    __content_140681743329328 = None
                else:
                    __tt = type(__content_140681743329328)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140681743329328 = str(__content_140681743329328)
                    else:
                        if (__tt is bytes):
                            __content_140681743329328 = decode(__content_140681743329328)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140681743329328 = __content_140681743329328.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140681743329328)
                                    __content_140681743329328 = (str(__content_140681743329328) if (__content_140681743329328 is __converted) else __converted)
                                else:
                                    __content_140681743329328 = __content_140681743329328()
            if (__content_140681743329328 is not None):
                __append(__content_140681743329328)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }