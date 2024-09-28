lint-all: format-check lint-scss
fix-all: fix-scss format-all

format-all:
    npx prettier . --write
    isort .
    black .
    flake8 .

format-check:
    npx prettier . --check

lint-scss:
    npx stylelint './**/*.scss'

fix-scss:
    npx stylelint './**/*.scss' --fix
