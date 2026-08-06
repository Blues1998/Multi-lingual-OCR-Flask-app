# Multi-lingual OCR — Flask app

Upload an image or a PDF, get the text back. Built as my final-year college
project.

The point of it is the language coverage: it recognises **English, Telugu, Urdu
and Hindi**, and does so in a single pass — one document can contain more than
one of them.

## Running it

Tesseract itself is a system binary, not a Python package, and must be
installed separately along with the language data:

```bash
# macOS
brew install tesseract tesseract-lang poppler

# Debian/Ubuntu
sudo apt install tesseract-ocr tesseract-ocr-tel tesseract-ocr-urd \
                 tesseract-ocr-hin poppler-utils
```

Then:

```bash
pip install flask pytesseract pillow pdf2image
python app.py
```

`poppler` is what `pdf2image` shells out to; PDF upload fails without it.

On Windows, Tesseract is not on `PATH` by default — `app.py` carries a
commented-out `pytesseract.tesseract_cmd` line pointing at the usual install
location, which needs uncommenting.

## How the languages work

The call is `lang='eng+tel+urd+hin'`. Tesseract takes several language codes at
once and will use all of them on the same page, which is why mixed-script
documents work. Each code needs its `traineddata` file present, hence the
language packages above.

`fonts/` holds Telugu and Nastaliq Urdu fonts for rendering the recognised text
back in the right script.

## Licence

MIT.
