# -*- coding: utf-8 -*-
__filename = '/home/nord/git/SHARK-cargo-quantity-fork/src/docs_templates/readme.pt'

__tokens = {76: ('ships', 3, 35), 83: ("${ship.title} ${' ' * (28-len(ship.title))} Introduced: ${ship.intro_date}; Speed: ${ship.speed}mph", 3, 42), 85: ('ship.title', 3, 44), 99: ("' ' * (28-len(ship.title))", 3, 58), 141: ('ship.intro_date', 3, 100), 168: ('ship.speed', 3, 127)}

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
            __append('--- THIS README NEEDS RE-WRITING :o ---\n\n')

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726204752
            __attrs_140681726204752 = _static_140681730573168
            __backup_ship_140681728479664 = get('ship', __marker)

            # <Value 'ships' (3:35)> -> __iterator
            __token = 76
            __iterator = getitem('ships')
            (__iterator, ____index_140681726200400, ) = getitem('repeat')('ship', __iterator)
            econtext['ship'] = None
            for __item in __iterator:
                econtext['ship'] = __item

                # <Interpolation value=<Substitution "${ship.title} ${' ' * (28-len(ship.title))} Introduced: ${ship.intro_date}; Speed: ${ship.speed}mph" (3:42)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7ff304513f50> -> __content_140681743329328
                __token = 83
                __token = 85
                __content_140681743329328 = _lookup_attr(getitem('ship'), 'title')
                __content_140681743329328 = __quote(__content_140681743329328, '\x00', '&#0;', None, None)
                __token = 99
                __content_140681743329328_97 = (' ' * (28 - len(_lookup_attr(getitem('ship'), 'title'))))
                __content_140681743329328_97 = __quote(__content_140681743329328_97, '\x00', '&#0;', None, None)
                __token = 141
                __content_140681743329328_139 = _lookup_attr(getitem('ship'), 'intro_date')
                __content_140681743329328_139 = __quote(__content_140681743329328_139, '\x00', '&#0;', None, None)
                __token = 168
                __content_140681743329328_166 = _lookup_attr(getitem('ship'), 'speed')
                __content_140681743329328_166 = __quote(__content_140681743329328_166, '\x00', '&#0;', None, None)
                __content_140681743329328 = ('%s%s%s%s%s%s%s%s' % ((__content_140681743329328 if (__content_140681743329328 is not None) else ''), ' ', (__content_140681743329328_97 if (__content_140681743329328_97 is not None) else ''), ' Introduced: ', (__content_140681743329328_139 if (__content_140681743329328_139 is not None) else ''), '; Speed: ', (__content_140681743329328_166 if (__content_140681743329328_166 is not None) else ''), 'mph', ))
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
                ____index_140681726200400 -= 1
                if (____index_140681726200400 > 0):
                    __append('')
            if (__backup_ship_140681728479664 is __marker):
                del econtext['ship']
            else:
                econtext['ship'] = __backup_ship_140681728479664
            __append('\n\nMy Fancy NewGRF Name\n-----------------------------------\n\nContents:\n\n1 About\n2 Usage and Parameters\n3 Building from source\n  3.1 Speed issues\n  3.2 Obtaining the source\n4 Credits\n5 License\n\n\n\n-------\n1 About\n-------\n\nThis is a NewGRF\n\nName of this Repo:  Example NewGRF project\nRepository version: {{REPO_REVISION}}\n\n\n\n----------------------\n2 Usage and Parameters\n----------------------\n\n\n\n----------------------\n3 Building from source\n----------------------\n\nUsually there\'s not much which needs to be changed when you obtain the\nsource. Your friends will usually be\n    make\n\tmake install\nBoth will build the grf from source, the latter will also try to copy\nthe grf into your grf folder so that it is available for testing and\nuse straight away.\n\nA brief overview over all Makefile targets is given here:\n\nall:\n\tThis is the default target, if also no parameter is given to\n\tmake. It will simply build the grf file, if it needs building\n\ndepend:\n\tRe-run the dependency check. Usually not manually needed.\n\ndocs:\n\tBuild the documentation files\n\nbundle:\n\tThis target will create a directory called "')

            # <Static value=<ast.Dict object at 0x7ff30493c370> name=None at 7ff304a38610> -> __attrs_140681726213520
            __attrs_140681726213520 = _static_140681730573168

            # <name ... (62:45)
            # --------------------------------------------------------
            __append('<name>-nightly" and\n\tcopy the grf file there and the documentation files, readme.txt,\n\tchangelog.txt and license.txt\n\nbundle_zip\n\tThis will zip the bundle directory into one zip for distribution\n\nbundle_tar\n\tThis will tar the bundle directory into a tar archive for\n\tdistribution or upload to bananas\n\nbundle_src\n\tCreates a source bundle\n\ninstall:\n\tThis will create a tar archive (like bundle_tar) and copy it\n\tinto the INSTALLDIR as specified in Makefile.local (or the\n\tdefault dir, if that isn\'t defined). Don\'t rely on a good\n\tdetection of the default installation directory. It\'s\n\tespecially bound to fail on windows machines.\n\ndistclean:\n\tThis phony target cleans everything from a source bundle which\n\twasn\'t shipped.\n\nclean:\n\tThis phony target will delete all files which this Makefile will\n\tcreate\n\nmrproper:\n\tThis phony target will delete also all directories created by\n\tdifferent Makefile targets\n\nremake:\n\tIt\'s a shortcut for first cleaning the dir and then making the\n\tgrf anew.\n\naddcheck:\n\tCheck whether there are some files required but not part of the\n\trepository.\n\ncheck:\n\tCheck the md5sum of the built newgrf against the supplied md5sum\n\t(Intended to be used when building from tar balls)\n\n\n3.1 Speed issues\n----------------\n\nA note concerning the speed of the makefile:\nIt seems that the required tools using MinGW and / or msys are thoroughly\nslow on windows. A few example run times for OpenGFX, same processor type\n(both core 2 duo, 2.26GHz for the windows machine, 2.0 GHz for the OSX\nmachine). Note that the values given are the \'real\' time. Even though\nthis varies more and is dependent on the processor load, that\'s what you\nhave to wait for; the \'user\' times are quite low on the windows machine\n(~16s), but that by no means reflects the build time. Times are from\nOpenGFX r539 with makefile r199.\n\nDEP_CHECK_TYPE         windows               bash native\n                 native       in VM            (OSX)\nnone            1m23.360s      -             0m32.781s\nmdep            1m54.484s   0m30.164s        0m33.807s\nnormal          2m37.857s      -             0m36.528s\n\n\n3.2 Obtaining the source\n------------------------\n\nThe source code can be obtained from the #openttdcoop DevZone at\n    http://dev.openttdcoop.org/projects/newgrf-makefile\nor via mercurial checkout\n    hg clone http://hg.openttdcoop.org/newgrf-makefile\n\n\n\n---------\n4 Credits\n---------\n\nAuthor: Ingo von Borstel (aka planetmaker)\n\nSpecial thanks to #openttdcoop and especially Ammler who provides and\nworks a lot on maintaining the Development Zone where this repository is\nhosted and who also frequently gives much valuable input. Thanks also to\nAlberth, Terkhen Yexo, Rubidium and Ammler who frequently give valuable\ninput in form of advice and patches to this project. Last but not least\nthanks to all the NewGRF authors whose NewGRFs can be my playground for\nthis project.\n\n\n\n--------------\n5 License\n--------------\n\nMy Fancy NewGRF\nCopyright (C) 2011 planetmaker and others\n\nThis program is free software; you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation; either version 2 of the License, or\n(at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License along\nwith this NewGRF; if not, write to the Free Software Foundation, Inc.,\n51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }