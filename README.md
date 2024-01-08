<p align="center">
  <br>
  <a href="https://ergin.dev"><img src="https://raw.githubusercontent.com/EyupErgin/HookHunter/banner.png" width="400px" alt="HookHunter"></a>
</p>
<h4 align="center">Algorithm Based Phishing and Impersonating Domain Detection Tool <br> Version: v1.0</h4>

---

## Purpose of the Project:
The aim of the project is to identify the domain names that can be used in phishing attacks through the method of creating a similar domain name used in website-based phishing attacks, which are frequently used today.

## Process of the Project:
The process of the project will include 4 different algorithms and similarity analysis as the main logic.
In this process, Fuzzy will be used for similarity analysis, Hypenation for character substitution, Homoglopht for hyphenation and TLD algorithm for TLD based analysis.

## HookHunter's To-Do:
- [x] Fuzzy Hash based similarity algorithm will be developed for similarity analysis,
- [x] Hyphenation algorithm will be developed for hyphen-based analysis,
- [x] Alphabet algorithm will be developed for Hyphenation analysis,
    - [x] Homoglyph algorithms based on alphabets:
        - [x] Turkish alphabet,
        - [x] Cyrillic alphabet,
        - [x] Swiss alphabet,
        - [x] French alphabet,
        - [x] Belgian alphabet,
        - [x] Canadian alphabet,
        - [x] Norwegian alphabet,
        - [x] Polish alphabet,
        - [x] Brazilian alphabet,
        - [x] German alphabet,
        - [x] Finnish alphabet,
        - [x] Danish alphabet,
        - [x] Liechtenstein alphabet,
        - [x] Wallis and Futuna alphabet,
        - [x] Saint Pierre and Miquelon alphabet.
    - [x] Glyph Homoglyph algorithm to be developed:
        - [x] Glyph Unicode,
        - [x] Glyph ASCII.
    - [x] Keyboard-based Homoglyph algorithms:
        - [x] Qwerty,
        - [x] Qwertz,
        - [x] Azerty.
         
---

## :inbox_tray:	Install HookHunter
1. Clone the project repository or download the zip file:
```bash
git clone https://github.com/eyupergin/hookhunter.git
```
2. Install the required Python packages by running the following command:
```bash
pip3 install -r requirements.txt
```
## :desktop_computer:	Use HookHunter
HuntRthys is used via a command-line interface. Below are examples of basic usage.

### Basic Usage
- List arguments:
```bash
python3 main.py
```

## :mag_right: Results
HookHunter Phishing and Impersonating Domain Scanner tool visualizes the scanning results in a tabular format and prints them to the console. 
Additionally, you can choose to save the results to a JSON file. (Soon)

Here is an example output of the results:
```
$ python3 run.py

______  __           ______ ______  __             _____               | Version: v1.0
___  / / /______________  /____  / / /___  __________  /_____________  | Developed by Eyup Sukru ERGIN
__  /_/ /_  __ \  __ \_  //_/_  /_/ /_  / / /_  __ \  __/  _ \_  ___/  | --------------------------------------
_  __  / / /_/ / /_/ /  ,<  _  __  / / /_/ /_  / / / /_ /  __/  /      | https://ergin.dev
/_/ /_/  \____/\____//_/|_| /_/ /_/  \__,_/ /_/ /_/\__/ \___//_/       | https://github.com/eyupergin/hookhunter

Advanced Domain Based Phishing and Impersonating Domain Detection Tool

[INFO] Please enter domain: google.com

Processing: 100%|███████████████████████████████████████████| 556/556 [21:47<00:00,  2.35s/ domains]


  #  SC    BASE DOMAIN    IMPERSONATING DOMAIN      SIMILARITY  HTTP STATUS    IP ADDRESS       ABUSE E-MAIL
---  ----  -------------  ----------------------  ------------  -------------  ---------------  --------------------------------------
  1  CA    google.com     agoogle.com                       95  200            198.251.81.30    abuse@namesilo.com
  2  CA    google.com     bgoogle.com                       95  200            209.141.38.71    abuse@namesilo.com
  3  CA    google.com     cgoogle.com                       95  200            199.59.243.225   abuse@dynadot.com
  4  CA    google.com     dgoogle.com                       95  ERR            N/A              abusecomplaints@markmonitor.com
  5  CA    google.com     egoogle.com                       95  ERR            82.192.82.226    abuse@metaregistrar.com
  6  CA    google.com     fgoogle.com                       95  ERR            127.0.0.10       abuse@pananames.com
  7  CA    google.com     ggoogle.com                       95  404            216.58.212.36    abusecomplaints@markmonitor.com
  8  CA    google.com     hgoogle.com                       95  200            198.251.81.30    abuse@namesilo.com
  9  CA    google.com     igoogle.com                       95  200            142.251.140.4    abusecomplaints@markmonitor.com
 10  CA    google.com     jgoogle.com                       95  ERR            N/A              abusecomplaints@markmonitor.com
 11  CA    google.com     kgoogle.com                       95  200            74.208.236.137   abuse@ionos.com
 12  CA    google.com     lgoogle.com                       95  ERR            N/A              abusecomplaints@markmonitor.com
 13  CA    google.com     mgoogle.com                       95  ERR            N/A              abusecomplaints@markmonitor.com
 14  CA    google.com     ngoogle.com                       95  ERR            N/A              abusecomplaints@markmonitor.com
 15  CA    google.com     ogoogle.com                       95  ERR            N/A              abusecomplaints@markmonitor.com
 16  CA    google.com     pgoogle.com                       95  436            103.224.182.251  abuse@above.com
 17  CA    google.com     qgoogle.com                       95  ERR            66.28.214.11
 18  CA    google.com     rgoogle.com                       95  ERR            47.254.33.193    abuse@ename.com
 19  CA    google.com     sgoogle.com                       95  ERR            N/A              abusecomplaints@markmonitor.com
 20  CA    google.com     tgoogle.com                       95  200            198.251.81.30    abuse@namesilo.com
 21  CA    google.com     ugoogle.com                       95  404            185.230.63.186   abuse@godaddy.com
 22  CA    google.com     vgoogle.com                       95  ERR            47.254.33.193    abuse@ename.com
 23  CA    google.com     wgoogle.com                       95  ERR            N/A              abusecomplaints@markmonitor.com
 24  CA    google.com     xgoogle.com                       95  ERR            N/A              abusecomplaints@markmonitor.com
```

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Contributing
Repo Update Date: 09-01-2024 <br>
> If you would like to contribute to this project, please open an issue or submit a pull request. Any contributions and suggestions are welcome!
