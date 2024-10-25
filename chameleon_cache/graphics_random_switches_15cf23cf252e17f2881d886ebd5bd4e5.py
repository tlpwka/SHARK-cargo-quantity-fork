# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/templates/graphics_random_switches.pynml'

__tokens = {53: ('ship.get_reduced_set_of_variant_dates()[:-1]', 1, 53), 104: ('random_switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_random_${year}) {', 2, 4), 139: ('ship.id', 2, 39), 173: ('year', 2, 73), 244: ('ship.get_variants_available_for_specific_year(year)', 3, 62), 310: ('1: return ${ship.id}_switch_graphics_${variation_num};', 4, 12), 322: ('ship.id', 4, 24), 349: ('variation_num', 4, 51), 457: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, build_year) {', 10, 0), 485: ('ship.id', 10, 28), 584: ('ship.get_nml_random_switch_fragments_for_model_variants()', 11, 59), 652: ('${nml_fragment};', 12, 8), 654: ('nml_fragment', 12, 10), 713: ('return ${ship.id}_switch_graphics_random_0;\n}', 14, 4), 722: ('ship.id', 14, 13)}

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

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726559696
            __attrs_140681726559696 = _static_140681730573168
            __backup_year_140681727853472 = get('year', __marker)

            # <Value 'ship.get_reduced_set_of_variant_dates()[:-1]' (1:53)> -> __iterator
            __token = 53
            __iterator = _lookup_attr(getitem('ship'), 'get_reduced_set_of_variant_dates')()[:- 1]
            (__iterator, ____index_140681726562384, ) = getitem('repeat')('year', __iterator)
            econtext['year'] = None
            for __item in __iterator:
                econtext['year'] = __item

                # <Interpolation value=<Substitution '\n    random_switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_random_${year}) {\n        ' (1:99)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304569550> -> __content_140681743329328
                __token = 104
                __token = 139
                __content_140681743329328 = _lookup_attr(getitem('ship'), 'id')
                __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                __token = 173
                __content_140681743329328_171 = getitem('year')
                __content_140681743329328_171 = __quote(__content_140681743329328_171, '\x00', '&#0;', None, None)
                __content_140681743329328 = ('%s%s%s%s%s' % ('\n    random_switch (FEAT_SHIPS, SELF, ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), '_switch_graphics_random_', (__content_140681743329328_171 if (__content_140681743329328_171 is not None) else ''), ') {\n        ', ))
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

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726561872
                __attrs_140681726561872 = _static_140681730573168
                __backup_variation_num_140681727953120 = get('variation_num', __marker)

                # <Value 'ship.get_variants_available_for_specific_year(year)' (3:62)> -> __iterator
                __token = 244
                __iterator = _lookup_attr(getitem('ship'), 'get_variants_available_for_specific_year')(getitem('year'))
                (__iterator, ____index_140681726562768, ) = getitem('repeat')('variation_num', __iterator)
                econtext['variation_num'] = None
                for __item in __iterator:
                    econtext['variation_num'] = __item

                    # <Interpolation value=<Substitution '\n            1: return ${ship.id}_switch_graphics_${variation_num};\n        ' (3:115)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304568d90> -> __content_140681743329328
                    __token = 310
                    __token = 322
                    __content_140681743329328 = _lookup_attr(getitem('ship'), 'id')
                    __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                    __token = 349
                    __content_140681743329328_347 = getitem('variation_num')
                    __content_140681743329328_347 = __quote(__content_140681743329328_347, '\x00', '&#0;', None, None)
                    __content_140681743329328 = ('%s%s%s%s%s' % ('\n            1: return ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), '_switch_graphics_', (__content_140681743329328_347 if (__content_140681743329328_347 is not None) else ''), ';\n        ', ))
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
                    ____index_140681726562768 -= 1
                    if (____index_140681726562768 > 0):
                        __append('')
                if (__backup_variation_num_140681727953120 is __marker):
                    del econtext['variation_num']
                else:
                    econtext['variation_num'] = __backup_variation_num_140681727953120
                __append('\n    }\n')
                ____index_140681726562384 -= 1
                if (____index_140681726562384 > 0):
                    __append('')
            if (__backup_year_140681727853472 is __marker):
                del econtext['year']
            else:
                econtext['year'] = __backup_year_140681727853472

            # <Interpolation value=<Substitution '\n\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, build_year) {\n    ' (7:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304568710> -> __content_140681743329328
            __token = 457
            __token = 485
            __content_140681743329328 = _lookup_attr(getitem('ship'), 'id')
            __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
            __content_140681743329328 = ('%s%s%s' % ('\n\n\nswitch (FEAT_SHIPS, SELF, ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), '_switch_graphics, build_year) {\n    ', ))
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

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726562832
            __attrs_140681726562832 = _static_140681730573168
            __backup_nml_fragment_140681728069344 = get('nml_fragment', __marker)

            # <Value 'ship.get_nml_random_switch_fragments_for_model_variants()' (11:59)> -> __iterator
            __token = 584
            __iterator = _lookup_attr(getitem('ship'), 'get_nml_random_switch_fragments_for_model_variants')()
            (__iterator, ____index_140681726563280, ) = getitem('repeat')('nml_fragment', __iterator)
            econtext['nml_fragment'] = None
            for __item in __iterator:
                econtext['nml_fragment'] = __item

                # <Interpolation value=<Substitution '\n        ${nml_fragment};\n    ' (11:118)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304569ed0> -> __content_140681743329328
                __token = 652
                __token = 654
                __content_140681743329328 = getitem('nml_fragment')
                __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                __content_140681743329328 = ('%s%s%s' % ('\n        ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), ';\n    ', ))
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
                ____index_140681726563280 -= 1
                if (____index_140681726563280 > 0):
                    __append('')
            if (__backup_nml_fragment_140681728069344 is __marker):
                del econtext['nml_fragment']
            else:
                econtext['nml_fragment'] = __backup_nml_fragment_140681728069344

            # <Interpolation value=<Substitution '\n    return ${ship.id}_switch_graphics_random_0;\n}\n' (13:39)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304569250> -> __content_140681743329328
            __token = 713
            __token = 722
            __content_140681743329328 = _lookup_attr(getitem('ship'), 'id')
            __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
            __content_140681743329328 = ('%s%s%s' % ('\n    return ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), '_switch_graphics_random_0;\n}\n', ))
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