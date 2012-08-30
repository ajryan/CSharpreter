# Sublime Text 2: CSharpreter plugin

## Description

CSharpreter compiles and executes snippets of C# code. The currently-selected text (or entire contents of the view, if no text is selected) is injected into the body of the Main routine of a C# console application. MSBuild is invoked and the executable is run in a shell window. This plugin has only been tested on Windows, but *may* be compatible with Mono's XBuild.

With the default settings, your code will be injected into a program defined as follows:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

class Program
{ 
  static void Main(string[] args)
  {
    // YOUR TEXT HERE
    
    Console.WriteLine();
    Console.WriteLine("Press any key to exit...");
    Console.ReadKey();
  }
}
```

## Commands

* CSharpreter: Interpret - Execute the currently-selected text, or with no selected text, the entire contents of the view.
* CSharpreter: Cleanup - Delete the %temp%\CSharpreter folder, where temporary source and binaries are written.

## Settings

In the CSharpreter package folder, edit c_sharpreter.sublime-settings file to modify the defaults.

* msbuild_path - Path to the MSBuild executable
* default_usings - List of namespaces to inject at the top of the source file.
* main_end - List of statements to inject at the end of the Main method.

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

### Easy

Install the (awesome!) [Package Control](http://wbond.net/sublime_packages/package_control) package, press Ctrl+Shift+P, choose Package Control: Install Package, and then type 'CSharpreter'.

### Manual

Clone this repository into your Sublime Text packages folder.

**Windows 7 / Vista and above**

    C:\Users\<username>\AppData\Roaming\Sublime Text 2\Packages

**Windows XP**

    C:\Documents and Settings\<username>\Application Data\Sublime Text 2\Packages

