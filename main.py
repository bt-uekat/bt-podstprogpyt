import cv2
from fastapi import FastAPI, HTTPException

app = FastAPI()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


@app.get("/count-persons")
def count_persons():
    image_path = "test.jpg"

    image = cv2.imread(image_path)

    if image is None:
        raise HTTPException(
            status_code=404,
            detail=f"Nie znaleziono pliku {image_path} na dysku."
        )

    image = cv2.resize(image, (800, 600))

    boxes, weights = hog.detectMultiScale(
        image, winStride=(8, 8),
        padding=(8, 8), scale=1.05
    )

    person_count = len(boxes)

    return {
        "filename": image_path,
        "persons_detected": person_count
    }
