lint-all: lint-html lint-scss
fix-all: fix-scss

lint-html:
    #!/usr/bin/env bash
    set -euo pipefail
    IFS=$'\n\t'
    files="$(find . -name "*.html" -type f | tr '\n' ' ')"
    echo "Validating HTML files: $files"
    docker run --platform linux/amd64 -it --rm -w /app -v $PWD:/app ghcr.io/validator/validator:latest vnu $files

lint-scss:
    npx stylelint './**/*.scss'

fix-scss:
    npx stylelint './**/*.scss' --fix
