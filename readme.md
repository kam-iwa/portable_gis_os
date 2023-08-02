# Portable GIS OS

A script that allows you to build a Linux distribution image containing tools for working with spatial data. 

## Building an image

1. Install the programs `live-build` and `squashfs` on your Debian operating system using the following commands:
    - `apt install live-build`
    - `apt install squashfs`
2. Run the script from the `make_os.sh` file.
3. After the successful completion of the script, the Live CD image of the operating system will be located in the `live-image-amd64.iso` file inside the `ready_(timestamp)` directory.