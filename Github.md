- 1. How to add folders to the git repo?
"git add <folder>/*" and then commit
https://stackoverflow.com/questions/8775850/how-do-i-add-files-and-folders-into-github-repos

- 2. How to remove the file only from the git repo, but not remove it from the file system?
"git rm --cached filename" and then push changes to the remote repo. 
https://stackoverflow.com/questions/2047465/how-can-i-delete-a-file-from-git-repo

- 3. Remove directory from git and local:
git rm -r one-of-the-directories
git commit -m "Remove duplicated directory"
git push origin <your-git-branch> (typically 'master', but not always)

- 4. How  to create a folder in github repo website?
   - step1: go to the folder inside which you want to create another folder
   - step2: click on New file
   - step3: on the text field for the file name, first write the folder name you want to create, then type /, this creates a folder

- 5. If the file name has white space, when using git add, use " git add 'file name' ".




# Udacity course: A beginner's Git and GitHub tutorial

## Lesson 1: what is version control?

- See Part 4 of Lesson 1: Mac/Linux Setup (including installing git and configuring termial)

## Lesson 2: Create a Git repo

- Create course dictories and change the directory to it 

  ```
  mkdir -p udacity-git-course/new-git-project && cd $_
  ```
  Note: ```$_``` expands the last argument of the previous command ```mkdir -p```

- Git Init: Use the ```git init``` command to create a **new, empty repository** in the current directory. Running this command creates a hidden ```.git``` directory. This ```.git``` directory is the brain/storage center for the repository. It holds all of the configuration files and is where all of the commits are stored. Running ```git init``` multiple times doesn't cause any problems since it just re-initializes the Git directory.   

- Clone an existing repo
  - what is cloning? ```to make an identical copy```
  - The command is ```git clone``` and then you pass the path to the Git repository that you want to clone. For example, if we want to clone a blog project located at https://github.com/udacity/course-git-blog-project, the full command to clone this blog project is 
  ```git clone https://github.com/udacity/course-git-blog-project```
  - We can also clone project and use different name
  
  ```git clone https://github.com/udacity/course-git-blog-project blog-project```
  
  - ```git clone``` can only clone repo at Github. It can not clone directories in the local computer. 

- Determine a repo's status
  - The ```git status``` is the key to the mind of Git. It will tell us what Git is thinking and the state of our repository as Git sees it. When you're first starting out, you should be using the ```git status``` command all of the time. 
  
## Lesson 3: Review a repo's history 
- Git log: ```git log``` command is used to display all of the commits of a repository. By default, this command displays: 
  - the SHA
  - the author
  - the date
  - and the message
- ```git log --oneline```: the ```-oneline``` flag is used to alter how ```git log``` displays information. This command lists one commit per line, shows the list 7 characters of the commit's SHA, and shows the commit's message.   
 
- ```git log --stat```: the ```--stat``` flag is used to alter how ```git log``` displays information. This command:
    - displays the files that have been modified
    - displays the number of lines that have been added/removed 
    - displays a summary line with the total number of modified files and lines that have been added/removed

- ```git log --patch``` or ```git log -p```: the ```-p``` flag is used to alter how ```git log``` displays information. This command adds the information to the default output: 
   - displays the files that have been modified 
   - displays the location of the lines that have been added/removed 
   - displays the actual changes that have been made
   
- ```git log -p <SHA>```: this command will start at that commit. Keep in mind that it will also show all of the commits that were maded prior to the supplied SHA. 

- ```git show <SHA>```: shows a specific commit. ```git show``` displays the commit, the author, the date, the commit message, and the patch information
   - ```git show``` can be used with ```--stat``` and ```-p```
   
## Lesson 4: Add commits to a repo

- ```git add```: the ```git add``` command is used to move files from the **working directory** to the **staging index**. This command:
   - takes a space-separated list of file names
   - alternatively, the period `.` can be used in place of a list of files to tell Git to add the current directory (and all nested files)

- ```git commit```: the command take files from the staging index and saves them in the repository. This command will open the code editor that is specified in your configuration. Inside the code editor, 
   - a commit message must be supplied
   - lines that start eith a ```#``` are comments and will not be recorded
   - save the file after adding a commit message
   - close the editor to make the commit
   
   We can also use ```git commit -m "<message>"```. 

- ```git diff```: the command is used to see changes that have been made but haven't been committed. 

- Having git igonre files: create a ```.gitignore``` file and add the file names we want to ignore in the file. The ```.gitignore``` file is used to tell Git about the files should not track. This file should be placed in the same directory that the ```.git``` directory is in. 
   
## Lesson 5: Tagging, Branching, and Merging

- Tagging
   - Running ```git tag -a <tagname>``` (e.g., ```git tag -a v1.0```) will tag the most recent commit. If we want to tag a commit that occurred farther back in the repo's history, we can use ```git tag -a v1.0 <SHA>```.  
   - A Git tag can be deleted with the ```-d``` falg and the name of the tag, e.g., ```git tag -d v1.0```. 
    
- Branching
  - ```git branch``` command is used to interact with Git's branches. It can be used to list all branch names in the repo, create new branches, and delete branches. 
  - Create a branch: ```git branch <branch name>```
  - The ```git checkout``` Command: when a commit is made, it will be added to the current branch. If we want to switch between branches, we need to use ```git checkout <branch name>```. It's important to understand how this command works. Running this command will: 1) remove all files and directories from the working directory that Git is tracking, and 2) go into the repository and pull out all of the files and directories of the commit that the branch points to.
  - ```git checkout -b <branch name1> <branch name2>```: for example, ```git checkout -b footer master``` command creates a new footer branch and have this footer branch start at the same location as the master branch. 
  - Delete a branch: ```git branch -d <branch name>```. The branch can be deleted only after the branch's changes have been merged. 
  - See all branches at once: ```git log --oneline --graph --all```
   
 - Merging  
   - The ```git merge <name-of-branch-to-merge-in>``` command is used to combine Git branches. When a merge happens, Git will:
     - look at the branches that it's going to merge
     - look back along the branch's history to find a single commit that both branches have in their commit history
     - combine the lines of code that were changed on the separate branches together
     - makes a commit to record the merge
     



