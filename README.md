# Canonical-Webteam-Website-Boilerplate
This is a flask website boilerplate

## Usage

1. Click `Use this template` button to create a new repo from this one. [More info here](https://help.github.com/en/articles/creating-a-repository-from-a-template). 

2. Clone the new repository locally.

```bash
git clone {link-to-the-new-repo}
```

3. Install [Yeoman](http://yeoman.io) and generator-canonical-webteam using [npm](https://www.npmjs.com/) globally.

```bash
npm install -g yo generator-canonical-webteam
```

4. Run the generator scripts *from within the project directory* to create or upgrade parts of the project:

```bash
cd {new-project-directory}
yo canonical-webteam:run
```

5. Open `requirements.txt` file and make sure you are using the latest version of [canonicalwebteam.flask-base](https://pypi.org/project/canonicalwebteam.flask-base/)
