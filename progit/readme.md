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
  
  
取消暂存的文件
git reset HEAD <file>... 来取消暂存    从暂存区回到修改区域

撤销对文件的修改
g checkout -- progit/readme.md   将文件恢复到未修改的状态。

  
查看远程仓库  git remote
指定选项 -v，会显示需要读写远程仓库使用的 Git 保存的简写与其对应的 URL。
  $ git remote -v
  originhttps://github.com/schacon/ticgit (fetch)
  originhttps://github.com/schacon/ticgit (push)
  

添加远程仓库
git remote add <shortname> <url>添加一个新的远程Git仓库，同时指定一个你可以轻松引用的简 写:
  $ git remote
    origin
  git remote add origin url(https://github.com/Zidoing/python_standard_lib.git)
  $ git remote add pb https://github.com/paulboone/ticgit
  $ git remote -v
  
  从远程仓库中抓取与拉取 就如刚才所见，从远程仓库中获得数据，可以执行:
  $ git fetch [remote-name]
  
推送到远程仓库 
git push origin master

查看远程仓库
➜  learning git:(master) ✗ git remote show origin
* remote origin
  Fetch URL: https://github.com/Zidoing/learning.git
  Push  URL: https://github.com/Zidoing/learning.git
  HEAD branch: master
  Remote branch:
    master tracked
  Local branch configured for 'git pull':
    master merges with remote master
  Local ref configured for 'git push':
    master pushes to master (local out of date)


远程仓库的移除与重命名
如果想要重命名引用的名字可以运行git remote rename去修改一个远程仓库的简写名。例如，想要将pb
重命名为paul，可以用git remote rename这样做:
  $ git remote rename pb paul
  $ git remote
  origin
  paul
  
  如果因为一些原因想要移除一个远程仓库 - 你已经从服务器上搬走了或不再想使用某一个特定的镜像了，又或者 某一个贡献者不再贡献了-可以使用git remote rm:
 
   $ git remote rm paul
  $ git remote
  
  
查看标签 git tag
创建标签 
Git 使用两种主要类型的标签:轻量标签(lightweight)与附注标签(annotated)。
在 Git 中创建一个附注标签是很简单的。最简单的方式是当你在运行 tag 命令时指定 -a 选项:
  $ git tag -a v1.4 -m 'my version 1.4'
  $ git tag
  v0.1
  v1.3
  
通过使用git show命令可以看到标签信息与对应的提交信息:
  $ git show v1.4
  tag v1.4
  Tagger: Ben Straub <ben@straub.cc>
  Date:   Sat May 3 20:19:12 2014 -0700
  my version 1.4
  commit ca82a6dff817ec66f44342007202690a93763949
  Author: Scott Chacon <schacon@gee-mail.com>
  Date:   Mon Mar 17 21:52:11 2008 -0700
      changed the version number
      
轻量标签
另一种给提交打标签的方式是使用轻量标签。轻量标签本质上是将提交校验和存储到一个文件中 - 没有保存任何 其他信息。创建轻量标签，不需要使用 -a、-s 或 -m 选项，只需要提供标签名字:
   $ git tag v1.4-lw
  $ git tag
  v0.1
  v1.3
  
 现在，假设在 v1.2 时你忘记给项目打标签，也就是在 “updated rakefile” 提交。你可以在之后补上标签。要 在那个提交上打标签，你需要在命令的末尾指定提交的校验和(或部分校验和):
  $ git tag -a v1.2 9fceb02


共享标签
默认情况下，git push命令并不会传送标签到远程仓库服务器上。在创建完标签后你必须显式地推送标签到共
享服务器上。这个过程就像共享远程分支一样-你可以运行git push origin [tagname]。
git push origin --tags

检出标签
在 Git 中你并不能真的检出一个标签，因为它们并不能像分支一样来回移动。如果你想要工作目录与仓库中特定 的标签版本完全一样，可以使用git checkout -b [branchname] [tagname]在特定的标签上创建一个 新分支:
  $ git checkout -b version2 v2.0.0
  Switched to a new branch 'version2'


给git创建快捷键


  $ git config --global alias.co checkout
  $ git config --global alias.br branch
  $ git config --global alias.ci commit
  $ git config --global alias.st status
  
  
  xxxxxxx
  
  sssss
