# Junior SW engineer task-seetree
In this assignment we implemented Flask -webserver that handles calculation of image statistics.
With the giving image we calculated different functions: min,max,mean,median and percentile.
Image statistics are common features in AI applications.

## Setup
Git all the files to a directory in your system.
```bash
git clone https://github.com/naderhammoud1495/SeeTree.git
```

## RUN using Flask

Open the Command Prompt and enter "SeeTree" folder.
To start the server, run the following:
```bash
py -m pip install -r requirements.txt
set FLASK_APP=main.py
python -m flask run 
```
Open https://127.0.0.1:5000 on your browser and start your trip in the website. 

## RUN using Dockerfile

Open the Command Prompt and enter "SeeTree" folder.
To start the web, run the following to create the image for the docker:
```bash
docker build -t seetree-nader .
```
and then run the following to start the container:
```bash
docker run -d -p 5000:5000 seetree-nader
```
Navigate to this url in your browser: https://127.0.0.0:5000 . 

## The Supported URLs after starting the application:
* http://127.0.0.1:5000/ 
  home page with all the images
* http://127.0.0.1:5000/health
  that returns OK to any request.
* http://127.0.0.1:5000/stats/IMAGE_FILE_NAME/FUNC_NAME
  while IMAGE_FILE_NAME is the Image name and FUNC_NAME is your required function. 

## Explanation
this web will calculate FUNC_NAME on the pixels of given IMAGE_NAME and return the result.
 Supported FUNC_NAMES are:
a- min : computes the minimum of image pixel values                                                                                                     
                                                                                         
b- max:  computes the maximum of image pixel values                                                                                                                                                 
c- mean: computes Average (arithmetic mean) pixel level in the image.                                                  
d- median: computes the median/middle of image pixel values                                                                       
e-  pXXX where XXX is a percentile between 0...100 :                                                           
For example p10 is the 10th percentile of the image, p80 is the 80th percentile                          

## Examples
1. Request to /stats/IMG_1.jpg/min responds with the correct min value in the
   image.

2. Request to /stats/IMG_7.jpg/nader responds with 404 error code.

3. Request to /stats/IMG_113.jpg/min responds with 404 error code.

4. Request to /stats/IMG_4.jpg/p10 responds with the 10'th percentile of the image.
  

