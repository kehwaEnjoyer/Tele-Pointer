
<a id="readme-top"></a>




<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kehwaEnjoyer/Tele-Pointer">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Tele-Pointer</h3>

  <p align="center">
    A project designed to allow the control of the cursor through the webcam using Mediapipe and opencv.
    <br />
    <a href="https://github.com/kehwaEnjoyer/Tele-Pointer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kehwaEnjoyer/Tele-Pointer">View Demo</a>
    &middot;
    <a href="https://github.com/kehwaEnjoyer/Tele-Pointer/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/kehwaEnjoyer/Tele-Pointer/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Google MediaPipe][Mediapipe-url]
* [OpenCV][OpenCV-url]
* [evdev][evdev-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

## Setup

### 1. Create a Python virtual environment

```sh
python3 -m venv venv
```

### 2. Create and activate virtual enviroment

```sh
source venv/bin/activate
```

### 3. Upgrade pip

```sh
python -m pip install --upgrade pip
```

### 4. Install dependencies

```sh
pip install opencv-python mediapipe evdev
```

### 5. Verify installations

```sh
python -c "import cv2, mediapipe, evdev; print('All dependencies installed successfully!')"
```


### Execution

1. Clone the repo
   ```sh
   git clone https://github.com/kehwaEnjoyer/Tele-Pointer.git
   ```
2. Execution: run the execution.py file with python

   ```sh
   python execution,py
   ```

3. Notes:
  permissions may need to be set around Uinput for evdev to work

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

 In this project both hands are used to control the cursor on screen.
 The left hand is used as the mode identifier while the the right is used to issue commands

1. Left hand index finger up (pointing up):
    move right hand around to control the position of the cursor.
    connect thumb and index tip to left click.
    connect thumb and middle tip to right click.

2. Left hand index and middle finger up (peace sign):
    move right hand up to scroll up and vice versa.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/kehwaEnjoyer/Tele-Pointer/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are much welcomed.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/kehwaEnjoyer/Tele-Pointer/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kehwaEnjoyer/Tele-Pointer" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

 yahyasmughal@gmail.com

Project Link: [https://github.com/kehwaEnjoyer/Tele-Pointer](https://github.com/kehwaEnjoyer/Tele-Pointer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kehwaEnjoyer/Tele-Pointer.svg?style=for-the-badge
[contributors-url]: https://github.com/kehwaEnjoyer/Tele-Pointer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kehwaEnjoyer/Tele-Pointer.svg?style=for-the-badge
[forks-url]: https://github.com/kehwaEnjoyer/Tele-Pointer/network/members
[stars-shield]: https://img.shields.io/github/stars/kehwaEnjoyer/Tele-Pointer.svg?style=for-the-badge
[stars-url]: https://github.com/kehwaEnjoyer/Tele-Pointer/stargazers
[issues-shield]: https://img.shields.io/github/issues/kehwaEnjoyer/Tele-Pointer.svg?style=for-the-badge
[issues-url]: https://github.com/kehwaEnjoyer/Tele-Pointer/issues
[license-shield]: https://img.shields.io/github/license/kehwaEnjoyer/Tele-Pointer.svg?style=for-the-badge
[license-url]: https://github.com/kehwaEnjoyer/Tele-Pointer/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Mediapipe-url]: https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker
[OpenCV-url]: https://opencv.org/
[evdev-url]: https://python-evdev.readthedocs.io/en/latest/
