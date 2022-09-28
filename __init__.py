from aqt import mw, gui_hooks
from aqt.qt import *
import re

#Add this to MorphMan if you want to see K 123 V 456
#addons21\900801631\morph\stats.py:68
"""
from aqt.qt import *
morphaction = QAction("K ? V ?", mw)
mw.form.menubar.addAction(morphaction)
def on_top_toolbar_did_init_links(links, toolbar):
    name, details = getStatsLink()
    links.append(
        toolbar.create_link(
            "morph", _(name), on_morph_link_clicked, tip=_(details), id="morph"
        )
    )
    morphaction.setText(_(name))
    morphaction.triggered.connect(toolbar.link_handlers["morph"])
"""

syncemoji, mediaemoji = "🗃","🖼" #"↻","⟳"

synctext = "S&ync"
syncaction = QAction(synctext,	mw)

def merge_toolbars():
	decksaction	= QAction(_("&Decks"),	mw)
	addaction	= QAction(_("&Add"),	mw)
	browseaction	= QAction(_("&Browse"),	mw)
	statsaction	= QAction(_("S&tats"),	mw)
	global syncaction#	= QAction(_("S&ync"),	mw)
	#studyaction	= QAction(_("&Study"),	mw)
	mw.form.menubar.addAction(decksaction	)
	mw.form.menubar.addAction(addaction	)
	mw.form.menubar.addAction(browseaction	)
	mw.form.menubar.addAction(statsaction	)
	mw.form.menubar.addAction(syncaction	)
	#mw.form.menubar.addAction(studyaction	)
	decksaction.triggered.connect(	mw.toolbar.link_handlers["decks"	])
	addaction.triggered.connect(	mw.toolbar.link_handlers["add"	])
	browseaction.triggered.connect(	mw.toolbar.link_handlers["browse"	])
	statsaction.triggered.connect(	mw.toolbar.link_handlers["stats"	])
	syncaction.triggered.connect(	mw.toolbar.link_handlers["sync"	])
	#studyaction.triggered.connect(	mw.toolbar.link_handlers["study"	])
	
	#gui_hooks.top_toolbar_did_init_links.append(	merge_morphman_link	)

def top_toolbar_close(top_toolbar):
	top_toolbar.web.setFixedHeight(0)
	top_toolbar.web.close()

def sync_will_start():
	global syncaction, synctext
	synctext = synctext+syncemoji
	syncaction.setText(synctext)

def sync_did_finish():
	global syncaction, synctext
	synctext = synctext.replace(syncemoji,"")
	syncaction.setText(synctext)

def media_sync_did_start_or_stop(running):
	global syncaction, synctext
	if running:
		synctext = synctext+mediaemoji
	else:
		synctext = synctext.replace(mediaemoji,"")
	syncaction.setText(synctext)

gui_hooks.main_window_did_init.append(	merge_toolbars	)
gui_hooks.top_toolbar_did_redraw.append(	top_toolbar_close	)
gui_hooks.sync_will_start.append(	sync_will_start	)
gui_hooks.sync_did_finish.append(	sync_did_finish	)
gui_hooks.media_sync_did_start_or_stop.append(	media_sync_did_start_or_stop	)

#==============================================================================

#def merge_morphman_link(links, top_toolbar):
#	#print(re.search(r"K \d+ V \d+", "<span>K 123 V 456</span>")[0])
#	print('merge_morphman_link')
#	KV = re.search(r"K \d+ V \d+", links.pop())
#	if KV:
#		morphsaction	= QAction(KV[0],	mw)
#		mw.form.menubar.addAction(morphsaction	)
#		morphsaction.triggered.connect(	mw.toolbar.link_handlers["morph"	])
#		top_toolbar.web.close()
#	top_toolbar.web.setFixedHeight(0)
#	top_toolbar.web.close()
#
##gui_hooks.top_toolbar_did_init_links.append(	merge_morphman_link	)
