# Computer-Vision-Python
Python utilities and sample codes for Computer Vision

## Scripts added so far

### `createBlankCanvas`

#### Arguments

**`color`** (default = (0,0,0)): Color of the canvas

**`height`** (default = 300 px): Height of the canvas

**`width`** (default = 300 px): Width of the canvas

#### Usage

```
from util import *
def main():
    # Create a black canvas of 300px*300px size
    img_black_default = createBlankCanvas()
    # Create a yellow canvas of 500px*200px size
    img_yellow_500_200 = createBlankCanvas(color=(0,255,255),height=500,width=200)
    cv2.imshow("Blank canvas", img_black_canvas)
    cv2.waitKey(0)
    cv2.imshow("Yellow canvas", img_yellow_500_200)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
