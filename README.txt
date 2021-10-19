# Init poetry

poetry init

<in the prompt:>
package name: sub1
version 0.1.0
description: Example project with a fixed dependency on pandas pre-1.0.0
author: <skip>
licence: na
compatible python versions: 3.7.4

Would you like to define your main dependencies interactively? yes

Search for package to add (or leave blank to continue): pandas=0.25.3
Add a package: <enter>

Would you like to define your development dependencies interactively? no

Generated file

[tool.poetry]
name = "sub1"
version = "0.1.0"
description = "Example project with a fixed dependancy on pandas pre-1.0.0"
authors = ["Your Name <you@example.com>"]
license = "na"

[tool.poetry.dependencies]
python = "3.7.4"
pandas = "0.25.3"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) yes

# pyproject.toml is now made, now make poetry lock file
poetry lock

# manually add an entrypoint to pyproject.toml
[tool.poetry.scripts]
sub1 = 'sub1.sub1_pandas:print_pandas'
