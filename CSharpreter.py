import sublime, sublime_plugin
import os, datetime, shutil, subprocess

class CsharpreterCommand(object):
	def get_temp_root(self):
		return os.path.join(os.environ['TEMP'], "CSharpreter")

	def get_temp_folder(self):
		timeStr = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
		tempFolder = os.path.join(self.get_temp_root(), timeStr)
		os.makedirs(tempFolder)
		return tempFolder

class CsharpreterInterpretCommand(CsharpreterCommand, sublime_plugin.TextCommand):
	CSHARP_START = "class Program { static void Main(string[] args) {"
	CSHARP_END = "}}"

	def __init__(self, view):
		self.view = view
		
		settings = sublime.load_settings('c_sharpreter.sublime-settings')
		self.msbuild_path = settings.get('msbuild_path')
		self.default_usings = settings.get('default_usings')
		self.main_end = settings.get('main_end')

	def run(self, edit):
		text = self.get_selected_text()
		if len(text) <= 0:
			print "CSharpreter: nothing to interpret"
			return

		tempFolder = self.get_temp_folder()
		self.write_temp_cs(text, tempFolder)
		shutil.copy("Build.xml", tempFolder)
		buildOk = self.build(tempFolder)
		if buildOk:
			self.execute(tempFolder)

	def get_selected_text(self):
		text = ""
		for region in self.view.sel():
			if not region.empty():
				text += self.view.substr(region)
		if len(text) <= 0:
			text = self.view.substr(sublime.Region(0, self.view.size()))
		return text

	def write_temp_cs(self, text, tempFolder):
		usings = "using " + "; using ".join(self.default_usings) + ";"
		mainEnd = ''.join(self.main_end)
		cstext = usings + self.CSHARP_START + text + mainEnd + self.CSHARP_END

		tempPath = os.path.join(tempFolder, "csharpreter.cs")
		tempFile = open(tempPath, 'w')
		tempFile.write(cstext)
		tempFile.close()

	def build(self, tempFolder):
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		commands = [self.msbuild_path, "Build.xml"]
		msbuildProcess = subprocess.Popen(commands, cwd=tempFolder, stdout=subprocess.PIPE, startupinfo=startupinfo)
		(out, err) = msbuildProcess.communicate()
		
		if (msbuildProcess.returncode != 0):
			print out
			print "CSharpreter: error in msbuild while building in %s" % tempFolder
			return False
		else:
			print "CSharpreter: successfully built " + os.path.join(tempFolder, "CSharpreter.exe")
			return True

	def execute(self, tempFolder):
		subprocess.Popen(os.path.join(tempFolder, "CSharpreter.exe"))

class CsharpreterCleanupCommand(CsharpreterCommand, sublime_plugin.TextCommand):
	def run(self, edit):
		tempRoot = self.get_temp_root()
		if os.path.exists(tempRoot):
			print "CSharpreter: deleting " + tempRoot
			shutil.rmtree(tempRoot)
