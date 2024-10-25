# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/docs_templates/translations.pt'

__tokens = {36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque

_static_140681727206608 = {'class': 'btn btn-primary btn-large', 'href': 'https://translator.openttdcoop.org/project/fish', }
_static_140681727203296 = {'href': 'https://translator.openttdcoop.org/project/fish', }
_static_140681727200080 = 'load:main_template.pt'
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

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726142352
            __attrs_140681726142352 = _static_140681730573168
            __backup_macroname_140681726099200 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7ff304604b50> name=None at 7ff304501dd0> -> __value
            __value = _static_140681727200080
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728992400
                __attrs_140681728992400 = _static_140681730573168

                # <div ... (2:0)
                # --------------------------------------------------------
                __append('<div>\n    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728984528
                __attrs_140681728984528 = _static_140681730573168

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div>\n        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728996112
                __attrs_140681728996112 = _static_140681730573168

                # <h2 ... (4:8)
                # --------------------------------------------------------
                __append('<h2>Help Translate Squid Ate FISH</h2>\n        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728986960
                __attrs_140681728986960 = _static_140681730573168

                # <p ... (5:8)
                # --------------------------------------------------------
                __append('<p>Squid Ate FISH has already been translated into multiple languages, and more translations are always welcome.</p>\n        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728992080
                __attrs_140681728992080 = _static_140681730573168

                # <p ... (6:8)
                # --------------------------------------------------------
                __append('<p>Translations can be added, checked and updated using the ')

                # <Static value=<ast.Dict object at 0x7ff3046057e0> name=None at 7ff3047b9550> -> __attrs_140681728999312
                __attrs_140681728999312 = _static_140681727203296

                # <a ... (6:68)
                # --------------------------------------------------------
                __append('<a href="https://translator.openttdcoop.org/project/fish">web translator</a>.</p>\n        ')

                # <Static value=<ast.Dict object at 0x7ff3046064d0> name=None at 7ff3047ba6d0> -> __attrs_140681726009360
                __attrs_140681726009360 = _static_140681727206608

                # <a ... (7:8)
                # --------------------------------------------------------
                __append('<a class="btn btn-primary btn-large" href="https://translator.openttdcoop.org/project/fish">Web Translator</a>\n        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726013264
                __attrs_140681726013264 = _static_140681730573168

                # <br ... (8:8)
                # --------------------------------------------------------
                __append('<br />')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726016144
                __attrs_140681726016144 = _static_140681730573168

                # <br ... (8:14)
                # --------------------------------------------------------
                __append('<br />\n    </div>\n</div>')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'load:main_template.pt' (1:36)> -> __macro
            __token = 36
            __macro = 'main_template.pt'
            __macro = __loader(__macro)
            __token = 36
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140681726099200 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140681726099200
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }