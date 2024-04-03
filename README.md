## Lyrics Extractor

A simple script for extracting lyrics embedded in HTML files and saving them in JSON format.  Created as a personal project.

### How-To-Use

**1. Setup**

* Create folders named `html_files` and `html_files_kannada` in your project's root directory.
* Place your English HTML lyric files inside the `html_files` folder.
* Place your Kannada HTML lyric files inside the `html_files_kannada` folder.

**2. Install Dependencies**

```bash
pip install requests beautifulsoup4 os json
```
**3. Run the Script**

* For English Lyrics, 

```bash
python lyrics_extract.py
```
* For Kannada Lyrics,

```bash
python lyrics_extract_kan.py
```
* Notes:

The scripts will generate JSON files with the same base name as your HTML files, saving them in the same directory.

The lyrics_extract_kan.py script is specifically designed to handle the UTF-8 encoding necessary for Kannada text.
