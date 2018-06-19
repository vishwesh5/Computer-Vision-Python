# Computer-Vision-Python
Python utilities and sample codes for Computer Vision

## Scripts

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
    cv2.imshow("Blank canvas", img_black_default)
    cv2.waitKey(0)
    cv2.imshow("Yellow canvas", img_yellow_500_200)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

### `createLine`

#### Arguments

**`image`** (default = None): The image on which a line is to be drawn

**`firstPoint`** (default=None): The starting point of the line

**`secondPoint`** (default=None): The ending point of the line

**`color`** (default=(255,255,255)): The color of the line (default = White)

**`lineThickness`** (default=3): Thickness of the line in pixels

#### Usage

```
from util import *
def main():
    
    # Create a black canvas of 300px*300px size
    img_black_default = createBlankCanvas()
    # Create a yellow canvas of 500px*200px size
    img_yellow_500_200 = createBlankCanvas(color=(0,255,255),height=500,width=200)
    
    # Plot a black line on yellow canvas
    img_black_line = createLine(image=img_yellow_500_200,color=(0,0,0))
    # Plot a white line on black canvas
    img_white_line = createLine(image=img_black_default)
    
    # Display results
    cv2.imshow("Blank canvas", img_black_canvas)
    cv2.waitKey(0)
    cv2.imshow("Yellow canvas", img_yellow_500_200)
    cv2.waitKey(0)
    cv2.imshow("Black canvas with white line", img_white_line)
    cv2.waitKey(0)
    cv2.imshow("Yellow canvas with black line", img_black_line)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

### `createSampleCross`

#### Arguments

**`bgColor`** (default=(0,0,0)): Background color of the canvas

**`crossColor`** (default=(255,255,255)): Line color of the cross

**`height`** (default=300): Height of the canvas

**`width`** (default=300): Width of the canvas

#### Usage

```
from util import *

def main():

    # Create a white cross on black canvas
    whiteCross = createSampleCross()
    # Create a blue cross on white canvas
    blueCross = createSampleCross(bgColor=(255,255,255),crossColor=(255,0,0))
    
    # Display results
    cv2.imshow("White cross on black canvas", whiteCross)
    cv2.waitKey(0)
    cv2.imshow("Blue cross on white canvas", blueCross)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
```
