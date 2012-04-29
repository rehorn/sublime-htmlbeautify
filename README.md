HTMLBeautify for Sublime Text 2 简介
========================
------------------------
HTMLBeautify for Sublime Text 2 是代码编辑器Sublime Text 2的一个 HTML/Css/JavaScript 代码格式化/美化插件，基于 NodeJS(nodejs.org) / JSBeautifier (jsbeautifier.org) 开发。

安装
------------------------
* 方式1
    * 下载并安装NodeJS(nodejs.org), windows 下需要重启
    * 打开 Sublime Text 2 的Packages目录， "Preferences" -> "Browse Packages"
    * 在Packages目录本代码仓库，Git Clone https://github.com/rehorn/sublime-htmlbeautify
    * 打开一个经过压缩的 .html/.htm/.js/.css 文件，用快捷键 ctrl+alt+q 执行格式化
* 方式2
    * 下载并安装NodeJS(nodejs.org), windows 下需要重启
    * 安装 Packages Control 后，将本代码仓库添加到源
        * ctrl+alt+p之后，输入add repository，输入https://github.com/rehorn/sublime-htmlbeautify
    * 执行 Packages Control 后，就能搜索到 sublime-uglifyjs ，安装即可
    * 打开一个经过压缩的 .html/.htm/.js/.css 文件，用快捷键 ctrl+alt+q 执行格式化

使用
------------------------
* 打开一个经过压缩的 .html/.htm/.js/.css 文件，用快捷键 ctrl+alt+q 执行格式化

自定义
------------------------
* 打开 Sublime Text 2 的Packages目录， "Preferences" -> "Browse Packages"
* 进入 sublime-htmlbeautify
* 修改 Default (Windows).sublime-keymap 文件，可以 Windows 自定义快捷键，其他平台可按照格式新建一个

其他
------------------------
* 本插件系 https://github.com/victorporof/Sublime-HTMLPrettify 的一个分支版本，修复了 windows 下无法正常运行和编码等问题。
