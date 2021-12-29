# {{ cookiecutter.project_name }}

## Project info
### Purpose of project
A brief description for the project
### Sourcing the data
Please include any details (if any) for sourcing the data, if not already part of the pipeline
### Instructions for running the pipeline
If `kedro run` is not the only step needed, please explain how the pipeline should be run

## Overview

This is your new Kedro project, which was generated using `Kedro 0.17.6`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/12_faq/01_faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

### Naming convention for data
The nodes should have outputs in the corresponding data folders, i.e. the nodes that are part of the `primary_pipeline`
under `src/<package_name>/pipeline.py` should import function(s) from `src/<package_name>/nodes/03_primary.py` and 
should output datasets to the `data/03_primary` folder.

Data folder/node | Purpose |
--- | --- | 
01_raw | Raw datasets/ direct downloads from s3 or Athena query results |
02_intermediate | Basic renaming of columns and defining dtypes |
03_primary | Joining dataframes, basic NaN filling that will not be experimented in model fitting |
04_feature | Feature engineering |
05_model_input | Split of X/y and train/test; set index of dataframes as you see fit |
06_models | Save model, attach predictions to datasets, SHAP values, model evaluation |
07_model_output | Impact of model on metrics, SHAP values, model evaluation |
08_reporting | YOLO |


## Create a new virtual environment
### Using pyenv
```shell
pyenv virtual env <any python version you have installed> <venv name>
# if not already here, navigate with your terminal to this project
pyenv local <venv name>
# this should have created a .python-version file with the only content being the name of the venv
# every time you navigate into this project now the virtual env should activate itself
```

### Using virtualenv
```shell
# install virtualenv package if not already installed
pip install virtualenv
# if not already here, navigate with your terminal to this project
# create the virtual environment
virtualenv <venv name>
# this should create a new folder called <venv name> under the project root
# open the /gitignore file and add <venv name> to it so that it is excluded from the commits
# make sure you activate the environment before install dependencies or running kedro
```

### Set up PyCharm
* PyCharm -> Preferences (`⌘,`)
* Click on Project -> Python Interpreter
* Choose the virtual env you have just created (most likely need to find the python<version> file within the bin folder)

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.
If it's a newly created venv, you will need to install the basic dependencies, which include kedro:
```shell
pip install -r src/requirements.txt
# if you also need to use athena/s3 run the command below
pip install -r src/private-requirements.txt
```


## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

## Project dependencies

To generate or update the dependency requirements for your project:

```
kedro build-reqs
```

This will copy the contents of `src/requirements.txt` into a new file `src/requirements.in` which will be used as the source for `pip-compile`. You can see the output of the resolution by opening `src/requirements.txt`.

After this, if you'd like to update your project requirements, please update `src/requirements.in` and re-run `kedro build-reqs`.

[Further information about project dependencies](https://kedro.readthedocs.io/en/stable/04_kedro_project_setup/01_dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, `catalog`, and `startup_error`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `kedro install` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to convert notebook cells to nodes in a Kedro project
You can move notebook code over into a Kedro project structure using a mixture of [cell tagging](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#release-5-0-0) and Kedro CLI commands.

By adding the `node` tag to a cell and running the command below, the cell's source code will be copied over to a Python file within `src/<package_name>/nodes/`:

```
kedro jupyter convert <filepath_to_my_notebook>
```
> *Note:* The name of the Python file matches the name of the original notebook.

Alternatively, you may want to transform all your notebooks in one go. Run the following command to convert all notebook files found in the project root directory and under any of its sub-folders:

```
kedro jupyter convert --all
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.


## Deployed pipelines
Dockerfiles have been included as starting templates:
* `Dockerfile` for the actual image to be used in ECR
* `Dockerfile.dev` for local testing of the image prior to pushing the prod image to ECR
### Building the image
Run the below commands to add ssh config and build the image
```shell script
export DOCKER_BUILDKIT=1  
eval 'ssh-agent'
ssh-add ~/.ssh/id_rsa
docker build -t <image-tag> --ssh default=$SSH_AUTH_SOCK .
# or use the following if building the test image
# --no-cache ensures everything is rebuilt (for example mm_kedro is re-downloaded)
docker build -t <image-tag> --no-cache --ssh default=$SSH_AUTH_SOCK -f Dockerfile.dev .
# docker build -t <image-tag>-test --ssh default=$SSH_AUTH_SOCK -f Dockerfile.dev .
```
Running the test image (env variables already set there)
```shell
docker run -v ~/.aws/:/home/kedro/.aws/ <image-tag>-test
```

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/03_tutorial/05_package_a_project.html)
