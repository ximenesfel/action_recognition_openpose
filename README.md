# Configuration

- **OS:** Linux [Ubuntu 16.04 LTS - 64 bits]
- **GPU:** NVIDIA GeForce GTX 1060 (6GB)
- **Memory:** 16 GB
- **Processor:** Intel Core i7 (7th Gen)

# Installation 

1. Install openpose using this [installation procedure](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation.md).
2. Install *virtualenv* using step #3 from this [post](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/).
3. Download *requirement.txt file* in this [link](https://www.dropbox.com/s/50hgmrnyz7shgpy/requirements.txt?dl=0).
4. Create a new env using this command ```mkvirtualenv "name_env" -p python3 ``` change *"name_env"* for your choice name.
5. Enter inside env: ```workon "name_env" ```.
6. Install dependences: ```pip -r requirements.txt```.
7. Clone this respository using ``` git clone ``` command.

# Usage

### To write json files from videos

- Open `write_json_from_video.py` and fill this variables: `path_videos` (path to your videos folder) and `path_output_data` (path where you like to save json data). Please insert all path. Ex: `/home/"user"/Desktop/....`.
- Run ```python write_json_from_videos.py```.


### Obtain database from json files 

- Open `generate_data.py` and fill the variable `path_data` (path where you save json files). Please insert all path. Ex: `/home/"user"/Desktop/....`.
- Run ```python generate_data.py```.
- The file `database.dat` will be saved in your current directory with all data from json's files.
