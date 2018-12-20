from fman import DirectoryPaneCommand, show_alert, DATA_DIRECTORY, FMAN_VERSION, load_json, save_json, DirectoryPaneListener
import os
from fman.url import as_human_readable
from fman.url import as_url

ntab = False
fmanv = 0

class OpenIterm2(DirectoryPaneCommand):
    def __call__(self):
        loadVars()
        dirName = as_human_readable(self.pane.get_path())
        goToDir(dirName)
        
def loadVars():
    global fmanv, ntab
    loc = load_json('OpenIterm2.json')
    if loc is None:
        jloc = dict()
        jloc['NewTab'] = False
        save_json('OpenIterm2.json', jloc)
    else:
        ntab = loc['NewTab']
    if isinstance(FMAN_VERSION, str):
        fmanvParts = FMAN_VERSION.split('.')
        if fmanvParts[0] == '0':
            fmanv = int(fmanvParts[1])
        else:
            fmanv = int(fmanvParts[0])*10 + int(fmanvParts[1])
    else:
        fmanv = FMAN_VERSION
   
def goToDir(dirName):
    global fmanv, ntab
    if fmanv > 4:
        if ntab:
            os.system("/usr/bin/osascript '" + DATA_DIRECTORY + "/Plugins/Third-party/OpeniTerm2/OpeniTerm2-newtab.scpt' '" + dirName + "'")
        else:
            os.system("/usr/bin/osascript '" + DATA_DIRECTORY + "/Plugins/Third-party/OpeniTerm2/OpeniTerm2.scpt' '" + dirName + "'")
    else:
        if ntab:
            os.system("/usr/bin/osascript '" + DATA_DIRECTORY + "/Plugins/OpeniTerm2/OpeniTerm2-newtab.scpt' '" + dirName + "'")
        else:
            os.system("/usr/bin/osascript '" + DATA_DIRECTORY + "/Plugins/OpeniTerm2/OpeniTerm2.scpt' '" + dirName + "'")

            
class OpenIterm2(DirectoryPaneCommand):
    def __call__(self):
        loadVars()
        dirName = as_human_readable(self.pane.get_path())
        goToDir(dirName)

class SetOpenIterm2TabOff(DirectoryPaneCommand):
    def __call__(self):
        loc = dict()
        loc['NewTab'] = False
        save_json("OpenIterm2.json",loc)

class SetOpenIterm2TabOn(DirectoryPaneCommand):
    def __call__(self):
        loc = dict()
        loc['NewTab'] = True
        save_json("OpenIterm2.json",loc)

class ToggleOpenIterm2Tab(DirectoryPaneCommand):
    def __call__(self):
        global fmanv, ntab
        loc = load_json('OpenIterm2.json')
        if loc is None:
            jloc = dict()
            jloc['NewTab'] = False
            save_json('OpenIterm2.json', jloc)
        else:
            ntab = loc['NewTab']
        loc['NewTab'] = not ntab
        ntab = not ntab
        save_json("OpenIterm2.json",loc)

fLeft = False
fRight = False

class DirectoryPaneListener(DirectoryPaneListener):
    def on_path_changed(self):
        global fLeft, fRight
        panes = self.pane.window.get_panes()
        if(fmanv == 0):
            loadVars()
        if((fLeft and (panes[0] == self.pane)) or (fRight and (panes[1] == self.pane))):
             goToDir(as_human_readable(self.pane.get_path()))

class ToggleFollowLeftPaneIterm2(DirectoryPaneCommand):
    def __call__(self):
        global fLeft
        fLeft = not fLeft
        
class ToggleFollowRightPaneIterm2(DirectoryPaneCommand):
    def __call__(self):
        global fRight
        fRight = not fRight
