# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/templates/debug_info.pynml'

__tokens = {0: ('// -- begin ${ship.title} --', 1, 0), 14: ('ship.title', 1, 14)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

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

            # <Interpolation value=<Substitution '// -- begin ${ship.title} -- ' (1:0)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304566450> -> __content_140681743329328
            __token = 0
            __token = 14
            __content_140681743329328 = _lookup_attr(getitem('ship'), 'title')
            __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
            __content_140681743329328 = ('%s%s%s' % ('// -- begin ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), ' -- ', ))
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
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }