Overview
========

A script outputs Company Name based on the provided MAC address.
A source of data: (https://macaddress.io)


How to
======

[1] The account has to be created on https://macaddress.io.

[2] Create the following environment variable:

    export TOKEN=<API key>

[3] Upload the script

    git clone https://github.com/MTuradek/maclkp.git maclkp

[4] Build the image and run command in a container

    cd maclkp
    docker build -t maclkp .
    docker run --rm --env TOKEN maclkp <MAC>
