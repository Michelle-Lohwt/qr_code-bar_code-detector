# QR code and Bar code Detector
The project uses `OpenCV` to detect qr code and bar code. For additional experience, the project includes testing with `pytest` and `tox` (unrelated to the project itself, just trying new stuff).

## To install the project
- Fork the repository
- Clone the forked repository to your local

## To run QR code and Bar code Detector
- Check the source code in the `src` folder
- Run `py main.py`
- Make sure the QR code or Bar code is clear (code on phone is not encouraged unless your camera has high resolution)

## To run the testing
- Make sure you have the python version installed (py27, py36, py38, py310) (you may change the python version you need in `tox.ini`)
- Check the source code in the `scripts` folder
- Run the `script.ps1` in the `scripts` folder
- It should show 1 fail test and 1 success test. You may play with the tests in the `tests` folder.

## Folder structure
```
qr-bar-code-detector
  |_scripts
    |_ script.ps1   # testing powershell script
  |_ src
    |_ sample_img   # store image
    |_ main.py      # qr and bar code detector source code
  |_ tests          # unit tests folder
    |_ fail_test.py
    |_ pass_test.py
  |_ .coveragerc
  |_ pyproject.toml
  |_ setup.cfg
  |_ requirement.txt
  |_ tox.ini
```

Related:
1. [Deprecation of setup.py](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)
2. [Doesn't my project need a setup.py or setup.cfg file?](https://tttapa.github.io/py-build-cmake/FAQ.html#doesnt-my-project-need-a-codesetuppycode-or-codesetupcfgcode-file)
3. [setup.py vs setup.cfg in Python](https://towardsdatascience.com/setuptools-python-571e7d5500f2)