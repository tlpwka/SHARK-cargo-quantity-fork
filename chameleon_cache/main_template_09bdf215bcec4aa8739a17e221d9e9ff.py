# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/docs_templates/main_template.pt'

__tokens = {1742: ("${doc_helper.get_active_nav(doc_name, 'get_started')}", 40, 27), 1744: ("doc_helper.get_active_nav(doc_name, 'get_started')", 40, 29), 1910: ("${doc_helper.get_active_nav(doc_name, 'ships')}", 43, 27), 1912: ("doc_helper.get_active_nav(doc_name, 'ships')", 43, 29), 2060: ("${doc_helper.get_active_nav(doc_name, 'code_reference')}", 46, 27), 2062: ("doc_helper.get_active_nav(doc_name, 'code_reference')", 46, 29), 2306: ("${doc_helper.get_active_nav(doc_name, 'translations')}", 51, 27), 2308: ("doc_helper.get_active_nav(doc_name, 'translations')", 51, 29), 2545: ("${metadata['dev_thread_url']}", 55, 29), 2547: ("metadata['dev_thread_url']", 55, 31)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140681727052096 = {'version': '1.0', 'encoding': 'iso-8859-1', }
_static_140681727194496 = {'style': 'margin-top:30px; text-align:center; color:#999; padding:5px; background-color:#eee; border-top:solid 1px #ddd; box-shadow: inset 0px 1px 1px #ddd', }
_static_140681730579744 = {'class': 'container', }
_static_140681727190416 = {'class': 'lead', }
_static_140681727193824 = {'style': 'font-size:48px; padding-top:30px;', }
_static_140681745300640 = {'class': 'container', }
_static_140681745299968 = {'class': 'pull-right', 'style': 'margin-top:-30px; margin-bottom:0;', 'src': "static/img/industries/'+ random_image +'.png", }
_static_140681745300832 = {'href': "ships.html#' + random_image + '", }
_static_140681730587328 = {'language': 'JavaScript', }
_static_140681730587136 = {'class': 'hero-unit subhead', }
_static_140681745300928 = {'class': 'icon-comment icon-white', }
_static_140681745299728 = {'href': "${metadata['dev_thread_url']}", }
_static_140681745295216 = {'class': 'icon-globe icon-white', }
_static_140681730588096 = {'href': 'translations.html', }
_static_140681730588192 = {'class': "${doc_helper.get_active_nav(doc_name, 'translations')}", }
_static_140681730584352 = {'class': 'nav navbar-nav pull-right', }
_static_140681730578976 = {'href': 'code_reference.html', }
_static_140681730586848 = {'class': "${doc_helper.get_active_nav(doc_name, 'code_reference')}", }
_static_140681730584256 = {'href': 'ships.html', }
_static_140681730580128 = {'class': "${doc_helper.get_active_nav(doc_name, 'ships')}", }
_static_140681730583776 = {'href': 'get_started.html', }
_static_140681730585120 = {'class': "${doc_helper.get_active_nav(doc_name, 'get_started')}", }
_static_140681730574464 = {'class': 'nav navbar-nav pull-left', }
_static_140681730586080 = {'class': 'container', }
_static_140681730580272 = {'class': 'navbar navbar-inverse navbar-static-top', 'style': 'margin-bottom:0; border-bottom:1px solid #000;', }
_static_140681730578736 = {'type': 'text/javascript', }
_static_140681730578928 = {'type': 'text/javascript', 'src': 'static/js/jquery.tablesorter.widgets.min.js', }
_static_140681730585312 = {'type': 'text/javascript', 'src': 'static/js/jquery.tablesorter.min.js', }
_static_140681730587232 = {'type': 'text/javascript', 'src': 'static/js/jquery.metadata.js', }
_static_140681730583056 = {'type': 'text/javascript', 'src': 'static/js/jquery-1.9.1.min.js', }
_static_140681730585744 = {'rel': 'stylesheet', 'href': 'static/font-awesome/css/font-awesome.min.css', }
_static_140681730584208 = {'type': 'text/css', 'href': 'static/css/style.css', 'rel': 'stylesheet', }
_static_140681743978256 = {'type': 'text/css', 'href': 'static/css/bootstrap-responsive.min.css', 'rel': 'stylesheet', }
_static_140681743978208 = {'type': 'text/css', 'href': 'static/css/bootstrap.min.css', 'rel': 'stylesheet', }
_static_140681743974608 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0', }
_static_140681736768096 = {'http-equiv': 'Content-Type', 'content': 'text/html; charset=iso-8859-1', }
_static_140681727049936 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'en', }
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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_body = econtext['__slot_body'].pop()
        except:
            __slot_body = None

        try:
            __slot_opt_page_header = econtext['__slot_opt_page_header'].pop()
        except:
            __slot_opt_page_header = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726498960
            __attrs_140681726498960 = _static_140681730573168
            __append('\n<!DOCTYPE html>\n')

            # <Static value=<ast.Dict object at 0x7ff3045e00d0> name=None at 7ff30455b750> -> __attrs_140681726004752
            __attrs_140681726004752 = _static_140681727049936

            # <html ... (4:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" lang="en">\n')

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726008720
            __attrs_140681726008720 = _static_140681730573168

            # <head ... (5:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726014800
            __attrs_140681726014800 = _static_140681730573168

            # <title ... (6:4)
            # --------------------------------------------------------
            __append('<title >Squid Ate FISH</title>\n    ')

            # <Static value=<ast.Dict object at 0x7ff304f24a60> name=None at 7ff3044e2cd0> -> __attrs_140681726017232
            __attrs_140681726017232 = _static_140681736768096

            # <meta ... (7:4)
            # --------------------------------------------------------
            __append('<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />\n\n    ')

            # <Static value=<ast.Dict object at 0x7ff3056040d0> name=None at 7ff3044e2150> -> __attrs_140681726001296
            __attrs_140681726001296 = _static_140681743974608

            # <meta ... (9:4)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    ')

            # <Static value=<ast.Dict object at 0x7ff305604ee0> name=None at 7ff3044e0150> -> __attrs_140681729220496
            __attrs_140681729220496 = _static_140681743978208

            # <link ... (10:4)
            # --------------------------------------------------------
            __append('<link type="text/css" href="static/css/bootstrap.min.css" rel="stylesheet">\n    ')

            # <Static value=<ast.Dict object at 0x7ff305604f10> name=None at 7ff3047f0510> -> __attrs_140681726832016
            __attrs_140681726832016 = _static_140681743978256

            # <link ... (11:4)
            # --------------------------------------------------------
            __append('<link type="text/css" href="static/css/bootstrap-responsive.min.css" rel="stylesheet">\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493ee90> name=None at 7ff3045abc10> -> __attrs_140681726836112
            __attrs_140681726836112 = _static_140681730584208

            # <link ... (12:4)
            # --------------------------------------------------------
            __append('<link type="text/css" href="static/css/style.css" rel="stylesheet">\n\n    <!--Font Awesome-->\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493f490> name=None at 7ff3045a9290> -> __attrs_140681726828624
            __attrs_140681726828624 = _static_140681730585744

            # <link ... (15:4)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" href="static/font-awesome/css/font-awesome.min.css" />\n    <!--/Font Awesome-->\n\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493ea10> name=None at 7ff3045aaf50> -> __attrs_140681726824784
            __attrs_140681726824784 = _static_140681730583056

            # <script ... (18:4)
            # --------------------------------------------------------
            __append('<script type="text/javascript" src="static/js/jquery-1.9.1.min.js"></script>\n\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493fa60> name=None at 7ff3045ab210> -> __attrs_140681726832336
            __attrs_140681726832336 = _static_140681730587232

            # <script ... (20:4)
            # --------------------------------------------------------
            __append('<script type="text/javascript" src="static/js/jquery.metadata.js"></script>\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493f2e0> name=None at 7ff3047b9f50> -> __attrs_140681728988560
            __attrs_140681728988560 = _static_140681730585312

            # <script ... (21:4)
            # --------------------------------------------------------
            __append('<script type="text/javascript" src="static/js/jquery.tablesorter.min.js"></script>\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493d9f0> name=None at 7ff3047b8190> -> __attrs_140681728987600
            __attrs_140681728987600 = _static_140681730578928

            # <script ... (22:4)
            # --------------------------------------------------------
            __append('<script type="text/javascript" src="static/js/jquery.tablesorter.widgets.min.js"></script>\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493d930> name=None at 7ff3047b88d0> -> __attrs_140681728997328
            __attrs_140681728997328 = _static_140681730578736

            # <script ... (23:4)
            # --------------------------------------------------------
            __append('<script type="text/javascript">\n        $(document).ready(function(){\n            $(\'.tablesorter\').tablesorter({\n                textExtraction: function(node){\n                            var cell_value = $(node).text();\n                            var sort_value = $(node).data(\'value\');\n                    return (sort_value != undefined) ? sort_value : cell_value;\n                 },\n            })\n        })\n    </script>\n</head>\n\n')

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728996112
            __attrs_140681728996112 = _static_140681730573168

            # <body ... (36:0)
            # --------------------------------------------------------
            __append('<body>\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493df30> name=None at 7ff3047bb490> -> __attrs_140681730270352
            __attrs_140681730270352 = _static_140681730580272

            # <div ... (37:4)
            # --------------------------------------------------------
            __append('<div class="navbar navbar-inverse navbar-static-top" style="margin-bottom:0; border-bottom:1px solid #000;">\n        ')

            # <Static value=<ast.Dict object at 0x7ff30493f5e0> name=None at 7ff3048f1490> -> __attrs_140681730274832
            __attrs_140681730274832 = _static_140681730586080

            # <div ... (38:8)
            # --------------------------------------------------------
            __append('<div class="container">\n            ')

            # <Static value=<ast.Dict object at 0x7ff30493c880> name=None at 7ff3044dc1d0> -> __attrs_140681725989008
            __attrs_140681725989008 = _static_140681730574464

            # <ul ... (39:12)
            # --------------------------------------------------------
            __append('<ul class="nav navbar-nav pull-left">\n                ')

            # <Static value=<ast.Dict object at 0x7ff30493f220> name=None at 7ff3044dddd0> -> __attrs_140681725994768
            __attrs_140681725994768 = _static_140681730585120

            # <li ... (40:16)
            # --------------------------------------------------------
            __append('<li')

            # <Symbol value=<DEFAULT> at 7ff3056169d0> -> __default_140681725993168
            __default_140681725993168 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'get_started')}" (40:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3045abe10> -> __attr_class
            __token = 1742
            __token = 1744
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'get_started')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n                    ')

            # <Static value=<ast.Dict object at 0x7ff30493ece0> name=None at 7ff3044df9d0> -> __attrs_140681725993936
            __attrs_140681725993936 = _static_140681730583776

            # <a ... (41:20)
            # --------------------------------------------------------
            __append('<a href="get_started.html">Get Started</a>\n                </li>\n                ')

            # <Static value=<ast.Dict object at 0x7ff30493dea0> name=None at 7ff3044dc290> -> __attrs_140681725987088
            __attrs_140681725987088 = _static_140681730580128

            # <li ... (43:16)
            # --------------------------------------------------------
            __append('<li')

            # <Symbol value=<DEFAULT> at 7ff3056169d0> -> __default_140681725990288
            __default_140681725990288 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'ships')}" (43:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3044de090> -> __attr_class
            __token = 1910
            __token = 1912
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'ships')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n                    ')

            # <Static value=<ast.Dict object at 0x7ff30493eec0> name=None at 7ff3044dc6d0> -> __attrs_140681726000976
            __attrs_140681726000976 = _static_140681730584256

            # <a ... (44:20)
            # --------------------------------------------------------
            __append('<a href="ships.html">Ships</a>\n                </li>\n                ')

            # <Static value=<ast.Dict object at 0x7ff30493f8e0> name=None at 7ff304504090> -> __attrs_140681726154256
            __attrs_140681726154256 = _static_140681730586848

            # <li ... (46:16)
            # --------------------------------------------------------
            __append('<li')

            # <Symbol value=<DEFAULT> at 7ff3056169d0> -> __default_140681726150352
            __default_140681726150352 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'code_reference')}" (46:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3045045d0> -> __attr_class
            __token = 2060
            __token = 2062
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'code_reference')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n                    ')

            # <Static value=<ast.Dict object at 0x7ff30493da20> name=None at 7ff3045050d0> -> __attrs_140681726157584
            __attrs_140681726157584 = _static_140681730578976

            # <a ... (47:20)
            # --------------------------------------------------------
            __append('<a href="code_reference.html">Code Reference</a>\n                </li>\n            </ul>\n            ')

            # <Static value=<ast.Dict object at 0x7ff30493ef20> name=None at 7ff304507350> -> __attrs_140681726158928
            __attrs_140681726158928 = _static_140681730584352

            # <ul ... (50:12)
            # --------------------------------------------------------
            __append('<ul class="nav navbar-nav pull-right">\n                ')

            # <Static value=<ast.Dict object at 0x7ff30493fe20> name=None at 7ff304507ad0> -> __attrs_140681725873040
            __attrs_140681725873040 = _static_140681730588192

            # <li ... (51:16)
            # --------------------------------------------------------
            __append('<li')

            # <Symbol value=<DEFAULT> at 7ff3056169d0> -> __default_140681726149840
            __default_140681726149840 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'translations')}" (51:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304505850> -> __attr_class
            __token = 2306
            __token = 2308
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'translations')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>\n                    ')

            # <Static value=<ast.Dict object at 0x7ff30493fdc0> name=None at 7ff3044c16d0> -> __attrs_140681726042768
            __attrs_140681726042768 = _static_140681730588096

            # <a ... (52:20)
            # --------------------------------------------------------
            __append('<a href="translations.html">')

            # <Static value=<ast.Dict object at 0x7ff305746770> name=None at 7ff30456e950> -> __attrs_140681726589456
            __attrs_140681726589456 = _static_140681745295216

            # <i ... (52:48)
            # --------------------------------------------------------
            __append('<i class="icon-globe icon-white"></i> Help Translate FISH</a>\n                </li>\n                ')

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726581072
            __attrs_140681726581072 = _static_140681730573168

            # <li ... (54:16)
            # --------------------------------------------------------
            __append('<li>\n                    ')

            # <Static value=<ast.Dict object at 0x7ff305747910> name=None at 7ff30456e350> -> __attrs_140681726579984
            __attrs_140681726579984 = _static_140681745299728

            # <a ... (55:20)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7ff3056169d0> -> __default_140681726577936
            __default_140681726577936 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "${metadata['dev_thread_url']}" (55:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff30456ee50> -> __attr_href
            __token = 2545
            __token = 2547
            __attr_href = getitem('metadata')['dev_thread_url']
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = __attr_href
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')

            # <Static value=<ast.Dict object at 0x7ff305747dc0> name=None at 7ff30456ce50> -> __attrs_140681726574672
            __attrs_140681726574672 = _static_140681745300928

            # <i ... (55:60)
            # --------------------------------------------------------
            __append('<i class="icon-comment icon-white"></i> Discuss at TT-Forums.net</a>\n                </li>\n            </ul>\n        </div>\n    </div>\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493fa00> name=None at 7ff30456d410> -> __attrs_140681726582224
            __attrs_140681726582224 = _static_140681730587136

            # <div ... (60:4)
            # --------------------------------------------------------
            __append('<div class="hero-unit subhead">\n        ')

            # <Static value=<ast.Dict object at 0x7ff30493fac0> name=None at 7ff3047d9d50> -> __attrs_140681729115344
            __attrs_140681729115344 = _static_140681730587328

            # <script ... (61:8)
            # --------------------------------------------------------
            __append('<script language="JavaScript">\n        function random_img(){\n            var images=new Array("",\n                                 "");\n\n            var random_image=images[Math.floor(Math.random()*images.length)];\n            document.write(\'')

            # <Static value=<ast.Dict object at 0x7ff305747d60> name=None at 7ff3047daf50> -> __attrs_140681729119696
            __attrs_140681729119696 = _static_140681745300832

            # <a ... (67:28)
            # --------------------------------------------------------
            __append('<a href="ships.html#\' + random_image + \'">')

            # <Static value=<ast.Dict object at 0x7ff305747a00> name=None at 7ff3047db850> -> __attrs_140681729129680
            __attrs_140681729129680 = _static_140681745299968

            # <img ... (67:70)
            # --------------------------------------------------------
            __append('<img class="pull-right" style="margin-top:-30px; margin-bottom:0;" src="static/img/industries/\'+ random_image +\'.png"></a>\')\n        }\n        random_img()\n        </script>\n        ')

            # <Static value=<ast.Dict object at 0x7ff305747ca0> name=None at 7ff3047d9350> -> __attrs_140681729122256
            __attrs_140681729122256 = _static_140681745300640

            # <div ... (71:8)
            # --------------------------------------------------------
            __append('<div class="container">\n            ')

            # <Static value=<ast.Dict object at 0x7ff3046032e0> name=None at 7ff3047d8790> -> __attrs_140681729451088
            __attrs_140681729451088 = _static_140681727193824

            # <h1 ... (72:12)
            # --------------------------------------------------------
            __append('<h1 style="font-size:48px; padding-top:30px;">Squid Ate FISH</h1>\n            ')

            # <Static value=<ast.Dict object at 0x7ff304602590> name=None at 7ff30482a650> -> __attrs_140681729446544
            __attrs_140681729446544 = _static_140681727190416

            # <p ... (73:12)
            # --------------------------------------------------------
            __append('<p class="lead">New Ships for OpenTTD</p>\n        </div>\n    </div>\n    ')
            if (__slot_opt_page_header is None):

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681729453840
                __attrs_140681729453840 = _static_140681730573168
                __append('\n        \n    ')
            else:
                __slot_opt_page_header(__stream, econtext.copy(), rcontext)
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7ff30493dd20> name=None at 7ff30482a350> -> __attrs_140681729456272
            __attrs_140681729456272 = _static_140681730579744

            # <div ... (79:4)
            # --------------------------------------------------------
            __append('<div class="container">\n        ')
            if (__slot_body is None):

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681729457488
                __attrs_140681729457488 = _static_140681730573168
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681729442704
                __attrs_140681729442704 = _static_140681730573168

                # <p ... (81:12)
                # --------------------------------------------------------
                __append('<p>Ooooops - there is no content for some reason. Something has probably gone nuts in the build. </p>\n        ')
            else:
                __slot_body(__stream, econtext.copy(), rcontext)
            __append('\n    </div>\n    ')

            # <Static value=<ast.Dict object at 0x7ff304603580> name=None at 7ff30482b6d0> -> __attrs_140681726640976
            __attrs_140681726640976 = _static_140681727194496

            # <div ... (84:4)
            # --------------------------------------------------------
            __append('<div style="margin-top:30px; text-align:center; color:#999; padding:5px; background-color:#eee; border-top:solid 1px #ddd; box-shadow: inset 0px 1px 1px #ddd">\n        Squid Ate FISH, with thanks to all who helped\n    </div>\n</body>\n</html>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x7ff3045e0940> name=None at 7ff304558710> -> __attrs_140681726504080
            __attrs_140681726504080 = _static_140681727052096

            # <?xml ... (1:0)
            # --------------------------------------------------------
            __append('<?xml version="1.0" encoding="iso-8859-1"?>\n')
            __token = None
            render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n\n\n\n\n\n\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }