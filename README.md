## Welcome to GitHub Pages.

You can use the [editor on GitHub](https://github.com/rg-28/DROOM/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/rg-28/DROOM/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.


# DROOM 
#### A plant disease detecting bot

**Students:** Dinesh <br/>
              Hemant <br/>
              Pranjal Shukla <br/>
              Priyadarshan Roy <br/>
              Rajan Gupta <br/>
              Shubhra Mittal
              
**Mentors:** Dr. Garima Joshi <br/> 
             Pranav Kumar 
             
**Code:**

## Objective 

- The primitive aim of the project is to detect and identify any sort of disease that originates in plants, without any kind of human interaction with the crops in the agricultural field. 
- Secondly, the data is to be sent to a local server for further processing by a software. 
- Thirdly, if there is any kind of discrepancy in the data, alert notification will be sent to the owner of the agricultural field.

## Introduction

### Problem Statement 
Now-a-days, due to the increased number of diseases in the agricultural fields across the crops, the production of the desired product is decreasing at a significant rate. This is to be tackled in a professional manner with correct use of efficient and economically stable technology. This can maneuver the agricultural production in a positive manner.

### Existing Technologies 
- There are few technologies which use visual inspection of plant germplasm and subsequent selection of healthy material. There are  technologies such as serodiagnostics, cytometry, real-time PCR. 
- The technology i.e. the bot that we will be using will not require any human interaction with the crops in the field.


## Project Overview 

### Block Diagram 

There are a few technologies which use Visual inspection of plant germplasm and subsequent selection of healthy materials. There are technologies such as sero-diagnostics, cytometry and real time PCR.

In our bot, image of the plant is captured through the camera which is controlled with the help of a gyroscope and servo motors. The gyroscope helps in stabilization of the camera and the servo motors provide the camera, a field of view through which the data is collected. The collected data is fed to the Raspberry Pi, which is our prime microcontroller used in this project. To the Raspberry Pi are connected a Magnetometer, GPS and Ultrasonic sensor. The magnetometer allows the bot to navigate through the field and the GPS gives the data of the current location in which the disease has been detected. The ultrasonic sensor plays a vital role of obstacle detection for the bot.

The bot primarily consists of 6 Motors in which four of them are the driving motors and two Servo Motors are attached for steering purposes. The Motors used in this project are simple Johnson Motors with 100 RPM, because this particular Motor provides an adequate speed for perfect detection of diseases in plant through the camera. Once the data is collected it is been uploaded to a server where the machine is trained to identify the disease and prescribe the accurate diagnosis to that particular disease. The machine is trained accordingly such that it also recommends the accurate brand for that particular disease and the nearest place where it is available.


## Detailed Discription 

### Components 

#### Hardware 
#### Software

### Timeline 

### Progress Till now
  Day 1: Discussion of basic outline of the project; selection of components, both hardware and software; preparation of timeline. <br/>
  Day 2: Familiarization with hardware. <br/>
  Day 3: Setting up of Raspberry pi. 


## Final Goals 

## Future Scope 
