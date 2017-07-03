progit学习

文件3种状态
已提交 commit
已修改 modify
已暂存 

git config 
/.gitconfig  /git/config 查看文件配置

git clone  url  localdir 克隆并重新命名文件夹

文件 .gitignore 的格式规范如下:
• 所有空行或者以 # 开头的行都会被 Git 忽略。
• 可以使用标准的 glob 模式匹配。
• 匹配模式可以以(/)开头防止递归。
• 匹配模式可以以(/)结尾指定目录。
• 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号(!)取反。
https://github.com/github/gitignore/blob/master/Python.gitignore
python忽略的文件集合

git diff  此命令比较的是工作目录中当前文件和暂存区域快照之间的差异，也就是修改之后还没有暂存起来的变化内容。
git diff --staged 查看下次要提交的内容


git commit -am 跳过暂存区直接添加并提交

git rm file --cached 从暂存区删除文件
git rm file   --> git commit 从版本库删除不进行后续跟踪


$ git mv file_from file_to 
相当于
$ mv README.md README
$ git rm README.md
$ git add README


git log 
一个常用的选项是 -p，用来显示每次提交的内容差异。你也可以加上 -2 来仅显示最近两次提交:
git log --stat 显示简略的信息
(learnenv) ➜  learning git:(master) ✗ git log --pretty=oneline
(learnenv) ➜  learning git:(master) ✗ git log --pretty=full   
(learnenv) ➜  learning git:(master) ✗ git log --pretty=short
(learnenv) ➜  learning git:(master) ✗ git log --graph    
-p
按补丁格式显示每个更新之间的差异。
--stat
显示每次更新的文件修改统计信息。
--shortstat
只显示 --stat 中最后的行数修改添加移除统计。
--name-only
仅在提交信息后显示已修改的文件清单。
--name-status
显示新增、修改、删除的文件清单。
--abbrev-commit
仅显示 SHA-1 的前几个字符，而非所有的 40 个字符。
--relative-date
使用较短的相对时间显示(比如，“2 weeks ago”)。
--graph
显示 ASCII 图形表示的分支合并历史。
--pretty
使用其他格式显示历史提交信息。可用的选项包括 oneline，short，full，fuller 和 format(后跟指定格式)。


撤销操作

文本编辑器启动后，可以看到之前的提交信息。编辑后保存会覆盖原来的提交信息。
例如，你提交后发现忘记了暂存某些需要的修改，可以像下面这样操作:
  $ git commit -m 'initial commit'
  $ git add forgotten_file
  $ git commit --amend
  