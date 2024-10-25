# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/docs_templates/get_started.pt'

__tokens = {855: ("Intro dates ${metadata['dates'][0]}-${metadata['dates'][1]}", 16, 59), 869: ("metadata['dates'][0]", 16, 73), 893: ("metadata['dates'][1]", 16, 97), 3077: ("${metadata['repo_url']}", 46, 67), 3079: ("metadata['repo_url']", 46, 69), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140681730574512 = {'href': 'changelog.html', }
_static_140681730588144 = {'class': 'lead', }
_static_140681730580368 = {'id': 'fish-changes', }
_static_140681730583056 = {'class': 'btn btn-large btn-default', 'href': 'code_reference.html', }
_static_140681730580032 = {'class': 'btn btn-large btn-primary', 'href': 'ships.html', }
_static_140681730580896 = {'class': 'lead', }
_static_140681730587664 = {'id': 'what-next', }
_static_140681730587616 = {'class': 'lead', }
_static_140681745040048 = {'id': 'setting-up', }
_static_140681745047488 = {'class': 'btn btn-default btn-block', 'href': "${metadata['repo_url']}", }
_static_140681745041440 = {'href': 'code_reference.html', }
_static_140681745292432 = {'class': 'col-sm-4', }
_static_140681745292864 = {'class': 'btn btn-info btn-block', 'href': 'http://bundles.openttdcoop.org/fish/releases/LATEST/', }
_static_140681745293920 = {'href': 'http://wiki.openttd.org/Newgrf#Manual_install', }
_static_140681743978592 = {'class': 'col-sm-4', }
_static_140681743977968 = {'class': 'btn btn-primary btn-block', 'href': 'http://wiki.openttd.org/Content_downloading', }
_static_140681743978208 = {'class': 'col-sm-4', }
_static_140681743974608 = {'class': 'row', }
_static_140681736768096 = {'class': 'lead', }
_static_140681728487344 = {'id': 'download-fish', }
_static_140681728486048 = {'class': 'fa fa-check-circle', }
_static_140681728484464 = {'class': 'fa fa-check-circle', }
_static_140681728483264 = {'class': 'fa fa-check-circle', }
_static_140681728481536 = {'class': 'fa fa-check-circle', }
_static_140681728490560 = {'class': 'fa fa-check-circle', }
_static_140681728482736 = {'class': 'fa fa-check-circle', }
_static_140681728476736 = {'class': 'fa fa-check-circle', }
_static_140681728477888 = {'class': 'fa fa-check-circle', }
_static_140681728481680 = {'class': 'list-inline', }
_static_140681728485712 = {'class': 'page-header', }
_static_140681728487008 = {'class': 'col-md-9', }
_static_140681728489552 = {'href': '#fish-changes', }
_static_140681728478080 = {'class': 'list-group-item', }
_static_140681728484944 = {'href': '#what-next', }
_static_140681728475440 = {'class': 'list-group-item', }
_static_140681728491472 = {'href': '#setting-up', }
_static_140681728477504 = {'class': 'list-group-item', }
_static_140681728490752 = {'href': '#download-fish', }
_static_140681728486672 = {'class': 'list-group-item', }
_static_140681728477456 = {'class': 'list-group', 'style': 'margin-top:35px;', }
_static_140681728486720 = {'class': 'col-md-3', }
_static_140681728475296 = {'class': 'row', }
_static_140681728477360 = 'load:main_template.pt'
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

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726337168
            __attrs_140681726337168 = _static_140681730573168
            __backup_macroname_140681726340224 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7ff30473c8b0> name=None at 7ff304532d10> -> __value
            __value = _static_140681728477360
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726332880
                __attrs_140681726332880 = _static_140681730573168
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7ff30473c0a0> name=None at 7ff30456a7d0> -> __attrs_140681726560208
                __attrs_140681726560208 = _static_140681728475296

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div class="row">\n        ')

                # <Static value=<ast.Dict object at 0x7ff30473ed40> name=None at 7ff304568310> -> __attrs_140681726566160
                __attrs_140681726566160 = _static_140681728486720

                # <div ... (4:8)
                # --------------------------------------------------------
                __append('<div class="col-md-3">\n            ')

                # <Static value=<ast.Dict object at 0x7ff30473c910> name=None at 7ff304569510> -> __attrs_140681726561552
                __attrs_140681726561552 = _static_140681728477456

                # <ul ... (5:12)
                # --------------------------------------------------------
                __append('<ul class="list-group" style="margin-top:35px;">\n                ')

                # <Static value=<ast.Dict object at 0x7ff30473ed10> name=None at 7ff30456bd10> -> __attrs_140681726572304
                __attrs_140681726572304 = _static_140681728486672

                # <li ... (6:16)
                # --------------------------------------------------------
                __append('<li class="list-group-item">')

                # <Static value=<ast.Dict object at 0x7ff30473fd00> name=None at 7ff3048fa290> -> __attrs_140681730306512
                __attrs_140681730306512 = _static_140681728490752

                # <a ... (6:44)
                # --------------------------------------------------------
                __append('<a href="#download-fish">Download Squid Ate FISH</a></li>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30473c940> name=None at 7ff3048fa8d0> -> __attrs_140681730297616
                __attrs_140681730297616 = _static_140681728477504

                # <li ... (7:16)
                # --------------------------------------------------------
                __append('<li class="list-group-item">')

                # <Static value=<ast.Dict object at 0x7ff30473ffd0> name=None at 7ff3044c31d0> -> __attrs_140681730268944
                __attrs_140681730268944 = _static_140681728491472

                # <a ... (7:44)
                # --------------------------------------------------------
                __append('<a href="#setting-up">Setting up a Game with Squid Ate FISH</a></li>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30473c130> name=None at 7ff3048f1810> -> __attrs_140681730271760
                __attrs_140681730271760 = _static_140681728475440

                # <li ... (8:16)
                # --------------------------------------------------------
                __append('<li class="list-group-item">')

                # <Static value=<ast.Dict object at 0x7ff30473e650> name=None at 7ff3048f1d50> -> __attrs_140681727537808
                __attrs_140681727537808 = _static_140681728484944

                # <a ... (8:44)
                # --------------------------------------------------------
                __append('<a href="#what-next">What Next?</a></li>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30473cb80> name=None at 7ff304657550> -> __attrs_140681727533712
                __attrs_140681727533712 = _static_140681728478080

                # <li ... (9:16)
                # --------------------------------------------------------
                __append('<li class="list-group-item">')

                # <Static value=<ast.Dict object at 0x7ff30473f850> name=None at 7ff304654ad0> -> __attrs_140681728939344
                __attrs_140681728939344 = _static_140681728489552

                # <a ... (9:44)
                # --------------------------------------------------------
                __append('<a href="#fish-changes">Squid Ate FISH Changes</a></li>\n            </ul>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x7ff30473ee60> name=None at 7ff3047afc10> -> __attrs_140681728948560
                __attrs_140681728948560 = _static_140681728487008

                # <div ... (12:8)
                # --------------------------------------------------------
                __append('<div class="col-md-9">\n            ')

                # <Static value=<ast.Dict object at 0x7ff30473e950> name=None at 7ff3047aef10> -> __attrs_140681726239632
                __attrs_140681726239632 = _static_140681728485712

                # <div ... (13:12)
                # --------------------------------------------------------
                __append('<div class="page-header">\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726246224
                __attrs_140681726246224 = _static_140681730573168

                # <h2 ... (14:16)
                # --------------------------------------------------------
                __append('<h2>Get Started</h2>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30473d990> name=None at 7ff30451b990> -> __attrs_140681726243536
                __attrs_140681726243536 = _static_140681728481680

                # <ul ... (15:16)
                # --------------------------------------------------------
                __append('<ul class="list-inline">\n                    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726241552
                __attrs_140681726241552 = _static_140681730573168

                # <li ... (16:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x7ff30473cac0> name=None at 7ff304519fd0> -> __attrs_140681729222992
                __attrs_140681729222992 = _static_140681728477888

                # <i ... (16:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i>')

                # <Interpolation value=<Substitution " Intro dates ${metadata['dates'][0]}-${metadata['dates'][1]}" (16:58)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3044eb8d0> -> __content_140681743329328
                __token = 855
                __token = 869
                __content_140681743329328 = getitem('metadata')['dates'][0]
                __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                __token = 893
                __content_140681743329328_891 = getitem('metadata')['dates'][1]
                __content_140681743329328_891 = __quote(__content_140681743329328_891, '\x00', '&#0;', None, None)
                __content_140681743329328 = ('%s%s%s%s' % (' Intro dates ', (__content_140681743329328 if (__content_140681743329328 is not None) else ''), '-', (__content_140681743329328_891 if (__content_140681743329328_891 is not None) else ''), ))
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
                __append('</li>\n                    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681729223504
                __attrs_140681729223504 = _static_140681730573168

                # <li ... (17:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x7ff30473c640> name=None at 7ff3047f0dd0> -> __attrs_140681729217296
                __attrs_140681729217296 = _static_140681728476736

                # <i ... (17:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Wide range of ship types and capacities</li>\n                    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681729224592
                __attrs_140681729224592 = _static_140681730573168

                # <li ... (18:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x7ff30473ddb0> name=None at 7ff3047f3850> -> __attrs_140681729224272
                __attrs_140681729224272 = _static_140681728482736

                # <i ... (18:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Compatible with all known cargos</li>\n                    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681725974032
                __attrs_140681725974032 = _static_140681730573168

                # <li ... (19:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x7ff30473fc40> name=None at 7ff3044db990> -> __attrs_140681726158928
                __attrs_140681726158928 = _static_140681728490560

                # <i ... (19:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Supports 2 company colours</li>\n                    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726161680
                __attrs_140681726161680 = _static_140681730573168

                # <li ... (20:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x7ff30473d900> name=None at 7ff304504690> -> __attrs_140681726159312
                __attrs_140681726159312 = _static_140681728481536

                # <i ... (20:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Autorefit support</li>\n                    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726151120
                __attrs_140681726151120 = _static_140681730573168

                # <li ... (21:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x7ff30473dfc0> name=None at 7ff304507250> -> __attrs_140681726148944
                __attrs_140681726148944 = _static_140681728483264

                # <i ... (21:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Parameter for ship speed</li>\n                    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726162448
                __attrs_140681726162448 = _static_140681730573168

                # <li ... (22:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x7ff30473e470> name=None at 7ff3045051d0> -> __attrs_140681726162320
                __attrs_140681726162320 = _static_140681728484464

                # <i ... (22:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Parameter for canal construction costs</li>\n                    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726163024
                __attrs_140681726163024 = _static_140681730573168

                # <li ... (23:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x7ff30473eaa0> name=None at 7ff30457fe50> -> __attrs_140681726649872
                __attrs_140681726649872 = _static_140681728486048

                # <i ... (23:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> GPL v2 license</li>\n                </ul>\n            </div>\n            ')

                # <Static value=<ast.Dict object at 0x7ff30473efb0> name=None at 7ff30457f490> -> __attrs_140681726655120
                __attrs_140681726655120 = _static_140681728487344

                # <div ... (26:12)
                # --------------------------------------------------------
                __append('<div id="download-fish">\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726294864
                __attrs_140681726294864 = _static_140681730573168

                # <h2 ... (27:16)
                # --------------------------------------------------------
                __append('<h2>1. Download Squid Ate FISH</h2>\n                ')

                # <Static value=<ast.Dict object at 0x7ff304f24a60> name=None at 7ff304526250> -> __attrs_140681726291344
                __attrs_140681726291344 = _static_140681736768096

                # <p ... (28:16)
                # --------------------------------------------------------
                __append('<p class="lead">\n                    Squid Ate FISH is available from the content service in OpenTTD, as a zip for manual installation,\n                    or as a source checkout for compiling locally (requires mercurial and various python dependencies).\n                </p>\n                ')

                # <Static value=<ast.Dict object at 0x7ff3056040d0> name=None at 7ff304527610> -> __attrs_140681729512080
                __attrs_140681729512080 = _static_140681743974608

                # <div ... (32:16)
                # --------------------------------------------------------
                __append('<div class="row">\n                    ')

                # <Static value=<ast.Dict object at 0x7ff305604ee0> name=None at 7ff30483bf90> -> __attrs_140681729510416
                __attrs_140681729510416 = _static_140681743978208

                # <div ... (33:20)
                # --------------------------------------------------------
                __append('<div class="col-sm-4">\n                        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681729510224
                __attrs_140681729510224 = _static_140681730573168

                # <h3 ... (34:24)
                # --------------------------------------------------------
                __append('<h3>Download in OpenTTD</h3>\n                        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681729516304
                __attrs_140681729516304 = _static_140681730573168

                # <p ... (35:24)
                # --------------------------------------------------------
                __append('<p>')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681729519248
                __attrs_140681729519248 = _static_140681730573168

                # <strong ... (35:27)
                # --------------------------------------------------------
                __append('<strong>Easiest</strong>: get Squid Ate FISH from the OpenTTD content service.</p>\n                        ')

                # <Static value=<ast.Dict object at 0x7ff305604df0> name=None at 7ff30483b590> -> __attrs_140681730659536
                __attrs_140681730659536 = _static_140681743977968

                # <a ... (36:24)
                # --------------------------------------------------------
                __append('<a class="btn btn-primary btn-block" href="http://wiki.openttd.org/Content_downloading">Instructions</a>\n                    </div>\n                    ')

                # <Static value=<ast.Dict object at 0x7ff305605060> name=None at 7ff304953e10> -> __attrs_140681730662224
                __attrs_140681730662224 = _static_140681743978592

                # <div ... (38:20)
                # --------------------------------------------------------
                __append('<div class="col-sm-4">\n                        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681730662864
                __attrs_140681730662864 = _static_140681730573168

                # <h3 ... (39:24)
                # --------------------------------------------------------
                __append('<h3>Download Zip</h3>\n                        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681730656592
                __attrs_140681730656592 = _static_140681730573168

                # <p ... (40:24)
                # --------------------------------------------------------
                __append('<p>Get the latest Squid Ate FISH release for ')

                # <Static value=<ast.Dict object at 0x7ff305746260> name=None at 7ff3049504d0> -> __attrs_140681730659408
                __attrs_140681730659408 = _static_140681745293920

                # <a ... (40:69)
                # --------------------------------------------------------
                __append('<a href="http://wiki.openttd.org/Newgrf#Manual_install">manual install</a>.</p>\n                        ')

                # <Static value=<ast.Dict object at 0x7ff305745e40> name=None at 7ff3044f2f50> -> __attrs_140681726008016
                __attrs_140681726008016 = _static_140681745292864

                # <a ... (41:24)
                # --------------------------------------------------------
                __append('<a class="btn btn-info btn-block" href="http://bundles.openttdcoop.org/fish/releases/LATEST/">Download Squid Ate FISH</a>\n                    </div>\n                    ')

                # <Static value=<ast.Dict object at 0x7ff305745c90> name=None at 7ff3044e3750> -> __attrs_140681726012560
                __attrs_140681726012560 = _static_140681745292432

                # <div ... (43:20)
                # --------------------------------------------------------
                __append('<div class="col-sm-4">\n                        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726011408
                __attrs_140681726011408 = _static_140681730573168

                # <h3 ... (44:24)
                # --------------------------------------------------------
                __append('<h3>Download Source</h3>\n                        ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726014608
                __attrs_140681726014608 = _static_140681730573168

                # <p ... (45:24)
                # --------------------------------------------------------
                __append('<p>Checkout source code and ')

                # <Static value=<ast.Dict object at 0x7ff305708820> name=None at 7ff3044e26d0> -> __attrs_140681726001232
                __attrs_140681726001232 = _static_140681745041440

                # <a ... (45:52)
                # --------------------------------------------------------
                __append('<a href="code_reference.html">compile your own Squid Ate FISH</a>.</p>\n                        ')

                # <Static value=<ast.Dict object at 0x7ff305709fc0> name=None at 7ff3044e09d0> -> __attrs_140681726008336
                __attrs_140681726008336 = _static_140681745047488

                # <a ... (46:24)
                # --------------------------------------------------------
                __append('<a class="btn btn-default btn-block"')

                # <Symbol value=<DEFAULT> at 7ff3056169d0> -> __default_140681726005200
                __default_140681726005200 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution "${metadata['repo_url']}" (46:67)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff3044e30d0> -> __attr_href
                __token = 3077
                __token = 3079
                __attr_href = getitem('metadata')['repo_url']
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
                __append('>Squid Ate FISH Source Repo</a>\n                    </div>\n                </div>\n            </div>\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726004944
                __attrs_140681726004944 = _static_140681730573168

                # <br ... (50:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726006672
                __attrs_140681726006672 = _static_140681730573168

                # <hr ... (51:12)
                # --------------------------------------------------------
                __append('<hr />\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728784336
                __attrs_140681728784336 = _static_140681730573168

                # <br ... (52:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<ast.Dict object at 0x7ff3057082b0> name=None at 7ff304787010> -> __attrs_140681728781584
                __attrs_140681728781584 = _static_140681745040048

                # <div ... (53:12)
                # --------------------------------------------------------
                __append('<div id="setting-up">\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728779280
                __attrs_140681728779280 = _static_140681730573168

                # <h2 ... (54:16)
                # --------------------------------------------------------
                __append('<h2>2. Setting Up a Game with Squid Ate FISH</h2>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493fbe0> name=None at 7ff304786050> -> __attrs_140681726511184
                __attrs_140681726511184 = _static_140681730587616

                # <p ... (55:16)
                # --------------------------------------------------------
                __append('<p class="lead">\n                    A few things to know before setting up a Squid Ate FISH game...\n                </p>\n                UNFINISHED - PARAMETERS ETC\n            </div>\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726516944
                __attrs_140681726516944 = _static_140681730573168

                # <br ... (60:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726521104
                __attrs_140681726521104 = _static_140681730573168

                # <hr ... (61:12)
                # --------------------------------------------------------
                __append('<hr />\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726512144
                __attrs_140681726512144 = _static_140681730573168

                # <br ... (62:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493fc10> name=None at 7ff30455ce90> -> __attrs_140681726515920
                __attrs_140681726515920 = _static_140681730587664

                # <div ... (63:12)
                # --------------------------------------------------------
                __append('<div id="what-next">\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726519888
                __attrs_140681726519888 = _static_140681730573168

                # <h2 ... (64:16)
                # --------------------------------------------------------
                __append('<h2>3. What Next?</h2>\n\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493e1a0> name=None at 7ff3047da810> -> __attrs_140681729127120
                __attrs_140681729127120 = _static_140681730580896

                # <p ... (66:16)
                # --------------------------------------------------------
                __append('<p class="lead">Find out more about Squid Ate FISH.  Or try it out in OpenTTD!</p>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493de40> name=None at 7ff3047d9b90> -> __attrs_140681729125584
                __attrs_140681729125584 = _static_140681730580032

                # <a ... (67:16)
                # --------------------------------------------------------
                __append('<a class="btn btn-large btn-primary" href="ships.html">List of Ships</a>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493ea10> name=None at 7ff3047d8090> -> __attrs_140681729128272
                __attrs_140681729128272 = _static_140681730583056

                # <a ... (68:16)
                # --------------------------------------------------------
                __append('<a class="btn btn-large btn-default" href="code_reference.html">Code Reference</a>\n            </div>\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728272336
                __attrs_140681728272336 = _static_140681730573168

                # <hr ... (70:12)
                # --------------------------------------------------------
                __append('<hr />\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728270288
                __attrs_140681728270288 = _static_140681730573168

                # <br ... (71:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493df90> name=None at 7ff30470ab10> -> __attrs_140681728264912
                __attrs_140681728264912 = _static_140681730580368

                # <div ... (72:12)
                # --------------------------------------------------------
                __append('<div id="fish-changes">\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728263888
                __attrs_140681728263888 = _static_140681730573168

                # <h2 ... (73:16)
                # --------------------------------------------------------
                __append('<h2>4. Changes in Squid Ate FISH</h2>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493fdf0> name=None at 7ff304708450> -> __attrs_140681728276368
                __attrs_140681728276368 = _static_140681730588144

                # <p ... (74:16)
                # --------------------------------------------------------
                __append('<p class="lead">Squid Ate FISH is updated and improved quite often.</p>\n                ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681728277392
                __attrs_140681728277392 = _static_140681730573168

                # <p ... (75:16)
                # --------------------------------------------------------
                __append('<p>The ')

                # <Static value=<ast.Dict object at 0x7ff30493c8b0> name=None at 7ff304460990> -> __attrs_140681725487504
                __attrs_140681725487504 = _static_140681730574512

                # <a ... (75:23)
                # --------------------------------------------------------
                __append('<a href="changelog.html">')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681725483664
                __attrs_140681725483664 = _static_140681730573168

                # <strong ... (75:48)
                # --------------------------------------------------------
                __append('<strong>Squid Ate FISH changelog</strong></a> keeps track of changes, including new features, bug fixes and updates to translations.</p>\n            </div>\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681725491472
                __attrs_140681725491472 = _static_140681730573168

                # <br ... (77:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681725489680
                __attrs_140681725489680 = _static_140681730573168

                # <br ... (78:12)
                # --------------------------------------------------------
                __append('<br />\n        </div>\n    </div>\n    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681725490832
                __attrs_140681725490832 = _static_140681730573168

                # <br ... (81:4)
                # --------------------------------------------------------
                __append('<br />\n    ')

                # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681725482640
                __attrs_140681725482640 = _static_140681730573168

                # <br ... (82:4)
                # --------------------------------------------------------
                __append('<br />\n')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'load:main_template.pt' (1:36)> -> __macro
            __token = 36
            __macro = 'main_template.pt'
            __macro = __loader(__macro)
            __token = 36
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140681726340224 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140681726340224
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }