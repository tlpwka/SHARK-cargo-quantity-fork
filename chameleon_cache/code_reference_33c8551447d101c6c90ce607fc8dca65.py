# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/docs_templates/code_reference.pt'

__tokens = {157: ('${len(ships)} ships', 5, 11), 159: ('len(ships)', 5, 13), 237: ('doc_helper.get_ships_by_subclass()', 7, 41), 333: ('doc_helper.get_props_to_print_in_code_reference(subclass)', 8, 59), 413: ('${subclass.__name__}', 9, 20), 415: ('subclass.__name__', 9, 22), 482: ('${subclass.__doc__}', 10, 19), 484: ('subclass.__doc__', 10, 21), 720: ('props_to_print[subclass]', 14, 51), 833: ('${prop}', 15, 86), 835: ('prop', 15, 88), 1022: ('doc_helper.get_ships_by_subclass()[subclass]', 20, 48), 1163: ('props_to_print[subclass]', 22, 61), 1230: ('${props_to_print[ship][prop_name]}', 23, 40), 1232: ('props_to_print[ship][prop_name]', 23, 42), 1372: ('dir(ship)', 25, 57), 2016: ('sorted(ships, key=doc_helper.get_base_numeric_id)', 45, 46), 2121: ('${vehicle.numeric_id}', 47, 28), 2123: ('vehicle.numeric_id', 47, 30), 2176: ('${vehicle.id}', 48, 28), 2178: ('vehicle.id', 48, 30), 2223: ('${vehicle.title}', 49, 28), 2225: ('vehicle.title', 49, 30), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140681725738960 = {'class': 'table table-striped table-condensed table-bordered', }
_static_140681725732192 = {'style': 'background-color:#eee; vertical-align:top', }
_static_140681725735984 = {'style': 'font-size:84%;', 'class': 'table table-striped table-condensed table-bordered', }
_static_140681725738528 = {'class': 'span12', }
_static_140681727482880 = 'load:main_template.pt'
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

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728267600
            __attrs_140681728267600 = _static_140681730573168
            __backup_macroname_140681728270784 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7ff304649c00> name=None at 7ff30470a810> -> __value
            __value = _static_140681727482880
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726034832
                __attrs_140681726034832 = _static_140681730573168

                # <div ... (2:0)
                # --------------------------------------------------------
                __append('<div>\n    ')

                # <Static value=<ast.Dict object at 0x7ff30449fe20> name=None at 7ff304907050> -> __attrs_140681726042832
                __attrs_140681726042832 = _static_140681725738528

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div class="span12">\n        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726146128
                __attrs_140681726146128 = _static_140681730573168

                # <h2 ... (4:8)
                # --------------------------------------------------------
                __append('<h2>Code Reference</h2>\n        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681725905552
                __attrs_140681725905552 = _static_140681730573168

                # <p ... (5:8)
                # --------------------------------------------------------
                __append('<p>')

                # <Interpolation value=<Substitution '${len(ships)} ships' (5:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304507950> -> __content_140681743329328
                __token = 157
                __token = 159
                __content_140681743329328 = len(getitem('ships'))
                __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                __content_140681743329328 = ('%s%s' % ((__content_140681743329328 if (__content_140681743329328 is not None) else ''), ' ships', ))
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
                __append('</p>\n        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726158096
                __attrs_140681726158096 = _static_140681730573168

                # <hr ... (6:8)
                # --------------------------------------------------------
                __append('<hr />\n        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726150096
                __attrs_140681726150096 = _static_140681730573168
                __backup_subclass_140681728062032 = get('subclass', __marker)

                # <Value 'doc_helper.get_ships_by_subclass()' (7:41)> -> __iterator
                __token = 237
                __iterator = _lookup_attr(getitem('doc_helper'), 'get_ships_by_subclass')()
                (__iterator, ____index_140681726150288, ) = getitem('repeat')('subclass', __iterator)
                econtext['subclass'] = None
                for __item in __iterator:
                    econtext['subclass'] = __item
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726153872
                    __attrs_140681726153872 = _static_140681730573168
                    __backup_props_to_print_140681727641632 = get('props_to_print', __marker)

                    # <Value 'doc_helper.get_props_to_print_in_code_reference(subclass)' (8:59)> -> __value
                    __token = 333
                    __value = _lookup_attr(getitem('doc_helper'), 'get_props_to_print_in_code_reference')(getitem('subclass'))
                    econtext['props_to_print'] = __value
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726154768
                    __attrs_140681726154768 = _static_140681730573168

                    # <h4 ... (9:16)
                    # --------------------------------------------------------
                    __append('<h4>')

                    # <Interpolation value=<Substitution '${subclass.__name__} ' (9:20)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304506bd0> -> __content_140681743329328
                    __token = 413
                    __token = 415
                    __content_140681743329328 = _lookup_attr(getitem('subclass'), '__name__')
                    __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                    __content_140681743329328 = ('%s%s' % ((__content_140681743329328 if (__content_140681743329328 is not None) else ''), ' ', ))
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

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726154896
                    __attrs_140681726154896 = _static_140681730573168

                    # <small ... (9:41)
                    # --------------------------------------------------------
                    __append('<small>Subclass</small></h4>\n                ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726163088
                    __attrs_140681726163088 = _static_140681730573168

                    # <p ... (10:16)
                    # --------------------------------------------------------
                    __append('<p>')

                    # <Interpolation value=<Substitution '${subclass.__doc__}' (10:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3045072d0> -> __content_140681743329328
                    __token = 482
                    __token = 484
                    __content_140681743329328 = _lookup_attr(getitem('subclass'), '__doc__')
                    __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                    __content_140681743329328 = __content_140681743329328
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
                    __append('</p>\n                ')

                    # <Static value=<ast.Dict object at 0x7ff30449f430> name=None at 7ff304507610> -> __attrs_140681726156368
                    __attrs_140681726156368 = _static_140681725735984

                    # <table ... (11:16)
                    # --------------------------------------------------------
                    __append('<table style="font-size:84%;" class="table table-striped table-condensed table-bordered">\n                    ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681729652752
                    __attrs_140681729652752 = _static_140681730573168

                    # <thead ... (12:20)
                    # --------------------------------------------------------
                    __append('<thead>\n                        ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728997264
                    __attrs_140681728997264 = _static_140681730573168

                    # <tr ... (13:24)
                    # --------------------------------------------------------
                    __append('<tr>\n                           ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728997968
                    __attrs_140681728997968 = _static_140681730573168
                    __backup_prop_140681728062704 = get('prop', __marker)

                    # <Value 'props_to_print[subclass]' (14:51)> -> __iterator
                    __token = 720
                    __iterator = getitem('props_to_print')[getitem('subclass')]
                    (__iterator, ____index_140681728994896, ) = getitem('repeat')('prop', __iterator)
                    econtext['prop'] = None
                    for __item in __iterator:
                        econtext['prop'] = __item
                        __append('\n                                ')

                        # <Static value=<ast.Dict object at 0x7ff30449e560> name=None at 7ff3047bbd10> -> __attrs_140681728987216
                        __attrs_140681728987216 = _static_140681725732192

                        # <th ... (15:32)
                        # --------------------------------------------------------
                        __append('<th style="background-color:#eee; vertical-align:top">')

                        # <Interpolation value=<Substitution '${prop}' (15:86)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3047b8a50> -> __content_140681743329328
                        __token = 833
                        __token = 835
                        __content_140681743329328 = getitem('prop')
                        __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                        __content_140681743329328 = __content_140681743329328
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
                        __append('</th>\n                            ')
                        ____index_140681728994896 -= 1
                        if (____index_140681728994896 > 0):
                            __append('')
                    if (__backup_prop_140681728062704 is __marker):
                        del econtext['prop']
                    else:
                        econtext['prop'] = __backup_prop_140681728062704
                    __append('\n                        </tr>\n                    </thead>\n                    ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728997328
                    __attrs_140681728997328 = _static_140681730573168

                    # <tbody ... (19:20)
                    # --------------------------------------------------------
                    __append('<tbody>\n                        ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728994448
                    __attrs_140681728994448 = _static_140681730573168
                    __backup_ship_140681728054160 = get('ship', __marker)

                    # <Value 'doc_helper.get_ships_by_subclass()[subclass]' (20:48)> -> __iterator
                    __token = 1022
                    __iterator = _lookup_attr(getitem('doc_helper'), 'get_ships_by_subclass')()[getitem('subclass')]
                    (__iterator, ____index_140681728998864, ) = getitem('repeat')('ship', __iterator)
                    econtext['ship'] = None
                    for __item in __iterator:
                        econtext['ship'] = __item
                        __append('\n                            ')

                        # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728991440
                        __attrs_140681728991440 = _static_140681730573168

                        # <tr ... (21:28)
                        # --------------------------------------------------------
                        __append('<tr>\n                                ')

                        # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726169424
                        __attrs_140681726169424 = _static_140681730573168
                        __backup_prop_name_140681728062176 = get('prop_name', __marker)

                        # <Value 'props_to_print[subclass]' (22:61)> -> __iterator
                        __token = 1163
                        __iterator = getitem('props_to_print')[getitem('subclass')]
                        (__iterator, ____index_140681726167824, ) = getitem('repeat')('prop_name', __iterator)
                        econtext['prop_name'] = None
                        for __item in __iterator:
                            econtext['prop_name'] = __item
                            __append('\n                                    ')

                            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726176784
                            __attrs_140681726176784 = _static_140681730573168

                            # <td ... (23:36)
                            # --------------------------------------------------------
                            __append('<td>')

                            # <Interpolation value=<Substitution '${props_to_print[ship][prop_name]}' (23:40)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff30450b710> -> __content_140681743329328
                            __token = 1230
                            __token = 1232
                            __content_140681743329328 = getitem('props_to_print')[getitem('ship')][getitem('prop_name')]
                            __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                            __content_140681743329328 = __content_140681743329328
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
                            __append('</td>\n                                ')
                            ____index_140681726167824 -= 1
                            if (____index_140681726167824 > 0):
                                __append('')
                        if (__backup_prop_name_140681728062176 is __marker):
                            del econtext['prop_name']
                        else:
                            econtext['prop_name'] = __backup_prop_name_140681728062176
                        __append('\n                                ')

                        # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726178896
                        __attrs_140681726178896 = _static_140681730573168
                        __backup_prop_140681726868592 = get('prop', __marker)

                        # <Value 'dir(ship)' (25:57)> -> __iterator
                        __token = 1372
                        __iterator = get('dir', dir)(getitem('ship'))
                        (__iterator, ____index_140681726175184, ) = getitem('repeat')('prop', __iterator)
                        econtext['prop'] = None
                        for __item in __iterator:
                            econtext['prop'] = __item
                            __append('\n                                    \n                                ')
                            ____index_140681726175184 -= 1
                            if (____index_140681726175184 > 0):
                                __append('')
                        if (__backup_prop_140681726868592 is __marker):
                            del econtext['prop']
                        else:
                            econtext['prop'] = __backup_prop_140681726868592
                        __append('\n                            </tr>\n                        ')
                        ____index_140681728998864 -= 1
                        if (____index_140681728998864 > 0):
                            __append('')
                    if (__backup_ship_140681728054160 is __marker):
                        del econtext['ship']
                    else:
                        econtext['ship'] = __backup_ship_140681728054160
                    __append('\n                    </tbody>\n                </table>\n                ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726169616
                    __attrs_140681726169616 = _static_140681730573168

                    # <br ... (32:16)
                    # --------------------------------------------------------
                    __append('<br />\n            ')
                    if (__backup_props_to_print_140681727641632 is __marker):
                        del econtext['props_to_print']
                    else:
                        econtext['props_to_print'] = __backup_props_to_print_140681727641632
                    __append('\n        ')
                    ____index_140681726150288 -= 1
                    if (____index_140681726150288 > 0):
                        __append('')
                if (__backup_subclass_140681728062032 is __marker):
                    del econtext['subclass']
                else:
                    econtext['subclass'] = __backup_subclass_140681728062032
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726162320
                __attrs_140681726162320 = _static_140681730573168

                # <hr ... (36:8)
                # --------------------------------------------------------
                __append('<hr />\n        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726126416
                __attrs_140681726126416 = _static_140681730573168

                # <h3 ... (37:8)
                # --------------------------------------------------------
                __append('<h3>Numeric IDs</h3>\n        ')

                # <Static value=<ast.Dict object at 0x7ff30449ffd0> name=None at 7ff3044fc1d0> -> __attrs_140681730306512
                __attrs_140681730306512 = _static_140681725738960

                # <table ... (38:8)
                # --------------------------------------------------------
                __append('<table class="table table-striped table-condensed table-bordered">\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726203408
                __attrs_140681726203408 = _static_140681730573168

                # <thead ... (39:12)
                # --------------------------------------------------------
                __append('<thead>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726208784
                __attrs_140681726208784 = _static_140681730573168

                # <th ... (40:16)
                # --------------------------------------------------------
                __append('<th>Numeric ID</th>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726211344
                __attrs_140681726211344 = _static_140681730573168

                # <th ... (41:16)
                # --------------------------------------------------------
                __append('<th>ID</th>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726212880
                __attrs_140681726212880 = _static_140681730573168

                # <th ... (42:16)
                # --------------------------------------------------------
                __append('<th>Title</th>\n            </thead>\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726208656
                __attrs_140681726208656 = _static_140681730573168

                # <tbody ... (44:12)
                # --------------------------------------------------------
                __append('<tbody>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726201552
                __attrs_140681726201552 = _static_140681730573168
                __backup_vehicle_140681728050608 = get('vehicle', __marker)

                # <Value 'sorted(ships, key=doc_helper.get_base_numeric_id)' (45:46)> -> __iterator
                __token = 2016
                __iterator = get('sorted', sorted)(getitem('ships'), key=_lookup_attr(getitem('doc_helper'), 'get_base_numeric_id'))
                (__iterator, ____index_140681726007184, ) = getitem('repeat')('vehicle', __iterator)
                econtext['vehicle'] = None
                for __item in __iterator:
                    econtext['vehicle'] = __item
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726015568
                    __attrs_140681726015568 = _static_140681730573168

                    # <tr ... (46:20)
                    # --------------------------------------------------------
                    __append('<tr>\n                        ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726008464
                    __attrs_140681726008464 = _static_140681730573168

                    # <td ... (47:24)
                    # --------------------------------------------------------
                    __append('<td>')

                    # <Interpolation value=<Substitution '${vehicle.numeric_id}' (47:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3044e2a10> -> __content_140681743329328
                    __token = 2121
                    __token = 2123
                    __content_140681743329328 = _lookup_attr(getitem('vehicle'), 'numeric_id')
                    __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                    __content_140681743329328 = __content_140681743329328
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
                    __append('</td>\n                        ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726015760
                    __attrs_140681726015760 = _static_140681730573168

                    # <td ... (48:24)
                    # --------------------------------------------------------
                    __append('<td>')

                    # <Interpolation value=<Substitution '${vehicle.id}' (48:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3044e0b50> -> __content_140681743329328
                    __token = 2176
                    __token = 2178
                    __content_140681743329328 = _lookup_attr(getitem('vehicle'), 'id')
                    __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                    __content_140681743329328 = __content_140681743329328
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
                    __append('</td>\n                        ')

                    # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726010320
                    __attrs_140681726010320 = _static_140681730573168

                    # <td ... (49:24)
                    # --------------------------------------------------------
                    __append('<td>')

                    # <Interpolation value=<Substitution '${vehicle.title}' (49:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3044e1810> -> __content_140681743329328
                    __token = 2223
                    __token = 2225
                    __content_140681743329328 = _lookup_attr(getitem('vehicle'), 'title')
                    __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                    __content_140681743329328 = __content_140681743329328
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
                    __append('</td>\n                    </tr>\n                ')
                    ____index_140681726007184 -= 1
                    if (____index_140681726007184 > 0):
                        __append('')
                if (__backup_vehicle_140681728050608 is __marker):
                    del econtext['vehicle']
                else:
                    econtext['vehicle'] = __backup_vehicle_140681728050608
                __append('\n            </tbody>\n        </table>\n    </div>\n\n</div>')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'load:main_template.pt' (1:36)> -> __macro
            __token = 36
            __macro = 'main_template.pt'
            __macro = __loader(__macro)
            __token = 36
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140681728270784 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140681728270784
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }