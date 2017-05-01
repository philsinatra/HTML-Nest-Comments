[![GitHub tag](https://img.shields.io/github/tag/philsinatra/HTML-Nest-Comments.svg?style=flat-square)](https://github.com/philsinatra/HTML-Nest-Comments)
[![Package Control](https://img.shields.io/packagecontrol/dt/HTML%20Nest%20Comments.svg?style=flat-square)](https://packagecontrol.io/packages/HTML%20Nest%20Comments)
[![license](https://img.shields.io/github/license/philsinatra/HTML-Nest-Comments.svg?style=flat-square)](https://github.com/philsinatra/HTML-Nest-Comments/blob/master/LICENSE)

# HTML Nest Comments for Sublime Text

## About
This is a Sublime Text 2 and 3 plugin allowing you to quickly comment out blocks of HTML code that already contain HTML comments.

![example image](http://cdn.philsinatra.com/libraries/sublime-text/html-nested-comments/sublime-nested-comments.gif)

## Installation
The easy way is:

### Through [Sublime Package Manager](http://wbond.net/sublime_packages/package_control)

* <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> in Linux/Windows/OS X
* type `install`, select `Package Control: Install Package`
* type `htmlnest`, select `HTML-Nest-Comments`

### Manually
Make sure you use the right Sublime Text folder. For example, on OS X, packages for version 2 are in `~/Library/Application\ Support/Sublime\ Text\ 2`, while version 3 is labeled `~/Library/Application\ Support/Sublime\ Text\ 3`.

These are for Sublime Text 3:

#### Mac
`git clone https://github.com/philsinatra/HTML-Nested-Comments.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/HTML-Nest-Comments`

#### Linux
`git clone https://github.com/philsinatra/HTML-Nested-Comments.git ~/.config/sublime-text-3/Packages/HTML-Nest-Comments`

#### Windows
`git clone https://github.com/philsinatra/HTML-Nested-Comments.git %APPDATA%/Sublime\ Text\ 3/Packages/HTML-Nest-Comments`

## Usage
Tools -> Command Palette (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) and type `nested`.

-- or --

<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>/</kbd> (or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>/</kbd> if you're on a Mac).

-- or --

Right click in the current buffer and select `HTML Nest Comments` -> `Comment/Uncomment Selection`.

-- or --

Open an HTML file, pop out the console in Sublime Text from View -> Show Console, and type `view.run_command("nest")`.

Writing commands in the console is ugly. Set up your own key combo for this, by going to Preferences -> Key Bindings - User, and adding a command in that array: `{ "keys": ["super+shift+/"], "command": "nest" }`. You can use any other command you want, thought most of them are already taken.

## What Happens
The built in comment function in Sublime Text runs into an issue if your HTML code contains comments that you want to maintain while block commenting larger areas of code. This plugin will temporarily disable the nested comments so that you can bulk comment out blocks of HTML that already contain comments.

```html
<div class="container">
  <div class="main">
    <div class="content"></div>
    <!-- /.content -->
    <aside></aside>
  </div>
  <!-- /.main -->
</div>
<!-- /.container -->
```

Each of the existing comment tags will be replaced with `<!~~` or `~~>` respectively when commenting, and then the effect will be reversed when uncommenting.

Run the nest command and the code is transformed into:

```html
<!--  <div class="container">
    <div class="main">
      <div class="content"></div>
      <!~~ /.content ~~>
      <aside></aside>
    </div>
    <!~~ /.main ~~>
  </div>
  <!~~ /.container ~~>
-->
```
