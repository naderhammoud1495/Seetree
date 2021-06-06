# Junior SW engineer task-seetree
In this assignment we implemented Flask -webserver that handles calculation of image statistics.
With the giving image we calculated different functions: min,max,mean,median and percentile.
Image statistics are common features in AI applications.

## Setup
Git all the files to a directory in your system.
```bash
git clone https://github.com/naderhammoud1495/Seetree.git
```

## RUN using Flask

Open the Command Prompt and enter "Seetree" folder.
To start the server, run the following:
```bash
py -m pip install -r requirements.txt
set FLASK_APP=seetree_task.py
python -m flask run 
```
Open https://127.0.0.1:5000 on your browser and start your trip in the website. 

## RUN using Dockerfile

Open the Command Prompt and enter "Seetree" folder.
To start the web, run the following to create the image for the docker:
```bash
docker build -t seetree-nader .
```
and then run the following to start the container:
```bash
docker run -d -p 5000:5000 seetree-nader
```
Navigate to this url in your browser: http://127.0.0.1:5000 . 

## RUN using docker-compose

Run the project in docker-compose with this command :
```bash
docker-compose up --build -d
```

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

You can only select p50 and if you want to check another percentage you should check by using a suitable routh directly.

## Examples
1. Request to /stats/IMG_1.jpg/min responds with the correct min value in the
   image.

2. Request to /stats/IMG_7.jpg/nader responds with 404 error code.

3. Request to /stats/IMG_113.jpg/min responds with 404 error code.

4. Request to /stats/IMG_4.jpg/p10 responds with the 10'th percentile of the image.

## The homepage: you want to choose a photo and a function:
![image](https://user-images.githubusercontent.com/57456841/120870071-9f1f4d00-c5a0-11eb-999a-adaeb79e3d03.png)

## /health : will respond with “OK” to any request:
![image](https://user-images.githubusercontent.com/57456841/120870231-1359f080-c5a1-11eb-8318-6d80670abbac.png)

## The server respond with error code 404 when you choose any wrong url:
![image](https://user-images.githubusercontent.com/57456841/120870477-b6ab0580-c5a1-11eb-8eb9-d155ed11f19d.png)

## The server respond with error code 404 if you choose an image that does not exist:
![image](https://user-images.githubusercontent.com/57456841/120870644-1bfef680-c5a2-11eb-8b4c-998cfa34206c.png)

## The server respond with error code 404 if you choose a function that does not exist:
![image](https://user-images.githubusercontent.com/57456841/120870732-52d50c80-c5a2-11eb-9f83-3162dd303cdf.png)

## Example:Request to /stats/IMG_6.jpg/max responds with the correct max value in the image:
![image](https://user-images.githubusercontent.com/57456841/120870967-15bd4a00-c5a3-11eb-9031-0ea1d76437df.png)

## Bonus solution:
I made a dictionary that save the images value , I don't have to wait until all the image processing done when I go another time to check the same image and that will save our time and make multiple identical requests more efficient.






