# Sublime Text 2: CSharpreter plugin

## Description

CSharpreter compiles and executes snippets of C# code. The currently-selected text (or entire contents of the view, if no text is selected) is injected into the body of the Main routine of a C# console application. MSBuild is invoked and the executable is run in a shell window.

## Settings

In the CSharpreter package folder, edit c_sharpreter.sublime-settings file to modify the defaults.

* msbuild_path: Path to the MSBuild executable
* default_usings: List of namespaces to inject at the top of the source file.
* main_end: List of statements to inject at the end of the Main method.

```json
{
	"msbuild_path": "C:/Windows/Microsoft.NET/Framework/v4.0.30319/MSBuild.exe",
	"default_usings":
	[
		"System", "System.Collections.Generic", "System.Linq"
	],
	"main_end":
	[
		"Console.WriteLine();",
		"Console.WriteLine(\"Press any key to exit...\");",
		"Console.ReadKey();"
	]
}
```

## Installation

Clone this repository into your Sublime Text packages folder.

**Windows 7 / Vista and above**

    C:\Users\<username>\AppData\Roaming\Sublime Text 2\Packages

**Windows XP**

    C:\Documents and Settings\<username>\Application Data\Sublime Text 2\Packages

