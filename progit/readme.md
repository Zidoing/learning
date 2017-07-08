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
  
  
 分支创建
Git 是怎么创建新分支的呢?很简单，它只是为你创建了一个可以移动的新的指针。比如，创建一个 testing 分
支，你需要使用git branch命令: $ git branch testing

  
  xxxxxxx
<<<<<<< HEAD
  
<<<<<<< HEAD
  fdasfdsa
  fdsfas
  
  sssss

分支切换
要切换到一个已存在的分支，你需要使用git checkout命令。我们现在切换到新创建的testing分支去:
 $ git checkout testing


新建分支并切换
$ git checkout -b iss53
  Switched to a new branch "iss53"

分支合并
git merge hotfix        hotfix分支名字  将分支hotfix合并到当前分支上

删除分支
git branch -d hotfix

遇到冲突时的分支合并
$ git merge iss53
  Auto-merging index.html
  CONFLICT (content): Merge conflict in index.html
  Automatic merge failed; fix conflicts and then commit the result.
此时 Git 做了合并，但是没有自动地创建一个新的合并提交。Git 会暂停下来，等待你去解决合并产生的冲突。 你可以在合并冲突后的任意时刻使用git status命令来查看那些因包含合并冲突而处于未合并 (unmerged)状态的文件:
  $ git status
  On branch master
  You have unmerged paths.
    (fix conflicts and run "git commit")
  Unmerged paths:
    (use "git add <file>..." to mark resolution)
      both modified:      index.html
  no changes added to commit (use "git add" and/or "git commit -a")
  
  解决冲突后  git add命令来将其标记为冲突已解决。一旦暂存这 些原本有冲突的文件，Git 就会将它们标记为冲突已解决。
  然后 git commit
  
分支详细信息
  ➜  learning git:(master) ✗ gb -v
  bb     54306cd [progit] page xxxx
* master 33a312d [ahead 8] [progit] page 70

--merged 与 --no-merged 这两个有用的选项可以过滤这个列表中已经合并或尚未合并到当前分支的分支。如 果要查看哪些分支已经合并到当前分支，可以运行git branch --merged:
当查看到已经merged的分支可以直接删除掉
当未合并的分支删除时候直接删除会报错，如果一定要删的话要加强制删除git branch -D testing



git fetch origin  
如果要同步你的工作，运行git fetch origin命令。这个命令查找“origin”是哪一个服务器(在本例 中，它是 git.ourcompany.com)，从中抓取本地没有的数据，并且更新本地数据库，移动 origin/master 指针指向新的、更新后的位置。

“推送本地 的 serverfix 分支，将其作为远程仓库的 serverfix 分支”可以通过这种格式来推送本地分支到一个命名不相同的 远程分支。如果并不想让远程仓库上的分支叫做serverfix，可以运行git push origin serverfix:awesomebranch 来将本地的 serverfix 分支推送到远程仓库上的 awesomebranch 分支。

git push origin master:dev  在远程创建一个分支并把master推送上去
git push origin :dev 删除远程分支上的dev
git push origin --delete dev 删除远程上的分支
  
 
git merge origin/master 将远程分支上的文件合并到本地本质来 

在远程分支上创建新的分支
$ git checkout -b serverfix origin/serverfix

```
跟踪分支   git branch -vv 查看详细情况
```
git checkout -b sf origin/master 直接跟踪远程
git checkout -b sf master 不会跟踪远程

git branch -u origin/master 将当前没有跟踪远程的分支跟踪远程master

git push -u origin featureA 直接推送到远程并给他增加分支追踪

   $ git checkout experiment
  $ git rebase master
  First, rewinding head to replay your work on top of it...
  Applying: added staged command
去分支上rebase master  后会在就会在主分支后面
然后去主分支merge 一下之前的分支

使用git rebase [basebranch] [topicbranch]命 令可以直接将特性分支(即本例中的 server)变基到目标分支(即 master)上。这样做能省去你先切换到 server 分支，再对其执行变基命令的多个步骤。
  $ git rebase master server

- 句号也是可以的。
- 项目符号可以使用典型的连字符或星号 前面一个空格，之间用空行隔开， 但是可以依据不同的惯例有所不同。


git fetch origin
git merge origin/master
$ git push origin master


$ git remote add myfork (url) 
$ git push -u myfork featureA

xxxxxx
