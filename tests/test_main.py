# Test file for use with pytest

import Image
from ..main import windows, windows0

testfile = "tests/test_image.png"

def test_windows_sizes():
    """
    Check that all windows have the corrrect
    dimensions.
    """
    im = Image.open(testfile)
    ws = windows0(im,[(20,10)],(20,10))
    im_t0 = im.crop((0,0,20,10))
    for win in ws:
        assert im_t0.size == win.size


def test_windows_first():
    im = Image.open(testfile)
    w = windows0(im,[(20,10)],(20,10))
    im_t0 = im.crop((0,0,20,10))
    im_t1 = w.next()
    for x,y in zip(im_t0.getdata(),im_t1.getdata()):
        assert x == y


def test_windows_last():
    im = Image.open(testfile)
    width, height = im.size
    x0, y0 = width - 20, height - 10
    w = windows0(im,[(20,10)],(20,10))
    im_t0 = im.crop((x0,y0,width,height))
    im_t1 = None
    for im_t1 in w:
        pass
    for x,y in zip(im_t0.getdata(),im_t1.getdata()):
        print x,y
        assert x == y
