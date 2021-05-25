Title: How To Set GitHub Page
Date: 2020-1-15
Modified: 2020-1-16
Tags: pelican, github
Authors: Audrey Wang

---

<br />

# About Pelican
[Pelican](http://docs.getpelican.com/en/) is a utility that lets you create beautiful weblogs using just text files. [Github Pages](https://pages.github.com/) allows users to store page content in a git repository along with their code. By combining Pelican with Github Pages, you can have a reliable and attractive blog site for your projects.

<br />

# Steps
## 1. Create a repository on GitHub
Head over to GitHub and create a new repository named `username.github.io`, where `username` is your username (or organization name) on GitHub. Note that this repository should be public.

![]({static}/pictures/1.png){:width="600px"}

<br />

## 2. Clone the repository
Go to the folder where you want to store your project, and clone the new repository:
```text
$ git clone https://github.com/username/username.github.io
$ cd username.github.io
```

<br />

## 3. Create new branch
When you enter `https://username.github.io`, what will happen? And how can GitHub detect your html file in repository? In fact, GitHub automatically detects `index.html` file from the master branch, and presents this file as your website entrance. Therefore, we need place our page files (the output/ folder in pelican) in master branch. I strongly prefer not to keep all the Pelican configuration files and raw Markdown files in master branch. So I keep the Pelican configuration and the raw content in a separate branch I like to call **source**.
```text
$ git checkout -b source
Switched to a new branch 'source'
```

<br />

## 4. Configure Pelican
Now it's time for content configuration. Pelican provides a great initialization tool called pelican-quickstart that will ask you a series of questions about your blog.
```text
$ pelican-quickstart
```
You can take the defaults on every question except:

- Website title (which should be unique and special)
- Website author (which can be a personal username or your full name)
- Time zone (Such as Asia/Shanghai)
- Upload to GitHub Pages, which is a "y" in our case

<br />

## 5. Add pelican files to the source branch
Add all the Pelican-generated files to the content branch of the local Git repo, commit the changes, and push the local changes to the remote repo hosted on GitHub by entering:
```text
$ git add .
$ git commit -m 'initial pelican commit to content'
$ git push origin content
```

<br />

## 6. Write content
Now you can get bloggy! All of your blog posts, photos, images, PDFs, etc., will live in the content directory, which is initially empty. We can use Markdown syntax. To begin creating a first post, enter:
```text
$ cd content
$ touch first-post.md
```
Next, open the empty file first-post.md in your favorite text editor and add the following:
```text
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.  
```
You can also have your own metadata keys (so long as they don’t conflict with reserved metadata keywords) for use in your templates. The following table contains a list of reserved metadata keywords:
![]({static}/pictures/2.jpg){:width="600px"}

<br />

## 7. Install ghp-import
```text
$ pip install pelican ghp-import Markdown
```

<br />

## 8. Publish
All that's left to do is:

- Run Pelican to generate the static HTML files in output. `-r` is to enable watching for your modifications, instead of manually re-running it every time you want to see your changes. 
```text
$ pelican content -s pelicanconf.py -r
```
- Use ghp-import to add the contents of the output directory to the master branch:
```text
$ ghp-import -m "Generate Pelican site" --no-jekyll -b master output
```
- Push the local master branch to the remote repo:
```text
$ git push origin master
```
- Commit and push the new content to the content branch:
```text
$ git add content
$ git commit -m 'added a first post, a photo and an about page'
$ git push origin content
```

<br />

## 9. Finally!
Now the exciting part is here when you get to view what you've published for everyone to see! Open your browser and enter: *https://username.github.io*

<br />

# References
1. Another useful blog: [https://opensource.com/article/19/5/run-your-blog-github-pages-python](https://opensource.com/article/19/5/run-your-blog-github-pages-python)
2. Pelican document: [https://docs.getpelican.com/en/stable/quickstart.html](https://docs.getpelican.com/en/stable/quickstart.html)