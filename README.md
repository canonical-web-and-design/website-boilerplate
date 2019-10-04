# Canonical-Webteam-Website-Boilerplate
This is a flask website boilerplate

## Usage

1. Clone this repo and rename the directory name.

```bash
git clone {link-to-this-repo}
mv Canonical-Webteam-Website-Boilerplate {new-project-directory}
```

2. Install [Yeoman](http://yeoman.io) and generator-canonical-webteam using [npm](https://www.npmjs.com/) globally.

```bash
npm install -g yo generator-canonical-webteam
```

3. Run the generator scripts *from within a project directory* to create or upgrade parts of the project:

```bash
cd {new-project-directory}
yo canonical-webteam:{script-name}
```

4. Open `requirements.txt` file and make sure you are using the latest version of [canonicalwebteam.flask-base](https://pypi.org/project/canonicalwebteam.flask-base/)

## Scripts

Each of these scripts can either be used to create new files or to update existing ones:

### run

``` bash
yo canonical-webteam:run
```

This installs [a `./run` script](generators/run-basic/templates/run) which will use [docker-yarn](https://github.com/canonical-webteam/docker-yarn) to automatically manage [NPM dependencies](https://docs.npmjs.com/files/package.json#dependencies) and run standard [NPM scripts](https://docs.npmjs.com/misc/scripts) defined in a [package.json](https://docs.npmjs.com/files/package.json).

``` bash
$ ./run --help

Usage
===

  $ ./run \
    [-m|--node-module PATH]  # A path to a local node module to use instead of the installed dependencies \
    [COMMAND]                # Optionally provide a command to run

If no COMMAND is provided, `serve` will be run.

Commands
---

- serve [-p|--port PORT] [-w|--watch] [-d|--detach]: Run `yarn run serve` (optionally running `watch` in the background) \
- watch: Run `yarn run watch`
- build: Run `yarn run build`
- test: Run `yarn run test`
- stop: Stop any running containers
- yarn <args>: Run yarn
- clean: Remove all images and containers, any installed dependencies and the .docker-project file
- clean-cache: Empty cache files, which are saved between projects (eg, yarn)
```