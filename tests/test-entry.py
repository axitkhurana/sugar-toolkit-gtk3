#!/usr/bin/env python

# Copyright (C) 2007, One Laptop Per Child
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
import gtk
import hippo

from sugar.graphics.toolbar import Toolbar
from sugar.graphics.frame import Frame
from sugar.graphics.button import Button
from sugar.graphics.entry import Entry

window = gtk.Window()
window.connect("destroy", lambda w: gtk.main_quit())
window.show()

canvas = hippo.Canvas()
window.add(canvas)
canvas.show()

vbox = hippo.CanvasBox()
canvas.set_root(vbox)

toolbar = Toolbar()
vbox.append(toolbar)

frame = Frame()
toolbar.append(frame)

button = Button('theme:stock-close')
frame.append(button)

entry = Entry()
toolbar.append(entry, hippo.PACK_EXPAND)

entry2 = Entry()
toolbar.append(entry2, hippo.PACK_EXPAND)

gtk.main()