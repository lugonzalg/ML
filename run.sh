#!/bin/bash

if [[ "$1" = "run" ]]; then
	docker run -ti -v ${PWD}:/tmp pyenv /bin/bash
elif [[ "$1" = "build" ]]; then
	docker build . -t pyenv
fi
