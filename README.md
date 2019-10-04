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
5. Replace the `package.json` file content with this:

```
{
  "author": "Canonical webteam",
  "license": "LGPL v3",
  "scripts": {
    "clean": "rm -rf node_modules yarn-error.log css static/css *.log *.sqlite _site/ build/ .jekyll-metadata .bundle",
    "watch": "watch -p 'static/sass/**/*.scss' -c 'yarn run build'",
    "build": "node-sass --include-path node_modules static/sass --source-map true --output-style compressed --output static/css && postcss --map false --use autoprefixer --replace 'static/css/**/*.css'",
    "format-python": "black --line-length 79 webapp",
    "lint-python": "flake8 webapp && black --check --line-length 79 webapp",
    "lint-scss": "sass-lint static/**/*.scss --verbose --no-exit",
    "serve": "./entrypoint 0.0.0.0:${PORT}",
    "test": "yarn run lint-scss && yarn run lint-python"
  },
  "dependencies": {
    "autoprefixer": "9.6.1",
    "node-sass": "4.12.0",
    "postcss-cli": "6.1.3",
    "sass-lint": "1.13.1",
    "vanilla-framework": "2.4.0",
    "watch-cli": "0.2.3"
  }
}
```

6. Open `requirements.txt` file and make sure you are using the latest version of [canonicalwebteam.flask-base](https://pypi.org/project/canonicalwebteam.flask-base/).

7. Change `PORT` number in the `.env` file.