from fman import DirectoryPaneCommand, show_alert, DATA_DIRECTORY, FMAN_VERSION
import os

class OpenIterm2(DirectoryPaneCommand):
    def __call__(self):
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
                os.system("/usr/bin/osascript '" + DATA_DIRECTORY + "/Plugins/Third-party/OpeniTerm2/OpeniTerm2.scpt' '" + dirName + "'")
            else:
                os.system("/usr/bin/osascript '" + DATA_DIRECTORY + "/Plugins/OpeniTerm2/OpeniTerm2.scpt' '" + dirName + "'")
        else:
            show_alert("No directory selected")
