# Ming's personal website

[![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/dd9e34b0/myli.page)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/tslmy/tslmy.github.io/main.svg)](https://results.pre-commit.ci/latest/github/tslmy/tslmy.github.io/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


`scrape.py` scrapes several websites for some personal metrics. It saves the data to `data.yaml`. I plan to have the data populated to the index page.


The Website is statically generated with [Jekyll](https://jekyllrb.com/). To serve it locally, run:

```shell
bundle exec jekyll serve
```

## Contributing
This repo uses [pre-commit hooks](https://pre-commit.com/) to automate many checks upon making a git commit. (See `.pre-commit-config.yaml` for a list of all hooks enabled.) Assuming you have [Homebrew](https://brew.sh/) installed, you can install the `pre-commit` program via:


```shell
brew install pre-commit
```

Then, install the pre-commit hooks via:

```shell
pre-commit install
```
