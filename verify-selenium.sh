#! /usr/bin/env bash

locate webdriver
if [ $? = 0 ]
    then echo > log.txt "True"
    else echo > log.txt "False"
fi