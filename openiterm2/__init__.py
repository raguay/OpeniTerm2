from fman import DirectoryPaneCommand, show_alert, DATA_DIRECTORY, FMAN_VERSION, load_json, save_json
import os

class OpenIterm2(DirectoryPaneCommand):
    def __call__(self):
        ntab = False
        loc = load_json('OpenIterm2.json')
        if loc is None:
            jloc = dict()
            jloc['NewTab'] = False
            save_json('OpenIterm2.json',jloc)
        else:
            ntab = loc['NewTab']
        fmanv = 0
        if isinstance(FMAN_VERSION, str):
            fmanvParts = FMAN_VERSION.split('.')
            if fmanvParts[0] == '0':
                fmanv = int(fmanvParts[1])
        else:
            fmanv = FMAN_VERSION
        selected_files = self.pane.get_selected_files()
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            dirName = selected_files[0]
            if os.path.isfile(dirName):
                dirName = os.path.dirname(dirName)
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
        else:
            show_alert("No directory selected")

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
       loc = load_json('OpenIterm2.json')
       ntab = False
       if loc is None:
            jloc = dict()
            jloc['NewTab'] = False
            save_json('OpenIterm2.json',jloc)
       else:
            ntab = loc['NewTab']
       loc['NewTab'] = not ntab
       save_json("OpenIterm2.json",loc)

