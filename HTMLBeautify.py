import sys, platform, subprocess, commands
import sublime, sublime_plugin


class HtmlbeautifyCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.save()
    self.beautify(edit)

  def save(self):
    self.view.run_command("save")

  def execCmdWin(self, args):
    execCmd = subprocess.Popen(args = args, shell = True, \
            stdout = subprocess.PIPE, stderr = subprocess.PIPE) 
    try : 
        # code = sys.getfilesystemencoding() 
        output = execCmd.communicate()[0] #.decode(code) 
    except Exception as ex: 
        print('Warning: sh_panda_funcs.py: execCmd: ex:', ex) 
        traceback.print_exc()
        output = '' 
    # print(output)
    # print("execCmd: returncode =", execCmd.returncode) 
    return execCmd.returncode, output

  def execCmd(self, args):
    return commands.getoutput(args)

  def beautify(self, edit):
    strCmd = ("node \"" +
      sublime.packages_path()+ "/HTMLPrettify/scripts/run.js\" " + "\"" + 
      self.view.file_name() +  "\""
        " indent_size:\ 2" +
        " indent_char:\ ' '" +
        " max_char:\ 80" +
        " brace_style:\ collapse")

    # adapt window version, test at windows xp, node0.6.6
    if('Windows' in platform.platform()):
      code, html = self.execCmdWin(strCmd)
    else:
      html = self.execCmd(strCmd)

    if len(html) > 0:
      self.view.replace(edit, sublime.Region(0, self.view.size()), html.decode('utf-8'))
     