# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/lang_templates/english.pylng'

__tokens = {135: ('ships', 4, 38), 143: ('STR_NAME_${ship.id}                                          :${ship.get_name_substr()}{STRING}', 5, 0), 154: ('ship.id', 5, 11), 207: ('ship.get_name_substr()', 5, 64)}

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
            __append('STR_GRF_NAME                                                    :SHARK 1.0\n\n\n')

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681725873296
            __attrs_140681725873296 = _static_140681730573168
            __backup_ship_140681727212080 = get('ship', __marker)

            # <Value 'ships' (4:38)> -> __iterator
            __token = 135
            __iterator = getitem('ships')
            (__iterator, ____index_140681725886032, ) = getitem('repeat')('ship', __iterator)
            econtext['ship'] = None
            for __item in __iterator:
                econtext['ship'] = __item

                # <Interpolation value=<Substitution '\nSTR_NAME_${ship.id}                                          :${ship.get_name_substr()}{STRING} ' (4:45)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3044c0c50> -> __content_140681743329328
                __token = 143
                __token = 154
                __content_140681743329328 = _lookup_attr(getitem('ship'), 'id')
                __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                __token = 207
                __content_140681743329328_205 = _lookup_attr(getitem('ship'), 'get_name_substr')()
                __content_140681743329328_205 = __quote(__content_140681743329328_205, '\x00', '&#0;', None, None)
                __content_140681743329328 = ('%s%s%s%s%s' % ('\nSTR_NAME_', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), '                                          :', (__content_140681743329328_205 if (__content_140681743329328_205 is not None) else ''), '{STRING} ', ))
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
                __append('\n')
                ____index_140681725886032 -= 1
                if (____index_140681725886032 > 0):
                    __append('')
            if (__backup_ship_140681727212080 is __marker):
                del econtext['ship']
            else:
                econtext['ship'] = __backup_ship_140681727212080
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }