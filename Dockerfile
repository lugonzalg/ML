FROM python:3

RUN apt-get update && apt-get install -y \
    man \
    make \
    vim \
    git \
    curl \
    less \
    zsh

RUN  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" --unattended

CMD ["zsh"]
