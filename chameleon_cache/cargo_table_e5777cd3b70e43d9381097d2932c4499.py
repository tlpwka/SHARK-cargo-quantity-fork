# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/templates/cargo_table.pynml'

__tokens = {203: ('global_constants.cargo_labels', 8, 41), 239: ('${cargo},', 9, 4), 241: ('cargo', 9, 6)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

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
            __append('/*\n * ********************************************\n * Define cargo translation table and refits\n * ********************************************\n */\n\ncargotable {\n    ')

            # <Static value=<ast.Dict object at 0x7f2fb83dc3d0> name=None at 7f2fb8365f50> -> __attrs_139842931330704
            __attrs_139842931330704 = _static_139842931246032
            __backup_cargo_139842946219168 = get('cargo', __marker)

            # <Value 'global_constants.cargo_labels' (8:41)> -> __iterator
            __token = 203
            __iterator = _lookup_attr(getitem('global_constants'), 'cargo_labels')
            (__iterator, ____index_139842931332048, ) = getitem('repeat')('cargo', __iterator)
            econtext['cargo'] = None
            for __item in __iterator:
                econtext['cargo'] = __item

                # <Interpolation value=<Substitution '\n    ${cargo},\n    ' (8:72)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f2fb83f2c90> -> __content_139842944183280
                __token = 239
                __token = 241
                __content_139842944183280 = getitem('cargo')
                __content_139842944183280 = __quote(__content_139842944183280, '\x00', '&#0;', None, None)
                __content_139842944183280 = ('%s%s%s' % ('\n    ', (__content_139842944183280 if (__content_139842944183280 is not None) else ''), ',\n    ', ))
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
                ____index_139842931332048 -= 1
                if (____index_139842931332048 > 0):
                    __append('')
            if (__backup_cargo_139842946219168 is __marker):
                del econtext['cargo']
            else:
                econtext['cargo'] = __backup_cargo_139842946219168
            __append('\n}\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }