#!/bin/sh

# build envoy sidecars 

# build container s
cd containerA && sudo docker build --tag container_a .
cd ../
cd containerB && sudo docker build --tag container_b .
cd ../
cd containerC && sudo docker build --tag container_c .
