import cv2
import numpy as np

def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def assign_casualties_to_pads(casualties, pads, capacities, alpha=0.1):
    """
    casualties: list of dicts {id, x, y, casualty_score, emergency_score}
    pads: dict {pad_name: (x, y)}
    capacities: dict {pad_name: capacity}
    alpha: weight for distance penalty
    """
    assignments = {p: [] for p in pads}
    candidates = []

    # Build candidate scores
    for c in casualties:
        priority_score = c["casualty_score"] * c["emergency_score"]
        for pad, (px, py) in pads.items():
            dist = calculate_distance(c["x"], c["y"], px, py)
            final_score = priority_score - alpha * dist
            candidates.append((c["id"], pad, final_score, priority_score, c["emergency_score"], dist))

    # Sort by (priority_score, emergency_score, final_score)
    candidates.sort(key=lambda x: (x[3], x[4], x[2]), reverse=True)

    used = set()
    for cid, pad, score, prio, emerg, dist in candidates:
        if cid in used:
            continue
        if len(assignments[pad]) < capacities[pad]:
            assignments[pad].append({
                "casualty_id": cid,
                "score": score,
                "priority_score": prio,
                "emergency_score": emerg,
                "distance": dist
            })
            used.add(cid)

    return assignments

# -----------------------------
# Your existing detection code
# -----------------------------

img1 = cv2.imread("1.png")
if img1 is None:
    print("Error: Could not load image")
    exit()

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

casualties = []
pads = {}
capacities = {"pink": 3, "blue": 4, "gray": 2}
cid = 0

# Detect pads (circles)
for contour in contours:
    apr = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    cor = len(apr)
    if cor > 20:  # Circle
        mask = np.zeros_like(img1)
        cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
        hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
        avg = cv2.mean(hsv, mask=mask[:, :, 0])
        h, s, v, _ = avg
        x, y, w, h_rect = cv2.boundingRect(contour)

        if 130 <= h <= 180 or 0 <= h < 10:   # Pink
            pads["pink"] = (x, y)
        elif 90 <= h <= 120:                 # Blue
            pads["blue"] = (x, y)
        elif s < 30 and v > 200:             # Gray (low saturation, high value)
            pads["gray"] = (x, y)

# Detect casualties (non-circles)
for contour in contours:
    apr = cv2.approxPolyDP(contour, 0.03 * cv2.arcLength(contour, True), True)
    cor = len(apr)
    x, y, w, h_rect = cv2.boundingRect(contour)

    # Skip if circle
    if cor > 20:
        continue

    # Classify casualty type
    if cor == 10:  # star
        casualty_score = 3
    elif cor == 3:  # triangle
        casualty_score = 2
    elif cor == 4:  # square
        casualty_score = 1
    else:
        continue

    # Emergency assignment example (here random for demo, you should map based on hue/color)
    emergency_score = np.random.choice([1, 2, 3])  # TODO: replace with actual logic

    casualties.append({
        "id": cid,
        "x": x,
        "y": y,
        "casualty_score": casualty_score,
        "emergency_score": emergency_score
    })
    cid += 1

# -----------------------------
# Perform assignment
# -----------------------------
assignments = assign_casualties_to_pads(casualties, pads, capacities, alpha=0.1)

# Print results
for pad, assigned in assignments.items():
    print(f"\nPad {pad} (capacity {capacities[pad]}):")
    total_score = 0
    for a in assigned:
        print(f"  Casualty {a['casualty_id']} | priority={a['priority_score']} "
              f"| emergency={a['emergency_score']} | dist={a['distance']:.1f} "
              f"| final_score={a['score']:.2f}")
        total_score += a["score"]
    print(f"  --> Total score: {total_score:.2f}")
