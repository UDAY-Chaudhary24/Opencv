import cv2
import numpy as np

def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize lists
li = []
li1, li2, li3, li4, li5, li6, li7, li8, li9 = [], [], [], [], [], [], [], [], []
li_pad1, li_pad2, li_pad3 = [], [], []  # Will store circle coordinates by color
out_pink, out_blue, out_gray = [], [], []
j = 0

# Read image and process
img1 = cv2.imread("1.png")
if img1 is None:
    print("Error: Could not load image '1.png'")
    exit()

# Convert to grayscale and apply adaptive thresholding for better contour detection
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# First pass - classify circles by color (pink, blue, gray) and store all coordinates
for contour in contours:
    # Check if it's a circle (cor > 20 from second pass)
    apr = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    cor = len(apr)
    if cor > 20:  # Circle detection
        # Create mask for mean color calculation
        mask = np.zeros_like(img1)
        cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
        
        # Convert to HSV and calculate mean color
        hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
        avg = cv2.mean(hsv, mask=mask[:, :, 0])
        h, s, v, _ = avg

        # Get bounding rectangle
        bbox_x, bbox_y, bbox_w, bbox_h = cv2.boundingRect(contour)

        # Classify circles by color and append coordinates
        if 130<= h <= 180 or 0 <= h < 10:  # Pink/magenta range
            li_pad1.extend([bbox_x, bbox_y])
        elif 10 <= h <= 50:  # Blue range
            li_pad2.extend([bbox_x, bbox_y])
        elif 100<h<120:  # Gray (low saturation, reasonable value)
            li_pad3.extend([bbox_x, bbox_y])

# Second pass - process all shapes and draw them
for contour in contours:
    apr = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    cor = len(apr)

    # Draw contours and shapes for visualization
    cv2.drawContours(img1, [contour], -1, (0, 255, 0), 2)

    # Define shape based on corner count
    if cor == 3:
        shape = "triangle"
    elif cor == 4:
        shape = "square"
    elif cor == 10:
        shape = "star"
    elif 20 > cor > 11:
        shape = "other"
    else:
        shape = "unknown"  # Default case to avoid undefined error

    cv2.drawContours(img1, [apr], 0, (255, 0, 0), 1)
    if len(apr) > 0:
        x = apr.ravel()[0]
        y = apr.ravel()[1]
        cv2.putText(img1, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

# Third pass - classify shapes by color and geometry (excluding circles)
for contour in contours:
    apr = cv2.approxPolyDP(contour, 0.03 * cv2.arcLength(contour, True), True)
    cor = len(apr)

    # Create mask for mean color calculation
    mask = np.zeros_like(img1)
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)

    # Convert to HSV and calculate mean color
    hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    avg = cv2.mean(hsv, mask=mask[:, :, 0])
    h, s, v, _ = avg

    # Skip invalid hue values
    if not (0 <= h <= 180):
        print(f"Warning: Invalid hue value {h:.2f} for contour with {cor} corners")
        continue

    # Get bounding rectangle
    x, y, w, bbox_h = cv2.boundingRect(contour)

    # Process based on corner count and hue (excluding circles)
    if cor == 10:
        if 0 <= h < 15 or 160 <= h <= 180:  # Red/pink range
            li.insert(0, 9)
            li1.extend([x, y])
            j += 2
        elif 15 <= h < 35:  # Orange range
            li.insert(0, 6)
            li2.extend([x, y])
            j += 2
        elif 35 <= h <= 85:  # Green range
            li.insert(0, 3)
            li3.extend([x, y])
            j += 2
    elif cor == 3:
        if 0 <= h < 15 or 160 <= h <= 180:
            li.insert(0, 6)
            li4.extend([x, y])
            j += 2
        elif 15 <= h < 35:
            li.insert(0, 4)
            li5.extend([x, y])
            j += 2
        elif 35 <= h <= 85:
            li.insert(0, 2)
            li6.extend([x, y])
            j += 2
    elif cor == 4:
        if 0 <= h < 15 or 160 <= h <= 180:
            li.insert(0, 3)
            li7.extend([x, y])
            j += 2
        elif 15 <= h < 35:
            li.insert(0, 2)
            li8.extend([x, y])
            j += 2
        elif 35 <= h <= 85:
            li.insert(0, 1)
            li9.extend([x, y])
            j += 2

# Distance calculations
# Process lists with safety checks
if (len(li_pad1) == 2) and (len(li_pad2) == 2) and (len(li_pad3) == 2):
    # Use first pair of coordinates as reference points
    pad1_x = li_pad1[0]
    pad1_y = li_pad1[1]
    pad2_x = li_pad2[0]
    pad2_y = li_pad2[1]
    pad3_x = li_pad3[0]
    pad3_y = li_pad3[1]

    # Process li1
    i = 0
    q = len(li1) // 2
    while i < q:
        if i + 1 < len(li1):
            pad1 = calculate_distance(pad1_x, pad1_y, li1[i], li1[i + 1])
            pad2 = calculate_distance(pad2_x, pad2_y, li1[i], li1[i + 1])
            pad3 = calculate_distance(pad3_x, pad3_y, li1[i], li1[i + 1])
            if pad1 > pad2 and pad1 > pad3:
                out_pink.insert(0, "[3,3]")
            elif pad2 > pad1 and pad2 > pad3:
                out_blue.insert(0, "[3,3]")
            elif pad3 > pad1 and pad3 > pad2:
                out_gray.insert(0, "[3,3]")
        i += 1

    # Process li2
    n = 0
    qq = len(li2) // 2
    while n < qq:
        if n + 1 < len(li2):
            pad1 = calculate_distance(pad1_x, pad1_y, li2[n], li2[n + 1])
            pad2 = calculate_distance(pad2_x, pad2_y, li2[n], li2[n + 1])
            pad3 = calculate_distance(pad3_x, pad3_y, li2[n], li2[n + 1])
            if pad1 > pad2 and pad1 > pad3 and len(out_pink) < 3:
                out_pink.append("[3,2]")
            elif pad2 > pad1 and pad2 > pad3 and len(out_blue) < 4:
                out_blue.append("[3,2]")
            elif pad3 > pad1 and pad3 > pad2 and len(out_gray) < 2:
                out_gray.append("[3,2]")
        n += 1

    # Process li4
    k = 0
    qqq = len(li4) // 2
    while k < qqq:
        if k + 1 < len(li4):
            pad1 = calculate_distance(pad1_x, pad1_y, li4[k], li4[k + 1])
            pad2 = calculate_distance(pad2_x, pad2_y, li4[k], li4[k + 1])
            pad3 = calculate_distance(pad3_x, pad3_y, li4[k], li4[k + 1])
            if pad1 > pad2 and pad1 > pad3 and len(out_pink) < 3:
                out_pink.append("[2,3]")
            elif pad2 > pad1 and pad2 > pad3 and len(out_blue) < 4:
                out_blue.append("[2,3]")
            elif pad3 > pad1 and pad3 > pad2 and len(out_gray) < 2:
                out_gray.append("[2,3]")
        k += 1

    # Process li5
    l = 0
    qqqq = len(li5) // 2
    while l < qqqq:
        if l + 1 < len(li5):
            pad1 = calculate_distance(pad1_x, pad1_y, li5[l], li5[l + 1])
            pad2 = calculate_distance(pad2_x, pad2_y, li5[l], li5[l + 1])
            pad3 = calculate_distance(pad3_x, pad3_y, li5[l], li5[l + 1])
            if pad1 > pad2 and pad1 > pad3 and len(out_pink) < 3:
                out_pink.append("[2,2]")
            elif pad2 > pad1 and pad2 > pad3 and len(out_blue) < 4:
                out_blue.append("[2,2]")
            elif pad3 > pad1 and pad3 > pad2 and len(out_gray) < 2:
                out_gray.append("[2,2]")
        l += 1

    # Process li3
    v = 0
    qqqqq = len(li3) // 2
    while v < qqqqq:
        if v + 1 < len(li3):
            pad1 = calculate_distance(pad1_x, pad1_y, li3[v], li3[v + 1])
            pad2 = calculate_distance(pad2_x, pad2_y, li3[v], li3[v + 1])
            pad3 = calculate_distance(pad3_x, pad3_y, li3[v], li3[v + 1])
            if pad1 > pad2 and pad1 > pad3 and len(out_pink) < 3:
                out_pink.append("[3,1]")
            elif pad2 > pad1 and pad2 > pad3 and len(out_blue) < 4:
                out_blue.append("[3,1]")
            elif pad3 > pad1 and pad3 > pad2 and len(out_gray) < 2:
                out_gray.append("[3,1]")
        v += 1

    # Process li6
    o = 0
    qqqqqqq = len(li6) // 2
    while o < qqqqqqq:
        if o + 1 < len(li6):
            pad1 = calculate_distance(pad1_x, pad1_y, li6[o], li6[o + 1])
            pad2 = calculate_distance(pad2_x, pad2_y, li6[o], li6[o + 1])
            pad3 = calculate_distance(pad3_x, pad3_y, li6[o], li6[o + 1])
            if pad1 > pad2 and pad1 > pad3 and len(out_pink) < 3:
                out_pink.append("[2,1]")
            elif pad2 > pad1 and pad2 > pad3 and len(out_blue) < 4:
                out_blue.append("[2,1]")
            elif pad3 > pad1 and pad3 > pad2 and len(out_gray) < 2:
                out_gray.append("[2,1]")
        o += 1

    # Process li8
    h = 0
    qqqqqqqq = len(li8) // 2
    while h < qqqqqqqq:
        if h + 1 < len(li8):
            pad1 = calculate_distance(pad1_x, pad1_y, li8[h], li8[h + 1])
            pad2 = calculate_distance(pad2_x, pad2_y, li8[h], li8[h + 1])
            pad3 = calculate_distance(pad3_x, pad3_y, li8[h], li8[h + 1])
            if pad1 > pad2 and pad1 > pad3 and len(out_pink) < 3:
                out_pink.append("[1,2]")
            elif pad2 > pad1 and pad2 > pad3 and len(out_blue) < 4:
                out_blue.append("[1,2]")
            elif pad3 > pad1 and pad3 > pad2 and len(out_gray) < 2:
                out_gray.append("[1,2]")
        h += 1

    # Process li9
    e = 0
    qqqqqqqqq = len(li9) // 2
    while e < qqqqqqqqq:
        if e + 1 < len(li9):
            pad1 = calculate_distance(pad1_x, pad1_y, li9[e], li9[e + 1])
            pad2 = calculate_distance(pad2_x, pad2_y, li9[e], li9[e + 1])
            pad3 = calculate_distance(pad3_x, pad3_y, li9[e], li9[e + 1])
            if pad1 > pad2 and pad1 > pad3 and len(out_pink) < 3:
                out_pink.append("[1,1]")
            elif pad2 > pad1 and pad2 > pad3 and len(out_blue) < 4:
                out_blue.append("[1,1]")
            elif pad3 > pad1 and pad3 > pad2 and len(out_gray) < 2:
                out_gray.append("[1,1]")
        e += 1

else:
    print("Error: Not all pad positions have exactly 2 coordinates")

# Show the image with detected shapes and print results
cv2.imshow("Image with Contours and Text", img1)
print("Image displayed with contours and text. Close the window to see output.")
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print results and debug
print("for pink")
print(out_pink)
print("for blue")
print(out_blue)
print("for gray")
print(out_gray)
print("li_pad1:", li_pad1)
print("li_pad2:", li_pad2)
print("li_pad3:", li_pad3)