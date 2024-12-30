import project
import pytest, sys
from PIL import Image, UnidentifiedImageError
from unittest.mock import patch

def test_main():
    args = [ "project.py", "xyz.png"]
    with patch.object(sys, "argv", args):
        with pytest.raises(SystemExit) as excinfo:
            project.main()
        assert str(excinfo.value) == "The file xyz.png  does not exists."
        
    args = [ "project.py", "project.py"]
    with patch.object(sys, "argv", args):
        with pytest.raises(SystemExit) as excinfo:
            project.main()
        assert str(excinfo.value) == "The file project.py cannot be identified as an image file."

def test_glevel_transform(monkeypatch):
     img = Image.open("shlokpal.jpg")
     monkeypatch.setattr('builtins.input', lambda _: "quit")
     with pytest.raises(SystemExit) as excinfo:
        project.glevel_transform(img)
     assert str(excinfo.value) == "Exiting with quit..."

def test_spatial_filter(monkeypatch):
     img = Image.open("shlokpal.jpg")
     monkeypatch.setattr('builtins.input', lambda _: "quit")
     with pytest.raises(SystemExit) as excinfo:
        project.spatial_filter(img)
     assert str(excinfo.value) == "Exiting with quit..."

def test_image_interpolation(monkeypatch):
     img = Image.open("shlokpal.jpg")
     monkeypatch.setattr('builtins.input', lambda _: "quit")
     with pytest.raises(SystemExit) as excinfo:
        project.image_interpolation(img)
     assert str(excinfo.value) == "Exiting with quit..."

def test_enhance(monkeypatch):
     img = Image.open("shlokpal.jpg")
     monkeypatch.setattr('builtins.input', lambda _: "quit")
     with pytest.raises(SystemExit) as excinfo:
        project.enhance(img)
     assert str(excinfo.value) == "Exiting with quit..."


