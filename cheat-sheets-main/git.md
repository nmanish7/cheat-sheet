
### Git Introduction
---

1. Generate a new SSH key:

	```shell
		ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
	```

1.  Initialize the Git repository:

	```shell
		git init
	```

1. Get local configuration
	```shell
		git config --list --local
	```

3.  Set the local SSH command for Git:

	```shell
		git config --local core.sshCommand "ssh -i ~/.ssh/id_rsa_repo -F /dev/null"
	```

1. Set local user name
	```shell
		git config --local user.name "Your Name"
	```
1. Set local email
	```shell
		git config --local user.email "youremail@example.com"
	```

3.  Clone the repository:

	```shell
		git clone git@github.com:user/repo.git
	```

1. Add the remote URL for the repository:

	```shell
		git remote add <name> <url>
		git remote add origin git@github.com:<username>/<reposito.git>
	```

1. To list remote repositories
	```shell
		git remote -v
	```

1. Fetch Changes from remote repositories
	```shell
		git fetch
	```
1.  Add all files to the staging area:

	```shell
		git add .
	```

6.  Commit the changes:

	```shell
		git commit -m "Initial commit"
	```

7.  Switch to the master branch:

	```shell
		git checkout master
	```

8.  Rename the master branch to main:

	```shell
		git branch -m main
	```

10.  Push the changes to the remote main branch:

		```shell
		git push orig main
		```

11.  If you encounter an unrelated histories error, use the `--allow-unrelated-histories` option to pull changes from the remote main branch:


		```shell
		git pull origin main --allow-unrelated-hiries
		```


### Git Useful Command
---

#### Configuration

1. **Set user name**
	```shell
		git config --global user.name "Your Name"
	```
1. **Set email**
	```shell
		git config --global user.email "youremail@example.com"
	```
1. **Check Setting**
	```shell
		git config --list
	```
1. **Set default editor**
	```shell
		git config --global core.editor nano
	```

#### Repository Setup
1. **Create new repository**
	```shell
		git init
	```
1. **Clone a repository**
	```shell
		git clone <repo-url>
	```
1. **Add remote repository**
	```shell
		git remote add <name> <repo-url>
		git remote add origin  git@github.com:nmanish7/demo.git
	```
1. **Change remote repository url**
	```shell
		git remote set-url <name> <repo-url>
		git remote set-url origin git@github.com:nmanish7/demo.git
	```
1. **List remote repositories**
	```shell
		git remote -v
	```

#### Basic Workflow
1. **Check status**
	- *Shows the status of the current branch, including any changes made to files and whether they have been staged or not.*
	```shell
		git status
	```
1. **Add changes to staging area**
	```shell
		git add <file>
	```
1. **Commit changes**
	```shell
		git commit -m "Commit message"
	```
1. **Push changes**
	- *Pushes changes from the local repository to a remote repository.*
	```shell
		git push
	```
1. **Pull changes**
	- *Fetches changes from a remote repository and merges them into the current branch.*

	```shell
		git pull
	```
1. **Fetch changes**
	- *Fetches changes from a remote repository, but does not merge them into the current branch.*
	```shell
		git fetch
	```


#### Branching

1. **Create new branch**
	```shell
		git branch <branch-name>
	```
1. **Switch to branch**
	- *Allows you to switch between branches or reset files to a previous commit.*
	```shell
		git checkout <branch-name>
	```
1. **Create and switch to branch**
	```shell
		git checkout -b <branch-name>
	```
2. **List branches**
	- *Lists all the branches in the repository, and shows which branch is currently checked out.*
	```shell
		git branch
	```
3. **Renaming current Branch**
	```shell
		git branch -m <new-branch-name>
	```
4. **Merge branch into current branch**
	- *Merges changes from one branch into another. For example, if you have made changes in a feature branch and want to merge them into the main branch, you would switch to the main branch and run `git merge feature_branch`.*

	```shell
		git merge <branch-name>
	```
5. **Delete branch**
	```shell
		git branch -d <branch-name>
	```
6. **Force delete branch**
	```shell
		git branch -D <branch-name>
	```

#### Stashing
1. **Save changes to stash**
	```shell
		git stash save "Message"
	```
1. **List stashes**
	```shell
		git stash list
	```
2. **Apply latest stash**
	```shell
		git stash apply
	```
3. **Apply specific stash**
	```shell
		git stash apply stash@{2}
	```
1. **Delete latest stash**
	```shell
		git stash drop
	```
2. **Delete specific stash**
	```shell
		git stash drop stash@{2}
	```

#### Undoing Changes
1. **Discard changes in working directory**
	```shell
		git checkout -- <file>
	```
1. **Unstage file**
	```shell
		git reset HEAD <file>
	```
2. **Undo commit**
	```shell
		git reset HEAD~
	```
3. **Discard all changes since last commit**
	```shell
		git reset --hard HEAD
	```
4. **Revert Commit**
	- *Creates a new commit that undoes the changes made in a previous commit.*
	```shell
		git revert <commit-hash>
	```

#### Miscellaneous
1. **Show commit history**
	- *Shows a list of all the commits made to the current branch, including the commit message, author, and timestamp.*
	```shell
		git log
	```
1. **Show differences between files**
	```shell
		git diff <file>
	```
2. **Show difference between commits**
	```shell
		git diff <commit1> <commit2>
	```
3. **Create a new commit from selected changes**
	```shell
		git cherry-pick <commit-hash>
	```
4. **Configure global ignore file**
	```shell
		git config --global core.excludesfile ~/.gitignore_global
	```
5. **Show file history**
	```shell
		git log -- <file>
	```



### References
---
> [GIT Cheatsheet Pdf](./data/git-ultimate-guide.pdf)
