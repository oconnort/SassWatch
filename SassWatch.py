import os
import sublime
import sublime_plugin
import subprocess

# Plugin to launch a SASS command to watch the current file and
# let the user input the output file name & location
class WatchCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        def fileNameInput(output_css_file):

            # Check that output CSS file has correct extension
            if output_css_file.rfind(".css") == -1:
                sublime.status_message("Please enter a CSS file name.")
                return

            activeFile = sublime.active_window().active_view().file_name()

            # Check if file is a SASS file
            if activeFile.rfind(".scss") == -1:
                sublime.status_message("Plugin only works on files with .scss/.sass extensions.")
                return

            index = activeFile.rfind("\\")
            sass_file = activeFile[(index+1): ]
            sass_file_dir = activeFile[ : index]
            plugin_dir = os.path.join(sublime.packages_path(), 'SassWatch')

            # Run our batch file
            subprocess.Popen(['cmd', '/c', 'start', 'sasswatch.bat', sass_file_dir, sass_file, output_css_file], cwd=plugin_dir, shell=True)

        self.view.window().show_input_panel('CSS Output File (Relative or Absolute Path):', '', fileNameInput, None, None)
