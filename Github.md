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
- Git Init

Use the ```git init``` command to create a **new, empty repository** in the current directory. Running this command creates a hidden ```.git``` directory. This ```.git``` directory is the brain/storage center for the repository. It holds all of the configuration files and is where all of the commits are stored.  
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





   
   
   
   
   
   
   
   



