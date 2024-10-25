# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/docs_templates/markdown_wrapper.pt'

__tokens = {153: ('${structure: content}', 7, 4), 155: ('structure: content', 7, 6), 166: ('content', 7, 17), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from chameleon.utils import Markup as _Markup
from collections import deque as _deque

_static_140681729037488 = {'class': 'span12', }
_static_140681729036192 = 'load:main_template.pt'
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

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681725491472
            __attrs_140681725491472 = _static_140681730573168
            __backup_macroname_140681725477888 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7ff3047c4fa0> name=None at 7ff304463690> -> __value
            __value = _static_140681729036192
            econtext['macroname'] = __value

            def __fill_sidebar_nav(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681725484304
                __attrs_140681725484304 = _static_140681730573168

                # <div ... (3:0)
                # --------------------------------------------------------
                __append('<div>\n</div>')
            _slots = econtext['__slot_sidebar_nav'] = _deque((__fill_sidebar_nav, ))

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7ff3047c54b0> name=None at 7ff304463450> -> __attrs_140681725478096
                __attrs_140681725478096 = _static_140681729037488

                # <div ... (6:0)
                # --------------------------------------------------------
                __append('<div class="span12">')

                # <Interpolation value=<Substitution '\n    ${structure: content}\n' (6:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304461450> -> __content_140681743329328
                __token = 153
                __token = 155
                __token = 166
                __content_140681743329328 = getitem('content')
                __content_140681743329328 = _Markup(__content_140681743329328)
                __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                __content_140681743329328 = ('%s%s%s' % ('\n    ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), '\n', ))
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
                __append('</div>')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'load:main_template.pt' (1:36)> -> __macro
            __token = 36
            __macro = 'main_template.pt'
            __macro = __loader(__macro)
            __token = 36
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140681725477888 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140681725477888
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }